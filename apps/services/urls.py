# apps/services/urls.py
from django.urls import path
from .views import CompanyListCreate, CompanyRetrieveUpdateDestroy, ProfessionalListCreate, ProfessionalRetrieveUpdateDestroy, ServiceListCreate, ServiceRetrieveUpdateDestroy

urlpatterns = [
    path('companies/', CompanyListCreate.as_view(), name='company-list-create'),
    path('companies/<int:pk>/', CompanyRetrieveUpdateDestroy.as_view(), name='company-retrieve-update-destroy'),
    path('professionals/', ProfessionalListCreate.as_view(), name='professional-list-create'),
    path('professionals/<int:pk>/', ProfessionalRetrieveUpdateDestroy.as_view(), name='professional-retrieve-update-destroy'),
    path('services/', ServiceListCreate.as_view(), name='service-list-create'),
    path('services/<int:pk>/', ServiceRetrieveUpdateDestroy.as_view(), name='service-retrieve-update-destroy'),
]