from django.urls import path, include
from . import views

app_name = "api-v1"

urlpatterns = [
    path("v1/products/", views.ProductList.as_view(), name="product-list"),
    path(
        "v1/products/<int:pk>/",
        views.ProductDetail.as_view(),
        name="product-detail",
    ),
    path('v1/prices/<int:pk>/', views.PriceHistory.as_view(), name="price-history")
]
