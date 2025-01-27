# Generated by Django 4.2.1 on 2023-05-24 06:05

import blocks.blocks
import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import re
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail_color_panel.blocks


class Migration(migrations.Migration):
    replaces = [
        ("news", "0001_initial"),
        ("news", "0002_alter_newsitem_body"),
        ("news", "0003_alter_newsitem_body"),
        ("news", "0004_alter_newsitem_body"),
        ("news", "0005_alter_newsitem_body"),
        ("news", "0006_alter_newsitem_body"),
        ("news", "0007_alter_newsitem_body"),
        ("news", "0008_alter_newsitem_body"),
        ("news", "0009_alter_newsitem_body"),
        ("news", "0010_alter_newsitem_body"),
        ("news", "0011_alter_newsitem_body"),
        ("news", "0012_alter_newsitem_body"),
        ("news", "0013_alter_newsitem_body"),
        ("news", "0014_alter_newsitem_body"),
        ("news", "0015_alter_newsitem_body"),
        ("news", "0016_newsitem_body_migrated"),
        ("news", "0017_newsitem_drupal_node_id"),
        ("news", "0018_alter_newsitem_news_topic_alter_newsitem_news_type_and_more"),
        ("news", "0019_newsitemtag_newsitem_tags"),
    ]

    initial = True

    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
        ("wagtailcore", "0066_collection_management_permissions"),
    ]

    operations = [
        migrations.CreateModel(
            name="NewsIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("intro", wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="NewsTopic",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("intro", wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="NewsTopicIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("intro", wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="NewsType",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("intro", wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="NewsTypeIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("intro", wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="NewsItem",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "teaser",
                    models.TextField(
                        blank=True,
                        help_text="Briefly summarize the news item for display in news lists",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            (
                                "heading",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "heading_level",
                                            wagtail.blocks.ChoiceBlock(
                                                choices=[
                                                    (
                                                        "h2",
                                                        "Level 2 (child of level 1)",
                                                    ),
                                                    (
                                                        "h3",
                                                        "Level 3 (child of level 2)",
                                                    ),
                                                    (
                                                        "h4",
                                                        "Level 4 (child of level 3)",
                                                    ),
                                                    (
                                                        "h5",
                                                        "Level 5 (child of level 4)",
                                                    ),
                                                    (
                                                        "h6",
                                                        "Level 6 (child of level 5)",
                                                    ),
                                                ],
                                                help_text="These different heading levels help to communicate the organization and hierarchy of the content on a page.",
                                            ),
                                        ),
                                        (
                                            "heading_text",
                                            wagtail.blocks.CharBlock(
                                                help_text="The text to appear in the heading."
                                            ),
                                        ),
                                        (
                                            "target_slug",
                                            wagtail.blocks.CharBlock(
                                                help_text="Used to link to a specific location within this page. A slug should only contain letters, numbers, underscore (_), or hyphen (-).",
                                                required=False,
                                                validators=(
                                                    django.core.validators.RegexValidator(
                                                        re.compile(
                                                            "^[-a-zA-Z0-9_]+\\Z"
                                                        ),
                                                        "Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.",
                                                        "invalid",
                                                    ),
                                                ),
                                            ),
                                        ),
                                        (
                                            "color",
                                            wagtail_color_panel.blocks.NativeColorBlock(
                                                required=False
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                            (
                                "rich_text",
                                wagtail.blocks.RichTextBlock(
                                    features=[
                                        "bold",
                                        "italic",
                                        "ol",
                                        "ul",
                                        "hr",
                                        "link",
                                        "document-link",
                                        "superscript",
                                        "superscript",
                                        "strikethrough",
                                        "blockquote",
                                    ]
                                ),
                            ),
                            ("pullquote", blocks.blocks.PullQuoteBlock()),
                            (
                                "image",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(),
                                        ),
                                        (
                                            "width",
                                            wagtail.blocks.IntegerBlock(
                                                help_text="Enter the desired image width value in pixels up to 800 max.",
                                                max_value=800,
                                                min_value=0,
                                            ),
                                        ),
                                        (
                                            "align",
                                            wagtail.blocks.ChoiceBlock(
                                                choices=[
                                                    ("left", "Left"),
                                                    ("right", "Right"),
                                                ],
                                                help_test="Optionally align image left or right",
                                                icon="file-richtext",
                                                required=False,
                                            ),
                                        ),
                                        (
                                            "link",
                                            wagtail.blocks.URLBlock(
                                                help_text="Optional web address to use as image link.",
                                                required=False,
                                            ),
                                        ),
                                    ],
                                    classname="full title",
                                ),
                            ),
                            (
                                "document",
                                wagtail.documents.blocks.DocumentChooserBlock(),
                            ),
                            (
                                "spacer",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "height",
                                            wagtail.blocks.DecimalBlock(
                                                decimal_places=1,
                                                help_text="The height of this spacer in 'em' values where 1 em is one uppercase M.",
                                                min_value=0,
                                            ),
                                        )
                                    ]
                                ),
                            ),
                        ],
                        use_json_field=True,
                    ),
                ),
                ("publication_date", models.DateField(default=datetime.date.today)),
                (
                    "news_topic",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="news_items",
                        to="news.newstopic",
                    ),
                ),
                (
                    "news_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="news_items",
                        to="news.newstype",
                    ),
                ),
                (
                    "body_migrated",
                    models.TextField(
                        blank=True,
                        help_text="Used only for content from old Drupal website.",
                        null=True,
                    ),
                ),
                (
                    "drupal_node_id",
                    models.PositiveIntegerField(blank=True, db_index=True, null=True),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="NewsItemTag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "content_object",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tagged_items",
                        to="news.newsitem",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(app_label)s_%(class)s_items",
                        to="taggit.tag",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="newsitem",
            name="tags",
            field=modelcluster.contrib.taggit.ClusterTaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="news.NewsItemTag",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
