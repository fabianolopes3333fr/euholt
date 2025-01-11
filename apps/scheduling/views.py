from rest_framework import generics
from .models import Scheduling
from .serializers import SchedulingSerializer

class SchedulingListCreate(generics.ListCreateAPIView):
    queryset = Scheduling.objects.all()
    serializer_class = SchedulingSerializer

class SchedulingRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Scheduling.objects.all()
    serializer_class = SchedulingSerializer