import datetime
from src.loader import _bot_client, _core_client, _vpn_client

async def run_daily_billing():
    print(f"💰 [{datetime.now().strftime('%H:%M')}] Начинаю ежедневное списание...")

    try:
        billing_data = await _core_client.daily_billing(start=True)

        if billing_data:
            await _vpn_client.remove_keys(keys=billing_data.deleted_keys)

            await _bot_client.post_user_warning_list(users=billing_data.user_lower)

            print("Billing success")
    except Exception as e:
        print(f"Billig error: {e}")