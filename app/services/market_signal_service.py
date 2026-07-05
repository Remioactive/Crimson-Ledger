class MarketSignalService:

    def generate(self, analytics: dict):

        signals = []

        # Price Signal

        price_percent = analytics["price_difference_percent"]

        if price_percent <= -5:
            signals.append({
                "type": "price",
                "impact": "very_positive",
                "weight": 35,
                "message": "Current price is well below the historical average."
            })

        elif price_percent <= -2:
            signals.append({
                "type": "price",
                "impact": "positive",
                "weight": 20,
                "message": "Current price is below the historical average."
            })

        elif price_percent >= 5:
            signals.append({
                "type": "price",
                "impact": "very_negative",
                "weight": -35,
                "message": "Current price is well above the historical average."
            })

        elif price_percent >= 2:
            signals.append({
                "type": "price",
                "impact": "negative",
                "weight": -20,
                "message": "Current price is above the historical average."
            })

        else:
            signals.append({
                "type": "price",
                "impact": "neutral",
                "weight": 0,
                "message": "Current price is close to the historical average."
            })

        # Supply Signal

        supply_percent = analytics["supply_difference_percent"]

        if supply_percent >= 10:
            signals.append({
                "type": "supply",
                "impact": "very_positive",
                "weight": 20,
                "message": "Supply is much higher than normal."
            })

        elif supply_percent >= 3:
            signals.append({
                "type": "supply",
                "impact": "positive",
                "weight": 10,
                "message": "Supply is above average."
            })

        elif supply_percent <= -10:
            signals.append({
                "type": "supply",
                "impact": "very_negative",
                "weight": -20,
                "message": "Supply is much lower than normal."
            })

        elif supply_percent <= -3:
            signals.append({
                "type": "supply",
                "impact": "negative",
                "weight": -10,
                "message": "Supply is below average."
            })

        else:
            signals.append({
                "type": "supply",
                "impact": "neutral",
                "weight": 0,
                "message": "Supply is close to normal."
            })

        # Volatility Signal

        volatility = analytics["volatility"]

        if volatility < 2:
            signals.append({
                "type": "volatility",
                "impact": "positive",
                "weight": 15,
                "message": "Market volatility is very low."
            })

        elif volatility < 5:
            signals.append({
                "type": "volatility",
                "impact": "positive",
                "weight": 10,
                "message": "Market volatility is low."
            })

        elif volatility < 10:
            signals.append({
                "type": "volatility",
                "impact": "neutral",
                "weight": 0,
                "message": "Market volatility is moderate."
            })

        else:
            signals.append({
                "type": "volatility",
                "impact": "negative",
                "weight": -15,
                "message": "Market volatility is high."
            })

        return signals