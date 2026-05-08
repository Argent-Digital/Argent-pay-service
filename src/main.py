import uvicorn 
from fastapi import FastAPI
from contextlib import asynccontextmanager
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from src.api.yookassa_api import router as yookassa_router
from src.loader import _core_client, _bot_client

scheduler = AsyncIOScheduler()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting argent pay...")
    
    scheduler.add_job()#run_daily_billing, "cron". hour=3, minute=0)
    scheduler.start()
    print("Billing Sheduler started")
    yield

    print("Stopping argent pay")
    await _core_client.close()
    await _bot_client.close()
    print("success closing client")

    scheduler.shutdown()
    print("Billing scheduler stopped")

app = FastAPI(
    title="Argent Pay",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(yookassa_router)

@app.get("/")
async def health_check():
    return {"status": "working", "service": "argent-pay"}

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)