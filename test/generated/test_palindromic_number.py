from glotter import project_test, project_fixture
import pytest


@project_fixture("palindromicnumber")
def palindromic_number(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test("palindromicnumber")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param("7", "true", id="sample input: one digit"),
        pytest.param("2442", "true", id="sample input: even digits"),
        pytest.param("232", "true", id="sample input: odd digits"),
        pytest.param("5215", "false", id="sample input: even digits not palindrome"),
        pytest.param("521", "false", id="sample input: odd digits not palindrome"),
    ],
)
def test_palindromic_number_valid(in_params, expected, palindromic_number):
    actual = palindromic_number.run(params=in_params)
    actual = actual.strip()
    assert actual == expected


@project_test("palindromicnumber")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(None, "Usage: please input a non-negative integer", id="no input"),
        pytest.param(
            "", "Usage: please input a non-negative integer", id="empty input"
        ),
        pytest.param(
            "a",
            "Usage: please input a non-negative integer",
            id="invalid input: not a number",
        ),
        pytest.param(
            "-7",
            "Usage: please input a non-negative integer",
            id="invalid input: negative integer",
        ),
        pytest.param(
            "5.41",
            "Usage: please input a non-negative integer",
            id="invalid input: float",
        ),
    ],
)
def test_palindromic_number_invalid(in_params, expected, palindromic_number):
    actual = palindromic_number.run(params=in_params)
    actual = actual.strip()
    assert actual == expected
