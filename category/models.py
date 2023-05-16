from django.db import models


# Create your models here.
class Category(models.Model):
    key = models.CharField(max_length=5, unique=True)
    category_name = models.CharField(unique=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name
