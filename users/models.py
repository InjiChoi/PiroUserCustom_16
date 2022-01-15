from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    GENDER_CHOICE = (
        ("MALE", "male"),
        ("FEMALE", "female"),
        ("ETC", "etc"),
    )

    desc = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICE)
