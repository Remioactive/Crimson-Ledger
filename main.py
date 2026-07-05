from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.analytics import router as analytics_router
from app.routes.dashboard import router as dashboard_router
from app.routes.history import router as history_router
from app.routes.market import router as market_router
from app.routes.scanner import router as scanner_router

app = FastAPI(
    title="Crimson Ledger",
    version="0.10.0"
)

# Allow the React frontend to access the API during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "project": "Crimson Ledger",
        "version": "0.10.0",
        "status": "Running"
    }


# Routes
app.include_router(market_router)
app.include_router(scanner_router)
app.include_router(history_router)
app.include_router(analytics_router)
app.include_router(dashboard_router)