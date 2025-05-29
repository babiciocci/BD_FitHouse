from kafka import KafkaConsumer
import json
from flask import Flask, request, jsonify
import threading

app = Flask(__name__)


# ---- ROTA HTTP ----
@app.route('/receber_s1', methods=['POST'])
def receber_s1():
    dados = request.json
    print("\n\n----> S3 recebeu do S1 via HTTP:")
    print(json.dumps(dados, indent=2, ensure_ascii=False))
    return jsonify({'status': 'recebido por S3', 'dados': dados}), 200


# ---- CONSUMIDOR KAFKA ----
def consumir_kafka():
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
    print("Aguardando mensagens do Kafka...")

    for msg in consumer:
        dados = msg.value
        topico = msg.topic

        if topico == 's1-kafka-s2':
            print("\n\n----> S3 recebeu do S1 via Kafka:")
        elif topico == 's2-kafka':
            print("\n\n----> S3 recebeu do S2 via Kafka:")

        print(json.dumps(dados, indent=2, ensure_ascii=False))


# ---- MAIN ----
if __name__ == '__main__':
    # Roda o Kafka consumidor em uma thread paralela
    kafka_thread = threading.Thread(target=consumir_kafka)
    kafka_thread.start()

    # Inicia o Flask na thread principal
    app.run(host='0.0.0.0', port=5003)
