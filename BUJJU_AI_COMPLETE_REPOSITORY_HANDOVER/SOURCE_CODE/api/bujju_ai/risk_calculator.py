from .risk_models import RiskLevel


class HiringRiskCalculator:

    def calculate(
        self,
        open_days: int,
        available_candidates: int,
        matching_candidates: int
    ):

        score = 0
        reasons = []
        recommendations = []

        if open_days > 30:
            score += 30
            reasons.append(
                "Position ageing beyond normal hiring cycle"
            )

        if available_candidates < 10:
            score += 35
            reasons.append(
                "Limited talent availability"
            )

        if matching_candidates < 5:
            score += 25
            reasons.append(
                "Low candidate match availability"
            )

        if score >= 70:
            level = RiskLevel.HIGH
            recommendations.append(
                "Activate targeted sourcing immediately"
            )

        elif score >= 40:
            level = RiskLevel.MEDIUM
            recommendations.append(
                "Increase sourcing channels"
            )

        else:
            level = RiskLevel.LOW
            recommendations.append(
                "Continue current recruitment strategy"
            )

        return {
            "risk_score": score,
            "risk_level": level,
            "reasons": reasons,
            "recommendations": recommendations
        }
