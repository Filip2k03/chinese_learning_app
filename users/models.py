from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.username
