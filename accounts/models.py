from django.contrib.auth.models import AbstractUser
from django.db import models  # noqa:F401


class CustomUser(AbstractUser):
    pass
