from rest_framework import serializers
from shop.api.v1.serializers import ProductSerializer
from .models import Cart, CartItem, Order, OrderItem


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ('id', 'user', 'created_at', 'items', 'total_price')

    def get_total_price(self, obj):
        return obj.get_total_price()


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'get_total', 'date_added']


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(
        many=True, read_only=True, source='orderitem_set')

    class Meta:
        model = Order
        fields = ['id', 'user', 'date_ordered', 'status', 'complete', 'shipping_address',
                  'payment_status', 'transaction_id', 'get_cart_total',
                  'get_cart_items', 'order_items']

    def create(self, validated_data):
        order_items_data = validated_data.pop('orderitem_set')
        order = Order.objects.create(**validated_data)
        for item_data in order_items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order
