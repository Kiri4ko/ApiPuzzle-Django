from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer


# Create class RegistrUserView
class ProjectView(viewsets.ModelViewSet):
    pass
