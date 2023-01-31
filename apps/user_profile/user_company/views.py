from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .models import head_company, po_company
from .serializers import HeadCompanySerializer, POCompanySerializer


class HeadCompanyView(viewsets.ModelViewSet):
    queryset = head_company.HeadCompany.objects.all()
    serializer_class = HeadCompanySerializer
    permission_classes = [IsAdminUser]


class POCompanyView(viewsets.ModelViewSet):
    queryset = po_company.POCompany.objects.all()
    serializer_class = POCompanySerializer
    permission_classes = [IsAdminUser]
