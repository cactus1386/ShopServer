from django.db import models

# Create your models here.


class Logo(models.Model):
    image = models.ImageField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)


class NavbarItem(models.Model):
    name = models.CharField(max_length=20)
    url = models.URLField(max_length=200)
    icon = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
