from django.contrib import admin
from apps.users.models import User
from django.utils.translation import gettext as _
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class MyUserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'full_name', 'email', 'phone', 'user_status',
        'is_active', 'is_staff', 'group', 'registered', 'last_login',
    )
    fieldsets = (
        (None, {'fields': ('id',)}),
        (_('Personal Info'), {'fields': ('full_name', 'email', 'phone', 'user_status')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important Dates'), {'fields': ('registered', 'last_login',)}),
        (_('Secret Data'), {'fields': ('password',)}),
    )
    readonly_fields = ('id', 'registered')
    list_filter = ('user_status', 'groups', 'is_staff', 'is_active')
    list_display_links = ('id', 'email', 'full_name')
    search_fields = ('email', 'full_name', 'user_status',)
    list_editable = ('is_staff', 'is_active')
    filter_horizontal = ('groups', 'user_permissions',)
    save_on_top = True

    #  Getting the user's group
    def group(self, obj):
        user_group = obj.groups.values()
        return '\n'.join([name.get('name') for name in user_group])

    group.short_description = 'Groups'

    ordering = ('email',)

    # fields = (
    #     'id', 'full_name', 'email', 'phone', 'user_status',
    #     'is_active', 'is_staff', 'is_superuser', 'groups',
    #     'user_permissions', 'registered', 'last_login', 'password',
    # )
