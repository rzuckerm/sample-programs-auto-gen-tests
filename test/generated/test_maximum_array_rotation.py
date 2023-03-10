from glotter import project_test, project_fixture
import pytest


@project_fixture("maximumarrayrotation")
def maximum_array_rotation(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test("maximumarrayrotation")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param('"3, 1, 2, 8"', "29", id="sample input no rotation"),
        pytest.param('"1, 2, 8, 3"', "29", id="sample input one rotation"),
        pytest.param('"8, 3, 1, 2"', "29", id="sample input many rotations"),
    ],
)
def test_maximimum_array_rotation_valid(in_params, expected, maximum_array_rotation):
    actual = maximum_array_rotation.run(params=in_params)
    actual = actual.strip()
    assert actual == expected


@project_test("maximumarrayrotation")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(
            None,
            'Usage: please provide a list of integers (e.g. "8, 3, 1, 2")',
            id="no input",
        ),
        pytest.param(
            '""',
            'Usage: please provide a list of integers (e.g. "8, 3, 1, 2")',
            id="empty input",
        ),
    ],
)
def test_maximimum_array_rotation_invalid(in_params, expected, maximum_array_rotation):
    actual = maximum_array_rotation.run(params=in_params)
    actual = actual.strip()
    assert actual == expected
