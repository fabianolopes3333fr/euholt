# apps/financial/serializers.py
from rest_framework import serializers
from .models import CashFlow, PaymentMethod, FinancialCategory
from django.db.models import Sum
from decimal import Decimal

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'

class FinancialCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialCategory
        fields = '__all__'

class CashFlowSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source='category.name',
        read_only=True
    )
    payment_method_name = serializers.CharField(
        source='payment_method.name',
        read_only=True
    )

    class Meta:
        model = CashFlow
        fields = '__all__'

    def validate(self, data):
        if data.get('payment_date'):
            if data['payment_date'] < data['due_date']:
                raise serializers.ValidationError(
                    'Data de pagamento não pode ser anterior à data de vencimento'
                )
        return data