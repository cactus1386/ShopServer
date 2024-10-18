from django.db import models
from django.conf import settings
from shop.models import Product
from account.models import Address
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items',
                             on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.name

    def get_total_price(self):
        return self.product.price * self.quantity


class OrderModel(models.Model):
    PENDING = "P"
    COMPLETED = "C"

    STATUS_CHOICES = ((PENDING, _("pending")), (COMPLETED, _("completed")))

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='pending')
    complete = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        Address, on_delete=models.SET_NULL, blank=True, null=True, related_name="shipping_orders")

    payment_status = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.email}"

    @cached_property
    def total_cost(self):
        return round(sum([order_item.cost for order_item in self.order_items.all()]), 2)


class OrderItemModel(models.Model):
    order = models.ForeignKey(
        OrderModel, related_name="order_items", on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name="product_order", on_delete=models.CASCADE
    )
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    @staticmethod
    def create_order_item(order, product, quantity, total):
        order_item = OrderItemModel()
        order_item.order = order
        order_item.product = product
        order_item.quantity = quantity
        order_item.total = total
        order_item.save()
        return order_item


# class OrderHistory(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     status = models.CharField(max_length=10, choices=Order.STATUS_CHOICES)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"Order {self.order.id} - Status: {self.status}"
