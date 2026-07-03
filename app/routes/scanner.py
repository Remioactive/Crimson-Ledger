from fastapi import APIRouter

from app.services.scanner_service import ScannerService

router = APIRouter(
    prefix="/scan",
    tags=["Scanner"]
)

scanner_service = ScannerService()


@router.get("")
def run_scan():
    return scanner_service.run_scan()