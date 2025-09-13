from typing import List, Iterator
from irls.Types import Run, NeighborType


class CodeTable:
    def __init__(self, neighbor = NeighborType.NEIGHBOR4) -> None:
        self.neighbor = neighbor
        self.table: List[Run] = list()

    def __len__(self) -> int:
        return len(self.table)

    def __repr__(self) -> str:
        return "\n".join(f"{i} : {str(run)}" for i, run in enumerate(self))

    def __iter__(self) -> Iterator[Run]:
        for run in self.table:
            yield run

    def __getitem__(self, label: int) -> List[Run]:
        return [run for run in self if run.label == label]

    @property
    def min_y(self) -> int:
        return min((run.y for run in self.table), default=0)

    @property
    def max_y(self) -> int:
        return max((run.y for run in self.table), default=0)

    @property
    def max_label(self) -> int:
        return max((run.label for run in self.table), default=-1)

    def append(self, run: Run) -> None:
        self.table.append(run)

    def get_y(self, y: int) -> List[Run]:
        return [run for run in self if run.y == y]
