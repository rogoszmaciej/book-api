from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from book_api.users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_display = ["id", "email", "username", "is_superuser", "is_active"]
    list_filter = ["is_active", "is_superuser"]
    fieldsets = (
        (None, {"fields": ["email", "password"]}),
        (
            _("Personal info"),
            {"fields": ["username"]}
        ),
        (
            _("Permissions"),
            {"fields": ["is_active", "is_staff", "is_superuser", "groups"]}
        ),
    )
    search_fields = ["email", "user_name"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    "email", "username", "is_active", "is_staff", "is_superuser",
                    "password1", "password2"
                ]
            }
        ),
    )
