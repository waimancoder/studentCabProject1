
from django.db import models

from django.contrib.auth.models import AbstractUser

class NewUser(AbstractUser):
    is_driver = models.BooleanField(default=False)
    is_passenger = models.BooleanField(default=False)

    
    def set_as_driver(self):
        self.is_driver = True
        self.save()

    def set_as_passenger(self):
        self.is_passenger = True
        self.save()