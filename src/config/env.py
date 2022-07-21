import asyncio
import os

# env Variable
MONGO_DB_URI = "localhost:27017"#os.environ['MONGO_DB_URI']
KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"#os.environ['KAFKA_BOOTSTRAP_SERVERS']
KAFKA_CONSUMER_GROUP = "group-id"#os.environ['KAFKA_CONSUMER_GROUP']
KAFKA_TOPIC = "kafka-topic-test"#os.environ['KAFKA_TOPIC']#"kafka-topic-test"

loop = asyncio.get_event_loop()
