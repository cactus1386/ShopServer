from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category


class Size(models.Model):
    CHOICES = (
        ("S", "S"),
        ("M", "M"),
        ("L", "L"),
        ("XL", "XL"),
        ("XXL", "XXL"),
        ("3XL", "3XL"),
    )
    size = models.CharField(max_length=255, default="", choices=CHOICES)

    def __str__(self):
        return self.size


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    discount = models.IntegerField()
    pic = models.CharField(max_length=255, null=True, blank=True)
    count = models.IntegerField(default=10)
    material = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    size = models.ManyToManyField(Size)
    created_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_api_url(self):
        return reverse("shop:api-v1:product-detail", kwargs={"pk": self.pk})
    


class Images(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images_set"
    )
    image = models.CharField(max_length=255, blank=True, null=True, default="")

    def __str__(self):
        return self.image


class Color(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="colors_set"
    )
    color = models.CharField(max_length=255, blank=True, null=True, default="")

    def __str__(self):
        return self.color
