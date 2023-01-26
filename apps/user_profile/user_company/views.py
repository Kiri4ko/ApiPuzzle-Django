from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from models import HeadCompany
from serializers import HeadCompanySerializer


class HeadCompanyView(viewsets.ModelViewSet):
    queryset = HeadCompany.objects.all()
    serializer_class = HeadCompanySerializer
    permission_classes = [IsAdminUser]
