import pytest
from glotter import project_test, project_fixture

PROJECT_NAME = "rot13"


@project_fixture(PROJECT_NAME)
def rot13(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test(PROJECT_NAME)
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(
            '"the quick brown fox jumped over the lazy dog"',
            "gur dhvpx oebja sbk whzcrq bire gur ynml qbt",
            id="sample input lower case",
        ),
        pytest.param(
            '"THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG"',
            "GUR DHVPX OEBJA SBK WHZCRQ BIRE GUR YNML QBT",
            id="sample input upper case",
        ),
        pytest.param(
            '"The quick brown fox jumped. Was it over the lazy dog?"',
            "Gur dhvpx oebja sbk whzcrq. Jnf vg bire gur ynml qbt?",
            id="sample input punctuation",
        ),
    ],
)
def test_rot13_valid(in_params, expected, rot13):
    actual = rot13.run(params=in_params)
    actual = actual.strip()
    assert actual == expected


@project_test(PROJECT_NAME)
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(None, "Usage: please provide a string to encrypt", id="no input"),
        pytest.param(
            '""', "Usage: please provide a string to encrypt", id="empty input"
        ),
    ],
)
def test_rot13_invalid(in_params, expected, rot13):
    actual = rot13.run(params=in_params)
    actual = actual.strip()
    assert actual == expected
