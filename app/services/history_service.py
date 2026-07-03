from app.config.items import ITEMS
from app.database.database import Database


class HistoryService:

    def __init__(self):
        self.database = Database()

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