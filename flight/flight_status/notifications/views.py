"""import pika
from core.models import Flight, Notification

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='flight_notifications')

def send_notification(flight_id, message):
    flight = Flight.objects.get(id=flight_id)
    notification = Notification(flight=flight, message=message)
    notification.save()
    channel.basic_publish(exchange='', routing_key='flight_notifications', body=message)
"""

# notifications/views.py
from core.models import Flight
from .rabbitmq import publish_message  # Import your RabbitMQ logic

def send_notification(flight_id, message):
    flight = Flight.objects.get(id=flight_id)
    publish_message('flight_notifications', message)
