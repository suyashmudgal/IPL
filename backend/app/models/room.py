import uuid
import enum
from sqlalchemy import Column, String, Integer, Enum as SAEnum, Boolean, JSON, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class AuctionMode(str, enum.Enum):
    MOCK_2026 = "mock_2026"
    MEGA = "mega"
    CUSTOM = "custom"

class RoomStatus(str, enum.Enum):
    LOBBY = "lobby"
    ACTIVE = "active"
    PAUSED = "paused"
    COMPLETE = "complete"

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
    player_set = Column(JSON, default=[])  # ordered list of player IDs
    participants = Column(JSON, default=[])  # list of {token, name, team, is_spectator}
    analysis_result = Column(JSON, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
