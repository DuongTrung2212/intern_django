from rest_framework import serializers
from .models import Img


class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Img
        fields = "__all__"
