from src.config import settings
from src.client.bot_client import ArgenBotClient
from src.client.core_client import ArgentCoreClient

_core_client = ArgentCoreClient(base_url=settings.CORE_URL)
_bot_client = ArgenBotClient(base_url=settings.BOT_URL)

async def get_core_client() -> ArgentCoreClient:
    return _core_client

async def get_bot_client() -> ArgenBotClient:
    return _bot_client