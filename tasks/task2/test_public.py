import pytest

from .task import find_regular_graph


class Case:
    def __init__(self, name: str, n: int, k: int, graph: list):
        self._name = name
        self.n = n
        self.k = k
        self.graph = graph

    def __str__(self) -> str:
        return 'task2_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        n=3,
        k=2,
        graph=[
            (1, 2),
            (2, 3),
            (3, 1),
        ],
    ),
    Case(
        name='base2',
        n=5,
        k=3,
        graph=None,
    ),
    Case(
        name='base3',
        n=5,
        k=4,
        graph=[
            (1, 2),
            (1, 3),
            (2, 3),
            (2, 4),
            (3, 4),
            (3, 5),
            (4, 5),
            (4, 1),
            (5, 1),
            (5, 2),
        ],
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task2(case: Case) -> None:
    answer = find_regular_graph(n=case.n, k=case.k)
    assert answer == case.graph
