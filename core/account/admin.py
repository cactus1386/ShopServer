from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_staff', 'is_active')
    list_filter = ('email', 'is_staff', 'is_active')
    searching_fields = ('email', )
    ordering = ('email',)


admin.site.register(User, CustomAdmin)