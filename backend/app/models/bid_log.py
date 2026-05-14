from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class BidLog(Base):
    __tablename__ = "bid_logs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    room_id = Column(String, ForeignKey("rooms.id"), nullable=False)
    player_id = Column(Integer, nullable=False)
    bidder_token = Column(String, nullable=False)
    team_name = Column(String, nullable=False)
    amount_lakhs = Column(Integer, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
