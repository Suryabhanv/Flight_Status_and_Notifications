# notifications/management/commands/send_notifications.py
from django.core.management.base import BaseCommand
from notifications.views import send_notification
from core.models import Flight

class Command(BaseCommand):
    help = 'Send notifications for flight status changes'

    def handle(self, *args, **kwargs):
        flights = Flight.objects.all()
        for flight in flights:
            if flight.status_changed():  # Implement your status change logic
                send_notification(flight.id, f'Flight {flight.flight_number} status changed to {flight.status}')
