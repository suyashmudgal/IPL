import enum
from sqlalchemy import Column, String, Integer, Enum as SAEnum, Boolean, JSON, Float
from app.database import Base

class PlayerRole(str, enum.Enum):
    BAT = "BAT"; BOWL = "BOWL"; AR = "AR"; WK = "WK"

class PlayerTier(str, enum.Enum):
    MARQUEE = "Marquee"; A = "A"; B = "B"; C = "C"

class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, index=True)
    nationality = Column(String, default="Indian")
    is_overseas = Column(Boolean, default=False)
    role = Column(SAEnum(PlayerRole), nullable=False)
    base_price_lakhs = Column(Integer, nullable=False)
    tier = Column(SAEnum(PlayerTier), nullable=False)
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
    last_season_runs = Column(Integer, default=0)
    last_season_wickets = Column(Integer, default=0)
    last_season_avg = Column(Float, default=0.0)
    ipl_history = Column(JSON, default=[])
