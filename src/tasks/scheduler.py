from apscheduler.schedulers.asyncio import AsyncIOScheduler

from src.tasks.billing import run_daily_billing

scheduler = AsyncIOScheduler()

async def setup_scheduler():
    scheduler.add_job(run_daily_billing, 'cron', hour=3, minute=0)

    scheduler.start()

async def stop_scheduler():
    scheduler.shutdown()
