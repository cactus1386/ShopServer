from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from .users import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    family = models.CharField(
        max_length=255, null=True, blank=True, default='')
    image = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.phone


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class Address(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.TextField()
    ostan = models.CharField(max_length=255)
    shahr = models.CharField(max_length=255)
    postcode = models.IntegerField(default=None)
    phone_number = models.CharField(max_length=255, default=None)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
