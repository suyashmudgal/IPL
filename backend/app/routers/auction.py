from fastapi import APIRouter, Depends, HTTPException
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
