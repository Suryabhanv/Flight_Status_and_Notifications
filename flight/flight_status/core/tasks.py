"""from celery import shared_task
import pika

@shared_task
def send_notification(flight_id):
    # Fetch flight details
    from .models import Flight
    flight = Flight.objects.get(id=flight_id)
    
    # Prepare message
    message = f"Flight {flight.flight_number} status update: {flight.status}. Departure: {flight.departure_time}, Arrival: {flight.arrival_time}, Gate: {flight.gate}"
    
    # Publish message to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='flight_status')
    channel.basic_publish(exchange='', routing_key='flight_status', body=message)
    connection.close()
"""
# tasks.py

from celery import shared_task
import json
import random

@shared_task
def update_flight_status():
    with open('mock_flight_data.json') as f:
        flights = json.load(f)
    
    # Simulate flight status update
    for flight in flights:
        flight['status'] = random.choice(["On Time", "Delayed", "Cancelled"])
    
    with open('mock_flight_data.json', 'w') as f:
        json.dump(flights, f, indent=4)

    return flights
