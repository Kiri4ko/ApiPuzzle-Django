from rest_framework import serializers
from .models import HeadCompany


# Create class HeadCompanySerializer
class HeadCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadCompany
        fields = [
            'company_name', 'logo', 'website', 'tagline', 'industry', 'software_stack', 'select_industries',
            'short_description', 'full_description', 'average_hourly_rate', 'minimum_project_budget',
            'team_size', 'location', 'foundation_date', 'clients_focus', 'contact_marketing', 'contact_expert',
            'links_case', 'client_describe', 'employee'
        ]

    # Saving a new user
    def save(self, *args, **kwargs):
        company = HeadCompany(
            company_name=self.validated_data['company_name'],
            logo=self.validated_data['logo'],
            website=self.validated_data['website'],
            tagline=self.validated_data['tagline'],
            industry=self.validated_data['industry'],
            software_stack=self.validated_data['software_stack'],
            select_industries=self.validated_data['select_industries'],
            short_description=self.validated_data['short_description'],
            full_description=self.validated_data['full_description'],
            average_hourly_rate=self.validated_data['average_hourly_rate'],
            minimum_project_budget=self.validated_data['minimum_project_budget'],
            team_size=self.validated_data['team_size'],
            location=self.validated_data['location'],
            foundation_date=self.validated_data['foundation_date'],
            clients_focus=self.validated_data['clients_focus'],
            contact_marketing=self.validated_data['contact_marketing'],
            contact_expert=self.validated_data['contact_expert'],
            links_case=self.validated_data['links_case'],
            client_describe=self.validated_data['client_describe'],
            # employee=self.validated_data['employee'],

        )
        # Save the company
        company.save()
        return company
