from django.urls import path, include
from . import views

app_name = 'api-v1'

urlpatterns = [
    path('product/', views.productList, name='product-list'),
    path('product/<int:id>/', views.productDetail, name='product-detail'),
]
