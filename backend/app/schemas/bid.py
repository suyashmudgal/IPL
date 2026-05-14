from pydantic import BaseModel

class PlaceBidRequest(BaseModel):
    amount_lakhs: int
    player_token: str

class BidResponse(BaseModel):
    success: bool
    new_amount_lakhs: int
    leader_team: str
    message: str = ""
