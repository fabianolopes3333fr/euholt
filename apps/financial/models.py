from django.db import models
from apps.scheduling.models import Scheduling

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    )

    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    scheduling = models.ForeignKey(Scheduling, on_delete=models.SET_NULL, null=True, blank=True) # Relação com agendamento, se aplicavel

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} on {self.date}"