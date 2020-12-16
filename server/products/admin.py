from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
# Register your models here.
from .models import Product, User


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    pass

@admin.register(Product)
class MovieAdmin(admin.ModelAdmin):
    fields = (
        "naziv", "kategorija", "godina", "created_at", "updated_at",
    )
    list_display = (
        "naziv", "kategorija", "godina", "created_at", "updated_at",

    )
    readonly_fields = (
        "created_at", "updated_at",
    )