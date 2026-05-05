import httpx
from schemas.pay_client_schema import SuccesPay

class ArgentCoreClient:
    def __init__(self, base_url: str = "http://127.0.0.1:8000"):
        self.base_url = base_url

        self.client = httpx.AsyncClient(base_url=base_url)

    async def update_balance(self, user_id: int, amount: int):
        data = SuccesPay(user_id=user_id, amount=amount)
        try:
            response = await self.client.post(f"/users/update_balance", json=data.model_dump())
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error amount{e}")
            return None