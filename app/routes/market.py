from fastapi import APIRouter, HTTPException

from app.config.items import ITEMS
from app.services.market_analyzer import MarketAnalyzer
from app.services.market_cleaner import MarketCleaner
from app.services.torn_api import TornAPI

router = APIRouter(prefix="/market", tags=["Market"])

api = TornAPI()
cleaner = MarketCleaner()
analyzer = MarketAnalyzer()


@router.get("")
def all_markets():

    results = []

    for key, item in ITEMS.items():

        try:

            data = api.get_item_market(item["id"])

            data = cleaner.clean(
                data,
                item["max_price_multiplier"]
            )

            analysis = analyzer.analyze(data)

            results.append({
                "key": key,
                "name": analysis["item"],
                "lowest_price": analysis["lowest_price"],
                "buy500_average": analysis["buy500"]["average_price"],
                "listing_count": analysis["listing_count"]
            })

        except Exception as e:

            results.append({
                "key": key,
                "name": item["name"],
                "error": str(e)
            })

    results.sort(
        key=lambda x: x.get("lowest_price", float("inf"))
    )

    return results


@router.get("/{item_name}")
def market(item_name: str):

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

        analysis = analyzer.analyze(data)

        analysis["key"] = item_name

        return analysis

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )