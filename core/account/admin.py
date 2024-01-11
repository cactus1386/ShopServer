from django.contrib import admin
from .models import User, Profile
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class CustomAdmin(UserAdmin):
    model = User
    list_display = ("email", "is_staff", "is_active")
    list_filter = ("email", "is_staff", "is_active")
    searching_fields = ("email",)
    ordering = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser")}),
        ("group permissions", {"fields": ("groups", "user_permissions")}),
        ("login date", {"fields": ("last_login",)}),

    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", 'is_superuser'
            )}
        ),
    )

admin.site.register(User, CustomAdmin)
admin.site.register(Profile)