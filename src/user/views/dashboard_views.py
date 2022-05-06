import django_filters.rest_framework
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import CursorPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from discussion.models import Flag
from discussion.serializers import DynamicFlagSerializer
from user.models import Action
from user.serializers import DynamicActionSerializer


class CursorSetPagination(CursorPagination):
    page_size = 10
    cursor_query_param = "page"
    ordering = "-created_date"


class DashboardViewSet(viewsets.GenericViewSet):
    # TODO: Permissions
    queryset = Action.objects.all()
    permission_classes = [AllowAny]
    pagination_class = CursorSetPagination
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["hubs"]
    models = [
        "thread",
        "comment",
        "reply",
        "researchhubpost",
        "paper",
        "hypothesis",
    ]

    def get_filtered_queryset(self):
        return self.filter_queryset(self.get_queryset())

    def _get_flagged_content(self):
        flagged_contributions = Flag.objects.all().values_list("object_id")
        actions = self.get_filtered_queryset().filter(id__in=flagged_contributions)
        return actions

    def _get_latest_actions(self):
        actions = (
            self.get_filtered_queryset()
            .filter(user__isnull=False, content_type__model__in=self.models)
            .select_related("user")
            .prefetch_related("item", "user__author_profile")
        )
        return actions

    def _get_latest_actions_context(self):
        context = {
            "usr_das_get_created_by": {
                "_include_fields": [
                    "id",
                    "first_name",
                    "last_name",
                    "author_profile",
                ]
            },
            "usr_dus_get_author_profile": {
                "_include_fields": [
                    "id",
                    "profile_image",
                ]
            },
            "usr_das_get_item": {
                "_include_fields": [
                    "unified_document",
                    "content_type",
                    "source",
                    "user",
                    "amount",
                    "plain_text",
                    "title",
                    "slug",
                ]
            },
            "pap_dps_get_unified_document": {
                "_include_fields": [
                    "id",
                    "document_type",
                ]
            },
            "dis_dts_get_unified_document": {
                "_include_fields": [
                    "id",
                    "document_type",
                    "documents",
                    "slug",
                ]
            },
            "dis_dcs_get_unified_document": {
                "_include_fields": [
                    "id",
                    "document_type",
                    "documents",
                    "slug",
                ]
            },
            "dis_drs_get_unified_document": {
                "_include_fields": [
                    "id",
                    "document_type",
                    "documents",
                    "slug",
                ]
            },
            "doc_dps_get_unified_document": {
                "_include_fields": [
                    "id",
                    "document_type",
                    "documents",
                    "slug",
                ]
            },
            "hyp_dhs_get_unified_document": {
                "_include_fields": [
                    "id",
                    "renderable_text",
                    "title",
                    "slug",
                ]
            },
            "doc_duds_get_documents": {
                "_include_fields": [
                    "id",
                    "title",
                    "post_title",
                    "slug",
                ]
            },
        }
        context["dis_dfs_get_item"] = context["usr_das_get_item"]
        context["dis_dfs_get_created_by"] = context["usr_das_get_created_by"]
        return context

    def list(self, request):
        from django.db.models import F
        from django.db.models.expressions import OuterRef, Subquery

        from paper.models import Paper
        from researchhub_document.related_models.researchhub_unified_document_model import (
            ResearchhubUnifiedDocument,
        )

        Paper.objects.all().update(
            unified_document_new=Subquery(
                ResearchhubUnifiedDocument.objects.filter(paper=OuterRef("id")).values(
                    "id"
                )[:1]
            )
        )
        # Paper.objects.all().update(unified_document_new=F('unified_document'))
        return Response()
        query_params = request.query_params
        get_flagged_content = query_params.get("flagged_content", False)

        if get_flagged_content:
            actions = self._get_flagged_content()
            serializer = DynamicFlagSerializer
        else:
            actions = self._get_latest_actions()
            serializer = DynamicActionSerializer

        page = self.paginate_queryset(actions)
        data = serializer(
            page,
            many=True,
            context=self._get_latest_actions_context(),
            _include_fields=[
                "id",
                "content_type",
                "created_by",
                "item",
                "created_date",
            ],
        ).data

        return self.get_paginated_response(data)
