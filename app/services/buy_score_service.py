class BuyScoreService:

    def calculate(self, signals):

        score = 50

        for signal in signals:
            score += signal["weight"]

        score = max(0, min(100, score))

        if score >= 90:
            rating = "Excellent"
            recommendation = "Strong Buy"

        elif score >= 75:
            rating = "Very Good"
            recommendation = "Buy"

        elif score >= 60:
            rating = "Good"
            recommendation = "Consider Buying"

        elif score >= 40:
            rating = "Fair"
            recommendation = "Watch"

        elif score >= 20:
            rating = "Poor"
            recommendation = "Wait"

        else:
            rating = "Avoid"
            recommendation = "Do Not Buy"

        return {
            "buy_score": score,
            "rating": rating,
            "recommendation": recommendation
        }