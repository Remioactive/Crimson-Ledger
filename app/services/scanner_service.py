from datetime import datetime

from app.config.items import ITEMS
from app.database.database import Database
from app.services.market_service import MarketService


class ScannerService:

    def __init__(self):
        self.market_service = MarketService()
        self.database = Database()
        self.database.create_tables()

    def run_scan(self):

        started = datetime.now()

        snapshots_saved = 0
        failed_items = []

        for key in ITEMS:

            try:

                print(f"Scanning {key}...")

                analysis = self.market_service.get_market(key)

                self.database.save_snapshot(
                    item_key=key,
                    lowest_price=analysis["lowest_price"],
                    buy500_average=analysis["buy500"]["average_price"],
                    listing_count=analysis["listing_count"],
                    total_quantity=analysis["total_quantity"]
                )

                snapshots_saved += 1

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
            "snapshots_saved": snapshots_saved,
            "failed_items": failed_items
        }