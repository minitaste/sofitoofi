from django.contrib import admin

from .models import Flight, FlightSchedule

admin.site.register(Flight)
admin.site.register(FlightSchedule)