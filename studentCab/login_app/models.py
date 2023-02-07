
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
    is_student = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_normal = models.BooleanField(default=False)
    matricNo = models.CharField(max_length=10,null=True)
    staffNo = models.CharField(max_length=255,null=True)


    objects = UserManager()
    
    def set_as_driver(self):
        self.is_driver = True
        self.save()

    def set_as_passenger(self):
        self.is_passenger = True
        self.save()

class Student(models.Model):
    matricNo = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    isDriver = models.BooleanField(default=False)
    isPassenger = models.BooleanField(default=False)
    isVerified = models.BooleanField(default=False)
    # profilePic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    

class Staff(models.Model):
    
    staffNo = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    isDriver = models.BooleanField(default=False)
    isPassenger = models.BooleanField(default=False)
    isVerified = models.BooleanField(default=False)
    # profilePic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    

class Driver(models.Model):
    
    objects = DriverManager()

    newuser = models.OneToOneField(NewUser, on_delete=models.CASCADE, null=True, blank=True)
    car_make = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_year = models.PositiveSmallIntegerField()
    license_plate = models.CharField(max_length=100)
    num_trips = models.PositiveIntegerField()

    
class Passenger(models.Model):

    objects = PassengerManager()

    phone_number = models.CharField(max_length=20)
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
