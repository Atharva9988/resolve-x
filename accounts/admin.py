from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('ResolveX Information', {'fields': ('role','organization')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('ResolveX Information', {'fields': ('role','organization')}),
    )

    list_display = ('username', 'email', 'role', 'organization', 'is_active')
    list_filter = ('role', 'organization', 'is_active')