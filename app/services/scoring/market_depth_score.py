class MarketDepthScore:

    MAX_SCORE = 20

    def calculate(self, analytics):

        buy100 = analytics["buy100_average"]
        buy500 = analytics["buy500_average"]
        buy1000 = analytics["buy1000_average"]

        spread = (
            (buy1000 - buy100)
            / buy100
        ) * 100

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