from kafka import KafkaConsumer, KafkaProducer
import json
import mysql.connector
from cassandra.cluster import Cluster
from pymongo import MongoClient


# =========================
# Configuração MySQL
# =========================
mysql_conn = mysql.connector.connect(
    host="mysql_db",
    user="user",
    password="userpass",
    database="fithouse_db",
    port=3306
)
mysql_cursor = mysql_conn.cursor(dictionary=True)

# # =========================
# # Configuração Cassandra
# # =========================
# cluster = Cluster(['cassandra_db'])
# session = cluster.connect()
# session.set_keyspace('db_cassandra')  # Você deve criar esse keyspace antes

# =========================
# Configuração MongoDB
# =========================
mongo_client = MongoClient('mongodb://root:rootpass@mongodb_db:27017/')
mongo_db = mongo_client['fithouse']  

# =========================
# Configuração Kafka
# =========================

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



print("S2 aguardando mensagens...")


for msg in consumer:
    mensagem = msg.value
    print(f"\nMensagem recebida: {json.dumps(mensagem, indent=2, ensure_ascii=False)}")

    banco = mensagem.get('banco')
    operacao = mensagem.get('operacao')
    tabela = mensagem.get('table')
    dados = mensagem.get('dados', {})

    print("tabela: ", mensagem.get('table')) ############# PEGANDO TABELA COMO NULO

    resposta = {}

    try:
        if banco == 'mysql':


            # ====================
            # Operações no MySQL
            # ====================
            if operacao == 'inserir':
                colunas = ', '.join(dados.keys())
                valores = ', '.join(['%s'] * len(dados))
                sql = f"INSERT INTO {tabela} ({colunas}) VALUES ({valores})"
                mysql_cursor.execute(sql, tuple(dados.values()))
                mysql_conn.commit()

                resposta = {
                    "status": "sucesso",
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

                resposta = {
                    "status": "sucesso",
                    "mensagem": f"Encontrados {len(resultado)} registros no MySQL",
                    "resultado": resultado
                }

            else:
                resposta = {
                    "status": "erro",
                    "mensagem": f"Operação '{operacao}' não suportada para MySQL"
                }

        elif banco == 'cassandra':




            # ===========================
            # Operações no Cassandra
            # ===========================
            if operacao == 'inserir':
                colunas = ', '.join(dados.keys())
                valores = ', '.join(['%s'] * len(dados))
                query = f"INSERT INTO {tabela} ({colunas}) VALUES ({valores})"
                session.execute(query, tuple(dados.values()))

                resposta = {
                    "status": "sucesso",
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
                    "status": "sucesso",
                    "mensagem": f"Encontrados {len(resultado)} registros no Cassandra",
                    "resultado": resultado
                }

            else:
                resposta = {
                    "status": "erro",
                    "mensagem": f"Operação '{operacao}' não suportada para Cassandra"
                }

        elif banco == 'mongodb':



            
            # ===========================
            # Operações no MongoDB
            # ===========================
            collection = mongo_db[tabela]

            if operacao == 'inserir':
                collection.insert_one(dados)

                resposta = {
                    "status": "sucesso",
                    "mensagem": "Registro inserido no MongoDB",
                    "dados": dados
                }

            elif operacao == 'buscar':
                resultados = list(collection.find(dados, {'_id': False}))

                resposta = {
                    "status": "sucesso",
                    "mensagem": f"Encontrados {len(resultados)} registros no MongoDB",
                    "resultado": resultados
                }

            else:
                resposta = {
                    "status": "erro",
                    "mensagem": f"Operação '{operacao}' não suportada para MongoDB"
                }

        else:
            resposta = {
                "status": "erro",
                "mensagem": f"Banco '{banco}' não reconhecido"
            }

    except Exception as e:
        resposta = {
            "status": "erro",
            "mensagem": str(e)
        }

    producer.send('s2-kafka', value=resposta)
    producer.flush()

    print("Resposta enviada:", json.dumps(resposta, indent=2, ensure_ascii=False))
