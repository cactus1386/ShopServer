# Generated by Django 4.2.7 on 2024-07-12 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0007_product_created_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="images",
            name="image",
            field=models.ImageField(upload_to="uploads/"),
        ),
        migrations.AlterField(
            model_name="product",
            name="pic",
            field=models.ImageField(upload_to="uploads/"),
        ),
    ]
