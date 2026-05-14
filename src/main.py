import uvicorn 
from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.api.yookassa_api import router as yookassa_router
from src.loader import _core_client, _bot_client, _vpn_client
from src.tasks.scheduler import setup_scheduler, stop_scheduler

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting argent pay...")
    
    await setup_scheduler()
    print("Stated scheduler")
    yield

    await stop_scheduler()
    print("Stoped scheduler")

    print("Stopping argent pay")
    await _core_client.close()
    await _bot_client.close()
    print("success closing client")

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