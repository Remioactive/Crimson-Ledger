from fastapi import FastAPI

from app.routes.market import router as market_router

app = FastAPI(
    title="Crimson Ledger",
    version="0.6.0"
)


@app.get("/")
def home():
    return {
        "project": "Crimson Ledger",
        "status": "Running"
    }


app.include_router(market_router)