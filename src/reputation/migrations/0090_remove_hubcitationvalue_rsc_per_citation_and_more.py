# Generated by Django 4.2.14 on 2024-07-29 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reputation", "0089_alter_paperreward_distribution"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="hubcitationvalue",
            name="rsc_per_citation",
        ),
        migrations.AddField(
            model_name="hubcitationvalue",
            name="variables",
            field=models.JSONField(blank=True, default=None, null=True),
        ),
    ]
