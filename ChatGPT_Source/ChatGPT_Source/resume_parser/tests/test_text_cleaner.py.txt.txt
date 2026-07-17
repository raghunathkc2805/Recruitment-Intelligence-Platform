from resume_parser.utils.text_cleaner import clean


def test_clean_removes_extra_spaces():

    text = "Python     Developer"

    assert clean(text) == "Python Developer"


def test_clean_normalizes_newlines():

    text = "Python\n\n\n\nDeveloper"

    assert clean(text) == "Python\n\nDeveloper"


def test_clean_strips_whitespace():

    text = "   Python Developer   "

    assert clean(text) == "Python Developer"


def test_clean_empty():

    assert clean("") == ""


def test_clean_none():

    assert clean(None) == ""