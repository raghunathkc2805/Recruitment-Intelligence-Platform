from datetime import datetime

from .executive_calculator import (
    ExecutiveIntelligenceCalculator
)


class BujjuExecutiveService:


    def __init__(self):

        self.calculator = (
            ExecutiveIntelligenceCalculator()
        )


    def generate(self, request):

        result = self.calculator.calculate(
            request.total_open_positions,
            request.critical_positions,
            request.ageing_positions,
            request.active_pipeline_candidates,
            request.offers_released,
            request.joined_candidates
        )


        result["generated_at"] = datetime.utcnow()

        return result
