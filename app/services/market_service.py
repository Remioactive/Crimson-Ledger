from app.config.items import ITEMS
from app.database.database import Database
from app.services.market_analyzer import MarketAnalyzer
from app.services.market_cleaner import MarketCleaner
from app.services.torn_api import TornAPI


class MarketService:

    def __init__(self):
        self.api = TornAPI()
        self.cleaner = MarketCleaner()
        self.analyzer = MarketAnalyzer()

        self.database = Database()
        self.database.create_tables()

    def get_market(self, item_name: str):

        item_name = item_name.replace("-", "_")

        if item_name not in ITEMS:
            raise ValueError(f"Unknown item '{item_name}'")

        item = ITEMS[item_name]

        listings = self.api.get_item_market(item["id"])

        listings = self.cleaner.clean(
            listings,
            item["max_price_multiplier"]
        )

        analysis = self.analyzer.analyze(listings)

        analysis["key"] = item_name

        self.database.save_snapshot(
            item_key=item_name,
            lowest_price=analysis["lowest_price"],
            listing_count=analysis["listing_count"],
            total_quantity=analysis["total_quantity"],
            buy100_average=analysis["buy100_average"],
            buy500_average=analysis["buy500_average"],
            buy1000_average=analysis["buy1000_average"]
        )

        return analysis

    def get_market_summary(self):

        results = []

        for key in ITEMS:

            try:

                analysis = self.get_market(key)

                results.append({
                    "key": key,
                    "name": analysis["item"],
                    "lowest_price": analysis["lowest_price"],
                    "buy500_average": analysis["buy500_average"],
                    "listing_count": analysis["listing_count"]
                })

            except Exception as e:

                results.append({
                    "key": key,
                    "name": ITEMS[key]["name"],
                    "error": str(e)
                })

        results.sort(
            key=lambda x: x.get(
                "lowest_price",
                float("inf")
            )
        )

        return results