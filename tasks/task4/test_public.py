import pytest

from .task import in_component


class Case:
    def __init__(self, name: str, n: list, vertices: list, edges: list,
                 answer: bool):
        self._name = name
        self.n = n
        self.vertices = vertices
        self.edges = edges
        self.answer = answer

    def __str__(self) -> str:
        return 'task4_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        n=4,
        vertices=[1, 2, 3],
        edges=[
            (1, 2),
            (2, 3),
            (1, 3),
        ],
        answer=True,
    ),
    Case(
        name='base2',
        n=4,
        vertices=[1, 2, 3],
        edges=[
            (1, 2),
            (3, 4),
        ],
        answer=False,
    ),
    Case(
        name='base3',
        n=4,
        vertices=[4, 2, 3, 1],
        edges=[
            (1, 2),
        ],
        answer=True,
    ),
    Case(
        name='base4',
        n=2,
        vertices=[1],
        edges=[
            (1, 2),
        ],
        answer=False,
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task3(case: Case) -> None:
    answer = in_component(
        n=case.n,
        vertices=case.vertices,
        edges=case.edges,
    )
    assert answer == case.answer
