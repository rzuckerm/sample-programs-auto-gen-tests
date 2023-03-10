from glotter import project_test, project_fixture
import pytest


@project_fixture("dijkstra")
def dijkstra(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test("dijkstra")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(
            '"0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0" "0" "1"',
            "2",
            id="sample input: routine",
        ),
    ],
)
def test_dijkstra_valid(in_params, expected, dijkstra):
    actual = dijkstra.run(params=in_params)
    actual = actual.replace("[", "").replace("]", "").strip()
    assert actual == expected


@project_test("dijkstra")
@pytest.mark.parametrize(
    ("in_params", "expected"),
    [
        pytest.param(
            None,
            "Usage: please provide three inputs: a serialized matrix, a source node and a destination node",
            id="no input",
        ),
        pytest.param(
            '"" "" ""',
            "Usage: please provide three inputs: a serialized matrix, a source node and a destination node",
            id="empty input",
        ),
        pytest.param(
            '"1, 0, 3, 0, 5, 1" "1" "2"',
            "Usage: please provide three inputs: a serialized matrix, a source node and a destination node",
            id="non-square input",
        ),
        pytest.param(
            '"0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0" "0" ""',
            "Usage: please provide three inputs: a serialized matrix, a source node and a destination node",
            id="no destination",
        ),
        pytest.param(
            '"0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0" "3" "" ""',
            "Usage: please provide three inputs: a serialized matrix, a source node and a destination node",
            id="no source or destination",
        ),
        pytest.param(
            '"0, 2, 0, 6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, 6, 8, 0, 0, 9, 0, 5, 7, 9, 0" "3" "-1" "2"',
            "Usage: please provide three inputs: a serialized matrix, a source node and a destination node",
            id="source or destination < 0",
        ),
        pytest.param(
            '"0, 2, 0, -6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, -6, 8, 0, 0, 9, 0, 5, 7, 9, 0" "3" "1" "2"',
            "Usage: please provide three inputs: a serialized matrix, a source node and a destination node",
            id="weight < 0",
        ),
        pytest.param(
            '"0, 2, 0, -6, 0, 2, 0, 3, 8, 5, 0, 3, 0, 0, 7, -6, 8, 0, 0, 9, 0, 5, 7, 9, 0" "3" "1" "10"',
            "Usage: please provide three inputs: a serialized matrix, a source node and a destination node",
            id="source or destination > number of vertices",
        ),
    ],
)
def test_dijkstra_invalid(in_params, expected, dijkstra):
    actual = dijkstra.run(params=in_params)
    actual = actual.strip()
    assert actual == expected
