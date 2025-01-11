# apps/services/views.py
from rest_framework import generics
from .models import Company, Professional, Service
from .serializers import CompanySerializer, ProfessionalSerializer, ServiceSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser



class CompanyListCreate(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

class CompanyRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAdminUser]

class ProfessionalListCreate(generics.ListCreateAPIView):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer

class ProfessionalRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer
    
class ServiceListCreate(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer