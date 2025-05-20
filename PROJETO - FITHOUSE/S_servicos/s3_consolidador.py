from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    's2-s3',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("S3 aguardando mensagens...")

for msg in consumer:
    dados = msg.value
    print("S3 recebeu:", json.dumps(dados, indent=2, ensure_ascii=False))
