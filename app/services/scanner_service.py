from datetime import datetime

from app.config.items import ITEMS
from app.services.market_service import MarketService


class ScannerService:

    def __init__(self):
        self.market_service = MarketService()

    def run_scan(self):

        started = datetime.now()

        scanned = 0
        failed_items = []

        for key in ITEMS:

            try:

                print(f"Scanning {key}...")

                # MarketService now handles saving snapshots
                self.market_service.get_market(key)

                scanned += 1

            except Exception as e:

                failed_items.append({
                    "item": key,
                    "error": str(e)
                })

        finished = datetime.now()

        duration = (finished - started).total_seconds()

        return {
            "status": "success" if not failed_items else "partial_success",
            "started_at": started.isoformat(),
            "finished_at": finished.isoformat(),
            "duration_seconds": round(duration, 2),
            "items_scanned": len(ITEMS),
            "snapshots_saved": scanned,
            "failed_items": failed_items
        }