from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import LogoSerializer
from .models import Logo

# Create your views here.


class LogoView(ListAPIView):
    serializer_class = LogoSerializer
    queryset = Logo.objects.all()
