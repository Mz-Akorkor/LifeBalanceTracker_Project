from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    fitness_goal = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.username