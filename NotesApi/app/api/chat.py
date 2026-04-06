from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.websocket.manager import manager

router = APIRouter()

@router.websocket("/ws/{note_id}")
async def websocket_endpoint(websocket: WebSocket, note_id: int):
    await manager.connect(note_id, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(note_id, data)
    except WebSocketDisconnect:
        manager.disconnect(note_id, websocket)