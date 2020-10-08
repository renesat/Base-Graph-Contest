import pytest

from .task import find_graphs_degrees


class Case:
    def __init__(self, name: str, graphs: list, degrees: list):
        self._name = name
        self.degrees = degrees
        self.graphs = graphs

    def __str__(self) -> str:
        return 'task1_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base',
        graphs=[
            (5, [
                (1, 2),
                (2, 3),
                (3, 1),
                (4, 3),
                (5, 4),
                (5, 2),
            ]),
            (3, [
                (1, 2),
                (2, 3),
            ]),
            (2, [
                (1, 2),
            ]),
            (4, []),
        ],
        degrees=[
            [2, 3, 3, 2, 2],
            [1, 2, 1],
            [1, 1],
            [0, 0, 0, 0],
        ],
    )
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task1(case: Case) -> None:
    answer = find_graphs_degrees(graphs=case.graphs)
    assert answer == case.degrees
