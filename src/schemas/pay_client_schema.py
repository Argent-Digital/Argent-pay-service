from pydantic import BaseModel

class SuccesPay(BaseModel):
    user_id: int
    amount: int

class BillingStart(BaseModel):
    start: bool