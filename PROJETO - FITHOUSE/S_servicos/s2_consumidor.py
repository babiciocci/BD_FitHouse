from kafka import KafkaConsumer, KafkaProducer
import json
import mysql.connector
from cassandra.cluster import Cluster
from pymongo import MongoClient

import time

consumer = KafkaConsumer(
    's1-s2',
    bootstrap_servers='kafka:9092',
    api_version=(3, 8, 0),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='consumidor',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)
print(f"Conectado ao tópico: {consumer.subscription()}")

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    api_version=(3, 8, 0),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Conexão com MySQL
try:
    mysql_conn = mysql.connector.connect(
        host='mysql',  # ou 'localhost' se for local
        user='user',
        password='userpass',
        database='fithouse'
    )
    mysql_cursor = mysql_conn.cursor(dictionary=True)
    print("Conectado no MySql!")
except Exception as e:
    print("Erro ao conectar MySQL:", e)
    mysql_conn = None

# Conexão com Cassandra
try:
    cassandra_cluster = Cluster(['MyCassandraCluster'])  # ou 'localhost'
    cassandra_session = cassandra_cluster.connect('fithouse')
    print("Conectado no CassandraB!")
except Exception as e:
    print("Erro ao conectar Cassandra:", e)
    cassandra_session = None

# Conexão com MongoDB
try:
    mongo_client = MongoClient('mongodb://mongo:27017/')  # ou 'localhost'
    mongo_db = mongo_client['fithouse']
    mongo_collection = mongo_db['treino']
    print("Conectado no MongoDB!")
except Exception as e:
    print("Erro ao conectar MongoDB:", e)
    mongo_client = None

if __name__ == '__main__':
    topic = 's2-s3'
    print("S2 aguardando mensagens...")

    for msg in consumer:
        dados = msg.value
        print("Mensagem recebida:", dados)

        # Simulando parâmetros que poderiam ser enviados
        usuario = dados.get('usuario', {})
        id_valor = usuario.get('id', None)

        resultado = None

        try:
            # Exemplo: consulta MySQL
            if mysql_conn and id_valor:
                mysql_cursor.execute("SELECT * FROM usuario WHERE id = %s", (id_valor,))
                resultado = mysql_cursor.fetchone()
                if resultado:
                    resultado['banco'] = 'MySQL'
            
            # Exemplo: consulta Cassandra
            if not resultado and cassandra_session and id_valor:
                query = f"SELECT * FROM dieta WHERE id = {id_valor};"
                cass_result = cassandra_session.execute(query).one()
                if cass_result:
                    resultado = dict(cass_result)
                    resultado['banco'] = 'Cassandra'
            
            # Exemplo: consulta MongoDB
            if not resultado and mongo_client and id_valor:
                mongo_result = mongo_collection.find_one({"id": id_valor})
                if mongo_result:
                    resultado = mongo_result
                    resultado['banco'] = 'MongoDB'
            
            if not resultado:
                resultado = {"info": "Nenhum dado encontrado"}

        except Exception as e:
            resultado = {"erro": str(e)}

        resposta = {
            "sistema": "S2",
            "resposta": resultado,
            "original": dados
        }

        producer.send(topic, resposta)
        print("S2 enviou resposta ao S3:", resposta)
