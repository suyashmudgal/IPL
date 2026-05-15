from fastapi import APIRouter, Depends, Query
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
