# apps/financial/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum, Q
from django.utils import timezone
from datetime import datetime, timedelta
from .models import CashFlow, PaymentMethod, FinancialCategory
from .serializers import (
    CashFlowSerializer,
    PaymentMethodSerializer,
    FinancialCategorySerializer
)
from django_filters.rest_framework import DjangoFilterBackend

class CashFlowViewSet(viewsets.ModelViewSet):
    queryset = CashFlow.objects.all()
    serializer_class = CashFlowSerializer
    filterset_fields = ['type', 'status', 'category', 'payment_method']
    search_fields = ['description', 'notes']

    def get_queryset(self):
        return super().get_queryset().filter(
            company=self.request.user.company
        )

    @action(detail=False, methods=['get'])
    def dashboard(self, request):
        today = timezone.now().date()
        thirty_days_ago = today - timedelta(days=30)
        
        # Totais do mês
        month_incomes = self.get_queryset().filter(
            type='income',
            status='paid',
            payment_date__month=today.month
        ).aggregate(total=Sum('amount'))['total'] or 0

        month_expenses = self.get_queryset().filter(
            type='expense',
            status='paid',
            payment_date__month=today.month
        ).aggregate(total=Sum('amount'))['total'] or 0

        # Pendências
        pending_incomes = self.get_queryset().filter(
            type='income',
            status='pending',
            due_date__lte=today
        ).aggregate(total=Sum('amount'))['total'] or 0

        pending_expenses = self.get_queryset().filter(
            type='expense',
            status='pending',
            due_date__lte=today
        ).aggregate(total=Sum('amount'))['total'] or 0

        return Response({
            'month_summary': {
                'incomes': month_incomes,
                'expenses': month_expenses,
                'balance': month_incomes - month_expenses
            },
            'pending': {
                'incomes': pending_incomes,
                'expenses': pending_expenses
            }
        })

class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer

    def get_queryset(self):
        return super().get_queryset().filter(
            company=self.request.user.company
        )

class FinancialCategoryViewSet(viewsets.ModelViewSet):
    queryset = FinancialCategory.objects.all()
    serializer_class = FinancialCategorySerializer

    def get_queryset(self):
        return super().get_queryset().filter(
            company=self.request.user.company
        )