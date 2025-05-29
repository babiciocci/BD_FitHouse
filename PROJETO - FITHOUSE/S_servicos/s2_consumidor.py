from kafka import KafkaConsumer, KafkaProducer
import json
import time
import mysql.connector
from cassandra.cluster import Cluster
from pymongo import MongoClient
import datetime


# FAZENDO CONEXAO COM MYSQL
mysql_conn = mysql.connector.connect(
    host="mysql_db",
    user="user",
    password="userpass",
    database="fithouse_db",
    port=3306
)
mysql_cursor = mysql_conn.cursor(dictionary=True)


# FAZENDO CONEXAO COM CASSANDRA
cluster = Cluster(['cassandra'], port=9042)
session = cluster.connect()
session.set_keyspace('fithouse')


# FAZENDO CONEXAO COM MONGODB
mongo_client = MongoClient('mongodb://root:rootpass@mongodb_db:27017/')
mongo_db = mongo_client['fithouse']  


time.sleep(3)
consumer = KafkaConsumer(
    's1-kafka-s2',
    bootstrap_servers='kafka:9092',
    api_version=(3, 8, 0),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    api_version=(3, 8, 0),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)



def convert_dates(obj):
    if isinstance(obj, dict):
        return {k: convert_dates(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_dates(elem) for elem in obj]
    elif isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.strftime("%Y-%m-%d")
    else:
        return obj



print("S2 aguardando mensagens...")


for msg in consumer:
    mensagem = msg.value
    print(f"\nMensagem recebida do S1: {json.dumps(mensagem, indent=2, ensure_ascii=False)}")

    banco = mensagem.get('banco')
    operacao = mensagem.get('operacao')
    tabela = mensagem.get('table')
    dados = mensagem.get('dados', {})

    resposta = {}

    try:



        if banco == 'mysql':

            if operacao == 'inserir':
                colunas = ', '.join(dados.keys())
                valores = ', '.join(['%s'] * len(dados))
                sql = f"INSERT INTO {tabela} ({colunas}) VALUES ({valores})"
                mysql_cursor.execute(sql, tuple(dados.values()))
                mysql_conn.commit()

                resposta = {
                    "Status MySQL": "sucesso",
                    "mensagem": "Registro inserido no MySQL",
                    "dados": dados
                }

            elif operacao == 'buscar':
                if dados:
                    where = ' AND '.join([f"{k}=%s" for k in dados.keys()])
                else:
                    where = '1'  # condição sempre verdadeira, para evitar erro no WHERE
                sql = f"SELECT * FROM {tabela} WHERE {where}"
                mysql_cursor.execute(sql, tuple(dados.values()))
                resultado = mysql_cursor.fetchall()
                resultado = convert_dates(resultado)

                resposta = {
                    "Status MySQL": "sucesso",
                    "mensagem": f"Encontrados {len(resultado)} registros no MySQL",
                    "resultado": resultado
                }


            else:
                resposta = {
                    "Status MySQL": "erro",
                    "mensagem": f"Operação '{operacao}' não suportada para MySQL"
                }




        elif banco == 'cassandra':

            if operacao == 'inserir':
                colunas = ', '.join(dados.keys())
                valores = ', '.join(['%s'] * len(dados))
                query = f"INSERT INTO {tabela} ({colunas}) VALUES ({valores})"
                session.execute(query, tuple(dados.values()))

                resposta = {
                    "Status Cassandra": "sucesso",
                    "mensagem": "Registro inserido no Cassandra",
                    "dados": dados
                }

            elif operacao == 'buscar':
                if dados: 
                    where = ' AND '.join([f"{k}=%s" for k in dados.keys()])
                    query = f"SELECT * FROM {tabela} WHERE {where} ALLOW FILTERING"
                    result = session.execute(query, tuple(dados.values()))
                else:
                    query = f"SELECT * FROM {tabela}"
                    result = session.execute(query)

                resultado = [dict(row._asdict()) for row in result]

                resposta = {
                    "Status Cassandra": "sucesso",
                    "mensagem": f"Encontrados {len(resultado)} registros no Cassandra",
                    "resultado": resultado
                }

            else:
                resposta = {
                    "Status Cassandra": "erro",
                    "mensagem": f"Operação '{operacao}' não suportada para Cassandra"
                }

        elif banco == 'mongodb':





            collection = mongo_db[tabela]

            if operacao == 'inserir':
                collection.insert_one(dados)

                resposta = {
                    "Status MongoDB": "sucesso",
                    "mensagem": "Registro inserido no MongoDB",
                    "dados": dados
                }

            elif operacao == 'buscar':
                resultados = list(collection.find(dados, {'_id': False}))

                resposta = {
                    "Status MongoDB": "sucesso",
                    "mensagem": f"Encontrados {len(resultados)} registros no MongoDB",
                    "resultado": resultados
                }

            else:
                resposta = {
                    "Status MongoDB": "erro",
                    "mensagem": f"Operação '{operacao}' não suportada para MongoDB"
                }

        else:
            resposta = {
                "Status": "erro",
                "mensagem": f"Banco '{banco}' não reconhecido"
            }

    except Exception as e:
        resposta = {
            "Status": "erro",
            "mensagem": str(e)
        }

    producer.send('s2-kafka', value=resposta)
    producer.flush()

    print("Resposta enviada:", json.dumps(resposta, indent=2, ensure_ascii=False))
