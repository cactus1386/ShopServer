from django.urls import path, include
from . import views
# from rest_framework.authtoken.views import ObtainAuthToken

app_name = 'api-v1'

urlpatterns = [
    # registration
    path('registration/', views.RegistrationApiView.as_view(), name='registration'),
    # login token
    path('token/login/', views.ObtainAuthTokenView.as_view(), name='token-login'),
    # login jwt
    # check password
    # reset password
]
