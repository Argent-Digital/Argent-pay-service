from pydantic import BaseModel


class CreatePaymentUrl(BaseModel):
    amount: int

class ReturnUrl(BaseModel):
    url: str
