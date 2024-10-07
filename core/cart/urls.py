from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartViewSet, OrderView, OrderItemView

router = DefaultRouter()
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'orders', OrderView, basename='order')
router.register(r'order-items', OrderItemView, basename='order-items')

urlpatterns = [
    path('', include(router.urls)),
]
