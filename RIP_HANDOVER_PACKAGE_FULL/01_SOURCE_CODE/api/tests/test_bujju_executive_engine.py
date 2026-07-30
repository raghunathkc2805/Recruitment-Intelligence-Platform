from api.bujju_ai.executive_calculator import (
    ExecutiveIntelligenceCalculator
)


def test_executive_high_risk():

    engine = ExecutiveIntelligenceCalculator()

    result = engine.calculate(
        total_open_positions=20,
        critical_positions=8,
        ageing_positions=10,
        active_pipeline_candidates=5,
        offers_released=10,
        joined_candidates=4
    )


    assert result["hiring_status"] == "HIGH_RISK"
