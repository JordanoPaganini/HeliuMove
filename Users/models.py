from django.db import models
from django.contrib.auth.models import AbstractUser
from Sistemas.models import Sistemas

class User(AbstractUser):
    sistemas = models.ManyToManyField(Sistemas, blank=True)