from rest_framework import serializers

from .models import Project


# Create class ProjectSerialize
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
