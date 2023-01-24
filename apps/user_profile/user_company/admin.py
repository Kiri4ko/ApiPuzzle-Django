from django.contrib import admin

from apps.user_profile.user_company.models import HeadCompany


@admin.register(HeadCompany)
class HeadCompanyAdmin(admin.ModelAdmin):
    fields = (
        'id', 'company_name', 'logo', 'website', 'tagline', 'industry',
        'software_stack', 'select_industries', 'short_description', 'full_description',
        'average_hourly_rate', 'minimum_project_budget', 'team_size', 'location', 'foundation_date',
        'clients_focus', 'contact_marketing', 'contact_expert', 'links_case',
        'client_describe', 'employee',
    )
    readonly_fields = ('id',)
