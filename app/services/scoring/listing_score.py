class ListingScore:

    MAX_SCORE = 10

    def calculate(self, analytics):

        listings = analytics["listing_count"]

        if listings >= 100:
            score = 10

        elif listings >= 75:
            score = 8

        elif listings >= 50:
            score = 6

        elif listings >= 25:
            score = 4

        else:
            score = 2

        return {
            "category": "Listing Health",
            "score": score,
            "max_score": self.MAX_SCORE,
            "reason": (
                f"There are currently "
                f"{listings} listings."
            )
        }