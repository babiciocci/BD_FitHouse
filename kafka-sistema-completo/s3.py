from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    's1-s3',
    's2-s3',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    group_id='grupo-s3'
)

print("S3 está ouvindo mensagens de S1 e S2...")

for msg in consumer:
    print(f"S3 recebeu do tópico '{msg.topic}':", msg.value)
