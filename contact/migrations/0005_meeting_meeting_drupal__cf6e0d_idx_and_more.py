# Generated by Django 4.1.5 on 2023-02-01 17:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contact", "0004_meeting_drupal_duplicate_author_ids_and_more"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="meeting",
            index=models.Index(
                fields=["drupal_author_id"], name="meeting_drupal__cf6e0d_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="organization",
            index=models.Index(
                fields=["drupal_author_id"], name="organizatio_drupal__81d4b0_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="person",
            index=models.Index(
                fields=["drupal_author_id"], name="person_drupal__650db4_idx"
            ),
        ),
    ]
