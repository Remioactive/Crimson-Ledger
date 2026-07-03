from fastapi import FastAPI, HTTPException

from app.config.items import ITEMS
from app.services.market_analyzer import MarketAnalyzer
from app.services.market_cleaner import MarketCleaner
from app.services.torn_api import TornAPI

app = FastAPI(
    title="Crimson Ledger",
    version="0.4.3"
)

api = TornAPI()
cleaner = MarketCleaner()
analyzer = MarketAnalyzer()


@app.get("/")
def home():
    return {
        "project": "Crimson Ledger",
        "status": "Running"
    }


@app.get("/market/{item_name}")
def market(item_name: str):

    # Allow both o-plus and o_plus
    item_name = item_name.replace("-", "_")

    if item_name not in ITEMS:
        raise HTTPException(
            status_code=404,
            detail=f"Unknown item '{item_name}'"
        )

    try:

        item = ITEMS[item_name]

        data = api.get_item_market(item["id"])

        data = cleaner.clean(
            data,
            item["max_price_multiplier"]
        )

        return analyzer.analyze(data)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )