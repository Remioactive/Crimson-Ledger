from statistics import mean


class MarketAnalyzer:

    BUY_AMOUNTS = (100, 500, 1000)

    def analyze(self, listings):

        if not listings:
            raise ValueError("No market listings found.")

        prices = [listing["price"] for listing in listings]
        quantities = [listing["quantity"] for listing in listings]

        total_quantity = sum(quantities)

        analysis = {
            "item": listings[0]["item_name"],
            "lowest_price": min(prices),
            "highest_price": max(prices),
            "listing_count": len(listings),
            "total_quantity": total_quantity,
            "weighted_average": round(
                sum(
                    listing["price"] * listing["quantity"]
                    for listing in listings
                ) / total_quantity,
                2
            ),
            "top5_average": round(mean(prices[:5]), 2),
            "top10_average": round(mean(prices[:10]), 2),
        }

        for amount in self.BUY_AMOUNTS:
            analysis[f"buy{amount}_average"] = self.calculate_buy_average(
                listings,
                amount
            )

        return analysis

    def calculate_buy_average(
        self,
        listings,
        amount
    ):

        remaining = amount
        total_cost = 0

        for listing in listings:

            if remaining <= 0:
                break

            purchased = min(
                remaining,
                listing["quantity"]
            )

            total_cost += purchased * listing["price"]

            remaining -= purchased

        purchased_total = amount - remaining

        if purchased_total == 0:
            return None

        return round(
            total_cost / purchased_total,
            2
        )