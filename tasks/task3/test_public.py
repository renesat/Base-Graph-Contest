import pytest

from .task import find_graph


class Case:
    def __init__(self, name: str, samples: list, answers: list):
        self._name = name
        self.samples = samples
        self.answers = answers

    def __str__(self) -> str:
        return 'task3_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base',
        samples=[
            (2, 2),
            (1, 2),
        ],
        answers=[
            [
                (1, 1),
                (1, 2),
                (2, 1),
                (2, 2),
            ],
            None,
        ],
    )
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task3(case: Case) -> None:
    answer = find_graph(samples=case.samples)
    assert answer == case.answers
