from fastapi import FastAPI

from app.routes.analytics import router as analytics_router
from app.routes.history import router as history_router
from app.routes.market import router as market_router
from app.routes.scanner import router as scanner_router

app = FastAPI(
    title="Crimson Ledger",
    version="0.10.0"
)


@app.get("/")
def home():
    return {
        "project": "Crimson Ledger",
        "version": "0.10.0",
        "status": "Running"
    }


app.include_router(market_router)
app.include_router(scanner_router)
app.include_router(history_router)
app.include_router(analytics_router)