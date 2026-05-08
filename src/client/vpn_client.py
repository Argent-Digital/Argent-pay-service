import httpx
from src.config import settings
from src.schemas.vpn_client_schema import DeleteKeys
from typing import List

class ArgentVpnClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        
        self.client = httpx.AsyncClient(
            base_url=base_url,
            timeout=httpx.Timeout(10.0, connect=5.0)
        )

    async def close(self):
        await self.client.aclose()

    async def remove_keys(self, keys: List[DeleteKeys]):
        try:
            payload = [key.model_dump(mode='json') for key in keys]

            response = await self.client.post("/vpn/remove_keys", json=payload)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"ERROR in vpn client: {e}")
            return None