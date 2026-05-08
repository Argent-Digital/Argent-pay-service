from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from uuid import UUID

class DeleteKeys(BaseModel):
    user_id: int
    server_key_if: Optional[str]
    protocol: str
    vless_uuid: Optional[UUID]

    model_config=ConfigDict(from_attributes=True)

class BillingResponse(BaseModel):
    status: str = "success"
    deleted_count: int
    deleted_keys: List[DeleteKeys]