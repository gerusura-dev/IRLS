from typing import List, Tuple, Iterator


class TransferTable:
    def __init__(self, length: int) -> None:
        self.table: List[int] = list(range(length + 1))

    def __iter__(self) -> Iterator[Tuple[int, int]]:
        for index, value in enumerate(self.table):
            yield index, value

    def __getitem__(self, index: int) -> int:
        return self.table[index]

    def append(self, old: int, new: int) -> None:
        new_label: int = min(self.table[old], self.table[new])
        old_label: int = max(self.table[old], self.table[new])
        self.table = [new_label if value == old_label else value for value in self.table]
