from fastapi import FastAPI, HTTPException

from app.config.items import ITEMS
from app.services.market_analyzer import MarketAnalyzer
from app.services.torn_api import TornAPI

app = FastAPI(
    title="Crimson Ledger",
    version="0.4.1"
)

api = TornAPI()
analyzer = MarketAnalyzer()


@app.get("/")
def home():
    return {
        "project": "Crimson Ledger",
        "status": "Running"
    }


@app.get("/market/o-plus")
def o_plus_market():
    try:
        data = api.get_item_market(
            ITEMS["o_plus"]["id"]
        )

        return analyzer.analyze(data)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )