from typing import List, Iterator
from irls.Types import Joint


class ConnectTable:
    def __init__(self) -> None:
        self.table: List[Joint] = list()

    def __len__(self) -> int:
        return len(self.table)

    def __iter__(self) -> Iterator[Joint]:
        for joint in self.table:
            yield joint

    def append(self, old: int, new: int) -> None:
        self.table.append(Joint(old, new))
