import os

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

backend_dir = r"c:\Users\suyas\IPL\backend\app"

# Create routers/players.py
players_content = """from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_
from typing import List, Optional
from app.database import get_db
from app.models.player import Player
from app.schemas.player import PlayerResponse

router = APIRouter()

@router.get("", response_model=List[PlayerResponse])
async def get_players(
    role: Optional[str] = None,
    tier: Optional[str] = None,
    nationality: Optional[str] = None,
    search: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    query = select(Player)
    if role: query = query.where(Player.role == role)
    if tier: query = query.where(Player.tier == tier)
    if nationality: query = query.where(Player.nationality == nationality)
    if search: query = query.where(Player.name.ilike(f"%{search}%"))
    
    result = await db.execute(query)
    return result.scalars().all()

@router.get("/{player_id}", response_model=PlayerResponse)
async def get_player(player_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Player).where(Player.id == player_id))
    return result.scalar_one_or_none()
"""
create_file(os.path.join(backend_dir, "routers", "players.py"), players_content)

# Create routers/auction.py
auction_content = """from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db

router = APIRouter()

@router.post("/{code}/start")
async def start_auction(code: str, db: AsyncSession = Depends(get_db)):
    return {"status": "started"}

@router.post("/{code}/bid")
async def place_bid(code: str, db: AsyncSession = Depends(get_db)):
    return {"status": "bid placed"}

@router.post("/{code}/host/{action}")
async def host_action(code: str, action: str, db: AsyncSession = Depends(get_db)):
    return {"status": "action performed"}
"""
create_file(os.path.join(backend_dir, "routers", "auction.py"), auction_content)

# Create routers/analysis.py
analysis_content = """from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db

router = APIRouter()

@router.post("/{code}/analyze")
async def analyze_room(code: str, db: AsyncSession = Depends(get_db)):
    return {"status": "analyzing"}

@router.get("/{code}/analysis")
async def get_analysis(code: str, db: AsyncSession = Depends(get_db)):
    return {"status": "analysis data"}
"""
create_file(os.path.join(backend_dir, "routers", "analysis.py"), analysis_content)

# Create websocket/manager.py
manager_content = """from typing import Dict, List
from fastapi import WebSocket

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, List[WebSocket]] = {}

    async def connect(self, room_code: str, websocket: WebSocket):
        await websocket.accept()
        if room_code not in self.active_connections:
            self.active_connections[room_code] = []
        self.active_connections[room_code].append(websocket)

    def disconnect(self, room_code: str, websocket: WebSocket):
        if room_code in self.active_connections:
            self.active_connections[room_code].remove(websocket)
            if not self.active_connections[room_code]:
                del self.active_connections[room_code]

    async def broadcast(self, room_code: str, message: dict):
        if room_code in self.active_connections:
            for connection in self.active_connections[room_code]:
                await connection.send_json(message)

manager = ConnectionManager()
"""
create_file(os.path.join(backend_dir, "websocket", "manager.py"), manager_content)

# Create websocket/handlers.py
handlers_content = """from fastapi import APIRouter, WebSocket, WebSocketDisconnect
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
"""
create_file(os.path.join(backend_dir, "websocket", "handlers.py"), handlers_content)

# Create data/players_seed.py
seed_content = """from app.models.player import Player, PlayerRole, PlayerTier
from sqlalchemy.ext.asyncio import AsyncSession

async def seed_players(db: AsyncSession):
    players = [
        Player(name="Virat Kohli", role=PlayerRole.BAT, tier=PlayerTier.MARQUEE, base_price_lakhs=200, ipl_runs=7000),
        Player(name="Rohit Sharma", role=PlayerRole.BAT, tier=PlayerTier.MARQUEE, base_price_lakhs=200, ipl_runs=6000),
        Player(name="Jasprit Bumrah", role=PlayerRole.BOWL, tier=PlayerTier.MARQUEE, base_price_lakhs=200, ipl_wickets=150),
    ]
    db.add_all(players)
    await db.commit()
"""
create_file(os.path.join(backend_dir, "data", "players_seed.py"), seed_content)

# Create services folder empty __init__.py files
create_file(os.path.join(backend_dir, "services", "__init__.py"), "")
create_file(os.path.join(backend_dir, "services", "auction_engine.py"), "# Auction logic goes here")
create_file(os.path.join(backend_dir, "services", "ai_service.py"), "# AI logic goes here")
create_file(os.path.join(backend_dir, "services", "player_service.py"), "# Player service goes here")

print("Files generated.")
