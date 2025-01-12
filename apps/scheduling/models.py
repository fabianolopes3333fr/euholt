# apps/scheduling/models.py
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime, timedelta
from django.db.models import Q
from core.validators import validate_business_hours, validate_future_date


class Appointment(models.Model):
    STATUS_CHOICES = (
        ('scheduled', 'Agendado'),
        ('confirmed', 'Confirmado'),
        ('in_progress', 'Em Andamento'),
        ('completed', 'Concluído'),
        ('cancelled', 'Cancelado'),
    )

    client = models.ForeignKey(
        'accounts.User',  # Corrigido
        on_delete=models.CASCADE,
        related_name='appointments_as_client'
    )
    service = models.ForeignKey('services.Service', on_delete=models.PROTECT)
    professional = models.ForeignKey(
        'accounts.User',  # Corrigido
        on_delete=models.CASCADE,
        related_name='appointments_as_professional'
    )
    date = models.DateField(validators=[validate_future_date])
    start_time = models.TimeField(validators=[validate_business_hours])
    end_time = models.TimeField(validators=[validate_business_hours])
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='scheduled'
    )
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date', 'start_time']
        indexes = [
            models.Index(fields=['date', 'start_time']),
            models.Index(fields=['professional', 'date']),
        ]

    def clean(self):
        if self.start_time and self.end_time:
            if self.start_time >= self.end_time:
                raise ValidationError(
                    'Horário de início deve ser anterior ao horário de término'
                )
            
            # Verifica conflito de horários
            conflicts = Appointment.objects.filter(
                professional=self.professional,
                date=self.date,
                status__in=['scheduled', 'confirmed', 'in_progress']
            ).exclude(id=self.id)

            for appointment in conflicts:
                if (self.start_time < appointment.end_time and 
                    self.end_time > appointment.start_time):
                    raise ValidationError(
                        'Existe um conflito de horário com outro agendamento'
                    )
    def __str__(self):
        return f"{self.client} - {self.service} - {self.date}"

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)