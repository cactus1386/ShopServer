from django.urls import path
from .views import LogoView, NavbarView

urlpatterns = [
    path('logo/<int:pk>', LogoView.as_view(), name='logo-url'),
    path('items/', NavbarView.as_view(), name='navbar-items'),
]
