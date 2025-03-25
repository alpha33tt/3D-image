from flask import Flask
from flask_sock import Sock
import json
import os
import time

app = Flask(__name__)
sock = Sock(app)

# WebSocket route
@sock.route('/ws')
def send_rotation(ws):
    angle = 0
    while True:
        angle += 0.05  # Rotation step
        if angle > 360:
            angle = 0  # Reset after full turn
        
        data = json.dumps({"rotationY": angle})
        ws.send(data)
        time.sleep(0.05)  # Control speed

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
