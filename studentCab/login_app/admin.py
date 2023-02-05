from django.contrib import admin
from .models import NewUser, Driver, Passenger, Trip

admin.site.register(NewUser)

@admin.register(Driver)
class Driver(admin.ModelAdmin):
    fields = (
        'car_make', 'car_model','car_year'
    )
    list_display = (
        'car_make', 'car_model','car_year'
    )
    
admin.site.register(Passenger)
admin.site.register(Trip)
