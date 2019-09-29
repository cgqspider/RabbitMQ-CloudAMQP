import pika, os

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqp://dtnazkje:UBnU5nlUEmua-sZVpfp2jkyhU9tUdjvI@wildboar.rmq.cloudamqp.com/dtnazkje')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)

channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue
i=""
while i!="exit":
    i=str(raw_input("Enter your name : "))
    channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=i
                      )

    print(" [x] Sent "+str(i))
connection.close()




