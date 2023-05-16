from rest_framework.routers import DefaultRouter
from .views import UploadViewSet
from django.urls import path, include

router = DefaultRouter()
router.register("upload", UploadViewSet, basename="upload")
urlpatterns = [path("", include(router.urls))]
