from pydantic import BaseModel, HttpUrl

class CreatePaymentUrl(BaseModel):
    amount: int

class ReturnUrl(BaseModel):
    url: HttpUrl