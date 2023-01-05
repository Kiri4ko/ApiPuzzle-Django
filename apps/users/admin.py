from django.contrib import admin
from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'full_name', 'email', 'phone', 'user_status',
        'is_active', 'is_staff', 'registered', 'last_login',
    )
    list_filter = ('is_staff', 'is_active', 'user_status',)
    list_display_links = ('full_name', 'email',)
    search_fields = ('email', 'full_name', 'user_status',)
    readonly_fields = ('last_login', 'registered',)
