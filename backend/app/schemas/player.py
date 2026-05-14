from pydantic import BaseModel
from typing import Optional, List
from enum import Enum

class PlayerRoleEnum(str, Enum):
    BAT="BAT"; BOWL="BOWL"; AR="AR"; WK="WK"

class PlayerTierEnum(str, Enum):
    MARQUEE="Marquee"; A="A"; B="B"; C="C"

class PlayerResponse(BaseModel):
    id: int
    name: str
    nationality: str
    is_overseas: bool
    role: str
    base_price_lakhs: int
    tier: str
    ipl_matches: int
    ipl_runs: int
    ipl_avg: float
    ipl_sr: float
    ipl_fifties: int
    ipl_hundreds: int
    ipl_wickets: int
    ipl_economy: float
    ipl_best_bowling: Optional[str]
    ipl_catches: int
    ipl_stumpings: int
    last_season_runs: int
    last_season_wickets: int
    last_season_avg: float
    ipl_history: list

    class Config:
        from_attributes = True
