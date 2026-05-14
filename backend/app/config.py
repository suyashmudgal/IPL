import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:password@localhost:5432/ipl_auction")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379")
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "ipl-auction-pro-secret-key-2026")
    CORS_ORIGINS: list = os.getenv("CORS_ORIGINS", "http://localhost:3000,http://localhost:3001").split(",")
    ROOM_TTL_SECONDS: int = 6 * 3600  # 6 hours

settings = Settings()
