from kafka import KafkaProducer
import time
import json
import socket
from datetime import datetime
import requests
import json

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


    if __name__ == '__main__':

        topic = 's1-kafka-s2'
        for i in range(0,50):

            # MENSAGENS DO MYSQL
            mensagem = {
                "banco": "mysql",
                "operacao": "buscar",
                "table": "usuario",
                "dados": {
                    "id": 1,
                    "nome": "Bruno Basso",
                    "data_registro": "2004-12-26",
                    "foco": "hypertrophy"
                }
            }

            producer.send(topic, value=mensagem)
            print("\nMysql: enviado ->", mensagem)

            # Enviando para o S3 direto
            res1 = requests.post('http://s3_consolidador:5003/receber_s1', json=mensagem)

            print("Resposta do S3:", res1.status_code, res1.json())

            # MENSAGENS DO MONGODB
            mensagem2 = {
                "banco": "mongodb",
                "operacao": "buscar",
                "table": "treino_usuario",
                "dados": {
                    'id': 3215,
                    'id_usuario': 0,
                    'id_treino': 733,
                    'treino_seg': 895,
                    'treino_ter': 687,
                    'treino_qua': 761,
                    'treino_qui': 802,
                    'treino_sex': 995,
                    'treino_sab': 733
                }
            }

            producer.send(topic, value=mensagem2)
            print("\nMongodb: enviado ->", mensagem2)

            # Enviando para o S3 direto
            res2 = requests.post('http://s3_consolidador:5003/receber_s1', json=mensagem2)

            print("Resposta do S3:", res2.status_code, res2.json())

            # MENSAGENS DO CASSANDRA
            mensagem3 = {
                "banco": "cassandra",
                "operacao": "buscar",
                "table": "fithouse.dieta_usuario",
                "dados": {
                    # 'id': 2273,
                    # 'id_dieta': 1078,
                    'id_usuario': 7
                }
            }

            producer.send(topic, value=mensagem3)
            print("\nCassandra: enviado ->", mensagem3)

            # Enviando para o S3 direto
            res3 = requests.post('http://s3_consolidador:5003/receber_s1', json=mensagem2)

            print("Resposta do S3:", res3.status_code, res3.json())

            time.sleep(1)


            

print("Chegaram todas as mensagens!")

