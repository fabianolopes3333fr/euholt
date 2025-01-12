from .base import *
from decouple import config

DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]

# Configuração do banco de dados PostgreSQL para desenvolvimento
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}

# Configurações de email (console para desenvolvimento)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Configurações do CORS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # Porta do frontend em desenvolvimento
    "http://localhost:3000",  # Porta alternativa comum para React
]