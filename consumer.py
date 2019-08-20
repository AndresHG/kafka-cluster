
from kafka import KafkaConsumer
from json import loads
import os

from dotenv import load_dotenv
load_dotenv()

port = "9092"
adress = os.getenv("SERVER_IP") + ":" + port

consumer = KafkaConsumer(
    'numtest',
     bootstrap_servers=[adress],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    message = message.value
    print('Se ha leido un nuevo mensaje {}'.format(message))
