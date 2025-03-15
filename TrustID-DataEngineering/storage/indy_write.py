from indy import IndyError, ledger, wallet, proof
import asyncio
import logging
from typing import List

logger = logging.getLogger(__name__)

class IndyLedger:
    def __init__(self):
        self.pool_handle = None
        self.wallet_handle = None

    async def connect(self):
        try:
            self.pool_handle = await ledger.open_pool_ledger("pool_config", None)
            self.wallet_handle = await wallet.open_wallet("wallet_config", None, None)
            logger.info("Connected to Indy ledger")
        except IndyError as e:
            logger.error(f"Failed to connect to Indy ledger: {e}", extra={"error": str(e)})
            raise

    async def register_schema(self, schema_name: str, schema_version: str, attributes: List[str]):
        try:
            schema_request = await ledger.build_schema_request("issuer_did", schema_name, schema_version, attributes)
            schema_response = await ledger.sign_and_submit_request(self.pool_handle, self.wallet_handle, "issuer_did", schema_request)
            schema_id = schema_response["result"]["txn"]["data"]["data"]["id"]
            logger.info(f"Registered schema: {schema_name}", extra={"schema_id": schema_id})
            return schema_id
        except IndyError as e:
            logger.error(f"Schema registration failed: {e}", extra={"error": str(e)})
            raise

    async def create_credential_definition(self, schema_id: str):
        try:
            cred_def_request = await ledger.build_cred_def_request("issuer_did", schema_id, "TAG", "CL", {"support_revocation": True})
            cred_def_response = await ledger.sign_and_submit_request(self.pool_handle, self.wallet_handle, "issuer_did", cred_def_request)
            cred_def_id = cred_def_response["result"]["txn"]["data"]["id"]
            logger.info(f"Created credential definition: {cred_def_id}", extra={"cred_def_id": cred_def_id})
            return cred_def_id
        except IndyError as e:
            logger.error(f"Credential definition creation failed: {e}", extra={"error": str(e)})
            raise

    async def issue_credential(self, cred_def_id: str, user_did: str, attributes: dict):
        try:
            credential_offer = await ledger.build_cred_offer_request("issuer_did", cred_def_id)
            credential_request = await proof.create_credential_request(self.wallet_handle, user_did, credential_offer, "master_secret_id", None)
            credential = await proof.create_credential(self.wallet_handle, credential_offer, credential_request, attributes, None, None)
            logger.info(f"Issued credential for user: {user_did}", extra={"cred_def_id": cred_def_id})
            return credential
        except IndyError as e:
            logger.error(f"Credential issuance failed: {e}", extra={"error": str(e)})
            raise

    async def revoke_credential(self, cred_def_id: str, credential_id: str):
        try:
            revoke_request = await ledger.build_revoke_cred_def_request("issuer_did", cred_def_id, credential_id)
            await ledger.sign_and_submit_request(self.pool_handle, self.wallet_handle, "issuer_did", revoke_request)
            logger.info(f"Revoked credential: {credential_id}", extra={"cred_def_id": cred_def_id})
        except IndyError as e:
            logger.error(f"Credential revocation failed: {e}", extra={"error": str(e)})
            raise

    async def close(self):
        if self.wallet_handle:
            await wallet.close_wallet(self.wallet_handle)
        if self.pool_handle:
            await ledger.close_pool_ledger(self.pool_handle)
        logger.info("Closed Indy ledger connection")