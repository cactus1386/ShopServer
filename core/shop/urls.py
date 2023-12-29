from django.urls import path, include
from .views import ProductListAPIView

urlpatterns = [
    path('v1/', include("shop.api.v1.urls"), name='api-v1')
]
