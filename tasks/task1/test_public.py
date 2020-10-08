import pytest

from .task import find_graph_vertices_degrees


class Case:
    def __init__(self, name: str, m: int, edges: list, degrees: list):
        self._name = name
        self.m = m
        self.edges = edges
        self.degrees = degrees

    def __str__(self) -> str:
        return 'task1_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        m=5,
        edges=[
            (1, 2),
            (2, 3),
            (3, 1),
            (4, 3),
            (5, 4),
            (5, 2),
        ],
        degrees=[2, 3, 3, 2, 2],
    ),
    Case(
        name='base2',
        m=3,
        edges=[
            (1, 2),
            (2, 3),
        ],
        degrees=[1, 2, 1],
    ),
    Case(
        name='base3',
        m=2,
        edges=[
            (1, 2),
        ],
        degrees=[1, 1],
    ),
    Case(
        name='base4',
        m=4,
        edges=[],
        degrees=[0, 0, 0, 0],
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task1(case: Case) -> None:
    answer = find_graph_vertices_degrees(
        m=case.m,
        edges=case.edges,
    )
    assert answer == case.degrees
