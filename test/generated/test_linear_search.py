from glotter import project_test, project_fixture
import pytest


@project_fixture("linearsearch")
def linear_search(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test("linearsearch")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param('"1, 3, 5, 7" "1"', "true", id="sample input first true"),
        pytest.param('"1, 3, 5, 7" "7"', "true", id="sample input last true"),
        pytest.param('"1, 3, 5, 7" "5"', "true", id="sample input middle true"),
        pytest.param('"5" "5"', "true", id="sample input one true"),
        pytest.param('"5" "7"', "false", id="sample input one false"),
        pytest.param('"1, 3, 5, 6" "7"', "false", id="sample input many false"),
    ],
)
def test_linear_search_valid(in_params, expected, linear_search):
    actual = linear_search.run(params=in_params)
    actual = actual.strip().lower()
    assert actual == expected


@project_test("linearsearch")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(
            None,
            'Usage: please provide a list of integers ("1, 4, 5, 11, 12") and the integer to find ("11")',
            id="no input",
        ),
        pytest.param(
            '"1, 2, 3, 4"',
            'Usage: please provide a list of integers ("1, 4, 5, 11, 12") and the integer to find ("11")',
            id="missing input: target",
        ),
        pytest.param(
            '"" "5"',
            'Usage: please provide a list of integers ("1, 4, 5, 11, 12") and the integer to find ("11")',
            id="missing input: list",
        ),
    ],
)
def test_linear_search_invalid(in_params, expected, linear_search):
    actual = linear_search.run(params=in_params)
    actual = actual.strip()
    assert actual == expected
