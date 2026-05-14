from sqlalchemy import Column, String, Integer, ForeignKey, JSON
from app.database import Base

class Squad(Base):
    __tablename__ = "squads"
    id = Column(Integer, primary_key=True, autoincrement=True)
    room_id = Column(String, ForeignKey("rooms.id"), nullable=False)
    team_name = Column(String, nullable=False)
    ipl_team = Column(String, nullable=False)
    owner_token = Column(String, nullable=False)
    budget_remaining_lakhs = Column(Integer, default=9000)
    players = Column(JSON, default=[])
    overseas_count = Column(Integer, default=0)
