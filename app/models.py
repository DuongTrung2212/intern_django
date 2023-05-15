from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class UserManager(BaseUserManager):
    def _create_user(
        self,
        username,
        phone,
        email,
        password,
        address,
        first_name,
        last_name,
        gender,
        **extra_fields
    ):
        user = User(
            username=username,
            phone=phone,
            email=email,
            password=password,
            address=address,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self,
        username,
        phone,
        email,
        password,
        address,
        first_name,
        last_name,
        gender,
        **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(
            username,
            phone,
            email,
            password,
            address,
            first_name,
            last_name,
            gender,
            **extra_fields
        )

    def create_user(
        self,
        username,
        phone,
        email,
        password,
        address,
        first_name,
        last_name,
        gender,
        **extra_fields
    ):
        # extra_fields.setdefault("is_staff", False)
        # extra_fields.setdefault("is_superuser", False)
        return self._create_user(
            username,
            phone,
            email,
            password,
            address,
            first_name,
            last_name,
            gender,
            **extra_fields
        )

    def create_staffuser(
        self,
        username,
        phone,
        email,
        password,
        address,
        first_name,
        last_name,
        gender,
        **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(
            username,
            phone,
            email,
            password,
            address,
            first_name,
            last_name,
            gender,
            **extra_fields
        )


class User(AbstractUser):
    avatar = models.ImageField(null=True, upload_to="uploads/users/%Y/%m")
    phone = models.CharField(unique=True, null=False)
    address = models.CharField(null=True)
    is_superuser = models.BooleanField(default=False)
    gender = models.BooleanField(default=True)
    objects = UserManager()

    def __str__(self):
        return self.username


class Tour(models.Model):
    tour_name = models.CharField(max_length=100, null=False, unique=True)
    price = models.IntegerField(null=False, validators=[MinValueValidator(0)])
    img_slide = models.ImageField(upload_to="uploads/tours/%Y/%m")
    amount = models.IntegerField(validators=[MinValueValidator(0)])
    start_address = models.CharField(null=True, max_length=200)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    pick_up_address = models.CharField(null=True)
    staff = models.ForeignKey("Staff", related_name="staff", on_delete=models.PROTECT)
    sale = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)], default=0
    )
    category = models.ManyToManyField("Category", blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tour_name


class Ticket(models.Model):
    CCCD = models.CharField(null=False)
    tour = models.JSONField(Tour)
    user = models.ForeignKey(
        "User", related_name="user", on_delete=models.CASCADE, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    key = models.CharField(max_length=5, unique=True)
    category_name = models.CharField(unique=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name


class Decription(models.Model):
    tour = models.ForeignKey("Tour", related_name="tour", on_delete=models.CASCADE)
    title = models.CharField(max_length=150, unique=True)
    img = models.ImageField(upload_to="uploads/tours/%Y/%m")
    content = models.CharField()


class Staff(models.Model):
    staff_name = models.CharField(max_length=50, null=False)
    gender = models.BooleanField(default=True)
    phone = models.CharField(unique=True, null=False)
    email = models.CharField(unique=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.staff_name


class Img(models.Model):
    img = models.ImageField()
