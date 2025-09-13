from typing import List, Optional
from .Run import Run
from .Rect import Rect
from .Point import Point


class Record:
    __slots__ = ("label", "rect", "area", "cor")

    def __init__(self, runs: List[Run]) -> None:
        self.label: Optional[int] = runs[0].label if runs else None
        self.rect: Rect = self.__get_rect(runs)
        self.area: int = self.__get_area(runs)
        self.cor: Point = self.__get_center_of_rect(self.rect)

    def __repr__(self) -> str:
        return f"Blob(label={self.label}, rect={self.rect}, area={self.area}, cor={self.cor})"

    @staticmethod
    def __get_rect(runs: List[Run]) -> Rect:
        xs = [run.xs for run in runs]
        xe = [run.xe for run in runs]
        y = [run.y for run in runs]
        min_x, max_x = min(xs), max(xe)
        min_y, max_y = min(y), max(y)
        return Rect(min_x, min_y, max_x - min_x + 1, max_y - min_y + 1)

    @staticmethod
    def __get_area(runs: List[Run]) -> int:
        return sum([len(run) for run in runs])

    @staticmethod
    def __get_center_of_rect(rect: Rect) -> Point:
        return Point(rect.x + rect.w / 2, rect.y + rect.h / 2)