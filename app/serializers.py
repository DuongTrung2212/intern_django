from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.http import JsonResponse
from django.core.validators import validate_email
from .models import *


class UserSerializers(ModelSerializer):
    confirm_password = serializers.CharField(
        required=True,
        write_only=True,
        max_length=20,
        min_length=6,
        error_messages={
            "blank": "empty",
            "required": "required",
            "max_length": "max_length",
            "min_length": "min_length",
        },
    )

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "username",
            "password",
            "avatar",
            "gender",
            "address",
            "confirm_password"
            # "is_superuser",
        ]
        # exclude = ["confirm_password"]
        extra_kwargs = {
            "password": {"write_only": "true"},
            # "confirm_password": {"read_only": "true"},
        }

    def validate(self, attrs):
        phone = attrs.get("phone", None)
        if User.objects.filter(phone=phone):
            raise serializers.ValidationError({"phone": "unique"})
        attrs.pop("confirm_password", None)
        return attrs

    def create(self, validated_data):
        # validated_data
        # user = User(**validated_data)
        # user.set_password(validated_data["password"])
        # user.save()
        return User.objects.create(**validated_data)


class CategorySerializers(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "key", "category_name", "active"]

    def create(self, validated_data):
        return Category(**validated_data)


class TourSerializers(ModelSerializer):
    class Meta:
        model = Tour
        fields = ["id", "tour_name", "price", "amount", "sale", "active"]

    def create(self, validated_data):
        return Tour(**validated_data)


class DecriptionSerializers(ModelSerializer):
    class Meta:
        model = Decription
        fields = ["id", "tour", "title", "img", "content"]

    def create(self, validated_data):
        return Decription(**validated_data)


class ImgSerializers(ModelSerializer):
    class Meta:
        model = Img
        fields = "__all__"
