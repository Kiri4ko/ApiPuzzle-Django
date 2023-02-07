from django.contrib import admin

from apps.projects.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fields = (
        'id', 'project_name', 'company_head', 'company_po', 'user',
    )
    readonly_fields = ('id',)
