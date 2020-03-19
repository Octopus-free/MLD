from django.db import models
from django.contrib.auth.models import AbstractUser


class MLDUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_author = models.BooleanField(default=False)


