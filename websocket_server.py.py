import asyncio
import websockets
import json
import os

# Get the port from the environment (Render default)
PORT = int(os.getenv("PORT", 10000))  # Default port 10000

async def send_rotation(websocket, path):
    angle = 0
    while True:
        angle += 0.05  # Rotate step
        if angle > 360:
            angle = 0  # Reset rotation after full turn

        data = json.dumps({"rotationY": angle})
        await websocket.send(data)
        await asyncio.sleep(0.05)  # Control rotation speed

# Start WebSocket server
async def start_server():
    server = await websockets.serve(send_rotation, "0.0.0.0", PORT)
    print(f"WebSocket Server Running on ws://0.0.0.0:{PORT}")
    await server.wait_closed()  # Keep running

if __name__ == "__main__":
    asyncio.run(start_server())
