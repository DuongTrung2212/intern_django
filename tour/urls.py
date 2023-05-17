from rest_framework.routers import DefaultRouter
from .views import TourViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r"tour", TourViewSet)
urlpatterns = [path("", include(router.urls))]
