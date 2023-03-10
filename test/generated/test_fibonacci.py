from glotter import project_test, project_fixture
import pytest


@project_fixture("fibonacci")
def fibonacci(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test("fibonacci")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param('"0"', [], id="sample input 0"),
        pytest.param('"1"', ["1: 1"], id="sample input 1"),
        pytest.param('"2"', ["1: 1", "2: 1"], id="sample input 2"),
        pytest.param(
            '"5"', ["1: 1", "2: 1", "3: 2", "4: 3", "5: 5"], id="sample input 5"
        ),
        pytest.param(
            '"10"',
            [
                "1: 1",
                "2: 1",
                "3: 2",
                "4: 3",
                "5: 5",
                "6: 8",
                "7: 13",
                "8: 21",
                "9: 34",
                "10: 55",
            ],
            id="sample input 10",
        ),
    ],
)
def test_fibonacci_valid(in_params, expected, fibonacci):
    actual = fibonacci.run(params=in_params)
    actual_list = actual.strip().splitlines()
    expected_list = expected
    assert len(actual_list) == len(expected_list), "Length not equal"
    for index in range(len(expected_list)):
        assert (
            actual_list[index] == expected_list[index]
        ), f"Item {index + 1} is not equal"


@project_test("fibonacci")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(
            None,
            "Usage: please input the count of fibonacci numbers to output",
            id="no input",
        ),
        pytest.param(
            '""',
            "Usage: please input the count of fibonacci numbers to output",
            id="empty input",
        ),
        pytest.param(
            '"a"',
            "Usage: please input the count of fibonacci numbers to output",
            id="invalid input: not a number",
        ),
    ],
)
def test_fibonacci_invalid(in_params, expected, fibonacci):
    actual = fibonacci.run(params=in_params)
    actual = actual.strip()
    assert actual == expected
