from dataclasses import dataclass


@dataclass(slots=True)
class Rect:
    x: int
    y: int
    w: int
    h: int

    def __repr__(self) -> str:
        return f"Rect(x={self.x}, y={self.y}, w={self.w}, h={self.h})"
