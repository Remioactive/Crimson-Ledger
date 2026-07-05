class StabilityScore:

    MAX_SCORE = 5

    def calculate(self, analytics):

        volatility = analytics["volatility"]

        if volatility <= 2:
            score = 5

        elif volatility <= 4:
            score = 4

        elif volatility <= 6:
            score = 3

        elif volatility <= 8:
            score = 2

        else:
            score = 1

        return {
            "category": "Stability",
            "score": score,
            "max_score": self.MAX_SCORE,
            "reason": (
                f"Volatility is "
                f"{volatility:.2f}%."
            )
        }