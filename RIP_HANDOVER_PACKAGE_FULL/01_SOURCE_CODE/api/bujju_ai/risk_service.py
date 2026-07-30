from datetime import datetime

from .risk_calculator import HiringRiskCalculator


class BujjuRiskService:

    def __init__(self):
        self.calculator = HiringRiskCalculator()


    def analyse(self, request):

        result = self.calculator.calculate(
            request.open_days,
            request.available_candidates,
            request.matching_candidates
        )

        result.update({
            "position_id": request.position_id,
            "generated_at": datetime.utcnow()
        })

        return result
