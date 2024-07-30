# flight/rabbitmq_consumer.py

import pika

def callback(ch, method, properties, body):
    print(f"Received {body}")
    # Implement your notification logic here (e.g., send email, SMS, etc.)

def consume_notifications():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='flight_status')
    channel.basic_consume(queue='flight_status', on_message_callback=callback, auto_ack=True)
    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
