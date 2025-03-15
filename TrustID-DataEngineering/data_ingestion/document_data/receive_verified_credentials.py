import logging
from pydantic import BaseModel, ValidationError
import requests
from tenacity import retry, stop_after_attempt, wait_fixed

logger = logging.getLogger(__name__)

class CredentialData(BaseModel):
    credential_type: str
    holder_name: str
    attributes: dict

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def receive_credentials(endpoint: str, api_key: str):
    try:
        response = requests.get(endpoint, headers={"Authorization": f"Bearer {api_key}"}, timeout=30, verify=True)
        response.raise_for_status()
        data = response.json()
        cred_data = CredentialData(**data)
        logger.info(f"Received valid credential: {cred_data}", extra={"credential_type": cred_data.credential_type})
        return cred_data.dict()
    except ValidationError as e:
        logger.error(f"Invalid credential format: {e}")
        raise
    except requests.RequestException as e:
        logger.error(f"API request failed: {e}")
        raise