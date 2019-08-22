
from flask import Flask, render_template, Response
from streamer import Streamer
import os

app = Flask(__name__)

from dotenv import load_dotenv
load_dotenv()

def gen():
  streamer = Streamer(os.getenv("SERVER_IP", 'localhost'), os.getenv("PORT", '9092'), os.getenv("TOPIC", 'test'))
  streamer.start()

  while True:
    if streamer.client_connected():
      yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + streamer.get_jpeg() + b'\r\n\r\n')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/video_feed')
def video_feed():
  return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
  app.run(host='localhost', threaded=True)
