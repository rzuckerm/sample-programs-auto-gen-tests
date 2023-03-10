from glotter import project_test, project_fixture
import pytest


@project_fixture("reversestring")
def reverse_string(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test("reversestring")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param('"Hello, World"', "dlroW ,olleH", id="None"),
    ],
)
def test_reverse_string(in_params, expected, reverse_string):
    actual = reverse_string.run(params=in_params)
    actual = actual.strip()
    assert actual == expected
