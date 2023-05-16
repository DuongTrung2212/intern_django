from django.db import models
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from user.models import User
from category.models import Category


# Create your models here.
class Tour(models.Model):
    tour_name = models.CharField(max_length=100, null=False, unique=True)
    price = models.IntegerField(null=False, validators=[MinValueValidator(0)])
    img_slide = models.ImageField(upload_to="uploads/tours/%Y/%m")
    amount = models.IntegerField(validators=[MinValueValidator(0)])
    start_address = models.CharField(null=True, max_length=200)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    pick_up_address = models.CharField(null=True)
    staff = models.ForeignKey(User, related_name="staff", on_delete=models.PROTECT)
    sale = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)], default=0
    )
    category = models.ManyToManyField(Category, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tour_name


class Decription(models.Model):
    tour = models.ForeignKey("Tour", related_name="tour", on_delete=models.CASCADE)
    title = models.CharField(max_length=150, unique=True)
    img = models.ImageField(upload_to="uploads/tours/%Y/%m")
    content = models.CharField()
