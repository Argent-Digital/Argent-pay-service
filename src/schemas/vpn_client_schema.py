from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from uuid import UUID
from src.schemas.pay_client_schema import UserWithLowBalance

class DeleteKeys(BaseModel):
    user_id: int
    server_key_if: Optional[str]
    protocol: str
    vless_uuid: Optional[UUID]

    model_config=ConfigDict(from_attributes=True)

class BillingResponse(BaseModel):
    deleted_count: int
    deleted_keys: List[DeleteKeys]
    user_lower: List[int]