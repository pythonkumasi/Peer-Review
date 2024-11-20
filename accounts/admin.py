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
    # Even though this can add a user in /admin/ you have to programmatically create a password for user.
    # >>> from django.contrib.auth import get_user_model
    # >>> User = get_user_model()
    # >>> u = User.objects.get(username="john")
    # >>> u.set_password("new password")
    # >>> u.save()

    # https://docs.djangoproject.com/en/5.1/topics/auth/default/#changing-passwords


admin.site.register(CustomUser, CustomUserAdmin)
