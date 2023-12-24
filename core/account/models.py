from django.db import models
from django.contrib.auth.models import AbstractUser

# class CustomUser(AbstractUser):
#     name = models.CharField(max_length=80)
#     last_name = models.CharField(max_length=80)
#     birth_date = models.DateField(null=True, blank=True)
#     profile_pic = models.ImageField(upload_to='profile_pic/' ,null=True, blank=True)
#     username = models.CharField(max_length=50, unique=True)
#     email = models.EmailField(max_length=100, unique=True)
#     phone_num = models.IntegerField(null=True, blank=True, unique=True)
#     password = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.username
