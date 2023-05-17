from django.shortcuts import render
from rest_framework import viewsets
from .models import Tour
from .serializers import TourSerializers


# Create your views here.
class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.filter(active=True)
    serializer_class = TourSerializers
