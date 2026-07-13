import asyncio
import uuid

from yookassa import Payment


async def create_payment(user_id: int, amount: int) -> str:
    idempotency_key = str(uuid.uuid4())
    payment = await asyncio.to_thread(
        Payment.create,
        {
        "amount": {
            "value": str(amount),
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "https://t.me/ArgentVPNbot"
        },
        "capture": True,
        "description": "Пополнение баланса Argent Proxy",
        "metadata": {
            "user_id": user_id
        }
    },
    idempotency_key
    )

    return payment.confirmation.confirmation_url
