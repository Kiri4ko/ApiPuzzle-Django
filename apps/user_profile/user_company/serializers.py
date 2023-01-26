from rest_framework import serializers
from .models import HeadCompany


# Create class HeadCompanySerializer
class HeadCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadCompany
        fields = [
            'id', 'company_name', 'logo', 'website', 'tagline', 'industry', 'software_stack', 'select_industries',
            'short_description', 'full_description', 'average_hourly_rate', 'currency_rate', 'minimum_project_budget',
            'currency_budget', 'team_size', 'location', 'foundation_date', 'clients_focus', 'contact_marketing',
            'contact_expert', 'links_case', 'client_describe', 'employees'
        ]
