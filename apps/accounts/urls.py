from django.urls import path
from . import views  # Importe o módulo views do seu app
from .views import UserCreate


app_name = 'accounts'  # Define o namespace do app (opcional, mas recomendado)

urlpatterns = [
    path('register/', UserCreate.as_view(), name='user-register'),
]