# apps/services/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from decimal import Decimal

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    company = models.ForeignKey('accounts.Company', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    duration = models.IntegerField(
        help_text='Duração em minutos',
        validators=[
            MinValueValidator(15),
            MaxValueValidator(480)  # 8 horas
        ]
    )
    category = models.ForeignKey(ServiceCategory, on_delete=models.PROTECT)
    company = models.ForeignKey(
        'accounts.Company',  # Corrigido
        on_delete=models.CASCADE
    )
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.price < 0:
            raise ValidationError('Preço não pode ser negativo')
        if self.duration < 15:
            raise ValidationError('Duração mínima é de 15 minutos')
        if self.duration > 480:
            raise ValidationError('Duração máxima é de 8 horas')

    def __str__(self):
        return self.name