from rest_framework import serializers
from .models import Img
from django.core.files.storage import default_storage
import os


def remove_folder_from_s3(instance):
    folder_root = "test"
    models_name = "img"
    default_storage.delete(os.path.join(folder_root, models_name))


class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Img
        fields = "__all__"

    def create(self, validated_data):
        remove_folder_from_s3()
        img = validated_data.pop("img", None)
        data = Img.objects.create(**validated_data)
        if img:
            data.img = img
            data.save()

        return data
