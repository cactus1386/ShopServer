# Generated by Django 4.2.7 on 2023-12-15 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0003_comment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="name",
        ),
        migrations.RemoveField(
            model_name="comment",
            name="product",
        ),
    ]
