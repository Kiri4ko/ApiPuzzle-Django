from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .models.head_company import HeadCompany
from .models.po_company import POCompany
from .serializers import HeadCompanySerializer, POCompanySerializer
from rest_framework.pagination import PageNumberPagination


class HeadCompanyView(viewsets.ModelViewSet):
    queryset = HeadCompany.objects.all()
    serializer_class = HeadCompanySerializer
    permission_classes = [IsAdminUser]
    pagination_class = PageNumberPagination


class POCompanyView(viewsets.ModelViewSet):
    queryset = POCompany.objects.all()
    serializer_class = POCompanySerializer
    permission_classes = [IsAdminUser]
    pagination_class = PageNumberPagination
