from rest_framework import serializers
from .models.head_company import HeadCompany
from .models.po_company import POCompany


# Create class HeadCompanySerializer
class HeadCompanySerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=False, read_only=True)

    class Meta:
        model = HeadCompany
        fields = [
            'id', 'company_name', 'logo', 'website', 'tagline', 'client_industry', 'software_stack', 'industry_choice',
            'short_description', 'full_description', 'average_hourly_rate', 'currency_rate', 'minimum_project_budget',
            'currency_budget', 'team_size', 'location', 'foundation_date', 'clients_focus', 'contact_marketing',
            'contact_expert', 'links_case', 'client_describe', 'employees', 'owner', 'is_active'
        ]


# Create class POCompanySerializer
class POCompanySerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=False, read_only=True)

    class Meta:
        model = POCompany
        fields = [
            'id', 'company_name', 'company_size', 'industry_choice', 'development_team',
            'use_outsourcing', 'description_project', 'business_requirements',
            'technological_stack', 'link_competitor', 'start_project', 'used_outsourcing',
            'owner', 'is_active'
        ]
