import json, asyncio
from typing import Any, Dict, Optional

# In-memory fallback when Redis is unavailable
_store: Dict[str, Any] = {}
_pubsub_channels: Dict[str, list] = {}
_use_redis = False
_redis = None

async def get_redis():
    global _redis, _use_redis
    if _redis is not None:
        return _redis
    try:
        import redis.asyncio as aioredis
        from app.config import settings
        r = aioredis.from_url(settings.REDIS_URL, encoding="utf-8", decode_responses=True, socket_connect_timeout=2)
        await r.ping()
        _redis = r
        _use_redis = True
        print("✅ Redis connected")
        return _redis
    except Exception:
        print("⚠️  Redis unavailable – using in-memory store")
        _use_redis = False
        return None

class FakeRedis:
    async def get(self, key):
        return _store.get(key)
    async def set(self, key, value, ex=None):
        _store[key] = value
    async def delete(self, key):
        _store.pop(key, None)
    async def publish(self, channel, message):
        for cb in _pubsub_channels.get(channel, []):
            asyncio.create_task(cb(message))

_fake = FakeRedis()

async def redis_get(key: str) -> Optional[str]:
    r = await get_redis()
    return await (r or _fake).get(key)

async def redis_set(key: str, value: str, ex: int = None):
    r = await get_redis()
    await (r or _fake).set(key, value, ex=ex)

async def redis_delete(key: str):
    r = await get_redis()
    await (r or _fake).delete(key)

async def redis_publish(channel: str, message: str):
    r = await get_redis()
    await (r or _fake).publish(channel, message)
