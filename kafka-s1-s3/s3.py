from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    's1-s3-comunicacao',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    group_id='grupo-s3'
)

print("Esperando mensagens do tópico...")

for mensagem in consumer:
    print("Mensagem recebida no S3:", mensagem.value)