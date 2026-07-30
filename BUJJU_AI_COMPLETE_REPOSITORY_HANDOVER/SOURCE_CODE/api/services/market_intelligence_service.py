from __future__ import annotations

import json

from sqlalchemy.orm import Session

from database.models.market_intelligence import MarketIntelligence


class MarketIntelligenceService:


    @classmethod
    def create(
        cls,
        db: Session,
        domain: str,
        intelligence_type: str,
        title: str,
        information: dict,
        confidence_score: float = 0,
    ):

        record = MarketIntelligence(
            domain=domain,
            intelligence_type=intelligence_type,
            title=title,
            information=json.dumps(
                information
            ),
            confidence_score=confidence_score,
        )

        db.add(record)

        db.commit()

        db.refresh(record)

        return record


    @classmethod
    def search(
        cls,
        db: Session,
        domain: str,
    ):

        return (
            db.query(MarketIntelligence)
            .filter(
                MarketIntelligence.domain ==
                domain
            )
            .order_by(
                MarketIntelligence.created_at.desc()
            )
            .all()
        )