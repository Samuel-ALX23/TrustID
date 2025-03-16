import logging
from pydantic import BaseModel, ValidationError
import requests
from tenacity import retry, stop_after_attempt, wait_fixed
from typing import Optional
import asyncio
from message_queue import RabbitMQ  # For decoupling data ingestion and processing

logger = logging.getLogger(__name__)

class UserData(BaseModel):
    first_name: str
    last_name: str
    email: str
    dob: str
    phone_number: Optional[str] = None

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
async def receive_data(endpoint: str, api_key: str):
    try:
        response = requests.get(endpoint, headers={"Authorization": f"Bearer {api_key}"}, timeout=30, verify=True)
        response.raise_for_status()
        data = response.json()
        user_data = UserData(**data)
        logger.info(f"Received valid user data: {user_data}")

        # Send data to message queue for decoupled processing
        await RabbitMQ.publish("user_data_queue", user_data.dict())
        return user_data.dict()
    except ValidationError as e:
        logger.error(f"Invalid data format: {e}")
        raise
    except requests.RequestException as e:
        logger.error(f"API request failed: {e}")
        raise