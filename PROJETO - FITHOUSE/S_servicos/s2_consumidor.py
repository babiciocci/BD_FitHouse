from kafka import KafkaConsumer, KafkaProducer
import json
import mysql.connector
from cassandra.cluster import Cluster
from pymongo import MongoClient

# Kafka consumer para escutar requisições
consumer = KafkaConsumer(
    's1-s2',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# Kafka producer para enviar respostas
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Conexões com os bancos
mysql_conn = mysql.connector.connect(
    host='localhost',
    user='user',
    password='userpass',
    database='fithouse'
)
mysql_cursor = mysql_conn.cursor(dictionary=True)

cassandra_cluster = Cluster(['localhost'])
cassandra_session = cassandra_cluster.connect('fithouse')

cassandra_cursor = cassandra.cursor(dictionary=True)

mongo_client = MongoClient('localhost', 27017)
mongo_db = mongo_client['fithouse']
mongo_collection = mongo_db['sua_colecao']

mongodb_cursor = mongodb.cursor(dictionary=True)

if __name__ == '__main__':
    topic = 's2-s3'

print("S2 aguardando mensagens...")

for msg in consumer:
    dados = msg.value
    parametros = dados.get('parametros', {})
    banco = parametros.get('banco')
    id_valor = parametros.get('id')

    resultado = None

    # CRIANDO O DATABASE MYSQL
    mysql_cursor.execute("""
    CREATE DATABASE fithouse;
    USE fithouse;
    CREATE TABLE usuario (
        id INT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        data_registro DATE NOT NULL,
        foco VARCHAR(255) NOT NULL
    );
    """)

    # CRIANDO O DATABASE CASSANDRA
    cassandra_cursor.execute("""
    CREATE KEYSPACE fithouse
    WITH replication = {
    'class': 'SimpleStrategy',
    'replication_factor': 1
    };
    
    CREATE TABLE dieta (
        id int PRIMARY KEY,
        tipo_dieta text,
        cafe_manha list<text>,
        almoco list<text>,
        cafe_tarde list<text>,
        jantar list<text>,
        ceia list<text>
    );

    CREATE TABLE dieta_usuario (
        id int PRIMARY KEY,
        id_dieta int,
        id_usuario int
    );
    """)

    # CRIANDO O DATABASE MONGO
    mongodb_cursor.execute("""
    use fitstore;
    db.createCollection("treino", {
    validator: {
        $jsonSchema: {
        bsonType: "object",
        required: ["id"],
        properties: {
            id: { bsonType: "int" },
            exercise_1: { bsonType: "string" },
            exercise_2: { bsonType: "string" },
            exercise_3: { bsonType: "string" },
            exercise_4: { bsonType: "string" },
            exercise_5: { bsonType: "string" },
            exercise_6: { bsonType: "string" }
        }
        }
    }
    });

    db.createCollection("treino_usuario", {
    validator: {
        $jsonSchema: {
        bsonType: "object",
        required: ["id", "id_usuario", "id_treino"],
        properties: {
            id: { bsonType: "int" },
            id_usuario: { bsonType: "int" },
            id_treino: { bsonType: "int" },
            treino_seg: { bsonType: "int" },
            treino_ter: { bsonType: "int" },
            treino_qua: { bsonType: "int" },
            treino_qui: { bsonType: "int" },
            treino_sex: { bsonType: "int" },
            treino_sab: { bsonType: "int" }
        }
        }
    }
    });
    """)

    # PRECISA COLOCAR OS DADOS NOS BANCOS
    
    try:
        if banco == 'mysql':
            mysql_cursor.execute("SELECT * FROM sua_tabela WHERE id = %s", (id_valor,))
            resultado = mysql_cursor.fetchone()

        elif banco == 'cassandra':
            query = f"SELECT * FROM sua_tabela WHERE id = {id_valor}"
            resultado = cassandra_session.execute(query).one()

        elif banco == 'mongodb':
            resultado = mongo_collection.find_one({"id": id_valor})
            if resultado and '_id' in resultado:
                resultado['_id'] = str(resultado['_id'])  # serializar ObjectId

        else:
            resultado = {"erro": "Banco não reconhecido"}

    except Exception as e:
        resultado = {"erro": str(e)}

    resposta = {
        "sistema": "S2",
        "resposta": resultado,
        "original": dados
    }

    producer.send('s2-s3', resposta)
    print("S2 enviou resposta ao S3:", resposta)
