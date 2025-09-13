from dataclasses import dataclass


@dataclass(slots=True)
class Point:
    x: float
    y: float

    def __repr__(self) -> str:
        return f"Point(x={self.x}, y={self.y})"
