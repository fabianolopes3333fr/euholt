from django.urls import path
from .views import TransactionListCreate, TransactionRetrieveUpdateDestroy

urlpatterns = [
    path('transactions/', TransactionListCreate.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', TransactionRetrieveUpdateDestroy.as_view(), name='transaction-retrieve-update-destroy'),
]