from django.urls import path, include

app_name = "account"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path('api/v1/', include('account.api.v1.urls'), name='account'),
    # path("api/v2/", include("djoser.urls")),
    # path("api/v2/", include("djoser.urls.jwt")),
]
