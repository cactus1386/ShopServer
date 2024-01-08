"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt import views as jwt_views


schema_view = get_schema_view(
   openapi.Info(
      title="Shop API",
      default_version='v1',
      description="The schema view for API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="cactusinjast@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', include('account.urls')),
    path("admin/", admin.site.urls),
    path("summernote/", include("django_summernote.urls")),
    path("api/", include('shop.urls')),
    path('', include('comment.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# path('token/', 
#       jwt_views.TokenObtainPairView.as_view(), 
#       name ='token_obtain_pair'),
# path('token/refresh/', 
#       jwt_views.TokenRefreshView.as_view(), 
#       name ='token_refresh'),