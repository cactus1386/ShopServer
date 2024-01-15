from django.urls import path, include

app_name = 'shop'

urlpatterns = [
    path('api/', include("shop.api.v1.urls"), name='api-v1')
]
