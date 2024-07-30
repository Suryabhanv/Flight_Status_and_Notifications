import pika

def callback(ch, method, properties, body):
    print(f"Received {body}")
    # Here, you can add code to send SMS, email, or app notifications
    # For example, using Twilio for SMS, SMTP for email, or Firebase for app notifications

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='flight_status')
channel.basic_consume(queue='flight_status', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
