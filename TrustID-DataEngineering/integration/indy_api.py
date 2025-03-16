import logging
from indy import ledger, wallet
import asyncio
from typing import Optional
from indy_sdk import proof

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