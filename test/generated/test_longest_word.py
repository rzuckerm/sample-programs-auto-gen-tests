from glotter import project_test, project_fixture
import pytest


@project_fixture("longestword")
def longest_word(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test("longestword")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param('"May the force be with you"', "5", id="sample input: many words"),
        pytest.param(
            '"Floccinaucinihilipilification"', "29", id="sample input: single word"
        ),
        pytest.param('"Hi,\nMy name is Paul!"', "5", id="sample input: multiline"),
    ],
)
def test_longest_word_valid(in_params, expected, longest_word):
    actual = longest_word.run(params=in_params)
    actual = actual.strip()
    assert actual == expected


@project_test("longestword")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(None, "Usage: please provide a string", id="no input"),
        pytest.param('""', "Usage: please provide a string", id="empty input"),
    ],
)
def test_longest_word_invalid(in_params, expected, longest_word):
    actual = longest_word.run(params=in_params)
    actual = actual.strip()
    assert actual == expected
