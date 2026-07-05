from fastapi import APIRouter, HTTPException

from app.config.items import ITEMS
from app.services.history_service import HistoryService
from app.services.market_service import MarketService

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

history_service = HistoryService()
market_service = MarketService()


@router.get("")
def dashboard():

    try:

        market = market_service.get_market_summary()

        analytics = []

        latest_scan = None

        for key in ITEMS:

            try:

                data = history_service.get_analytics(key)

                analytics.append({
                    "key": key,
                    "item": data["item"],
                    "buy_score": data["buy_score"],
                    "rating": data["rating"],
                    "recommendation": data["recommendation"],
                    "current_price": data["current_price"],
                    "price_difference_percent": data["price_difference_percent"],
                    "signals": data["signals"]
                })

                latest = history_service.get_latest(key)

                if latest:

                    timestamp = latest["timestamp"]

                    if latest_scan is None or timestamp > latest_scan:
                        latest_scan = timestamp

            except Exception:
                continue

        analytics.sort(
            key=lambda x: x["buy_score"],
            reverse=True
        )

        return {
            "last_scan": latest_scan,
            "items": len(market),
            "market": market,
            "top_buys": analytics[:3]
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )