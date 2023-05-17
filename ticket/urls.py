from rest_framework.routers import DefaultRouter
from .views import TicketViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r"ticket", TicketViewSet)
urlpatterns = [path("", include(router.urls))]
