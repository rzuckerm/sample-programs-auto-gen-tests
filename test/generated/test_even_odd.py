import pytest
from glotter import project_test, project_fixture

PROJECT_NAME = "evenodd"


@project_fixture(PROJECT_NAME)
def even_odd(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test(PROJECT_NAME)
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param("2", "Even", id="sample input: even"),
        pytest.param("5", "Odd", id="sample input: odd"),
        pytest.param("-14", "Even", id="sample input: negative even"),
        pytest.param("-27", "Odd", id="sample input: negative odd"),
    ],
)
def test_even_odd_valid(in_params, expected, even_odd):
    actual = even_odd.run(params=in_params)
    actual = actual.strip()
    assert actual == expected


@project_test(PROJECT_NAME)
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(None, "Usage: please input a number", id="no input"),
        pytest.param('""', "Usage: please input a number", id="empty input"),
        pytest.param(
            '"a"', "Usage: please input a number", id="invalid input: not a number"
        ),
    ],
)
def test_even_odd_invalid(in_params, expected, even_odd):
    actual = even_odd.run(params=in_params)
    actual = actual.strip()
    assert actual == expected
