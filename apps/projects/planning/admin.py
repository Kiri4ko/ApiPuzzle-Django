from apps.projects.planning.models import Planning
from django.contrib import admin


@admin.register(Planning)
class MyProjectAdmin(admin.ModelAdmin):
    pass
