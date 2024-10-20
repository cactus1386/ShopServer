from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# from rest_framework.authtoken.views import ObtainAuthToken

app_name = "api-v1"

urlpatterns = [
    # registration
    path(
        "registration/",
        views.RegistrationApiView.as_view(),
        name="registration",
    ),
    # login token
    # path(
    #     "token/login/",
    #     views.ObtainAuthTokenView.as_view(),
    #     name="token-login",
    # ),
    path(
        "token/logout/",
        views.CustomDiscardAuthToken.as_view(),
        name="token-logout",
    ),
    # login jwt
    path(
        "jwt/create/",
        views.CustomTokenObtainPairView.as_view(),
        name="JWT-token-create",
    ),
    path(
        "jwt/refresh/", TokenRefreshView.as_view(), name="JWT-token-refresh"
    ),
    path("jwt/verify/", TokenVerifyView.as_view(), name="JWT-token-verify"),
    # change password
    path(
        "password-change/",
        views.ChangePasswordApiView.as_view(),
        name="change-password",
    ),
    # Profile
    path("profile/<int:pk>", views.ProfileApiView.as_view(), name="profile"),
    path("address/", views.AddressApiView.as_view(), name="address"),

    # path('test-email/', views.TestEmail.as_view(), name='test-email')
    # Activation
    # Resend activation
]
