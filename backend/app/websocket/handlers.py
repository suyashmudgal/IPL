from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.websocket.manager import manager

router = APIRouter()

@router.websocket("/{code}/{token}")
async def websocket_endpoint(websocket: WebSocket, code: str, token: str):
    await manager.connect(code, websocket)
    try:
        while True:
            data = await websocket.receive_json()
            # Handle socket messages (bids, chat, emojis)
            await manager.broadcast(code, data)
    except WebSocketDisconnect:
        manager.disconnect(code, websocket)
