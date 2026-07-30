from __future__ import annotations

import json

from sqlalchemy.orm import Session

from database.models.talent_marketplace import TalentMarketplace


class TalentMarketplaceService:


    @classmethod
    def add_candidate(
        cls,
        db: Session,
        candidate_id: str,
        candidate_type: str,
        skills: list,
        previous_outcome: str,
    ):

        record = TalentMarketplace(
            candidate_id=candidate_id,
            candidate_type=candidate_type,
            skill_profile=json.dumps(
                skills
            ),
            previous_outcome=previous_outcome,
        )


        db.add(record)

        db.commit()

        db.refresh(record)

        return record



    @classmethod
    def search(
        cls,
        db: Session,
        required_skills: list,
    ):

        records = (
            db.query(
                TalentMarketplace
            )
            .all()
        )


        results = []


        required = {
            x.lower()
            for x in required_skills
        }


        for record in records:

            skills = {
                x.lower()
                for x in json.loads(
                    record.skill_profile
                )
            }


            matched = (
                required
                &
                skills
            )


            score = 0


            if required:

                score = round(
                    (
                        len(matched)
                        /
                        len(required)
                    )
                    *
                    100,
                    2,
                )


            if score:

                results.append(
                    {
                        "candidate_id":
                            record.candidate_id,

                        "candidate_type":
                            record.candidate_type,

                        "match_score":
                            score,

                        "matched_skills":
                            list(matched),
                    }
                )


        return sorted(
            results,
            key=lambda x:x["match_score"],
            reverse=True,
        )