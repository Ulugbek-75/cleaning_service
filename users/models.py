from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from users.manager import UserManager


class CustomUser(AbstractUser):
    username = None
    background_image = models.ImageField()
    image = models.ImageField()
    phone_number = models.CharField(max_length=14, unique=True)
    phone_number2 = models.CharField(max_length=14, null=True, blank=True)
    position_name = models.CharField(max_length=255)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"