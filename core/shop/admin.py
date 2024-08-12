from django.contrib import admin
from .models import Product, Images, Color, Size, Category, PriceHistory
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Images)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Category)
admin.site.register(PriceHistory)


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    list_display = ("name", "price", "count", "brand")
    list_filter = ("brand",)
    search_fields = ("name", "description", "brand", "material")
    summernote_fields = "__all__"
