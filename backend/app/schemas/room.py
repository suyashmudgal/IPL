from pydantic import BaseModel
from typing import Optional, List
from enum import Enum

class AuctionModeEnum(str, Enum):
    MOCK_2026 = "mock_2026"; MEGA = "mega"; CUSTOM = "custom"

class CreateRoomRequest(BaseModel):
    room_name: str
    host_name: str
    ipl_team: str
    mode: AuctionModeEnum = AuctionModeEnum.MOCK_2026
    timer_seconds: int = 15

class JoinRoomRequest(BaseModel):
    player_name: str
    ipl_team: str
    is_spectator: bool = False

class CreateRoomResponse(BaseModel):
    room_code: str
    host_token: str

class JoinRoomResponse(BaseModel):
    player_token: str
    room_code: str

class ParticipantInfo(BaseModel):
    token: str
    name: str
    ipl_team: str
    is_spectator: bool = False
    is_ready: bool = False

class RoomStateResponse(BaseModel):
    code: str
    room_name: str
    mode: str
    status: str
    timer_seconds: int
    participants: List[dict]
    current_player_index: int
