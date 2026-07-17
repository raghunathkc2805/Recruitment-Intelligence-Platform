"""
Ranking Engine Exceptions
"""


class RankingEngineError(Exception):
    """
    Base Ranking Engine Exception.
    """


class InvalidRankingInput(RankingEngineError):
    """
    Invalid ranking input.
    """


class RankingExecutionError(RankingEngineError):
    """
    Ranking execution failed.
    """