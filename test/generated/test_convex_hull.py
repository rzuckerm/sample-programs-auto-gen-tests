import pytest
from glotter import project_test, project_fixture

PROJECT_NAME = "convexhull"


@project_fixture(PROJECT_NAME)
def convex_hull(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test(PROJECT_NAME)
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(
            '"100, 180, 240" "220, 120, 20"',
            ["(100, 220)", "(240, 20)", "(180, 120)"],
            id="sample input: triangle",
        ),
        pytest.param(
            '"100, 140, 320, 480, 280" "240, 60, 40, 200, 300"',
            ["(100, 240)", "(140, 60)", "(320, 40)", "(480, 200)", "(280, 300)"],
            id="sample input: pentagon",
        ),
        pytest.param(
            '"260, 280, 300, 320, 600, 360, 20, 240" "160, 100, 180, 140, 160, 320, 200, 0"',
            ["(20, 200)", "(240, 0)", "(600, 160)", "(360, 320)"],
            id="sample input: cluster",
        ),
    ],
)
def test_convex_hull_valid(in_params, expected, convex_hull):
    actual = convex_hull.run(params=in_params)
    actual_list = sorted(set(actual.strip().splitlines()))
    expected_list = sorted(set(expected))
    assert len(actual_list) == len(expected_list), "Length not equal"
    for index in range(len(expected_list)):
        assert (
            actual_list[index] == expected_list[index]
        ), f"Item {index + 1} is not equal"


@project_test(PROJECT_NAME)
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(
            None,
            'Usage: please provide at least 3 x and y coordinates as separate lists (e.g. "100, 440, 210")',
            id="no input",
        ),
        pytest.param(
            '"100, 180, 240"',
            'Usage: please provide at least 3 x and y coordinates as separate lists (e.g. "100, 440, 210")',
            id="missing y",
        ),
        pytest.param(
            '"100, 180" "240, 300"',
            'Usage: please provide at least 3 x and y coordinates as separate lists (e.g. "100, 440, 210")',
            id="invalid shape",
        ),
        pytest.param(
            '"100, 180, 240" "240, 60, 40, 200, 300"',
            'Usage: please provide at least 3 x and y coordinates as separate lists (e.g. "100, 440, 210")',
            id="different cardinality",
        ),
        pytest.param(
            '"100, 1A0, 240" "220, 120, 20"',
            'Usage: please provide at least 3 x and y coordinates as separate lists (e.g. "100, 440, 210")',
            id="invalid integers",
        ),
    ],
)
def test_convex_hull_invalid(in_params, expected, convex_hull):
    actual = convex_hull.run(params=in_params)
    actual = actual.strip()
    assert actual == expected
