from typing import List
from irls.Types import Joint


class ConnectTable:
    def __init__(self) -> None:
        self.table: List[Joint] = list()

    def __len__(self) -> int:
        return len(self.table)

    def append(self, old: int, new: int) -> None:
        self.table.append(Joint(old, new))

    def replace(self, old: int, new: int) -> None:
        for record in self.table:
            record.replace(old, new)

    def pop(self) -> Joint:
        return self.table.pop()
