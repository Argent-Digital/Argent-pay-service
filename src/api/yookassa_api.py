from fastapi import APIRouter, Depends, Request
from yookassa.domain.notification import WebhookNotificationFactory
from src.client.bot_client import ArgenBotClient
from src.client.core_client import ArgentCoreClient
from src.loader import get_bot_client, get_core_client


router = APIRouter(tags=["Yookassa Webhook"])

@router.post("/yookassa_webhook")
async def yookassa_webhook(request: Request,
                           core_client: ArgentCoreClient = Depends(get_core_client),
                           bot_client: ArgenBotClient = Depends(get_bot_client)):
    
    event_json = await request.json()

    try:
        notification = WebhookNotificationFactory().create(event_json)
        payment = notification.object

        if notification.event == "payment.succeeded":
            amount = int(float(payment.amount.value))
            user_id = payment.metadata.get('user_id')

            if user_id:
                core_res = await core_client.update_balance(
                    user_id=int(user_id),
                    amount=amount
                )

                if core_res:
                    await bot_client.send_notification(
                        user_id=int(user_id),
                        amount=amount
                    )
                    print(f"Users {user_id} balance updated")

                else:
                    print("Don't search user id in metadata (naverna)")

        return {"status": "success"}
    
    except Exception as e:
        print(f"Error in webhook: {e}")
        return {"status": "error", "message": str(e)}