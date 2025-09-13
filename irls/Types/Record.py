from typing import List, Optional
import math
from irls.Types import Run, Rect, Point


class Record:
    __slots__ = ("label", "rect", "area", "cor", "cog", "theta")

    def __init__(self, runs: List[Run]) -> None:
        self.label: Optional[int] = runs[0].label if runs else None
        self.rect: Rect = self.__get_rect(runs)
        self.area: int = self.__get_area(runs)
        self.cor: Point = self.__get_center_of_rect(self.rect)
        self.cog: Point = self.__get_center_of_gravity(runs)
        self.theta: float = self.__get_theta(runs, self.cog)

    def __repr__(self) -> str:
        return f"Blob(label={self.label}, rect={self.rect}, area={self.area}, cor={self.cor}, cog={self.cog}, theta={self.theta})"

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

    @staticmethod
    def __get_center_of_gravity(runs: List[Run]) -> Point:
        x, y = 0, 0
        length = 0

        for run in runs:
            x += sum(list(range(run.xs, run.xe + 1)))
            y += run.y * len(run)
            length += len(run)

        return Point(x / length + 0.5, y / length + 0.5)

    @staticmethod
    def __get_theta(runs: List[Run], cog: Point) -> float:
        m11 = 0
        m20 = 0
        m02 = 0

        for run in runs:
            m11 += sum([(pos + 0.5 - cog.x) * (run.y + 0.5 - cog.y) for pos in range(run.xs, run.xe + 1)])
            m20 += sum([(pos + 0.5 - cog.x) * (pos + 0.5 - cog.x) for pos in range(run.xs, run.xe + 1)])
            m02 += sum([(run.y + 0.5 - cog.y) * (run.y + 0.5 - cog.y) for _ in range(run.xs, run.xe + 1)])

        if m11 + m20 + m02 == 0:
            return 0

        return math.atan((2 * m11) / (m20 - m02))
