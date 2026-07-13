from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from src.api.bot_api import router as bot_router
from src.api.yookassa_api import router as yookassa_router
from src.loader import _bot_client, _core_client
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
app.include_router(bot_router)

@app.get("/")
async def health_check():
    return {"status": "working", "service": "argent-pay"}

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
