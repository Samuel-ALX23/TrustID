from cryptography.hazmat.primitives import serialization, asymmetric
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
import logging
import os

logger = logging.getLogger(__name__)

class KeyManager:
    def __init__(self):
        self.key_dir = os.path.join(os.getcwd(), "keys")
        os.makedirs(self.key_dir, exist_ok=True)

    def generate_key_pair(self):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        logger.info("Generated new key pair")
        return private_key, public_key

    def store_key(self, private_key, user_id: str):
        try:
            serialized_private = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )
            key_path = os.path.join(self.key_dir, f"{user_id}_private.pem")
            with open(key_path, "wb") as f:
                f.write(serialized_private)
            logger.info(f"Stored private key for user: {user_id}", extra={"key_path": key_path})
        except Exception as e:
            logger.error(f"Failed to store private key: {e}", extra={"error": str(e)})
            raise