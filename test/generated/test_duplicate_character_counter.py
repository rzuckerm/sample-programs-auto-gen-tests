from glotter import project_test, project_fixture
import pytest


@project_fixture("duplicatecharactercounter")
def duplicate_character_counter(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test("duplicatecharactercounter")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(
            '"hola"', ["No duplicate characters"], id="sample input: no duplicates"
        ),
        pytest.param(
            '"goodbyeblues"', ["o: 2", "b: 2", "e: 2"], id="sample input: routine"
        ),
    ],
)
def test_duplicate_character_counter_valid(
    in_params, expected, duplicate_character_counter
):
    actual = duplicate_character_counter.run(params=in_params)
    actual_list = actual.strip().splitlines()
    expected_list = expected
    assert len(actual_list) == len(expected_list), "Length not equal"
    for index in range(len(expected_list)):
        assert (
            actual_list[index] == expected_list[index]
        ), f"Item {index + 1} is not equal"


@project_test("duplicatecharactercounter")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(None, "Usage: please provide a string", id="no input"),
        pytest.param('""', "Usage: please provide a string", id="empty input"),
    ],
)
def test_duplicate_character_counter_invalid(
    in_params, expected, duplicate_character_counter
):
    actual = duplicate_character_counter.run(params=in_params)
    actual = actual.strip()
    assert actual == expected
