from __future__ import annotations

from sqlalchemy.orm import joinedload
from sqlalchemy.orm import selectinload


class QueryOptimizer:

    @staticmethod
    def eager(query, *relationships):
        for relation in relationships:
            query = query.options(joinedload(relation))
        return query

    @staticmethod
    def batch(query, *relationships):
        for relation in relationships:
            query = query.options(selectinload(relation))
        return query

    @staticmethod
    def limit(query, limit: int = 100):
        return query.limit(limit)

    @staticmethod
    def offset(query, offset: int = 0):
        return query.offset(offset)


query_optimizer = QueryOptimizer()
