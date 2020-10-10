import pytest

from .task import find_graph


class Case:
    def __init__(self, name: str, d_1: int, d_2: int, graph: list):
        self._name = name
        self.d_1 = d_1
        self.d_2 = d_2
        self.graph = graph

    def __str__(self) -> str:
        return 'task3_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        d_1=2,
        d_2=2,
        graph=(2, [
            (1, 1),
            (1, 2),
            (2, 1),
            (2, 2),
        ]),
    ),
    Case(
        name='base2',
        d_1=1,
        d_2=2,
        graph=None,
    )
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task3(case: Case) -> None:
    answer = find_graph(
        d_1=case.d_1,
        d_2=case.d_2,
    )
    assert answer == case.graph
