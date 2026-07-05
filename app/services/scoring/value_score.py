class ValueScore:

    MAX_SCORE = 30

    def calculate(self, analytics):

        percent = analytics["price_difference_percent"]

        if percent <= -10:
            score = 30

        elif percent <= -7:
            score = 27

        elif percent <= -5:
            score = 24

        elif percent <= -3:
            score = 20

        elif percent <= -1:
            score = 15

        elif percent < 2:
            score = 10

        elif percent < 5:
            score = 5

        else:
            score = 0

        return {
            "category": "Value",
            "score": score,
            "max_score": self.MAX_SCORE,
            "reason": (
                f"Current price is "
                f"{percent:.2f}% compared to "
                f"the historical average."
            )
        }