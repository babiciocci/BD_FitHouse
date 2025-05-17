from kafka import KafkaConsumer, KafkaProducer
import json
import time

consumer = KafkaConsumer(
    's1-s2',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    group_id='grupo-s2'
)

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("S2 está escutando mensagens do S1...")

for msg in consumer:
    recebido = msg.value
    print("S2 recebeu:", recebido)
    nova_mensagem = {
        "sistema": "S2",
        "dados": f"[Repassado pelo S2]: {recebido['dados']}"
    }
    producer.send('s2-s3', nova_mensagem)
    print("S2 enviou para S3:", nova_mensagem)
    time.sleep(2)
