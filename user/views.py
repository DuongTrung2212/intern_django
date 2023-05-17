from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializers
from .models import User


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializers
