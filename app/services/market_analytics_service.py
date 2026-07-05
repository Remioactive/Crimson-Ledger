from statistics import mean


class MarketAnalyticsService:

    def summarize(self, item_name: str, snapshots: list):

        if not snapshots:
            return {
                "item": item_name,
                "snapshots": 0
            }

        newest = snapshots[0]
        oldest = snapshots[-1]

        prices = [s["lowest_price"] for s in snapshots]
        supplies = [s["total_quantity"] for s in snapshots]

        current_price = newest["lowest_price"]
        current_supply = newest["total_quantity"]

        average_price = round(mean(prices), 2)
        average_supply = round(mean(supplies), 2)

        lowest_price = min(prices)
        highest_price = max(prices)

        lowest_supply = min(supplies)
        highest_supply = max(supplies)

        price_difference = round(
            current_price - average_price,
            2
        )

        price_difference_percent = round(
            (price_difference / average_price) * 100,
            2
        ) if average_price else 0

        supply_difference = round(
            current_supply - average_supply,
            2
        )

        supply_difference_percent = round(
            (supply_difference / average_supply) * 100,
            2
        ) if average_supply else 0

        if current_price > oldest["lowest_price"]:
            price_trend = "up"
        elif current_price < oldest["lowest_price"]:
            price_trend = "down"
        else:
            price_trend = "flat"

        if current_supply > oldest["total_quantity"]:
            supply_trend = "up"
        elif current_supply < oldest["total_quantity"]:
            supply_trend = "down"
        else:
            supply_trend = "flat"

        volatility = round(
            ((highest_price - lowest_price) / average_price) * 100,
            2
        ) if average_price else 0

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

            "current_price": current_price,
            "lowest_price": lowest_price,
            "highest_price": highest_price,
            "average_price": average_price,

            "price_difference": price_difference,
            "price_difference_percent": price_difference_percent,

            "current_supply": current_supply,
            "lowest_supply": lowest_supply,
            "highest_supply": highest_supply,
            "average_supply": average_supply,

            "supply_difference": supply_difference,
            "supply_difference_percent": supply_difference_percent,

            "listing_count": newest["listing_count"],

            "buy100_average": newest["buy100_average"],
            "buy500_average": newest["buy500_average"],
            "buy1000_average": newest["buy1000_average"],

            "price_trend": price_trend,
            "supply_trend": supply_trend,

            "market_health": market_health,
            "volatility": volatility
        }