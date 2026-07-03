from fastapi import APIRouter, HTTPException

from app.services.market_service import MarketService

router = APIRouter(
    prefix="/market",
    tags=["Market"]
)

market_service = MarketService()


@router.get("")
def all_markets():
    return market_service.get_market_summary()


@router.get("/{item_name}")
def market(item_name: str):
    try:
        return market_service.get_market(item_name)

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

    except Exception as e:
        raise e