from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .models import head_company, po_company
from .serializers import HeadCompanySerializer, POCompanySerializer
from rest_framework.pagination import PageNumberPagination


class HeadCompanyView(viewsets.ModelViewSet):
    queryset = head_company.HeadCompany.objects.all()
    serializer_class = HeadCompanySerializer
    permission_classes = [IsAdminUser]
    pagination_class = PageNumberPagination


class POCompanyView(viewsets.ModelViewSet):
    queryset = po_company.POCompany.objects.all()
    serializer_class = POCompanySerializer
    permission_classes = [IsAdminUser]
    pagination_class = PageNumberPagination
