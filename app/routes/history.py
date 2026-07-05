from fastapi import APIRouter, HTTPException

from app.services.history_service import HistoryService

router = APIRouter(
    prefix="/history",
    tags=["History"]
)

history_service = HistoryService()


@router.get("/{item_name}/latest")
def latest_snapshot(item_name: str):

    try:
        return history_service.get_latest(item_name)

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


@router.get("/{item_name}")
def snapshot_history(
    item_name: str,
    limit: int = 100
):

    try:
        return history_service.get_history(item_name, limit)

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