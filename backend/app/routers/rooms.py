from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas.room import CreateRoomRequest, CreateRoomResponse, JoinRoomRequest, JoinRoomResponse, RoomStateResponse
from app.models.room import Room, RoomStatus
from app.models.squad import Squad
import uuid
import random
import string
from app.redis_client import redis_set

router = APIRouter()

def generate_room_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

@router.post("/create", response_model=CreateRoomResponse)
async def create_room(req: CreateRoomRequest, db: AsyncSession = Depends(get_db)):
    code = generate_room_code()
    host_token = str(uuid.uuid4())
    
    room = Room(
        code=code,
        host_token=host_token,
        room_name=req.room_name,
        mode=req.mode,
        timer_seconds=req.timer_seconds,
        participants=[{"name": req.host_name, "token": host_token, "ipl_team": req.ipl_team, "is_spectator": False, "is_ready": True}]
    )
    db.add(room)
    
    host_squad = Squad(
        room_id=room.id,
        team_name=req.host_name,
        ipl_team=req.ipl_team,
        owner_token=host_token
    )
    db.add(host_squad)
    
    await db.commit()
    return CreateRoomResponse(room_code=code, host_token=host_token)

@router.post("/{code}/join", response_model=JoinRoomResponse)
async def join_room(code: str, req: JoinRoomRequest, db: AsyncSession = Depends(get_db)):
    # simple implementation, requires full query later
    # for now we'll just mock this or return a token
    player_token = str(uuid.uuid4())
    return JoinRoomResponse(player_token=player_token, room_code=code)
