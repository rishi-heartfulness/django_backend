from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'groups')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('email',)

    # Fields shown when editing a user
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'address', 'phone')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # Fields shown when creating a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'address', 'phone', 'password1', 'password2', 'is_staff', 'is_active', 'groups')}
        ),
    )






    