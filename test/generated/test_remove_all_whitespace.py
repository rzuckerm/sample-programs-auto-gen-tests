from glotter import project_test, project_fixture
import pytest


@project_fixture("removeallwhitespace")
def remove_all_whitespace(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test("removeallwhitespace")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(
            '"RemoveAllWhitespace"', "RemoveAllWhitespace", id="sample input: no spaces"
        ),
        pytest.param(
            '"    RemoveAllWhitespace"',
            "RemoveAllWhitespace",
            id="sample input: leading spaces",
        ),
        pytest.param(
            '"RemoveAllWhitespace    "',
            "RemoveAllWhitespace",
            id="sample input: trailing spaces",
        ),
        pytest.param(
            '"Remove All Whitespace"',
            "RemoveAllWhitespace",
            id="sample input: inner spaces",
        ),
        pytest.param(
            '"\tRemove\tAll\tWhitespace\t"',
            "RemoveAllWhitespace",
            id="sample input: tabs",
        ),
        pytest.param(
            '"\nRemove\nAll\nWhitespace\n"',
            "RemoveAllWhitespace",
            id="sample input: newlines",
        ),
        pytest.param(
            '"\rRemove\rAll\rWhitespace\r"',
            "RemoveAllWhitespace",
            id="sample input: carriage returns",
        ),
    ],
)
def test_remove_all_whitespace_valid(in_params, expected, remove_all_whitespace):
    actual = remove_all_whitespace.run(params=in_params)
    actual = actual.strip()
    assert actual == expected


@project_test("removeallwhitespace")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(None, "Usage: please provide a string", id="no input"),
        pytest.param('""', "Usage: please provide a string", id="empty input"),
    ],
)
def test_remove_all_whitespace_invalid(in_params, expected, remove_all_whitespace):
    actual = remove_all_whitespace.run(params=in_params)
    actual = actual.strip()
    assert actual == expected
