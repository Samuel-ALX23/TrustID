import logging
from sqlmodel import create_engine
from config.settings import settings

logger = logging.getLogger(__name__)

def setup_replication():
    try:
        primary_engine = create_engine(settings.POSTGRES_URL)
        replica_engine = create_engine(settings.POSTGRES_REPLICA_URL)
        logger.info("PostgreSQL replication setup completed.")
    except Exception as e:
        logger.error(f"Failed to setup replication: {e}")