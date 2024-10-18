from django.contrib import admin
from .models import CartItem, Cart, OrderModel, OrderItemModel

# Register your models here.
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(OrderModel)
admin.site.register(OrderItemModel)
