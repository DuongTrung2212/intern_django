from .views import some_view
from django.urls import path, include

urlpatterns = [path("pdf", some_view, name="create PDF file")]
