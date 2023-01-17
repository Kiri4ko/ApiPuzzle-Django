from django.contrib import admin

from apps.projects.models import Project


@admin.register(Project)
class MyProjectAdmin(admin.ModelAdmin):
    pass
