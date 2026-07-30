from api.bujju_ai.risk_calculator import (
    HiringRiskCalculator
)


def test_high_hiring_risk():

    engine = HiringRiskCalculator()

    result = engine.calculate(
        open_days=60,
        available_candidates=3,
        matching_candidates=2
    )

    assert result["risk_score"] >= 70
    assert result["risk_level"].value == "HIGH"
