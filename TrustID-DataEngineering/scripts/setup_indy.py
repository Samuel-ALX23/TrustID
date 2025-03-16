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