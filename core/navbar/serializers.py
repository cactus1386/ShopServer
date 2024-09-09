from rest_framework import serializers
from .models import Logo, NavbarItem


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = ('id', 'image', 'created_at',)


class NavbarSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavbarItem
        fields = ('id', 'name', 'icon', 'url', 'created_at')
