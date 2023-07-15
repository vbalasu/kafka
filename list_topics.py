from kafka.admin import KafkaAdminClient, NewTopic
from dotenv import load_dotenv
import os

load_dotenv()
bootstrap_servers = os.environ.get('BOOTSTRAP_SERVERS')
admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)
topic_metadata = admin_client.list_topics()
print(topic_metadata)
admin_client.close()

