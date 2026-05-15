from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.database import init_db
from app.routers import rooms, auction, players, analysis
from app.websocket import handlers

app = FastAPI(title="IPL Auction Pro API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    await init_db()

app.include_router(rooms.router, prefix="/api/rooms", tags=["Rooms"])
app.include_router(auction.router, prefix="/api/rooms", tags=["Auction"])
app.include_router(players.router, prefix="/api/players", tags=["Players"])
app.include_router(analysis.router, prefix="/api/rooms", tags=["Analysis"])
app.include_router(handlers.router, prefix="/api/ws", tags=["WebSocket"])

@app.get("/api/health")
def health_check():
    return {"status": "ok"}
