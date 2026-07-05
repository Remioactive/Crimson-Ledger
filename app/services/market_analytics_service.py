from statistics import mean


class MarketAnalyticsService:

    def summarize(self, item_name: str, snapshots: list, market=None):

        if not snapshots:

            return {
                "item": item_name,
                "snapshots": 0,

                "current_price": None,
                "lowest_price": None,
                "highest_price": None,
                "average_price": None,
                "price_difference": None,
                "price_difference_percent": None,

                "current_supply": None,
                "lowest_supply": None,
                "highest_supply": None,
                "average_supply": None,
                "supply_difference": None,
                "supply_difference_percent": None,

                "listing_count": 0,

                "buy100_average": None,
                "buy500_average": None,
                "buy1000_average": None,

                "price_trend": "unknown",
                "supply_trend": "unknown",

                "market_health": "unknown",
                "volatility": 0
            }

        newest = snapshots[0]
        oldest = snapshots[-1]

        prices = [snapshot["lowest_price"] for snapshot in snapshots]
        supplies = [snapshot["total_quantity"] for snapshot in snapshots]

        current_price = newest["lowest_price"]
        current_supply = newest["total_quantity"]

        lowest_price = min(prices)
        highest_price = max(prices)
        average_price = round(mean(prices), 2)

        lowest_supply = min(supplies)
        highest_supply = max(supplies)
        average_supply = round(mean(supplies), 2)

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

        if current_price < oldest["lowest_price"]:
            price_trend = "down"
        elif current_price > oldest["lowest_price"]:
            price_trend = "up"
        else:
            price_trend = "flat"

        if current_supply > oldest["total_quantity"]:
            supply_trend = "up"
        elif current_supply < oldest["total_quantity"]:
            supply_trend = "down"
        else:
            supply_trend = "flat"

        price_range = highest_price - lowest_price

        volatility = round(
            (price_range / average_price) * 100,
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

        analytics = {
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

            "price_trend": price_trend,
            "supply_trend": supply_trend,

            "market_health": market_health,
            "volatility": volatility,

            "listing_count": newest["listing_count"]
        }

        if market:

            analytics["buy100_average"] = market["buy100"]["average_price"]
            analytics["buy500_average"] = market["buy500"]["average_price"]
            analytics["buy1000_average"] = market["buy1000"]["average_price"]

        else:

            analytics["buy100_average"] = None
            analytics["buy500_average"] = None
            analytics["buy1000_average"] = None

        return analytics