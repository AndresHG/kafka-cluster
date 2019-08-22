
from kafka import KafkaConsumer
from json import loads
import os

from dotenv import load_dotenv
load_dotenv()

adress = os.getenv("SERVER_IP") + ":" + os.getenv("PORT")

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
