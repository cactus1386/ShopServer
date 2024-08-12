from rest_framework import serializers
from ...models import Product, Images, Color, Size, PriceHistory


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ("id", "image")


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ("id", "color")


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ("id", "size")


class PriceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceHistory
        fields = ('old_price', 'new_price', 'date')


class ProductSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True, read_only=True, source="images_set")
    colors = ColorSerializer(many=True, read_only=True, source="colors_set")
    size = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    relative_url = serializers.URLField(
        source="get_absolute_api_url", read_only=True
    )
    price_histories = PriceHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "price",
            "discount",
            "pic",
            "count",
            "material",
            "brand",
            "description",
            "images",
            "colors",
            "size",
            "category",
            "relative_url",
            "price_histories",
        )

    def get_size(self, instance):
        return instance.size.values_list("size", flat=True)

    def get_category(self, instance):
        return instance.category.values_list("category", flat=True)

    def update(self, instance, validated_data):
        # Extract the new price from validated data
        new_price = validated_data.get('price', instance.price)

        # Check if the price has changed
        if instance.price != new_price:
            # Create a PriceHistory entry
            PriceHistory.objects.create(
                product=instance,
                old_price=instance.price,
                new_price=new_price,
                date=timezone.now()
            )

        # Update the product instance
        return super().update(instance, validated_data)
