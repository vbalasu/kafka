from kafka import KafkaConsumer
from dotenv import load_dotenv
import os

load_dotenv()
bootstrap_servers = os.environ.get('BOOTSTRAP_SERVERS')
topic_name = os.environ.get('TOPIC_NAME')
group_id = 'my-consumer-group'

# Create Kafka consumer
consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=bootstrap_servers,
    group_id=group_id
)

# Continuously poll for new messages
for message in consumer:
    # Print the received message
    print(message.value.decode('utf-8'))

# Close the consumer
consumer.close()
