from kafka import KafkaProducer
import time
import json
import random

producer = KafkaProducer(
    bootstrap_servers='kafka:9093',
    api_version=(3,8,0),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

if __name__ == '__main__':
    topic = 's1-s2'

    for i in range(0,11):
        mensagem = {
            "dieta": "frango",
            "treino": "biceps",
            "usuario": {"id": 123}
        }
        print(mensagem)
        producer.send(topic, value=mensagem)
        producer.flush()
