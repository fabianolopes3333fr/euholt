from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from .models import Appointment
from .serializers import AppointmentSerializer
from django_filters.rest_framework import DjangoFilterBackend

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    filterset_fields = ['date', 'status', 'professional', 'client']
    search_fields = ['client__first_name', 'client__last_name', 'notes']
