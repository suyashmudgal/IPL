import uuid
from sqlalchemy import Column, String, Integer, Enum as SAEnum, Boolean, JSON, Float, Text, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
import enum

class PlayerRole(str, enum.Enum):
    BAT = "BAT"
    BOWL = "BOWL"
    AR = "AR"
    WK = "WK"

class PlayerTier(str, enum.Enum):
    MARQUEE = "Marquee"
    A = "A"
    B = "B"
    C = "C"

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, index=True)
    nationality = Column(String, nullable=False, default="Indian")
    is_overseas = Column(Boolean, default=False)
    dob = Column(String, nullable=True)
    role = Column(SAEnum(PlayerRole), nullable=False)
    base_price_lakhs = Column(Integer, nullable=False)
    tier = Column(SAEnum(PlayerTier), nullable=False)

    # Career stats
    ipl_matches = Column(Integer, default=0)
    ipl_runs = Column(Integer, default=0)
    ipl_avg = Column(Float, default=0.0)
    ipl_sr = Column(Float, default=0.0)
    ipl_fifties = Column(Integer, default=0)
    ipl_hundreds = Column(Integer, default=0)
    ipl_wickets = Column(Integer, default=0)
    ipl_economy = Column(Float, default=0.0)
    ipl_best_bowling = Column(String, nullable=True)
    ipl_catches = Column(Integer, default=0)
    ipl_stumpings = Column(Integer, default=0)

    # Recent form (last season)
    last_season_runs = Column(Integer, default=0)
    last_season_wickets = Column(Integer, default=0)
    last_season_avg = Column(Float, default=0.0)

    # IPL history as JSON
    ipl_history = Column(JSON, default=[])
