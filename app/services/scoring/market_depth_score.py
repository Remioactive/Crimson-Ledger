class MarketDepthScore:

    MAX_SCORE = 20

    def calculate(self, analytics):

        buy100 = analytics.get("buy100_average")
        buy500 = analytics.get("buy500_average")
        buy1000 = analytics.get("buy1000_average")

        # Not enough data to calculate market depth
        if (
            buy100 is None
            or buy500 is None
            or buy1000 is None
        ):
            return {
                "category": "Market Depth",
                "score": 0,
                "max_score": self.MAX_SCORE,
                "reason": "Not enough market depth data available."
            }

        # Prevent division by zero
        if buy100 <= 0:
            return {
                "category": "Market Depth",
                "score": 0,
                "max_score": self.MAX_SCORE,
                "reason": "Invalid market depth data."
            }

        spread = ((buy1000 - buy100) / buy100) * 100

        if spread <= 2:
            score = 20

        elif spread <= 4:
            score = 16

        elif spread <= 6:
            score = 12

        elif spread <= 8:
            score = 8

        else:
            score = 0

        return {
            "category": "Market Depth",
            "score": score,
            "max_score": self.MAX_SCORE,
            "reason": (
                f"Buying from 100 to 1000 bags "
                f"moves the market by "
                f"{spread:.2f}%."
            )
        }