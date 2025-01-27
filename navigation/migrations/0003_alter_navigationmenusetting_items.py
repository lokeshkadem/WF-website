# Generated by Django 3.2.13 on 2022-04-26 08:37

import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("navigation", "0002_auto_20220426_0835"),
    ]

    operations = [
        migrations.AlterField(
            model_name="navigationmenusetting",
            name="items",
            field=wagtail.fields.StreamField(
                [
                    (
                        "internal_page",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                ("page", wagtail.blocks.PageChooserBlock()),
                                (
                                    "anchor",
                                    wagtail.blocks.CharBlock(
                                        help_text="For linking to specific page elements. Enter the anchor text without the leading '#' symbol.",
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "external_link",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                ("url", wagtail.blocks.URLBlock()),
                                (
                                    "anchor",
                                    wagtail.blocks.CharBlock(
                                        help_text="For linking to specific page elements. Enter the anchor text without the leading '#' symbol.",
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "drop_down",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                (
                                    "items",
                                    wagtail.blocks.StreamBlock(
                                        [
                                            (
                                                "page",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "title",
                                                            wagtail.blocks.CharBlock(),
                                                        ),
                                                        (
                                                            "page",
                                                            wagtail.blocks.PageChooserBlock(),
                                                        ),
                                                        (
                                                            "anchor",
                                                            wagtail.blocks.CharBlock(
                                                                help_text="For linking to specific page elements. Enter the anchor text without the leading '#' symbol.",
                                                                required=False,
                                                            ),
                                                        ),
                                                    ]
                                                ),
                                            ),
                                            (
                                                "external_link",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "title",
                                                            wagtail.blocks.CharBlock(),
                                                        ),
                                                        (
                                                            "url",
                                                            wagtail.blocks.URLBlock(),
                                                        ),
                                                        (
                                                            "anchor",
                                                            wagtail.blocks.CharBlock(
                                                                help_text="For linking to specific page elements. Enter the anchor text without the leading '#' symbol.",
                                                                required=False,
                                                            ),
                                                        ),
                                                    ]
                                                ),
                                            ),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                ]
            ),
        ),
    ]
