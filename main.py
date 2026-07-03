from fastapi import FastAPI

from app.routes.market import router as market_router
from app.routes.scanner import router as scanner_router

app = FastAPI(
    title="Crimson Ledger",
    version="0.8.0"
)


@app.get("/")
def home():
    return {
        "project": "Crimson Ledger",
        "status": "Running"
    }


app.include_router(market_router)
app.include_router(scanner_router)