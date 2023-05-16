from rest_framework import serializers
from .models import Category


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "key", "category_name", "active"]

    def create(self, validated_data):
        return Category(**validated_data)
