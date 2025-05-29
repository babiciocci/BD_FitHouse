from kafka import KafkaProducer
import time
import json
import socket
from datetime import datetime

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

data_str = "2004-12-26"
data_convertida = datetime.strptime(data_str, "%Y-%m-%d").date()

if(aguardarkafka):
    # Tópico Kafka
    if __name__ == '__main__':
        topic = 's1-kafka-s2'
        for i in range(0,50):
            mensagem = {
                "banco": "mysql",
                "operacao": "buscar",
                "table": "usuario",
                "dados": {
                    "id": 1,
                    "nome": "Bruno Basso",
                "data_registro": data_convertida.strftime("%Y-%m-%d"),
                "foco": "hypertrophy"
                }
            }


            #mensagem2 = {
            #     "banco": "mongodb",
            #     "operacao": "buscar",
            #     "table": "treino_usuario",
            #     "dados": {
            #         'id': 3215,
            #         'id_usuario': 0,
            #         'id_treino': 733,
            #         'treino_seg': 895,
            #         'treino_ter': 687,
            #         'treino_qua': 761,
            #         'treino_qui': 802,
            #         'treino_sex': 995,
            #         'treino_sab': 733
            #     }
            # }
            producer.send(topic, value=mensagem)
            #producer.send(topic, value=mensagem2)
            print("Enviando:", mensagem)
            #print("Enviando:", mensagem2)
            time.sleep(1)






            

print("Chegaram todas as mensagens!")

