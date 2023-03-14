import pytest
from glotter import project_test, project_fixture

PROJECT_NAME = "depthfirstsearch"


@project_fixture(PROJECT_NAME)
def depth_first_search(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test(PROJECT_NAME)
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(
            '"0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0" "1, 3, 5, 2, 4" "1"',
            "true",
            id="sample input: first true",
        ),
        pytest.param(
            '"0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0" "1, 3, 5, 2, 4" "4"',
            "true",
            id="sample input: last true",
        ),
        pytest.param(
            '"0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0" "1, 3, 5, 2, 4" "5"',
            "true",
            id="sample input: middle true",
        ),
        pytest.param('"0" "1" "1"', "true", id="sample input: one true"),
        pytest.param('"0" "1" "6"', "false", id="sample input: one false"),
        pytest.param(
            '"0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0" "1, 3, 5, 2, 4" "7"',
            "false",
            id="sample input: many false",
        ),
    ],
)
def test_depth_first_search_valid(in_params, expected, depth_first_search):
    actual = depth_first_search.run(params=in_params)
    actual = actual.strip()
    assert actual == expected


@project_test(PROJECT_NAME)
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(
            None,
            'Usage: please provide a tree in an adjacency matrix form ("0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0") together with a list of vertex values ("1, 3, 5, 2, 4") and the integer to find ("4")',
            id="no input",
        ),
        pytest.param(
            '"" "1, 3, 5, 2, 4" "4"',
            'Usage: please provide a tree in an adjacency matrix form ("0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0") together with a list of vertex values ("1, 3, 5, 2, 4") and the integer to find ("4")',
            id="missing input: tree",
        ),
        pytest.param(
            '"0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0" "" "1"',
            'Usage: please provide a tree in an adjacency matrix form ("0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0") together with a list of vertex values ("1, 3, 5, 2, 4") and the integer to find ("4")',
            id="missing input: vertex values",
        ),
        pytest.param(
            '"0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0" "1, 3, 5, 2, 4" ""',
            'Usage: please provide a tree in an adjacency matrix form ("0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0") together with a list of vertex values ("1, 3, 5, 2, 4") and the integer to find ("4")',
            id="missing input: target",
        ),
    ],
)
def test_depth_first_search_invalid(in_params, expected, depth_first_search):
    actual = depth_first_search.run(params=in_params)
    actual = actual.strip()
    assert actual == expected
