from fastapi import APIRouter, Depends
from yookassa import Configuration, Payment
from src.config import settings

router = APIRouter(tags=["Yookassa Webhook"])

Configuration.configure(account_id=settings.SHOP_ID, secret_key=settings.SECRET_KEY)

@router.post("/yookassa_webhook")