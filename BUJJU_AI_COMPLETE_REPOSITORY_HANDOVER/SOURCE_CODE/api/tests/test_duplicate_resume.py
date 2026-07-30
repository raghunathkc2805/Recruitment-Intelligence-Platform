"""
Duplicate Resume Tests
"""

from pathlib import Path

from api.utils.hash_util import HashUtil


def test_same_file_same_hash(tmp_path):

    file = tmp_path / "resume.pdf"

    file.write_bytes(
        b"Sample Resume"
    )

    hash1 = HashUtil.calculate(file)

    hash2 = HashUtil.calculate(file)

    assert hash1 == hash2


def test_different_file_different_hash(tmp_path):

    file1 = tmp_path / "resume1.pdf"

    file2 = tmp_path / "resume2.pdf"

    file1.write_bytes(
        b"Resume One"
    )

    file2.write_bytes(
        b"Resume Two"
    )

    assert (

        HashUtil.calculate(file1)

        !=

        HashUtil.calculate(file2)

    )


def test_hash_length(tmp_path):

    file = tmp_path / "resume.pdf"

    file.write_bytes(
        b"Recruitment Intelligence"
    )

    digest = HashUtil.calculate(file)

    assert len(digest) == 64
