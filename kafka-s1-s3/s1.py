from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    mensagem = {"sistema": "S1", "dados": "Mensagem de teste"}
    producer.send('s1-s3-comunicacao', mensagem)
    print("Mensagem enviada:", mensagem)
    time.sleep(5)