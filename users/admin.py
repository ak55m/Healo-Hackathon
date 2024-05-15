from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_admin', 'is_user', 'is_doctor')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_admin', 'is_user', 'is_doctor')}),
    )

admin.site.register(User, CustomUserAdmin)