# Generated by Django 4.2.14 on 2024-07-25 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("reputation", "0087_paperreward_hubcitationvalue"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="paperreward",
            name="is_paid",
        ),
        migrations.AddField(
            model_name="paperreward",
            name="distribution",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="reputation.distribution",
            ),
        ),
        migrations.AlterField(
            model_name="distribution",
            name="distribution_type",
            field=models.CharField(
                choices=[
                    ("FLAG_PAPER", "FLAG_PAPER"),
                    ("PAPER_UPVOTED", "PAPER_UPVOTED"),
                    ("PAPER_Downvoted", "PAPER_Downvoted"),
                    ("CREATE_BULLET_POINT", "CREATE_BULLET_POINT"),
                    ("BULLET_POINT_FLAGGED", "BULLET_POINT_FLAGGED"),
                    ("BULLET_POINT_UPVOTED", "BULLET_POINT_UPVOTED"),
                    ("BULLET_POINT_DOWNVOTED", "BULLET_POINT_DOWNVOTED"),
                    ("COMMENT_CENSORED", "COMMENT_CENSORED"),
                    ("COMMENT_FLAGGED", "COMMENT_FLAGGED"),
                    ("COMMENT_UPVOTED", "COMMENT_UPVOTED"),
                    ("COMMENT_DOWNVOTED", "COMMENT_DOWNVOTED"),
                    ("REPLY_CENSORED", "REPLY_CENSORED"),
                    ("REPLY_FLAGGED", "REPLY_FLAGGED"),
                    ("REPLY_UPVOTED", "REPLY_UPVOTED"),
                    ("REPLY_DOWNVOTED", "REPLY_DOWNVOTED"),
                    ("THREAD_CENSORED", "THREAD_CENSORED"),
                    ("THREAD_FLAGGED", "THREAD_FLAGGED"),
                    ("THREAD_UPVOTED", "THREAD_UPVOTED"),
                    ("THREAD_DOWNVOTED", "THREAD_DOWNVOTED"),
                    ("CREATE_SUMMARY", "CREATE_SUMMARY"),
                    ("SUMMARY_UPVOTED", "SUMMARY_UPVOTED"),
                    ("SUMMARY_DOWNVOTED", "SUMMARY_DOWNVOTED"),
                    ("HYPOTHESIS_UPVOTED", "HYPOTHESIS_UPVOTED"),
                    ("HYPOTHESIS_DOWNVOTED", "HYPOTHESIS_DOWNVOTED"),
                    ("UPVOTE_RSC_POT", "UPVOTE_RSC_POT"),
                    ("STORED_PAPER_POT", "STORED_PAPER_POT"),
                    ("PAPER_REWARD", "PAPER_REWARD"),
                    ("REWARD", "REWARD"),
                    ("PURCHASE", "PURCHASE"),
                    ("EDITOR_COMPENSATION", "EDITOR_COMPENSATION"),
                    ("EDITOR_PAYOUT", "EDITOR_PAYOUT"),
                ],
                max_length=255,
            ),
        ),
    ]
