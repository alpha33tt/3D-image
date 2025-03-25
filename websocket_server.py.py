from flask import Flask
from flask_sockets import Sockets
import os
import json
import time

app = Flask(__name__)
sockets = Sockets(app)

@sockets.route('/ws')
def send_rotation(ws):
    angle = 0
    while not ws.closed:
        angle += 0.05
        if angle > 360:
            angle = 0

        data = json.dumps({"rotationY": angle})
        ws.send(data)
        time.sleep(0.05)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
