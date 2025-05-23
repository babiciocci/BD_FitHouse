from kafka import KafkaProducer
import time
import json
import socket

# Cria o produtor Kafka
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    api_version=(3, 8, 0),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)



def aguardarkafka( delay=3, max_tentativas=30):
    tentativas = 0
    while tentativas < max_tentativas:
        try:
            with socket.create_connection((kafka, 9092), timeout=2) as s:
                print(f"Kafka disponível.")
                return True
        except (socket.timeout, ConnectionRefusedError):
            print(f"KAFKA não disponível. Tentando novamente em {delay} segundos...")
            time.sleep(delay)
            tentativas += 1

if(aguardarkafka):
    # Tópico Kafka
    topic = 's1-s2'
    if __name__ == '__main__':
        for i in range(0,21):
            mensagem = {
                "dieta": "frango",
                "treino": "biceps",
                "usuario": {"id": 123}
            }
            print("Enviando:", mensagem)
            producer.send(topic, value=mensagem)

print("nao esta rodando ainda")

