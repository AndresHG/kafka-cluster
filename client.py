
import cv2
import base64
import socket
import  numpy as np
from pprint import pprint
from io import StringIO
from kafka import KafkaProducer
import pickle
import time
import os
import sys
import json
# import dlib
from datetime import datetime
import imutils

from dotenv import load_dotenv
load_dotenv()

topic = os.getenv("TOPIC", 'test')

def show_webcam(mirror=False, rotate=0):

    producer = KafkaProducer(bootstrap_servers=os.getenv('SERVER-IP', 'localhost') + ':' + os.getenv('PORT', '9092'))
    print("Conectado al servidor kafka.")
    cam = cv2.VideoCapture(0)
    print("Conectado a la camara.")

    while True:
        #cam.set(3, 1920)
        #cam.set(4, 1080)

        ret_val, img = cam.read()

        if rotate != 0:
            img = imutils.rotate_bound(img, 180)
        if mirror:
            img = cv2.flip(img, 1)

        # img = cv2.resize(img, (1920, 1080))
        h, w, rrr = img.shape
        # print('I am sending: {}, w: {}, h: {}'.format(datetime.now(), w, h))

        tm = datetime.now()

        # Round date to 0 or 5
        # try:
        #     tm = tm.replace(second=tm.second - (tm.second % 5) if (tm.second % 5) < 3 else tm.second + (5 - (tm.second % 5)))
        # except Exception as e:
        #     tm.replace(minute=tm.minute+1 if tm.minute%59 != 0 else tm.minute)
        #         tm.replace(second=0)

        timestamp = tm.strftime("%Y-%m-%d %H:%M:%S").encode('utf8')
        to_send = cv2.imencode('.jpg', img)[1].tostring()

        producer.send(topic, to_send, key=timestamp)

        k = cv2.waitKey(1)
        if k == 27:
            break  # esc to quit

    cam.release()
    cv2.destroyAllWindows()


# This is a redundant function, not necesarry if you implement if __name__ == '__main__'
#def main():
#    show_webcam(mirror=False)


if __name__ == '__main__':
    try:
        show_webcam(mirror=False, rotate=0)
    except KeyboardInterrupt:
        print("Ha habdo un error en la ejecución.")
