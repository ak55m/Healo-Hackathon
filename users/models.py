from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField("Is admin", default=False)
    is_user = models.BooleanField("Is user", default=False)
    is_doctor = models.BooleanField("Is doctor", default=False)
    phone_number = models.CharField("Phone Number", max_length=15, blank=True, null=True)


    class Meta:
        app_label = 'users'
