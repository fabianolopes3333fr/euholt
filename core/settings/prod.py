from .base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['.euholt.com', 'www.euholt.com'] # Adicione seus domínios aqui

# Configuração do banco de dados PostgreSQL (usando dj_database_url)
DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}

# Configurações de email (usando um serviço de email real, como SendGrid, Mailgun, etc.)
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.sendgrid.net' # Exemplo
# EMAIL_PORT = 587 # Exemplo
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

# Configurações de segurança
SECURE_SSL_REDIRECT = True  # Redirecionar HTTP para HTTPS
SESSION_COOKIE_SECURE = True # Cookie de sessão apenas por HTTPS
CSRF_COOKIE_SECURE = True  # Cookie CSRF apenas por HTTPS
SECURE_HSTS_SECONDS = 31536000  # HSTS (HTTP Strict Transport Security)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Configurações do CORS
CORS_ALLOWED_ORIGINS = [
    "https://euholt.com",  # Adicione o domínio do seu frontend em produção
]