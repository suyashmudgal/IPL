import os
from dotenv import load_dotenv
load_dotenv()

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./ipl_auction.db")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379")
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "ipl-auction-pro-2026")
    CORS_ORIGINS: list = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")
    ROOM_TTL: int = 6 * 3600

settings = Settings()
