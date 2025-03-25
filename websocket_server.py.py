import asyncio
import websockets
import json
import os

# Get the port from Render's environment (default to 10000)
PORT = int(os.getenv("PORT", 10000))

async def send_rotation(websocket, path):
    angle = 0
    while True:
        angle += 0.05
        if angle > 360:
            angle = 0  # Reset after full rotation

        # Send rotation data
        data = json.dumps({"rotationY": angle})
        await websocket.send(data)

        await asyncio.sleep(0.05)  # Control rotation speed

# Bind to the PORT (Render requires this)
start_server = websockets.serve(send_rotation, "0.0.0.0", PORT)

print(f"✅ WebSocket Server Running on ws://0.0.0.0:{PORT}")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
