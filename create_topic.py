from kafka.admin import KafkaAdminClient, NewTopic
from dotenv import load_dotenv
import os

load_dotenv()
bootstrap_servers = os.environ.get('BOOTSTRAP_SERVERS')

admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)
topic_name = os.environ.get('TOPIC_NAME')
num_partitions = 1  # Adjust the number of partitions as needed
replication_factor = 1  # Adjust the replication factor as needed

new_topic = NewTopic(
    name=topic_name,
    num_partitions=num_partitions,
    replication_factor=replication_factor
)
admin_client.create_topics(new_topics=[new_topic])
admin_client.close()
print('topic created')
