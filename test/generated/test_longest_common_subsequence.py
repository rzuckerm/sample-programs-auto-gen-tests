from glotter import project_test, project_fixture
import pytest


@project_fixture("longestcommonsubsequence")
def longest_common_subsequence(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test("longestcommonsubsequence")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(
            '"1, 4, 5, 3, 15, 6" "1, 7, 4, 5, 11, 6"',
            "1, 4, 5, 6",
            id="sample input same length",
        ),
        pytest.param(
            '"1, 4, 8, 6, 9, 3, 15, 11, 6" "1, 7, 4, 5, 8, 11, 6"',
            "1, 4, 8, 11, 6",
            id="sample input different length",
        ),
    ],
)
def test_lcs_valid(in_params, expected, longest_common_subsequence):
    actual = longest_common_subsequence.run(params=in_params)
    actual = actual.replace("[", "").replace("]", "").strip()
    assert actual == expected


@project_test("longestcommonsubsequence")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(
            None,
            'Usage: please provide two lists in the format "1, 2, 3, 4, 5"',
            id="no input",
        ),
        pytest.param(
            '""',
            'Usage: please provide two lists in the format "1, 2, 3, 4, 5"',
            id="empty input",
        ),
        pytest.param(
            '"25 15 10 5"',
            'Usage: please provide two lists in the format "1, 2, 3, 4, 5"',
            id="missing input",
        ),
    ],
)
def test_lcs_invalid(in_params, expected, longest_common_subsequence):
    actual = longest_common_subsequence.run(params=in_params)
    actual = actual.strip()
    assert actual == expected
