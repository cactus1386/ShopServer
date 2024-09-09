from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import LogoSerializer, NavbarSerializer
from .models import Logo, NavbarItem

# Create your views here.


class LogoView(ListAPIView):
    serializer_class = LogoSerializer
    queryset = Logo.objects.all()


class NavbarView(ListAPIView):
    serializer_class = NavbarSerializer
    queryset = NavbarItem.objects.all()
