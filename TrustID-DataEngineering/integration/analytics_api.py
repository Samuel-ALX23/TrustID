import logging
from typing import Dict, List
from storage import postgres_models
from sqlmodel import Session, select

logger = logging.getLogger(__name__)

class AnalyticsAPI:
    def __init__(self, session: Session):
        self.session = session

    def get_user_credentials(self, user_id: str) -> List[Dict]:
        try:
            user = self.session.exec(select(postgres_models.User).where(postgres_models.User.user_id == user_id)).first()
            if not user:
                logger.error(f"User not found: {user_id}")
                return []
            return [cred.dict() for cred in user.credentials]
        except Exception as e:
            logger.error(f"Failed to fetch user credentials: {e}")
            return []

    def get_credential_stats(self) -> Dict:
        try:
            total_credentials = self.session.exec(select(postgres_models.Credential)).count()
            active_credentials = self.session.exec(select(postgres_models.Credential).where(postgres_models.Credential.status == "Active")).count()
            return {
                "total_credentials": total_credentials,
                "active_credentials": active_credentials
            }
        except Exception as e:
            logger.error(f"Failed to fetch credential stats: {e}")
            return {}