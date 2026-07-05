class MarketSignalService:

    def generate(self, analytics):

        signals = []

        price = analytics["price_difference_percent"]

        if price <= -5:
            signals.append({
                "type": "price",
                "impact": "very_positive",
                "message": "Current price is well below the historical average."
            })

        elif price <= -2:
            signals.append({
                "type": "price",
                "impact": "positive",
                "message": "Current price is below the historical average."
            })

        elif price >= 5:
            signals.append({
                "type": "price",
                "impact": "very_negative",
                "message": "Current price is well above the historical average."
            })

        elif price >= 2:
            signals.append({
                "type": "price",
                "impact": "negative",
                "message": "Current price is above the historical average."
            })

        else:
            signals.append({
                "type": "price",
                "impact": "neutral",
                "message": "Current price is close to average."
            })

        supply = analytics["supply_difference_percent"]

        if supply >= 10:
            signals.append({
                "type": "supply",
                "impact": "very_positive",
                "message": "Supply is much higher than normal."
            })

        elif supply >= 3:
            signals.append({
                "type": "supply",
                "impact": "positive",
                "message": "Supply is above average."
            })

        elif supply <= -10:
            signals.append({
                "type": "supply",
                "impact": "very_negative",
                "message": "Supply is much lower than normal."
            })

        elif supply <= -3:
            signals.append({
                "type": "supply",
                "impact": "negative",
                "message": "Supply is below average."
            })

        else:
            signals.append({
                "type": "supply",
                "impact": "neutral",
                "message": "Supply is close to normal."
            })

        volatility = analytics["volatility"]

        if volatility < 2:
            impact = "positive"
            message = "Market volatility is very low."

        elif volatility < 5:
            impact = "positive"
            message = "Market volatility is low."

        elif volatility < 10:
            impact = "neutral"
            message = "Market volatility is moderate."

        else:
            impact = "negative"
            message = "Market volatility is high."

        signals.append({
            "type": "volatility",
            "impact": impact,
            "message": message
        })

        return signals