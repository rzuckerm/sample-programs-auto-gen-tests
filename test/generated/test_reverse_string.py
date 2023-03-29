import pytest
from glotter import project_test, project_fixture

PROJECT_NAME = "reversestring"


@project_fixture(PROJECT_NAME)
def reverse_string(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test(PROJECT_NAME)
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(None, "", id="No input"),
        pytest.param('""', "", id="Empty input"),
        pytest.param('"Hello, World"', "dlroW ,olleH", id="Ascii String"),
    ],
)
def test_reverse_string(in_params, expected, reverse_string):
    actual = reverse_string.run(params=in_params)
    actual = actual.strip()
    assert actual == expected
