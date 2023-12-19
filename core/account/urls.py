from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='HomeTestPage'),
    path('logout/', views.LogoutView.as_view(), name='LogoutTestPage'),
]
