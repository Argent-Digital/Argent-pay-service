from pydantic import BaseModel, ConfigDict
from typing import List

class SuccesPay(BaseModel):
    amount: int

class BillingStart(BaseModel):
    start: bool

class IdsByDelUser(BaseModel):
    user_id: int

class UserWithLowBalance(BaseModel):
    user_id: int

    model_config=ConfigDict(from_attributes=True)

class BillingResponse(BaseModel):
    deleted_keys: List[int]
    user_lower: List[int]