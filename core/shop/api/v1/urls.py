from django.urls import path, include
from . import views

app_name = 'api-v1'

urlpatterns = [
    path('products/', views.ProductList.as_view(), name='product-list'),
    path('products/<int:id>/', views.productDetail, name='product-detail'),
]
