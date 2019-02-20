from django.db import models
from django.contrib.auth.models import AbstractUser
class MyUser(AbstractUser):
    is_employer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

