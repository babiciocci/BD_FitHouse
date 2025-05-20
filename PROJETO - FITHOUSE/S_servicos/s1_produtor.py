from kafka import KafkaProducer
from faker import Faker
import time
import json
import random

fake = Faker()

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    api_version=(3,8,0),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

if __name__ == '__main__':
    topic = 's1-s2'

    while True:
        mensagem = {
            "dieta": "frango",
            "table": "valor",
            "table": {"id": 123}
        }
        print(mensagem)
        producer.send(topic, value=mensagem)