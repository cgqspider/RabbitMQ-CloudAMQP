import pika, os

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqp://dtnazkje:UBnU5nlUEmua-sZVpfp2jkyhU9tUdjvI@wildboar.rmq.cloudamqp.com/dtnazkje')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue



method_frame, header_frame, body = channel.basic_get(queue = 'hello')
print(body)      
channel.basic_ack(delivery_tag=method_frame.delivery_tag)
connection.close() 
  

