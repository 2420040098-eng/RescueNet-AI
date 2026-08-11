class PredictionAgent:

    def predict_risk(self, rainfall, temperature, population):

        population_factor = population / 10000

        score = (
            rainfall * 0.5
            + temperature * 0.2
            + population_factor * 0.3
        )

        score = min(score, 100)

        if score >= 70:
            risk_level = "HIGH"
        elif score >= 40:
            risk_level = "MEDIUM"
        else:
            risk_level = "LOW"

        return {
            "risk_score": round(score, 2),
            "risk_level": risk_level
        }
