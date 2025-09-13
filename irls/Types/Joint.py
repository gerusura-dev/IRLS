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
