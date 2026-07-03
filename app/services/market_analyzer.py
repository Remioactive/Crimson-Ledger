from typing import Dict, List


class MarketAnalyzer:

    def cost_to_buy(self, listings: List[Dict], quantity_needed: int):
        """
        Calculates the total cost and average price required to buy
        a specific quantity of items from the cheapest listings.
        """

        remaining = quantity_needed
        total_cost = 0

        for listing in listings:
            available = listing["amount"]
            price = listing["price"]

            buy = min(remaining, available)

            total_cost += buy * price
            remaining -= buy

            if remaining == 0:
                break

        if remaining > 0:
            return None

        return {
            "quantity": quantity_needed,
            "total_cost": total_cost,
            "average_price": round(total_cost / quantity_needed, 2)
        }

    def analyze(self, market_data: Dict) -> Dict:

        listings: List[Dict] = market_data["itemmarket"]["listings"]
        item = market_data["itemmarket"]["item"]

        # Sort listings from cheapest to most expensive
        listings = sorted(listings, key=lambda x: x["price"])

        prices = [listing["price"] for listing in listings]
        quantities = [listing["amount"] for listing in listings]

        total_quantity = sum(quantities)

        weighted_value = sum(
            listing["price"] * listing["amount"]
            for listing in listings
        )

        weighted_average = (
            weighted_value / total_quantity
            if total_quantity > 0
            else 0
        )

        top5 = prices[:5]
        top10 = prices[:10]

        buy100 = self.cost_to_buy(listings, 100)
        buy500 = self.cost_to_buy(listings, 500)
        buy1000 = self.cost_to_buy(listings, 1000)

        return {
            "item": item["name"],
            "item_id": item["id"],

            "market_average": item["average_price"],

            "lowest_price": prices[0],
            "highest_price": prices[-1],

            "listing_count": len(listings),
            "total_quantity": total_quantity,

            "weighted_average": round(weighted_average, 2),
            "top5_average": round(sum(top5) / len(top5), 2),
            "top10_average": round(sum(top10) / len(top10), 2),

            "buy100": buy100,
            "buy500": buy500,
            "buy1000": buy1000
        }