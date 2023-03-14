import pytest
from glotter import project_test, project_fixture

PROJECT_NAME = "primenumber"


@project_fixture(PROJECT_NAME)
def prime_number(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test(PROJECT_NAME)
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param("'0'", "composite", id="sample input 0"),
        pytest.param("'1'", "composite", id="sample input 1"),
        pytest.param("'2'", "prime", id="sample input 2"),
        pytest.param("'4'", "composite", id="sample input small composite"),
        pytest.param("'7'", "prime", id="sample input small prime"),
        pytest.param("'4011'", "composite", id="sample input large composite"),
        pytest.param('"3727"', "prime", id="sample input large prime"),
    ],
)
def test_prime_valid(in_params, expected, prime_number):
    actual = prime_number.run(params=in_params)
    actual = actual.strip().lower()
    assert actual == expected


@project_test(PROJECT_NAME)
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(None, "Usage: please input a non-negative integer", id="no input"),
        pytest.param(
            '""', "Usage: please input a non-negative integer", id="empty input"
        ),
        pytest.param(
            '"a"',
            "Usage: please input a non-negative integer",
            id="invalid input: not a number",
        ),
        pytest.param(
            '"6.7"',
            "Usage: please input a non-negative integer",
            id="invalid input: not an integer",
        ),
        pytest.param(
            '"-7"',
            "Usage: please input a non-negative integer",
            id="invalid input: negative",
        ),
    ],
)
def test_prime_invalid(in_params, expected, prime_number):
    actual = prime_number.run(params=in_params)
    actual = actual.strip()
    assert actual == expected
