# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'staff_category')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'staff_category', 'is_staff', 'is_superuser')}
        ),
    )
    list_display = ('email', 'staff_category', 'is_staff')
    ordering = ('email',)

    def has_change_permission(self, request, obj=None):
        """
        Allow only users with the 'supperadmin' category to change other users.
        """
        if obj and obj != request.user and not request.user.can_reset_password():
            return False
        return super().has_change_permission(request, obj)

admin.site.register(CustomUser, CustomUserAdmin)
