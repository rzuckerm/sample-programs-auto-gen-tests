from glotter import project_test, project_fixture
import pytest


@project_fixture("romannumeral")
def roman_numeral(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test("romannumeral")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param('""', "0", id="empty input"),
        pytest.param('"I"', "1", id="single I"),
        pytest.param('"V"', "5", id="single V"),
        pytest.param('"X"', "10", id="single X"),
        pytest.param('"L"', "50", id="single L"),
        pytest.param('"C"', "100", id="single C"),
        pytest.param('"D"', "500", id="single D"),
        pytest.param('"M"', "1000", id="single M"),
        pytest.param('"XXV"', "25", id="addition"),
        pytest.param('"XIV"', "14", id="subtraction"),
    ],
)
def test_roman_numeral_valid(in_params, expected, roman_numeral):
    actual = roman_numeral.run(params=in_params)
    actual = actual.strip()
    assert actual == expected


@project_test("romannumeral")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(
            None, "Usage: please provide a string of roman numerals", id="no input"
        ),
        pytest.param(
            '"XT"', "Error: invalid string of roman numerals", id="invalid input"
        ),
    ],
)
def test_roman_numeral_invalid(in_params, expected, roman_numeral):
    actual = roman_numeral.run(params=in_params)
    actual = actual.strip()
    assert actual == expected
