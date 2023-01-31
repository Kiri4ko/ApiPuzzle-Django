from django.contrib import admin

from .models import head_company, po_company


@admin.register(head_company.HeadCompany)
class HeadCompanyAdmin(admin.ModelAdmin):
    fields = (
        'id', 'company_name', 'logo', 'website', 'tagline', 'industry',
        'software_stack', 'select_industries', 'short_description', 'full_description',
        'average_hourly_rate', 'minimum_project_budget', 'team_size', 'location', 'foundation_date',
        'clients_focus', 'contact_marketing', 'contact_expert', 'links_case',
        'client_describe', 'employees',
    )
    readonly_fields = ('id',)
    filter_horizontal = ['employees']


@admin.register(po_company.POCompany)
class POCompanyAdmin(admin.ModelAdmin):
    fields = (
        'id', 'company_name', 'company_size', 'company_industry', 'development_team',
        'use_outsourcing', 'description_project', 'business_requirements',
        'technological_stack', 'link_competitor', 'start_project', 'used_outsourcing',
        'employees',
    )
    readonly_fields = ('id',)
    filter_horizontal = ['employees']
