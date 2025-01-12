from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
#from core.validators import validate_document


class User(AbstractUser):
    company = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE,
        null=True,
        related_name='employees'
    )
    phone = models.CharField(max_length=20, blank=True)
    is_staff_member = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.is_staff_member and not self.is_staff:
            self.is_staff = True
        super().save(*args, **kwargs)
    
    class Meta:
        app_label = 'accounts'

class Company(models.Model):
    name = models.CharField(max_length=200)
    document = models.CharField(
        max_length=20,
        unique=True,
        validators=[validate_document],
        help_text='CNPJ da empresa (apenas números)'

        
    )
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    active = models.BooleanField(default=True)
    business_hours_start = models.TimeField(default='08:00')
    business_hours_end = models.TimeField(default='20:00')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.business_hours_start >= self.business_hours_end:
            raise ValidationError(
                'Horário de início deve ser anterior ao horário de término'
            )

    class Meta:
        verbose_name_plural = 'Companies'
        indexes = [
            models.Index(fields=['document']),
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name