from kafka import KafkaConsumer
import json

# Cria um consolidador que escuta os dois tópicos
consumer = KafkaConsumer(
    's1-kafka-s2', 's2-kafka',
    bootstrap_servers='kafka:9092',
    api_version=(3, 8, 0),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='s3_consolidador',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print(f"Conectado aos tópicos: {consumer.subscription()}")

if __name__ == '__main__':
    print("Aguardando mensagens...")

    for msg in consumer:
        dados = msg.value
        topico = msg.topic

        if topico == 's1-kafka-s2':
            print("----> S3 recebeu do S1:")
        elif topico == 's2-kafka':
            print("----> S3 recebeu do S2:")

        print(json.dumps(dados, indent=2, ensure_ascii=False))