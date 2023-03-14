import pytest
from glotter import project_test, project_fixture

PROJECT_NAME = "capitalize"


@project_fixture(PROJECT_NAME)
def capitalize(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test(PROJECT_NAME)
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param('"hello"', "Hello", id="sample input: lowercase string"),
        pytest.param('"Hello"', "Hello", id="sample input: uppercase string"),
        pytest.param('"hello world"', "Hello world", id="sample input: long string"),
        pytest.param('"heLLo World"', "HeLLo World", id="sample input: mixed casing"),
        pytest.param('"12345"', "12345", id="sample input: symbols"),
    ],
)
def test_capitalize_valid(in_params, expected, capitalize):
    actual = capitalize.run(params=in_params)
    actual = actual.strip()
    assert actual == expected


@project_test(PROJECT_NAME)
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(None, "Usage: please provide a string", id="no input"),
        pytest.param("", "Usage: please provide a string", id="empty input"),
    ],
)
def test_capitalize_invalid(in_params, expected, capitalize):
    actual = capitalize.run(params=in_params)
    actual = actual.strip()
    assert actual == expected
