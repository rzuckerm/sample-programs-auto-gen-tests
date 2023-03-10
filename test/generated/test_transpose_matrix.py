from glotter import project_test, project_fixture
import pytest


@project_fixture("transposematrix")
def transpose_matrix(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test("transposematrix")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(
            '"3" "2" "1, 2, 3, 4, 5, 6"', "1, 4, 2, 5, 3, 6", id="sample input: routine"
        ),
    ],
)
def test_transpose_matrix_valid(in_params, expected, transpose_matrix):
    actual = transpose_matrix.run(params=in_params)
    actual = actual.replace("[", "").replace("]", "").strip()
    assert actual == expected


@project_test("transposematrix")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(
            None,
            "Usage: please enter the dimension of the matrix and the serialized matrix",
            id="no input",
        ),
        pytest.param(
            '"" "" "1, 2, 3, 4, 5, 6"',
            "Usage: please enter the dimension of the matrix and the serialized matrix",
            id="missing input: no columns or rows",
        ),
        pytest.param(
            '"3" "3" ""',
            "Usage: please enter the dimension of the matrix and the serialized matrix",
            id="missing input: no matrix",
        ),
    ],
)
def test_transpose_matrix_invalid(in_params, expected, transpose_matrix):
    actual = transpose_matrix.run(params=in_params)
    actual = actual.strip()
    assert actual == expected
