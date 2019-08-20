
from time import sleep
from json import dumps
from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers=['0.0.0.0:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

print("Conectado")
for e in range(1000):
    data = {'number' : e}
    producer.send('numtest', value=data)
    sleep(5)

