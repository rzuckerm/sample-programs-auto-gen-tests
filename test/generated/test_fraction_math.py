import pytest
from glotter import project_test, project_fixture

PROJECT_NAME = "fractionmath"


@project_fixture(PROJECT_NAME)
def fraction_math(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test(PROJECT_NAME)
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param('"2/3" "+" "4/5"', "22/15", id="sample input: addition"),
        pytest.param('"2/3" "*" "4/5"', "8/15", id="sample input: multiplication"),
        pytest.param('"2/3" "-" "4/5"', "-2/15", id="sample input: subtraction"),
        pytest.param('"2/3" "/" "4/5"', "5/6", id="sample input: division"),
        pytest.param('"2/3" "==" "4/5"', "0", id="sample input: equals"),
        pytest.param('"2/3" ">" "4/5"', "0", id="sample input: greater than"),
        pytest.param('"2/3" "<" "4/5"', "1", id="sample input: less than"),
        pytest.param('"2/3" ">=" "4/5"', "0", id="sample input: greater than equals"),
        pytest.param('"2/3" "<=" "4/5"', "1", id="sample input: less than equals"),
        pytest.param('"2/3" "!=" "4/5"', "1", id="sample input: not equals"),
    ],
)
def test_fractions_valid(in_params, expected, fraction_math):
    actual = fraction_math.run(params=in_params)
    actual = actual.strip()
    assert actual == expected


@project_test(PROJECT_NAME)
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(
            None, "Usage: ./fraction-math operand1 operator operand2", id="no input"
        ),
        pytest.param(
            '""', "Usage: ./fraction-math operand1 operator operand2", id="empty input"
        ),
    ],
)
def test_fractions_invalid(in_params, expected, fraction_math):
    actual = fraction_math.run(params=in_params)
    actual = actual.strip()
    assert actual == expected
