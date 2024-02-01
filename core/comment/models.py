from django.db import models
from shop.models import Product

from django.contrib.auth.models import User


# Create your models here.
class Comment(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    # post = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
