import enum, uuid
from sqlalchemy import Column, String, Integer, Enum as SAEnum, JSON, DateTime
from sqlalchemy.sql import func
from app.database import Base

class AuctionMode(str, enum.Enum):
    MOCK_2026 = "mock_2026"; MEGA = "mega"; CUSTOM = "custom"

class RoomStatus(str, enum.Enum):
    LOBBY = "lobby"; ACTIVE = "active"; PAUSED = "paused"; COMPLETE = "complete"

class Room(Base):
    __tablename__ = "rooms"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    code = Column(String(6), unique=True, nullable=False, index=True)
    host_token = Column(String, nullable=False)
    room_name = Column(String, nullable=False)
    mode = Column(SAEnum(AuctionMode), default=AuctionMode.MOCK_2026)
    status = Column(SAEnum(RoomStatus), default=RoomStatus.LOBBY)
    timer_seconds = Column(Integer, default=15)
    current_player_index = Column(Integer, default=0)
    player_set = Column(JSON, default=[])
    participants = Column(JSON, default=[])
    analysis_result = Column(JSON, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
