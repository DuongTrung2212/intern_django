from rest_framework import serializers
from .models import Tour


class TourSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ["id", "tour_name", "price", "amount", "sale", "active"]

    def create(self, validated_data):
        return Tour(**validated_data)
