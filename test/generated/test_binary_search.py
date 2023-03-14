import pytest
from glotter import project_test, project_fixture

PROJECT_NAME = "binarysearch"


@project_fixture(PROJECT_NAME)
def binary_search(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test(PROJECT_NAME)
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param('"1, 3, 5, 7" "1"', "true", id="sample input first true"),
        pytest.param('"1, 3, 5, 7" "7"', "true", id="sample input last true"),
        pytest.param('"1, 3, 5, 7" "5"', "true", id="sample input middle true"),
        pytest.param('"5" "5"', "true", id="sample input one true"),
        pytest.param('"5" "7"', "false", id="sample input one false"),
        pytest.param('"1, 3, 5, 6" "7"', "false", id="sample input many false"),
        pytest.param(
            '"1, 2, 3, 4, 5, 6, 7" "3"', "true", id="sample input middle true"
        ),
    ],
)
def test_binary_search_valid(in_params, expected, binary_search):
    actual = binary_search.run(params=in_params)
    actual = actual.strip().lower()
    assert actual == expected


@project_test(PROJECT_NAME)
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(
            None,
            'Usage: please provide a list of sorted integers ("1, 4, 5, 11, 12") and the integer to find ("11")',
            id="no input",
        ),
        pytest.param(
            '"1, 2, 3, 4"',
            'Usage: please provide a list of sorted integers ("1, 4, 5, 11, 12") and the integer to find ("11")',
            id="missing input: target",
        ),
        pytest.param(
            '"" "5"',
            'Usage: please provide a list of sorted integers ("1, 4, 5, 11, 12") and the integer to find ("11")',
            id="missing input: list",
        ),
        pytest.param(
            '"3, 5, 1, 2" "3"',
            'Usage: please provide a list of sorted integers ("1, 4, 5, 11, 12") and the integer to find ("11")',
            id="out of order input",
        ),
    ],
)
def test_binary_search_invalid(in_params, expected, binary_search):
    actual = binary_search.run(params=in_params)
    actual = actual.strip()
    assert actual == expected
