import pytest
from glotter import project_test, project_fixture

PROJECT_NAME = "minimumspanningtree"


@project_fixture(PROJECT_NAME)
def minimum_spanning_tree(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test(PROJECT_NAME)
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(
            '"0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0"',
            "16",
            id="sample input: routine",
        ),
    ],
)
def test_minimum_spanning_tree_valid(in_params, expected, minimum_spanning_tree):
    actual = minimum_spanning_tree.run(params=in_params)
    actual = actual.strip()
    assert actual == expected


@project_test(PROJECT_NAME)
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(
            None,
            "Usage: please provide a comma-separated list of integers",
            id="no input",
        ),
        pytest.param(
            '""',
            "Usage: please provide a comma-separated list of integers",
            id="empty input",
        ),
        pytest.param(
            '"1, 0, 3, 0, 5, 1"',
            "Usage: please provide a comma-separated list of integers",
            id="non-square input",
        ),
    ],
)
def test_minimum_spanning_tree_invalid(in_params, expected, minimum_spanning_tree):
    actual = minimum_spanning_tree.run(params=in_params)
    actual = actual.strip()
    assert actual == expected
