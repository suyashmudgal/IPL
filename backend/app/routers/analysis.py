from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db

router = APIRouter()

@router.post("/{code}/analyze")
async def analyze_room(code: str, db: AsyncSession = Depends(get_db)):
    return {"status": "analyzing"}

@router.get("/{code}/analysis")
async def get_analysis(code: str, db: AsyncSession = Depends(get_db)):
    return {"status": "analysis data"}
