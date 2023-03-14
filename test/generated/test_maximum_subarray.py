import pytest
from glotter import project_test, project_fixture

PROJECT_NAME = "maximumsubarray"


@project_fixture(PROJECT_NAME)
def maximum_subarray(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test(PROJECT_NAME)
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param('"1"', "1", id="sample input: one element"),
        pytest.param('"1, 2, 3"', "6", id="sample input: many positive values"),
        pytest.param('"-1, -2, -3"', "-1", id="sample input: many negative values"),
        pytest.param(
            '"-2, -1, 3, 4, 5"',
            "12",
            id="sample input: many negative followed by positive values",
        ),
        pytest.param(
            '"-1, -4, 2, 3, -3, -4, 9"',
            "9",
            id="sample input: many alternating positive and negative values",
        ),
    ],
)
def test_maximum_subarray_valid(in_params, expected, maximum_subarray):
    actual = maximum_subarray.run(params=in_params)
    actual = actual.strip()
    assert actual == expected


@project_test(PROJECT_NAME)
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(
            None,
            'Usage: Please provide a list of integers in the format: "1, 2, 3, 4, 5"',
            id="no input",
        ),
        pytest.param(
            '""',
            'Usage: Please provide a list of integers in the format: "1, 2, 3, 4, 5"',
            id="empty input",
        ),
    ],
)
def test_maximum_subarray_invalid(in_params, expected, maximum_subarray):
    actual = maximum_subarray.run(params=in_params)
    actual = actual.strip()
    assert actual == expected
