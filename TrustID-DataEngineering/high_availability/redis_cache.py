import redis
import logging
from config.settings import settings
from typing import Optional

logger = logging.getLogger(__name__)

class RedisCache:
    def __init__(self):
        self.client = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)

    def get(self, key: str) -> Optional[str]:
        try:
            return self.client.get(key)
        except Exception as e:
            logger.error(f"Failed to get key from Redis: {e}")
            return None

    def set(self, key: str, value: str, ttl: int = 3600) -> bool:
        try:
            self.client.set(key, value, ex=ttl)
            return True
        except Exception as e:
            logger.error(f"Failed to set key in Redis: {e}")
            return False