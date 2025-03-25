import asyncio
import websockets
import json

# WebSocket server function
async def send_rotation(websocket, path):
    angle = 0  # Initial rotation angle
    while True:
        # Increase the rotation angle
        angle += 0.05
        if angle > 360:
            angle = 0  # Reset after full rotation

        # Send rotation data to the client
        data = json.dumps({"rotationY": angle})  # Send Y-axis rotation
        await websocket.send(data)

        await asyncio.sleep(0.05)  # Control rotation speed

# Start the WebSocket server
start_server = websockets.serve(send_rotation, "localhost", 8765)

print("WebSocket Server Started on ws://localhost:8765")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
