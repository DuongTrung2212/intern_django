from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser

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

    def create(
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
        extra_fields.setdefault("is_staff", False)
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
