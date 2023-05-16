from rest_framework import serializers
from .models import User


class UserSerializers(serializers.ModelSerializer):
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
        return User.objects.create_user(**validated_data)
