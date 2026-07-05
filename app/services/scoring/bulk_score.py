class BulkScore:

    MAX_SCORE = 25

    def calculate(self, analytics):

        current = analytics["current_price"]
        bulk = analytics["buy500_average"]

        slippage = (
            (bulk - current)
            / current
        ) * 100

        if slippage <= 1:
            score = 25

        elif slippage <= 2:
            score = 20

        elif slippage <= 3:
            score = 15

        elif slippage <= 5:
            score = 10

        else:
            score = 0

        return {
            "category": "Bulk",
            "score": score,
            "max_score": self.MAX_SCORE,
            "reason": (
                f"Buying 500 increases the "
                f"average price by "
                f"{slippage:.2f}%."
            )
        }