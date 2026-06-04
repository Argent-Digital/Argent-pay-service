import httpx
from src.schemas.pay_client_schema import SuccesPay, UserWithLowBalance, IdsByDelUser, BillingResponse
from src.schemas.jwt_schema import TokenData
from src.auth.security import create_access_token
from typing import List

class ArgenBotClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

        self.client = httpx.AsyncClient(base_url=base_url,
                                        timeout=httpx.Timeout(10.0, connect=5.0))
    
    async def close(self):
        await self.client.aclose()

    async def send_notification(self, user_id: int, amount: int):
        token_data = TokenData(user_id=user_id)
        token = create_access_token(data=token_data)
        data = SuccesPay(amount=amount)
        try:
            header = {"Authorization": f"Bearer {token}"}
            response = await self.client.post(f"/pays/success_pay", json=data.model_dump(), headers=header)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error of notification on bot service: {e}")
            return None
        
    async def sending_notif_user(self, billing_response: BillingResponse, user_id: int = 0):
        token_data = TokenData(user_id=user_id)
        token = create_access_token(data=token_data)
        try:
            header = {"Authorization": f"Bearer {token}"}
            response = await self.client.post("/pays/warning_users", json=billing_response.model_dump(), headers=header)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error send users list on bot api: {e}")
            return None