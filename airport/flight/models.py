from django.db import models

class Flight(models.Model):
    start = models.CharField(max_length=100, default='')
    finish = models.CharField(max_length=100, default='')
    international = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.start} {self.finish}"
    
    class Meta:
        unique_together = ('start', 'finish')

class FlightSchedule(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    @property
    def time_in_air(self):
        return self.arrival_time - self.departure_time
    
    def __str__(self):
        return f"{self.flight.start} -> {self.flight.finish} | Time in air: {self.time_in_air} | Time: [{self.departure_time} - {self.arrival_time}] "
