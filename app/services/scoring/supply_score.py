class SupplyScore:

    MAX_SCORE = 10

    def calculate(self, analytics):

        percent = analytics["supply_difference_percent"]

        if percent >= 20:
            score = 10

        elif percent >= 10:
            score = 8

        elif percent >= 5:
            score = 6

        elif percent >= 0:
            score = 4

        else:
            score = 2

        if percent > 0:
            direction = "above"
        elif percent < 0:
            direction = "below"
        else:
            direction = "equal to"

        if direction == "equal to":
            reason = (
                "Supply is equal to the historical average."
            )
        else:
            reason = (
                f"Supply is "
                f"{abs(percent):.2f}% {direction} "
                f"the historical average."
            )

        return {
            "category": "Supply",
            "score": score,
            "max_score": self.MAX_SCORE,
            "reason": reason
        }