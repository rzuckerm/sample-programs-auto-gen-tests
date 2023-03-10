from glotter import project_test, project_fixture
import pytest


@project_fixture("josephusproblem")
def josephus_problem(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test("josephusproblem")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param('"5" "2"', "3", id="sample input 5, 2"),
        pytest.param('"7" "3"', "4", id="sample input 7 3"),
        pytest.param('"41" "4"', "11", id="sample input 41 4"),
    ],
)
def test_josephus_problem_valid(in_params, expected, josephus_problem):
    actual = josephus_problem.run(params=in_params)
    actual = actual.strip()
    assert actual == expected


@project_test("josephusproblem")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(
            None,
            "Usage: please input the total number of people and number of people to skip.",
            id="no input",
        ),
        pytest.param(
            '""',
            "Usage: please input the total number of people and number of people to skip.",
            id="empty input",
        ),
        pytest.param(
            '"a"',
            "Usage: please input the total number of people and number of people to skip.",
            id="invalid input: not a number",
        ),
        pytest.param(
            '"1"',
            "Usage: please input the total number of people and number of people to skip.",
            id="invalid input: no k",
        ),
    ],
)
def test_josephus_problem_invalid(in_params, expected, josephus_problem):
    actual = josephus_problem.run(params=in_params)
    actual = actual.strip()
    assert actual == expected
