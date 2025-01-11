from django.urls import path
from .views import SchedulingListCreate, SchedulingRetrieveUpdateDestroy

urlpatterns = [
    path('scheduling/', SchedulingListCreate.as_view(), name='scheduling-list-create'),
    path('scheduling/<int:pk>/', SchedulingRetrieveUpdateDestroy.as_view(), name='scheduling-retrieve-update-destroy'),
]