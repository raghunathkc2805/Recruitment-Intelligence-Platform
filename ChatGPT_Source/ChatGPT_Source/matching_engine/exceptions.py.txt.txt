"""
Matching Engine Exceptions
"""


class MatchingEngineError(Exception):
    """
    Base exception.
    """


class InvalidCandidateError(MatchingEngineError):
    """
    Invalid candidate profile.
    """


class InvalidJobError(MatchingEngineError):
    """
    Invalid job profile.
    """


class MatcherExecutionError(MatchingEngineError):
    """
    Matcher execution failed.
    """