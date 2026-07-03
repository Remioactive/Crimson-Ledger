from app.config.items import ITEMS
from app.services.market_analyzer import MarketAnalyzer
from app.services.market_cleaner import MarketCleaner
from app.services.torn_api import TornAPI


class MarketService:

    def __init__(self):
        self.api = TornAPI()
        self.cleaner = MarketCleaner()
        self.analyzer = MarketAnalyzer()

    def get_market(self, item_name: str):

        item_name = item_name.replace("-", "_")

        if item_name not in ITEMS:
            raise ValueError(f"Unknown item '{item_name}'")

        item = ITEMS[item_name]

        data = self.api.get_item_market(item["id"])

        data = self.cleaner.clean(
            data,
            item["max_price_multiplier"]
        )

        analysis = self.analyzer.analyze(data)

        analysis["key"] = item_name

        return analysis

    def get_market_summary(self):

        results = []

        for key, item in ITEMS.items():

            try:

                analysis = self.get_market(key)

                results.append({
                    "key": key,
                    "name": analysis["item"],
                    "lowest_price": analysis["lowest_price"],
                    "buy500_average": analysis["buy500"]["average_price"],
                    "listing_count": analysis["listing_count"]
                })

            except Exception as e:

                results.append({
                    "key": key,
                    "name": item["name"],
                    "error": str(e)
                })

        results.sort(
            key=lambda x: x.get("lowest_price", float("inf"))
        )

        return results