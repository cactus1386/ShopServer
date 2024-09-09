from django.urls import path
from .views import LogoView

urlpatterns = [
    path('logo/<int:pk>', LogoView.as_view(), name='logo-url')
]
