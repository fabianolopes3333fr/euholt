from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Service, ServiceCategory
from .serializers import ServiceSerializer, ServiceCategorySerializer
from django_filters.rest_framework import DjangoFilterBackend

class ServiceCategoryViewSet(viewsets.ModelViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
    filterset_fields = ['company', 'active']
    search_fields = ['name', 'description']

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filterset_fields = ['category', 'company', 'active']
    search_fields = ['name', 'description']