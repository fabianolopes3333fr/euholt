# apps/financial/models.py
from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from decimal import Decimal
from django.core.exceptions import ValidationError
from django.db.models import Sum, Q
from datetime import datetime, timedelta
from core.validators import validate_business_hours


class PaymentMethod(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    company = models.ForeignKey('accounts.Company', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class CashFlow(models.Model):
    TYPE_CHOICES = (
        ('income', 'Receita'),
        ('expense', 'Despesa'),
    )

    STATUS_CHOICES = (
        ('pending', 'Pendente'),
        ('paid', 'Pago'),
        ('cancelled', 'Cancelado'),
    )

    description = models.CharField(max_length=200)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    due_date = models.DateField()
    payment_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )
    payment_method = models.ForeignKey(
        PaymentMethod,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    company = models.ForeignKey(
        'accounts.Company',  # Corrigido
        on_delete=models.CASCADE
    )
    appointment = models.ForeignKey(
        'scheduling.Appointment',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        'financial.FinancialCategory',
        on_delete=models.PROTECT
    )
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-due_date', '-created_at']
        indexes = [
            models.Index(fields=['due_date', 'status']),
            models.Index(fields=['type', 'status']),
        ]

    def clean(self):
        if self.payment_date and self.payment_date < self.due_date:
            raise ValidationError(
                'Data de pagamento não pode ser anterior à data de vencimento'
            )

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

class FinancialCategory(models.Model):
    TYPE_CHOICES = (
        ('income', 'Receita'),
        ('expense', 'Despesa'),
        ('both', 'Ambos'),
    )

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    company = models.ForeignKey('accounts.Company', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Financial Categories'

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"