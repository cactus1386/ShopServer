# Generated by Django 4.2.7 on 2023-11-06 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Banner",
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
                ("link", models.CharField(max_length=255)),
                ("image", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Category",
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
                ("category", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Size",
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
                    "size",
                    models.CharField(
                        choices=[
                            ("S", "S"),
                            ("M", "M"),
                            ("L", "L"),
                            ("XL", "XL"),
                            ("XXL", "XXL"),
                            ("3XL", "3XL"),
                        ],
                        default="",
                        max_length=255,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Sliders",
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
                ("link", models.CharField(max_length=255)),
                ("image", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=255)),
                ("price", models.IntegerField()),
                ("discount", models.IntegerField()),
                ("pic", models.CharField(blank=True, max_length=255, null=True)),
                ("count", models.IntegerField(default=10)),
                ("material", models.CharField(max_length=255)),
                ("brand", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("category", models.ManyToManyField(to="shop.category")),
                ("size", models.ManyToManyField(to="shop.size")),
            ],
        ),
        migrations.CreateModel(
            name="Images",
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
                    "image",
                    models.CharField(blank=True, default="", max_length=255, null=True),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images_set",
                        to="shop.product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Color",
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
                    "color",
                    models.CharField(blank=True, default="", max_length=255, null=True),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="colors_set",
                        to="shop.product",
                    ),
                ),
            ],
        ),
    ]
