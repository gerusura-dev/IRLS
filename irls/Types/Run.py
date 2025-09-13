from typing import Optional
from dataclasses import dataclass


@dataclass(slots=True)
class Run:
    temp: int = -1
    y: int = -1
    xs: int = -1
    xe: int = -1
    label: Optional[int] = None

    def __len__(self) -> int:
        return self.xe - self.xs + 1

    def __repr__(self) -> str:
        return f"Run(label={self.label}, temp={self.temp}, y={self.y}, xs={self.xs}, xe={self.xe})"

    def is_neighbor(self, run: "Run", dilation: int) -> bool:
        return max(run.xs, self.xs - dilation) <= min(run.xe, self.xe + dilation)
