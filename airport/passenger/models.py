from django.contrib.auth.models import User
from django.db import models
from flight.models import Flight

class Passenger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    passport_number = models.CharField(max_length=20, default="")
    phone_number = models.CharField(max_length=15, default="")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Ticket(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.passenger} - {self.flight}"