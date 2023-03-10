from glotter import project_test, project_fixture
import pytest


@project_fixture("quicksort")
def quick_sort(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test("quicksort")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param('"4, 5, 3, 1, 2"', "1, 2, 3, 4, 5", id="sample input"),
        pytest.param(
            '"4, 5, 3, 1, 4, 2"', "1, 2, 3, 4, 4, 5", id="sample input: with duplicate"
        ),
        pytest.param(
            '"1, 2, 3, 4, 5"', "1, 2, 3, 4, 5", id="sample input: already sorted"
        ),
        pytest.param(
            '"9, 8, 7, 6, 5, 4, 3, 2, 1"',
            "1, 2, 3, 4, 5, 6, 7, 8, 9",
            id="sample input: reverse sorted",
        ),
    ],
)
def test_quick_sort_valid(in_params, expected, quick_sort):
    actual = quick_sort.run(params=in_params)
    actual = actual.replace("[", "").replace("]", "").strip()
    assert actual == expected


@project_test("quicksort")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(
            None,
            'Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"',
            id="no input",
        ),
        pytest.param(
            "",
            'Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"',
            id="empty input",
        ),
        pytest.param(
            "1",
            'Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"',
            id="invalid input: not a list",
        ),
        pytest.param(
            '"4 5 3"',
            'Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"',
            id="invalid input: wrong format",
        ),
    ],
)
def test_quick_sort_invalid(in_params, expected, quick_sort):
    actual = quick_sort.run(params=in_params)
    actual = actual.strip()
    assert actual == expected
