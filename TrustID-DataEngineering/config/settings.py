import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    POSTGRES_URL = os.getenv("POSTGRES_URL", "postgresql://user:password@localhost:5432/trustid")
    INDY_POOL_NAME = os.getenv("INDY_POOL_NAME", "trustid_pool")
    INDY_WALLET_NAME = os.getenv("INDY_WALLET_NAME", "trustid_wallet")
    INDY_WALLET_KEY = os.getenv("INDY_WALLET_KEY", "trustid_key")
    BACKEND_API_KEY = os.getenv("BACKEND_API_KEY", "default_api_key")
    ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY", "default_encryption_key")

settings = Settings()