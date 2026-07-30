from resume_parser.utils import (
    knowledge_base,
    regex_patterns,
    text_cleaner,
)


def test_utils_modules_loaded():

    assert knowledge_base is not None

    assert regex_patterns is not None

    assert text_cleaner is not None


def test_text_cleaner_has_clean():

    assert hasattr(text_cleaner, "clean")


def test_regex_patterns_loaded():

    assert hasattr(regex_patterns, "EMAIL")

    assert hasattr(regex_patterns, "PHONE")

    assert hasattr(regex_patterns, "NAME")


def test_knowledge_base_loaded():

    assert hasattr(knowledge_base, "SKILLS")

    assert hasattr(knowledge_base, "EDUCATION")

    assert hasattr(knowledge_base, "CERTIFICATIONS")