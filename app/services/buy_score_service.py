from app.services.scoring.value_score import ValueScore
from app.services.scoring.bulk_score import BulkScore
from app.services.scoring.market_depth_score import MarketDepthScore
from app.services.scoring.supply_score import SupplyScore
from app.services.scoring.listing_score import ListingScore
from app.services.scoring.stability_score import StabilityScore


class BuyScoreService:

    def __init__(self):

        self.value = ValueScore()
        self.bulk = BulkScore()
        self.depth = MarketDepthScore()
        self.supply = SupplyScore()
        self.listing = ListingScore()
        self.stability = StabilityScore()

    def calculate(self, analytics):

        value = self.value.calculate(analytics)
        bulk = self.bulk.calculate(analytics)
        depth = self.depth.calculate(analytics)
        supply = self.supply.calculate(analytics)
        listing = self.listing.calculate(analytics)
        stability = self.stability.calculate(analytics)

        breakdown = {
            "value": value,
            "bulk": bulk,
            "depth": depth,
            "supply": supply,
            "listing": listing,
            "stability": stability
        }

        score = (
            value["score"] +
            bulk["score"] +
            depth["score"] +
            supply["score"] +
            listing["score"] +
            stability["score"]
        )

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
            "recommendation": recommendation,
            "breakdown": breakdown
        }