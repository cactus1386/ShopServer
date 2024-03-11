# Generated by Django 4.2.7 on 2024-03-11 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0005_profile_address"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="first_name",
            new_name="name",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="last_name",
        ),
        migrations.AddField(
            model_name="profile",
            name="phone",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
