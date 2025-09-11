from typing import List, Iterator
from enum import Enum, auto
from dataclasses import dataclass


class NeighborType(Enum):
    NEIGHBOR4 = auto()
    NEIGHBOR8 = auto()

    @property
    def dilation(self) -> int:
        return 0 if self is NeighborType.NEIGHBOR4 else 1


@dataclass(slots=True)
class Record:
    label: int = -1
    temp: int = -1
    y: int = -1
    xs: int = -1
    xe: int = -1

    def __len__(self) -> int:
        return self.xe - self.xs + 1

    def __repr__(self) -> str:
        return f"Record(label={self.label}, temp={self.temp}, y={self.y}, xs={self.xs}, xe={self.xe})"

    def is_neighbor(self, record: "Record", dilation: int) -> bool:
        return max(record.xs, self.xs - dilation) <= min(record.xe, self.xe + dilation)


class CodeTable:
    def __init__(self, neighbor: NeighborType = NeighborType.NEIGHBOR4) -> None:
        self.table: List[Record] = list()
        self.neighbor: NeighborType = neighbor

    def __len__(self) -> int:
        return len(self.table)

    def __repr__(self) -> str:
        return "\n".join(f"{i} : {str(record)}" for i, record in enumerate(self))

    def __iter__(self) -> Iterator[Record]:
        for record in self.table:
            yield record

    def __getitem__(self, label: int) -> List[Record]:
        return [record for record in self if record.label == label]

    @property
    def min_y(self) -> int:
        return min((record.y for record in self.table), default=0)

    @property
    def max_y(self) -> int:
        return max((record.y for record in self.table), default=0)

    def append(self, record: Record) -> None:
        self.table.append(record)

    def get_y(self, y: int) -> List[Record]:
        return [record for record in self if record.y == y]
