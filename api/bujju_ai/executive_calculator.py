class ExecutiveIntelligenceCalculator:


    def calculate(
        self,
        total_open_positions,
        critical_positions,
        ageing_positions,
        active_pipeline_candidates,
        offers_released,
        joined_candidates
    ):

        score = 100
        insights = []
        recommendations = []


        if ageing_positions > 5:
            score -= 20
            insights.append(
                "Multiple positions are ageing"
            )


        if critical_positions > 3:
            score -= 25
            insights.append(
                "Critical hiring dependency detected"
            )


        if active_pipeline_candidates < total_open_positions:
            score -= 20
            insights.append(
                "Pipeline strength is below requirement"
            )


        if offers_released > 0:

            joining_ratio = (
                joined_candidates /
                offers_released
            ) * 100

            if joining_ratio < 70:
                score -= 15
                insights.append(
                    "Offer conversion risk detected"
                )


        if score >= 80:
            status = "HEALTHY"

        elif score >= 60:
            status = "MODERATE_RISK"
            recommendations.append(
                "Increase recruitment focus"
            )

        else:
            status = "HIGH_RISK"
            recommendations.append(
                "Leadership intervention required"
            )


        return {
            "hiring_health_score": max(score,0),
            "hiring_status": status,
            "insights": insights,
            "recommendations": recommendations
        }
