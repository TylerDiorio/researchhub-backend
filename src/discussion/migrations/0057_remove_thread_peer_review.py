# Generated by Django 4.2.15 on 2024-08-12 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("discussion", "0056_remove_thread_citation_remove_thread_hypothesis"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="thread",
            name="peer_review",
        ),
    ]
