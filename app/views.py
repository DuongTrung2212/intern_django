from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import viewsets, status
from .serializers import *
from .models import *


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializers

    # def create(self, request, *args, **kwargs):
    #     return JsonResponse(
    #         {
    #             "data": request.data,
    #             "status": status.HTTP_200_OK,
    #         }
    #     )

    @action(
        methods=["post"],
        detail=False,
        permission_classes=[
            AllowAny,
        ],
        url_path="register-superuser",
    )
    def create_superuser(self, request):
        request.data.pop("confirm_password")
        if User.objects.filter(phone=request.data["phone"]):
            raise serializers.ValidationError({"phone": "unique"})
        user = User.objects.create_superuser(**request.data)
        return JsonResponse(
            {
                "data": UserSerializers(user).data,
                "status": status.HTTP_200_OK,
            }
        )


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(active=True)
    serializer_class = CategorySerializers


class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.filter(active=True)
    serializer_class = TourSerializers


class DecriptionViewSet(viewsets.ModelViewSet):
    serializer_class = DecriptionSerializers


class ImgViewSet(viewsets.ModelViewSet):
    queryset = Img.objects.all()
    serializer_class = ImgSerializers
