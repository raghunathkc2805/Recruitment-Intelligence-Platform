"""
Enterprise Search Service
"""

from __future__ import annotations

from sqlalchemy.orm import Session

from api.services.boolean_search_service import BooleanSearchService

from database.repositories.candidate_search_repository import CandidateSearchRepository
from database.repositories.candidate_skill_repository import CandidateSkillRepository
from database.repositories.search_repository import SearchRepository


class SearchService:

    PAGE_SIZE = 25

    @classmethod
    def run(
        cls,
        db: Session,
        payload: dict,
    ):

        query_text = payload.get(
            "query",
            "",
        )

        parsed = BooleanSearchService.parse(
            query_text
        )

        repository = CandidateSearchRepository(
            db
        )

        candidates = repository.search(

            skills=(
                parsed["and"]
                +
                parsed["phrases"]
            ),

            designation=payload.get(
                "designation"
            ),

            location=payload.get(
                "location"
            ),

            minimum_experience=payload.get(
                "experience"
            ),

        )

        skill_repository = CandidateSkillRepository(
            db
        )

        requested_skills = {

            skill.lower()

            for skill in (

                parsed["and"]
                +
                parsed["phrases"]

            )

        }

        results = []

        for candidate in candidates:

            candidate_skills = {

                item.skill_name.lower()

                for item in skill_repository.list_by_candidate(
                    candidate.id
                )

            }

            matched_skills = (

                candidate_skills
                &
                requested_skills

            )

            confidence = 100.0

            if requested_skills:

                confidence = round(

                    (
                        len(matched_skills)
                        /
                        len(requested_skills)
                    )
                    *
                    100,

                    2,

                )

            results.append(

                {

                    "candidate_id": candidate.id,

                    "candidate_code": candidate.candidate_code,

                    "candidate_name": candidate.full_name,

                    "designation": candidate.current_designation,

                    "experience": candidate.experience_years,

                    "location": candidate.location,

                    "confidence": confidence,

                    "matched_skills": sorted(
                        matched_skills
                    ),

                }

            )

        results.sort(

            key=lambda item: (

                item["confidence"],

                item["experience"],

            ),

            reverse=True,

        )

        total_results = len(
            results
        )

        page = max(

            int(

                payload.get(
                    "page",
                    1,
                )

            ),

            1,

        )

        start = (

            page - 1

        ) * cls.PAGE_SIZE

        end = start + cls.PAGE_SIZE

        SearchRepository(db).save_search(

            user_id=payload.get(
                "user_id",
                "system",
            ),

            query=query_text,

            search_type="ADVANCED",

        )

        return {

            "page": page,

            "page_size": cls.PAGE_SIZE,

            "total_results": total_results,

            "total_pages": (

                (
                    total_results
                    +
                    cls.PAGE_SIZE
                    -
                    1
                )
                //
                cls.PAGE_SIZE

            ),

            "results": results[start:end],

        }
