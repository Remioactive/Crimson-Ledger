from typing import Dict, List


class MarketCleaner:
    """
    Removes invalid or unrealistic listings before analysis.
    """

    def clean(self, market_data: Dict, max_multiplier: int) -> Dict:

        item = market_data["itemmarket"]["item"]
        listings: List[Dict] = market_data["itemmarket"]["listings"]

        average_price = item["average_price"]
        max_price = average_price * max_multiplier

        cleaned = []

        for listing in listings:

            price = listing["price"]
            amount = listing["amount"]

            if amount <= 0:
                continue

            if price <= 0:
                continue

            if price > max_price:
                continue

            cleaned.append(listing)

        market_data["itemmarket"]["listings"] = cleaned

        return market_data