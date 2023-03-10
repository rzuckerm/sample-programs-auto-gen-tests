from glotter import project_test, project_fixture
import pytest


@project_fixture("longestpalindromicsubstring")
def longest_palindromic_substring(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test("longestpalindromicsubstring")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param("racecar", "racecar", id="sample input: one palindrome"),
        pytest.param("kayak mom", "kayak", id="sample input: two palindrome"),
        pytest.param(
            '"step on no pets"',
            "step on no pets",
            id="sample input: complex palindrome",
        ),
    ],
)
def test_lps_valid(in_params, expected, longest_palindromic_substring):
    actual = longest_palindromic_substring.run(params=in_params)
    actual = actual.strip().lower()
    assert actual == expected


@project_test("longestpalindromicsubstring")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(
            None,
            "Usage: please provide a string that contains at least one palindrome",
            id="no input",
        ),
        pytest.param(
            '""',
            "Usage: please provide a string that contains at least one palindrome",
            id="empty input",
        ),
        pytest.param(
            "polip",
            "Usage: please provide a string that contains at least one palindrome",
            id="invalid input: no palindromes",
        ),
    ],
)
def test_lps_invalid(in_params, expected, longest_palindromic_substring):
    actual = longest_palindromic_substring.run(params=in_params)
    actual = actual.strip()
    assert actual == expected
