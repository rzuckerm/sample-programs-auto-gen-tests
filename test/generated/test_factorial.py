from glotter import project_test, project_fixture
import pytest


@project_fixture("factorial")
def factorial(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test("factorial")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param('"0"', "1", id="sample input: zero"),
        pytest.param('"1"', "1", id="sample input: one"),
        pytest.param('"4"', "24", id="sample input: four"),
        pytest.param('"8"', "40320", id="sample input: eight"),
        pytest.param('"10"', "3628800", id="sample input: ten"),
    ],
)
def test_factorial_valid(in_params, expected, factorial):
    actual = factorial.run(params=in_params)
    actual = actual.strip()
    assert actual == expected


@project_test("factorial")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(None, "Usage: please input a non-negative integer", id="no input"),
        pytest.param(
            '""', "Usage: please input a non-negative integer", id="empty input"
        ),
        pytest.param(
            '"asdf"',
            "Usage: please input a non-negative integer",
            id="invalid input: not a number",
        ),
        pytest.param(
            '"-1"',
            "Usage: please input a non-negative integer",
            id="invalid input: negative",
        ),
    ],
)
def test_factorial_invalid(in_params, expected, factorial):
    actual = factorial.run(params=in_params)
    actual = actual.strip()
    assert actual == expected
