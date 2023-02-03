from rest_framework import serializers
from .models import head_company, po_company


# Create class HeadCompanySerializer
class HeadCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = head_company.HeadCompany
        fields = [
            'id', 'company_name', 'logo', 'website', 'tagline', 'client_industry', 'software_stack', 'industry_choice',
            'short_description', 'full_description', 'average_hourly_rate', 'currency_rate', 'minimum_project_budget',
            'currency_budget', 'team_size', 'location', 'foundation_date', 'clients_focus', 'contact_marketing',
            'contact_expert', 'links_case', 'client_describe', 'employees'
        ]


# Create class POCompanySerializer
class POCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = po_company.POCompany
        fields = [
            'id', 'company_name', 'company_size', 'industry_choice', 'development_team',
            'use_outsourcing', 'description_project', 'business_requirements',
            'technological_stack', 'link_competitor', 'start_project', 'used_outsourcing',
            'employees',
        ]
