from statistics import mean


class MarketAnalyticsService:

    def summarize(self, item_name: str, snapshots: list):

        if not snapshots:

            return {
                "item": item_name,
                "snapshots": 0,
                "lowest_price": None,
                "highest_price": None,
                "average_price": None,
                "lowest_supply": None,
                "highest_supply": None,
                "average_supply": None,
                "price_trend": "unknown",
                "supply_trend": "unknown",
                "market_health": "unknown",
                "volatility": 0
            }

        prices = [
            snapshot["lowest_price"]
            for snapshot in snapshots
        ]

        supplies = [
            snapshot["total_quantity"]
            for snapshot in snapshots
        ]

        lowest_price = min(prices)
        highest_price = max(prices)
        average_price = round(mean(prices), 2)

        lowest_supply = min(supplies)
        highest_supply = max(supplies)
        average_supply = round(mean(supplies), 2)

        oldest = snapshots[-1]
        newest = snapshots[0]

        if newest["lowest_price"] < oldest["lowest_price"]:
            price_trend = "down"
        elif newest["lowest_price"] > oldest["lowest_price"]:
            price_trend = "up"
        else:
            price_trend = "flat"

        if newest["total_quantity"] > oldest["total_quantity"]:
            supply_trend = "up"
        elif newest["total_quantity"] < oldest["total_quantity"]:
            supply_trend = "down"
        else:
            supply_trend = "flat"

        price_range = highest_price - lowest_price

        if average_price == 0:
            volatility = 0
        else:
            volatility = round(
                (price_range / average_price) * 100,
                2
            )

        if volatility < 2:
            market_health = "excellent"
        elif volatility < 5:
            market_health = "good"
        elif volatility < 10:
            market_health = "fair"
        else:
            market_health = "volatile"

        return {
            "item": item_name,
            "snapshots": len(snapshots),
            "lowest_price": lowest_price,
            "highest_price": highest_price,
            "average_price": average_price,
            "lowest_supply": lowest_supply,
            "highest_supply": highest_supply,
            "average_supply": average_supply,
            "price_trend": price_trend,
            "supply_trend": supply_trend,
            "market_health": market_health,
            "volatility": volatility
        }