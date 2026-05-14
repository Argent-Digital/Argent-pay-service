import datetime
from src.loader import _bot_client, _core_client

async def run_daily_billing():
    print(f"💰 [{datetime.now().strftime('%H:%M')}] Начинаю ежедневное списание...")

    try:
        billing_data = await _core_client.daily_billing(start=True)

        if billing_data:
            await _bot_client.sending_notif_user(users_del=billing_data.deleted_keys, users_warning=billing_data.user_lower)

            print("Billing success")
    except Exception as e:
        print(f"Billig error: {e}")