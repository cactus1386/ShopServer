# Generated by Django 4.2.7 on 2024-09-09 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("navbar", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="NavbarItem",
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
                ("name", models.CharField(max_length=20)),
                ("url", models.URLField()),
                ("icon", models.CharField(blank=True, max_length=255, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
