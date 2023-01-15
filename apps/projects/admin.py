from apps.projects.models import Project
from django.contrib import admin


@admin.register(Project)
class MyProjectAdmin(admin.ModelAdmin):
    pass

