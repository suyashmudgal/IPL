from app.models.player import Player, PlayerRole, PlayerTier
from sqlalchemy.ext.asyncio import AsyncSession

async def seed_players(db: AsyncSession):
    players = [
        Player(name="Virat Kohli", role=PlayerRole.BAT, tier=PlayerTier.MARQUEE, base_price_lakhs=200, ipl_runs=7000),
        Player(name="Rohit Sharma", role=PlayerRole.BAT, tier=PlayerTier.MARQUEE, base_price_lakhs=200, ipl_runs=6000),
        Player(name="Jasprit Bumrah", role=PlayerRole.BOWL, tier=PlayerTier.MARQUEE, base_price_lakhs=200, ipl_wickets=150),
    ]
    db.add_all(players)
    await db.commit()
