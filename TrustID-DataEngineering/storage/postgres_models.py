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