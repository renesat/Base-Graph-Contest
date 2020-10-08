import pytest

from .task import find_regular_graph


class Case:
    def __init__(self, name: str, samples: list, answers: list):
        self._name = name
        self.samples = samples
        self.answers = answers

    def __str__(self) -> str:
        return 'task2_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base',
        samples=[
            (3, 2),
            (5, 3),
            (5, 4),
        ],
        answers=[
            [
                (1, 2),
                (2, 3),
                (3, 1),
            ],
            None,
            [
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
        ],
    )
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task2(case: Case) -> None:
    answer = find_regular_graph(samples=case.samples)
    assert answer == case.answers
