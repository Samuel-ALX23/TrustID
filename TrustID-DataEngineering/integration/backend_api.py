import logging
import requests
from tenacity import retry, stop_after_attempt, wait_fixed
from typing import Dict, Optional
from typing import Optional

logger = logging.getLogger(__name__)

class BackendAPI:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def get_user_data(self, user_id: str) -> Optional[Dict]:
        try:
            response = requests.get(
                f"{self.base_url}/users/{user_id}",
                headers={"Authorization": f"Bearer {self.api_key}"},
                timeout=30,
                verify=True
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Failed to fetch user data: {e}")
            return None

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def get_credential_data(self, credential_id: str) -> Optional[Dict]:
        try:
            response = requests.get(
                f"{self.base_url}/credentials/{credential_id}",
                headers={"Authorization": f"Bearer {self.api_key}"},
                timeout=30,
                verify=True
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Failed to fetch credential data: {e}")
            return None