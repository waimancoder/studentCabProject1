from django.contrib import admin
from .models import NewUser, Driver, Passenger, Trip, Student, Staff

admin.site.register(NewUser)

admin.site.register(Driver)
# class Driver(admin.ModelAdmin):
#     fields = (
#         'car_make', 'car_model','car_year'
#     )
#     list_display = (
#         'car_make', 'car_model','car_year'
#     )
    
admin.site.register(Passenger)
admin.site.register(Trip)
admin.site.register(Student)
admin.site.register(Staff)