from django.urls import path, include
from . import views

app_name = 'api-v1'

urlpatterns = [
    # registration
    path('registration/', views.RegistrationApiView.as_view(), 'registration'),
    # login token
    # login jwt
    # check password
    # reset password
]
