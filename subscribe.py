import pika, os

url = os.environ.get('CLOUDAMQP_URL', 'amqp://dtnazkje:UBnU5nlUEmua-sZVpfp2jkyhU9tUdjvI@wildboar.rmq.cloudamqp.com/dtnazkje')

params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue
def callback(ch, method, properties, body):
  print(" [x] Received " + str(body))

channel.basic_consume('hello',
                      callback,
                      auto_ack=False)

print(' [*] Waiting for messages:')
channel.start_consuming()
connection.close()
  

