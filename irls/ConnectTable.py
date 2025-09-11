from typing import Iterator
from dataclasses import dataclass


@dataclass(slots=True)
class Joint:
    old: int
    new: int

    def __repr__(self) -> str:
        return f"Joint(old={self.old}, new={self.new})"

    def __iter__(self) -> Iterator[int]:
        yield self.old
        yield self.new

    def replace(self, old: int, new: int) -> None:
        if self.old == old:
            self.old = new
        if self.new == old:
            self.new = new


class ConnectTable:
    def __init__(self) -> None:
        self.table = list()

    def __len__(self) -> int:
        return len(self.table)

    def __repr__(self) -> str:
        return "\n".join(f"{i}: {str(joint)}" for i, joint in enumerate(self.table))

    def append(self, old: int, new: int) -> None:
        self.table.append(Joint(old, new))

    def replace(self, old: int, new: int) -> None:
        for record in self.table:
            record.replace(old, new)

    def pop(self) -> Joint:
        return self.table.pop()
