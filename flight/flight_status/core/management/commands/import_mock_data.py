"""from django.core.management.base import BaseCommand
from core.models import Flight
from datetime import datetime

class Command(BaseCommand):
    help = 'Import mock flight data'

    def handle(self, *args, **kwargs):
        mock_flights = [
            {'flight_number': 'AA123', 'status': 'On Time', 'departure_time': '2024-08-01T10:00:00Z', 'arrival_time': '2024-08-01T12:00:00Z', 'gate': 'A1'},
            {'flight_number': 'BB456', 'status': 'Delayed', 'departure_time': '2024-08-01T14:00:00Z', 'arrival_time': '2024-08-01T16:00:00Z', 'gate': 'B2'},
            {'flight_number': 'CC789', 'status': 'Cancelled', 'departure_time': '2024-08-01T18:00:00Z', 'arrival_time': '2024-08-01T20:00:00Z', 'gate': 'C3'},
        ]
        for flight_data in mock_flights:
            Flight.objects.update_or_create(
                flight_number=flight_data['flight_number'],
                defaults={
                    'status': flight_data['status'],
                    'departure_time': datetime.fromisoformat(flight_data['departure_time']),
                    'arrival_time': datetime.fromisoformat(flight_data['arrival_time']),
                    'gate': flight_data['gate']
                }
            )
        self.stdout.write(self.style.SUCCESS('Successfully imported mock flight data'))
"""

import json
from django.core.management.base import BaseCommand
from core.models import Flight

class Command(BaseCommand):
    help = 'Load mock flight data into the database'

    def handle(self, *args, **kwargs):
        with open('mock_flight_data.json', 'r') as f:
            flights = json.load(f)

        for flight_data in flights:
            Flight.objects.update_or_create(
                flight_number=flight_data['flight_number'],
                defaults={
                    'status': flight_data['status'],
                    'departure_time': flight_data['departure_time'],
                    'arrival_time': flight_data['arrival_time'],
                    'gate': flight_data['gate']
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully loaded mock flight data'))
