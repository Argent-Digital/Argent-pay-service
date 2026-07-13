from fastapi import APIRouter, Depends, HTTPException

from src.auth.dependencies import get_current_user_id
from src.schemas.bot_schemas import CreatePaymentUrl, ReturnUrl
from src.tasks.url_payment_generator import create_payment

router = APIRouter(prefix="/pay-url", tags=["Payment url generator"])

@router.post("/create_url", response_model=ReturnUrl)
async def create_payment_url(url_data: CreatePaymentUrl, user_id: int = Depends(get_current_user_id)):
    try:
        url = await create_payment(amount=url_data.amount, user_id=user_id)
        return ReturnUrl(url=url)
    except Exception as e:
        print(f"error create pay url: {e}")
        raise HTTPException(status_code=500, detail="don't create payment url") from e
