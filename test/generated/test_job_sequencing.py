from glotter import project_test, project_fixture
import pytest


@project_fixture("jobsequencing")
def job_sequencing(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test("jobsequencing")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param('"25, 15, 10, 5" "3, 1, 2, 2"', "50", id="sample input one"),
        pytest.param('"20, 15, 10, 5, 1" "2, 2, 1, 3, 3"', "40", id="sample input two"),
    ],
)
def test_sequencing_valid(in_params, expected, job_sequencing):
    actual = job_sequencing.run(params=in_params)
    actual = actual.strip()
    assert actual == expected


@project_test("jobsequencing")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(
            None,
            "Usage: please provide a list of profits and a list of deadlines",
            id="no input",
        ),
        pytest.param(
            '""',
            "Usage: please provide a list of profits and a list of deadlines",
            id="empty input",
        ),
        pytest.param(
            '"25 15 10 5"',
            "Usage: please provide a list of profits and a list of deadlines",
            id="missing input",
        ),
        pytest.param(
            '"1, 2, 3, 4", "1, 2, 3, 4, 5"',
            "Usage: please provide a list of profits and a list of deadlines",
            id="lists different lengths",
        ),
    ],
)
def test_sequencing_invalid(in_params, expected, job_sequencing):
    actual = job_sequencing.run(params=in_params)
    actual = actual.strip()
    assert actual == expected
