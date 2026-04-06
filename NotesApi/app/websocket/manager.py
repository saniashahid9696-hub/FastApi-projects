from fastapi import WebSocket
from collections import defaultdict

class ConnectionManager:
    def __init__(self):
        self.active_connections = defaultdict(list)

    async def connect(self, note_id: int, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[note_id].append(websocket)

    def disconnect(self, note_id: int, websocket: WebSocket):
        self.active_connections[note_id].remove(websocket)

    async def broadcast(self, note_id: int, message: str):
        for connection in self.active_connections[note_id]:
            await connection.send_text(message)

manager = ConnectionManager()