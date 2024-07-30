# consume_messages.py
import pika

def callback(ch, method, properties, body):
    print(f"Received message: {body.decode()}")

def start_consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='flight_notifications')

    channel.basic_consume(queue='flight_notifications', on_message_callback=callback, auto_ack=True)
    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    start_consumer()
