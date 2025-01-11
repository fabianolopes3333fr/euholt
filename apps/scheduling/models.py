from django.db import models
from apps.services.models import Service, Professional  # Importe os modelos necessários
from django.conf import settings

class Scheduling(models.Model):
    STATUS_CHOICES = (
        ('scheduled', 'Scheduled'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
        ('completed', 'Completed'),
    )

    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True) # Relação com o Usuário, você pode optar por criar um modelo separado para `Cliente`
    professional = models.ForeignKey(Professional, on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.service} with {self.professional} on {self.date} at {self.start_time}"