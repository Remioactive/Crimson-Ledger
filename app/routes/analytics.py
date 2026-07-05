from fastapi import APIRouter, HTTPException

from app.services.history_service import HistoryService

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

history_service = HistoryService()


@router.get("/{item_name}")
def market_analytics(
    item_name: str,
    hours: int = 24
):

    try:

        return history_service.get_analytics(
            item_name,
            hours
        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )