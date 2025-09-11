class Point:
    __slots__ = ("__x", "__y")

    def __init__(self, x: float, y: float) -> None:
        self.__x: float = x
        self.__y: float = y

    def __repr__(self) -> str:
        return f"Point(x={self.x}, y={self.y})"

    @property
    def x(self) -> float:
        return self.__x

    @property
    def y(self) -> float:
        return self.__y


class Rect:
    __slots__ = ("__x", "__y", "__w", "__h")

    def __init__(self, x: int, y: int, w: int, h: int) -> None:
        self.__x: int = x
        self.__y: int = y
        self.__w: int = w
        self.__h: int = h

    def __repr__(self) -> str:
        return f"Rect(x={self.x}, y={self.y}, w={self.w}, h={self.h})"

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @property
    def w(self) -> int:
        return self.__w

    @property
    def h(self) -> int:
        return self.__h
