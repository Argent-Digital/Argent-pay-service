import datetime

async def run_daily_billing():
    print(f"💰 [{datetime.now().strftime('%H:%M')}] Начинаю ежедневное списание...")

    try:
        