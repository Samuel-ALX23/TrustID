

code 2: 📥 data_ingestion/
receive_verified_data.py
python
Copy
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
receive_verified_credentials.py

import logging
from pydantic import BaseModel, ValidationError
import requests
from tenacity import retry, stop_after_attempt, wait_fixed
from typing import Dict, List
import asyncio
from message_queue import RabbitMQ  # For decoupling data ingestion and processing

logger = logging.getLogger(__name__)

class CredentialData(BaseModel):
    credential_type: str
    holder_name: str
    attributes: Dict[str, str]

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
async def receive_credentials(endpoint: str, api_key: str):
    try:
        response = requests.get(endpoint, headers={"Authorization": f"Bearer {api_key}"}, timeout=30, verify=True)
        response.raise_for_status()
        data = response.json()
        cred_data = CredentialData(**data)
        logger.info(f"Received valid credential: {cred_data}", extra={"credential_type": cred_data.credential_type})

        # Send data to message queue for decoupled processing
        await RabbitMQ.publish("credential_data_queue", cred_data.dict())
        return cred_data.dict()
    except ValidationError as e:
        logger.error(f"Invalid credential format: {e}")
        raise
    except requests.RequestException as e:
        logger.error(f"API request failed: {e}")
        raise
🔄 data_processing/
clean_data.py

import re
from datetime import datetime
import logging
from typing import Optional

logger = logging.getLogger(__name__)

class DataCleaner:
    @staticmethod
    def clean_name(name: str) -> str:
        cleaned = name.strip().title()
        if not re.match(r"^[A-Za-z \-']+$", cleaned):
            logger.error(f"Invalid name format: {name}", extra={"input": name})
            raise ValueError("Invalid name format: must contain only letters, spaces, hyphens, or apostrophes")
        return cleaned

    @staticmethod
    def clean_email(email: str) -> str:
        cleaned = email.strip().lower()
        if not re.match(r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$", cleaned):
            logger.error(f"Invalid email format: {email}", extra={"input": email})
            raise ValueError("Invalid email format: must be a valid email address")
        return cleaned

    @staticmethod
    def clean_date(date_str: str) -> str:
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            logger.error(f"Invalid date format: {date_str}", extra={"input": date_str})
            raise ValueError("Invalid date format: must be YYYY-MM-DD")

    @staticmethod
    def clean_phone(phone: Optional[str]) -> Optional[str]:
        if not phone:
            return None
        cleaned = re.sub(r"[^\d+]", "", phone)
        if not re.match(r"^\+?[1-9]\d{7,14}$", cleaned):
            logger.error(f"Invalid phone number: {phone}", extra={"input": phone})
            raise ValueError("Invalid phone number: must be 8-15 digits, optionally starting with +")
        return cleaned
	    
transform_data.py

from uuid import uuid4
from datetime import datetime
from storage import postgres_models
from indy import ledger
import asyncio
import logging
from typing import Dict

logger = logging.getLogger(__name__)

class DataTransformer:
    async def transform_user(self, clean_data: Dict) -> postgres_models.User:
        user = postgres_models.User(
            user_id=str(uuid4()),
            first_name=clean_data["first_name"],
            last_name=clean_data["last_name"],
            email=clean_data["email"],
            dob=clean_data["dob"],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        logger.info(f"Transformed user data: {user}", extra={"user_id": user.user_id})
        return user

    async def transform_credential(self, clean_data: Dict, schema_name: str) -> postgres_models.Credential:
        try:
            # Register schema if not exists
            schema_request = await ledger.build_schema_request("issuer_did", schema_name, "1.0", list(clean_data.keys()))
            schema_response = await ledger.sign_and_submit_request("pool_handle", "wallet_handle", "issuer_did", schema_request)
            schema_id = schema_response["result"]["txn"]["data"]["data"]["id"]
            logger.info(f"Registered schema: {schema_name}", extra={"schema_id": schema_id})

            # Create credential definition
            cred_def_request = await ledger.build_cred_def_request("issuer_did", schema_id, "TAG", "CL", {"support_revocation": True})
            cred_def_response = await ledger.sign_and_submit_request("pool_handle", "wallet_handle", "issuer_did", cred_def_request)
            cred_def_id = cred_def_response["result"]["txn"]["data"]["id"]
            logger.info(f"Created credential definition: {cred_def_id}", extra={"cred_def_id": cred_def_id})

            credential = postgres_models.Credential(
                credential_id=str(uuid4()),
                cred_def_id=cred_def_id,
                user_id=clean_data["user_id"],
                attributes=str(clean_data),
                status="Active",
                created_at=datetime.utcnow()
            )
            logger.info(f"Transformed credential: {credential}", extra={"credential_id": credential.credential_id})
            return credential
        except ledger.IndyError as e:
            logger.error(f"Credential transformation failed: {e}", extra={"error": str(e)})
            raise
encrypt_data.py
python
Copy
from cryptography.fernet import Fernet
from storage import openssl_keys
import logging

logger = logging.getLogger(__name__)

class DataEncryptor:
    def __init__(self):
        self.key_manager = openssl_keys.KeyManager()
        self.key = self.key_manager.generate_key()
        logger.info("Initialized DataEncryptor with new key")

    def encrypt_field(self, data: str) -> str:
        try:
            f = Fernet(self.key)
            encrypted = f.encrypt(data.encode()).decode()
            logger.info("Data encrypted successfully", extra={"data_length": len(data)})
            return encrypted
        except Exception as e:
            logger.error(f"Encryption failed: {e}", extra={"error": str(e)})
            raise

    def decrypt_field(self, encrypted_data: str) -> str:
        try:
            f = Fernet(self.key)
            decrypted = f.decrypt(encrypted_data.encode()).decode()
            logger.info("Data decrypted successfully", extra={"data_length": len(decrypted)})
            return decrypted
        except Exception as e:
            logger.error(f"Decryption failed: {e}", extra={"error": str(e)})
            raise
		
🗄️ storage/
postgres_models.py

from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import List, Optional

class User(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    user_id: str = Field(unique=True, index=True)
    first_name: str
    last_name: str
    email: str = Field(encrypted=True)
    phone_number: Optional[str] = Field(encrypted=True)
    dob: datetime.date = Field(encrypted=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default=None)
    dids: List["DID"] = Relationship(back_populates="user")
    credentials: List["Credential"] = Relationship(back_populates="user")

class DID(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    did_id: str = Field(unique=True, index=True)
    user_id: str = Field(foreign_key="user.user_id")
    public_key: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    user: Optional[User] = Relationship(back_populates="dids")

class Schema(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    schema_id: str = Field(unique=True, index=True)
    schema_name: str
    attributes: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class CredentialDefinition(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    cred_def_id: str = Field(unique=True, index=True)
    schema_id: str = Field(foreign_key="schema.schema_id")
    issuer_did: str
    signature_type: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    schema: Optional[Schema] = Relationship(back_populates="credential_definitions")

class Credential(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    credential_id: str = Field(unique=True, index=True)
    cred_def_id: str = Field(foreign_key="credentialdefinition.cred_def_id")
    user_id: str = Field(foreign_key="user.user_id")
    attributes: str
    status: str = Field(default="Active")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    user: Optional[User] = Relationship(back_populates="credentials")
    credential_definition: Optional[CredentialDefinition] = Relationship(back_populates="credentials")

class RevocationRegistry(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    revocation_id: str = Field(unique=True, index=True)
    credential_id: str = Field(foreign_key="credential.credential_id")
    revoked_at: datetime = Field(default_factory=datetime.utcnow)
    credential: Optional[Credential] = Relationship(back_populates="revocation_registries")

class VerificationRequest(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    verification_id: str = Field(unique=True, index=True)
    verifier_id: str
    user_id: str = Field(foreign_key="user.user_id")
    status: str = Field(default="Pending")
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    user: Optional[User] = Relationship(back_populates="verification_requests")

class EncryptionKey(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    key_id: str = Field(unique=True, index=True)
    user_id: str = Field(foreign_key="user.user_id")
    public_key: str
    private_key: str = Field(encrypted=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    user: Optional[User] = Relationship(back_populates="encryption_keys")

🔗 integration/
backend_api.py

import logging
import requests
from tenacity import retry, stop_after_attempt, wait_fixed
from typing import Dict, Optional

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
indy_api.py

import logging
from indy import ledger, wallet
import asyncio

logger = logging.getLogger(__name__)

class IndyAPI:
    def __init__(self, pool_handle: str, wallet_handle: str, issuer_did: str):
        self.pool_handle = pool_handle
        self.wallet_handle = wallet_handle
        self.issuer_did = issuer_did

    async def register_schema(self, schema_name: str, schema_version: str, attributes: list) -> Optional[str]:
        try:
            schema_request = await ledger.build_schema_request(self.issuer_did, schema_name, schema_version, attributes)
            schema_response = await ledger.sign_and_submit_request(self.pool_handle, self.wallet_handle, self.issuer_did, schema_request)
            schema_id = schema_response["result"]["txn"]["data"]["data"]["id"]
            logger.info(f"Registered schema: {schema_name}", extra={"schema_id": schema_id})
            return schema_id
        except ledger.IndyError as e:
            logger.error(f"Schema registration failed: {e}")
            return None

    async def issue_credential(self, cred_def_id: str, user_did: str, attributes: dict) -> Optional[dict]:
        try:
            credential_offer = await ledger.build_cred_offer_request(self.issuer_did, cred_def_id)
            credential_request = await proof.create_credential_request(self.wallet_handle, user_did, credential_offer, "master_secret_id", None)
            credential = await proof.create_credential(self.wallet_handle, credential_offer, credential_request, attributes, None, None)
            logger.info(f"Issued credential for user: {user_did}", extra={"cred_def_id": cred_def_id})
            return credential
        except ledger.IndyError as e:
            logger.error(f"Credential issuance failed: {e}")
            return None
analytics_api.py

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
⚙️ config/
settings.py

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
database.py
python
Copy
from sqlmodel import create_engine, Session
from config.settings import settings

engine = create_engine(settings.POSTGRES_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session
📜 scripts/
setup_db.py

from sqlmodel import SQLModel, create_engine
from config.settings import settings
from storage import postgres_models

def initialize_db():
    engine = create_engine(settings.POSTGRES_URL)
    SQLModel.metadata.create_all(engine)
    print("Database tables created successfully.")

if __name__ == "__main__":
    initialize_db()
setup_indy.py
python
Copy
from indy import pool, wallet
import asyncio
from config.settings import settings

async def initialize_indy():
    try:
        await pool.create_pool_ledger_config(settings.INDY_POOL_NAME, None)
        await wallet.create_wallet(settings.INDY_POOL_NAME, settings.INDY_WALLET_NAME, None, None, settings.INDY_WALLET_KEY)
        print("Indy ledger and wallet initialized successfully.")
    except Exception as e:
        print(f"Failed to initialize Indy: {e}")

if __name__ == "__main__":
    asyncio.run(initialize_indy())
	
🧪 tests/
test_data_pipeline.py

import pytest
from data_ingestion.receive_verified_data import receive_data
from data_processing.clean_data import DataCleaner
from storage.postgres_models import User
from config.database import get_session

@pytest.mark.asyncio
async def test_data_pipeline():
    # Test data ingestion
    test_data = {"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com", "dob": "1990-01-01"}
    ingested_data = await receive_data("https://api.example.com/users", "test_api_key")
    assert ingested_data == test_data

    # Test data cleaning
    cleaner = DataCleaner()
    cleaned_data = {
        "first_name": cleaner.clean_name(test_data["first_name"]),
        "last_name": cleaner.clean_name(test_data["last_name"]),
        "email": cleaner.clean_email(test_data["email"]),
        "dob": cleaner.clean_date(test_data["dob"])
    }
    assert cleaned_data["email"] == "john.doe@example.com"

    # Test data storage
    session = next(get_session())
    user = User(**cleaned_data)
    session.add(user)
    session.commit()
    assert user.user_id is not None
🐳 docker/
Dockerfile

FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
docker-compose.yml
yaml
Copy
version: "3.8"
services:
  postgres:
    image: postgres:13
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: trustid
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  app:
    build: .
    depends_on:
      - postgres
    environment:
      POSTGRES_URL: "postgresql://user:password@postgres:5432/trustid"
    ports:
      - "8000:8000"

volumes:
  postgres_data:
.dockerignore
Copy
.env
__pycache__
*.pyc
*.pyo
*.pyd
.DS_Store
Makefile
makefile
Copy
build:
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down

test:
	docker-compose run app pytest
🔄 high_availability/
postgres_replication_setup.py

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
redis_cache.py

import redis
import logging
from config.settings import settings

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
🔧 ci_cd/
github_actions.yml

name: CI/CD Pipeline

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: "3.9"
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run tests
        run: pytest
📜 requirements.txt
sqlmodel==0.0.6
psycopg2-binary==2.9.3
indy-sdk==1.16.0
cryptography==36.0.1
requests==2.26.0
python-dotenv==0.19.2
pytest==7.0.1
redis==4.1.0
