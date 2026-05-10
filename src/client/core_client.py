import httpx
from src.schemas.pay_client_schema import SuccesPay, BillingStart
from src.schemas.vpn_client_schema import BillingResponse

class ArgentCoreClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

        self.client = httpx.AsyncClient(
            base_url=base_url,
            timeout=httpx.Timeout(10.0, connect=5.0)
            )
        
    async def close(self):
        await self.client.aclose()

    async def update_balance(self, user_id: int, amount: int):
        data = SuccesPay(user_id=user_id, amount=amount)
        try:
            response = await self.client.post(f"/users/update_balance", json=data.model_dump())
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error amount{e}")
            return None
        
    async def daily_billing(self, start: bool) -> BillingResponse:
        data = BillingStart(start=start)
        try:
            response = await self.client.post(f"/pay/start_billing", json=data.model_dump())
            response.raise_for_status()
            return BillingResponse(**response.json())
        except Exception as e:
            print(f"Error billing request on core: {e}")
            return None