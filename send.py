#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('ip_string | localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World! - again')
print(" [x] Sent 'Hello World!' - again")
connection.close()
