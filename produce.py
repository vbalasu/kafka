from kafka import KafkaProducer
from dotenv import load_dotenv
import os

load_dotenv()
bootstrap_servers = os.environ.get('BOOTSTRAP_SERVERS')
topic_name = os.environ.get('TOPIC_NAME')
message = 'Hello, World!'

# Create Kafka producer
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# Publish message to the topic
producer.send(topic_name, value=message.encode('utf-8'))

# Flush and close the producer
producer.flush()
producer.close()
