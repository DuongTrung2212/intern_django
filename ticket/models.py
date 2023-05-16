from django.db import models
from tour.models import Tour
from user.models import User


# Create your models here.
class Ticket(models.Model):
    CCCD = models.CharField(null=False)
    tour = models.JSONField(Tour)
    user = models.ForeignKey(
        User, related_name="user", on_delete=models.CASCADE, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
