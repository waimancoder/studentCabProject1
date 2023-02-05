
from django.db import models

from django.contrib.auth.models import AbstractUser, Permission
from django.contrib.auth.models import UserManager


class NewUserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_driver=False, is_passenger=False)

class DriverManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_driver=True)

class PassengerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_passenger=True)



class NewUser(AbstractUser):
    is_driver = models.BooleanField(default=False)
    is_passenger = models.BooleanField(default=False)
    # driver = models.OneToOneField(Driver, on_delete=models.CASCADE, null=True, blank=True)
    # passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE, null=True, blank=True)

    objects = UserManager()
    
    def set_as_driver(self):
        self.is_driver = True
        self.save()

    def set_as_passenger(self):
        self.is_passenger = True
        self.save()

class Driver(models.Model):
    
    objects = DriverManager()

    newuser = models.OneToOneField(NewUser, on_delete=models.CASCADE, null=True, blank=True)
    car_make = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_year = models.PositiveSmallIntegerField()
    license_plate = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    num_trips = models.PositiveIntegerField()
    is_driver = models.BooleanField(default=True)
   
    

class Passenger(models.Model):

    objects = PassengerManager()

    phone_number = models.CharField(max_length=20)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    num_trips = models.PositiveIntegerField()



class Trip(models.Model):
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    STATUS_CHOICES = [
        ('requested', 'Requested'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    date = models.DateTimeField(auto_now_add=True)