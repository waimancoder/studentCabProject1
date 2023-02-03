from django.db import models

# Create your models here.
class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    isDriver = models.BooleanField(default=False)
    isPassenger = models.BooleanField(default=False)