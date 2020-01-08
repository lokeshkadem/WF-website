# Generated by Django 2.2.8 on 2019-12-30 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0006_auto_20191230_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivearticle',
            name='toc_page_number',
            field=models.PositiveIntegerField(help_text='Enter the page number as it appears in the Table of Contents', verbose_name='ToC page #'),
        ),
    ]