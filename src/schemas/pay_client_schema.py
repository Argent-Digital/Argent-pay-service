from pydantic import BaseModel, ConfigDict

class SuccesPay(BaseModel):
    user_id: int
    amount: int

class BillingStart(BaseModel):
    start: bool

class UserWithLowBalance(BaseModel):
    user_id: int

    model_config=ConfigDict(from_attributes=True)