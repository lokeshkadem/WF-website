# Generated by Django 3.1.7 on 2021-02-26 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_libraryitemtopic'),
    ]

    operations = [
        migrations.AddField(
            model_name='libraryitem',
            name='drupal_node_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]