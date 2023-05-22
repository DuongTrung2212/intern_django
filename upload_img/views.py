from django.shortcuts import render
import time
from rest_framework import status, viewsets
from rest_framework.response import Response
from django.core.files.storage import default_storage
from .serializers import UploadSerializer
from .models import Img
from rest_framework.response import Response


# Create your views here.
class UploadViewSet(viewsets.ModelViewSet):
    queryset = Img.objects.all()
    serializer_class = UploadSerializer
