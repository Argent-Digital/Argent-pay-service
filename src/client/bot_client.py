import httpx
from src.schemas.pay_client_schema import SuccesPay, UserWithLowBalance
from src.schemas.vpn_client_schema import DeleteKeys, BillingResponse
from typing import List

class ArgenBotClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

        self.client = httpx.AsyncClient(base_url=base_url,
                                        timeout=httpx.Timeout(10.0, connect=5.0))
    
    async def close(self):
        await self.client.aclose()

    async def send_notification(self, user_id: int, amount: int):
        data = SuccesPay(user_id=user_id, amount=amount)
        try:
            response = await self.client.post(f"/pays/success_pay", json=data.model_dump())
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error of notification on bot service: {e}")
            return None
        
    async def sending_notif_user(self, users_warning: List[UserWithLowBalance], users_del: List[DeleteKeys]) -> BillingResponse:
        try:
            data = BillingResponse(deleted_keys=users_del, user_lower=users_warning)

            response = await self.client.post("/pays/warning_users", json=data.model_dump())
            response.raise_for_status()
            return BillingResponse(**response.json())
        except Exception as e:
            print(f"Error send users list on bot api: {e}")
            return None