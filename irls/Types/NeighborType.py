from enum import Enum, auto


class NeighborType(Enum):
    NEIGHBOR4 = auto()
    NEIGHBOR8 = auto()

    @property
    def dilation(self) -> int:
        return 0 if self is NeighborType.NEIGHBOR4 else 1
