from pydantic import BaseModel
from typing import List, Optional

class TeamRanking(BaseModel):
    rank: int
    team_name: str
    overall_score: float
    grade: str

class HeadToHead(BaseModel):
    vs_team: str
    win_probability_percent: float
    reason: str

class TeamReport(BaseModel):
    team_name: str
    overall_score: float
    batting_depth: float
    bowling_balance: float
    all_round_strength: float
    value_for_money: float
    overseas_balance: float
    strengths: List[str]
    weaknesses: List[str]
    best_xi: List[str]
    captain_pick: str
    verdict: str
    head_to_head: List[HeadToHead]

class AuctionHighlights(BaseModel):
    biggest_buy: dict
    best_value_pick: dict
    worst_value_pick: dict
    biggest_rivalry: dict

class AnalysisResponse(BaseModel):
    team_rankings: List[TeamRanking]
    team_reports: List[TeamReport]
    auction_highlights: AuctionHighlights
