from rest_framework import serializers
from .models import Project
from apps.users.models import User
from ..user_profile.user_company.models.head_company import HeadCompany
from ..user_profile.user_company.models.po_company import POCompany


# Create class ProjectSerialize
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = 'project_name', 'company_head', 'company_po', 'user'
        extra_kwargs = {
            'company_head': {'read_only': True},
            'company_po': {'read_only': True},
            'user': {'read_only': True},
        }

    #  Create company id based on user id
    def create(self, validated_data):
        user = User.objects.get(id=self.context['request'].user.id)
        instance_user = User.objects.get(id=user.id)
        if 'Product Owner' in user.role:
            company_id = user.company_po.first().id
            instance_po = POCompany.objects.get(id=company_id)
            project = Project(
                project_name=validated_data['project_name'],
                company_po=instance_po,
            )
            project.save()
            project.user.add(instance_user.id)
            return project
        else:
            company_id = user.companies_head.first().id
            instance_head = HeadCompany.objects.get(id=company_id)
            project = Project(
                project_name=validated_data['project_name'],
                company_head=instance_head,
            )
            project.save()
            project.user.add(instance_user.id)
            return project

    def update(self, instance, validated_data):
        instance.project_name = validated_data.get('project_name', instance.project_name)
        instance.save()
        return instance
