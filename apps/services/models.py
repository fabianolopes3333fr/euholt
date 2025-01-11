# apps/services/models.py
from django.db import models
#from .models import Company

class Company(models.Model):
    name = models.CharField(max_length=255)
    # Outros campos...

    def __str__(self):
        return self.name

class Professional(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    # Outros campos...

    def __str__(self):
        return self.name
    
    
class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(help_text="Duração em minutos")
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name