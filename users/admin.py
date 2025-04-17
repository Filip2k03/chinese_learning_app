from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'is_premium', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_premium',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('is_premium',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
