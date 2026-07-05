from app.config.items import ITEMS
from app.database.database import Database
from app.services.market_analytics_service import MarketAnalyticsService
from app.services.market_signal_service import MarketSignalService
from app.services.buy_score_service import BuyScoreService


class HistoryService:

    def __init__(self):
        self.database = Database()
        self.analytics = MarketAnalyticsService()
        self.signals = MarketSignalService()
        self.buy_score = BuyScoreService()

    def get_latest(self, item_name: str):

        item_name = item_name.replace("-", "_")

        if item_name not in ITEMS:
            raise ValueError(f"Unknown item '{item_name}'")

        snapshot = self.database.get_latest_snapshot(item_name)

        if snapshot is None:
            raise ValueError(f"No history found for '{item_name}'")

        return snapshot

    def get_history(self, item_name: str, limit: int = 100):

        item_name = item_name.replace("-", "_")

        if item_name not in ITEMS:
            raise ValueError(f"Unknown item '{item_name}'")

        history = self.database.get_snapshot_history(item_name, limit)

        return {
            "item": ITEMS[item_name]["name"],
            "key": item_name,
            "count": len(history),
            "history": history
        }

    def get_analytics(
        self,
        item_name: str,
        hours: int = 24
    ):

        item_name = item_name.replace("-", "_")

        if item_name not in ITEMS:
            raise ValueError(f"Unknown item '{item_name}'")

        snapshots = self.database.get_snapshot_history_by_hours(
            item_name,
            hours
        )

        if not snapshots:
            raise ValueError(f"No history found for '{item_name}'")

        analytics = self.analytics.summarize(
            ITEMS[item_name]["name"],
            snapshots
        )

        signals = self.signals.generate(
            analytics
        )

        analytics["signals"] = signals

        analytics.update(
            self.buy_score.calculate(analytics)
        )

        return analytics