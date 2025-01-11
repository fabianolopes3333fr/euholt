from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Adicione related_name aos campos groups e user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="%(app_label)s_%(class)s_related",  # Adicione esta linha
        related_query_name="%(app_label)s_%(class)ss",  # Adicione esta linha
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name="%(app_label)s_%(class)s_related",  # Adicione esta linha
        related_query_name="%(app_label)s_%(class)ss",  # Adicione esta linha
    )

    def __str__(self):
        return self.email