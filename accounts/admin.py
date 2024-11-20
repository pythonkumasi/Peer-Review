from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = [
        "email",
        "username",
        "role",
        "is_staff",
        "is_active",
    ]
    fields = [
        "email",
        "username",
        "role",
        "is_staff",
        "password",
    ]


admin.site.register(CustomUser, CustomUserAdmin)
