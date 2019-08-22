
import cv2
import threading
from PIL import Image
import io
from json import loads
import json
from kafka import KafkaConsumer
import numpy

class Streamer (threading.Thread):
  def __init__(self, hostname, port, topic):
    threading.Thread.__init__(self)

    self.hostname = hostname
    self.port = port
    self.topic = topic
    self.connected = False
    self.jpeg = None

  def run(self):

    self.isRunning = True

    consumer = KafkaConsumer(
        self.topic,
        bootstrap_servers=[self.hostname + ":" + self.port],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group')

    while self.isRunning:

        for msg in consumer:

            memfile = Image.open(io.BytesIO(msg.value))
            frame = numpy.array(memfile)
            # Convert RGB to BGR
            frame = frame[:, :, ::-1].copy()

            ret, jpeg = cv2.imencode('.jpg', frame)
            self.jpeg = jpeg

            self.connected = True

        self.connected = False

  def stop(self):
    self.isRunning = False

  def client_connected(self):
    return self.connected

  def get_jpeg(self):
    return self.jpeg.tobytes()
