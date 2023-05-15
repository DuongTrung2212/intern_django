from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register("user", UserViewSet, basename="user")
router.register("category", CategoryViewSet, basename="category")
router.register("tour", TourViewSet, basename="tour")
router.register("decription", DecriptionViewSet, basename="decription")
router.register("demo_upload", ImgViewSet, basename="img")
urlpatterns = [path("", include(router.urls))]
