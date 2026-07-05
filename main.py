from fastapi import FastAPI

from app.routes.analytics import router as analytics_router
from app.routes.dashboard import router as dashboard_router
from app.routes.history import router as history_router
from app.routes.market import router as market_router
from app.routes.scanner import router as scanner_router

app = FastAPI(
    title="Crimson Ledger API",
    description=(
        "Market intelligence and analytics for Torn blood bags.\n\n"
        "Provides live market data, historical analytics, "
        "buy scoring, and dashboard endpoints."
    ),
    version="1.0.0",
    contact={
        "name": "Remioactive",
        "url": "https://github.com/Remioactive/Crimson-Ledger"
    }
)


@app.get("/")
def home():
    return {
        "project": "Crimson Ledger",
        "version": "1.0.0",
        "status": "Running"
    }


app.include_router(scanner_router)
app.include_router(market_router)
app.include_router(history_router)
app.include_router(analytics_router)
app.include_router(dashboard_router)