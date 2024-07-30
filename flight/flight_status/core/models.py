"""from django.db import models
from .tasks import send_notification

class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    status = models.CharField(max_length=50)  # e.g., On Time, Delayed, Cancelled
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    gate = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Trigger the notification task
        send_notification.delay(self.id)

    def __str__(self):
        return f"{self.flight_number} - {self.status}"
"""

from django.db import models

class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    status = models.CharField(max_length=20)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    gate = models.CharField(max_length=5)

    def __str__(self):
        return self.flight_number
