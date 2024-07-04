from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True)
    active_code_mobile = models.CharField(max_length=5, unique=True)

