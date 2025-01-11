# apps/services/serializers.py
from rest_framework import serializers
from .models import Company, Professional, Service

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class ProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        fields = '__all__'
        
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'