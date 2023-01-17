from django.contrib import admin

from apps.projects.planning.models import Planning


@admin.register(Planning)
class MyProjectAdmin(admin.ModelAdmin):
    pass
