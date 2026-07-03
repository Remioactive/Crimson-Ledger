from fastapi import FastAPI, HTTPException

from app.config.items import ITEMS
from app.services.market_analyzer import MarketAnalyzer
from app.services.torn_api import TornAPI

app = FastAPI(
    title="Crimson Ledger",
    version="0.4.2"
)

api = TornAPI()
analyzer = MarketAnalyzer()


@app.get("/")
def home():
    return {
        "project": "Crimson Ledger",
        "status": "Running"
    }


@app.get("/market/{item_name}")
def market(item_name: str):

    if item_name not in ITEMS:
        raise HTTPException(
            status_code=404,
            detail=f"Unknown item '{item_name}'"
        )

    try:

        item = ITEMS[item_name]

        data = api.get_item_market(item["id"])

        return analyzer.analyze(data)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )