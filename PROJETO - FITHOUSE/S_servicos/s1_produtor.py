from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    mensagem = {"sistema": "S1", "dados": "Dado importante"}
    # Envia tanto para S3 quanto para S2
    producer.send('s1-s3', mensagem)
    producer.send('s1-s2', mensagem)
    print("S1 enviou:", mensagem)
    time.sleep(5)
