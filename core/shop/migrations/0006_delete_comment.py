# Generated by Django 4.2.7 on 2023-12-18 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0005_alter_comment_options_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Comment",
        ),
    ]
