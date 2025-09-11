from typing import List, Dict, Tuple, Optional, Iterator
from .Types import Rect, Point
from .CodeTable import Record, CodeTable


class Blob:
    __slots__ = ("__label", "__rect", "__area", "__cor")

    def __init__(self, records: List[Record]) -> None:
        self.__label: Optional[int] = records[0].label if records else None
        self.__rect: Rect = self.__get_rect(records)
        self.__area: int = self.__get_area(records)
        self.__cor: Point = self.__get_center_of_rect(self.__rect)

    def __repr__(self) -> str:
        return f"Blob(label={self.label}, rect={self.rect}, area={self.area}, cor={self.cor})"

    @property
    def label(self) -> Optional[int]:
        return self.__label

    @property
    def rect(self) -> Rect:
        return self.__rect

    @property
    def area(self) -> int:
        return self.__area

    @property
    def cor(self) -> Point:
        return self.__cor

    @staticmethod
    def __get_rect(records: List[Record]) -> Rect:
        x = [record.xs for record in records] + [record.xe for record in records]
        y = [record.y for record in records]
        return Rect(min(x), min(y), max(x) - min(x) + 1, max(y) - min(y) + 1)

    @staticmethod
    def __get_area(records: List[Record]) -> int:
        return sum([len(record) for record in records])

    @staticmethod
    def __get_center_of_rect(rect: Rect) -> Point:
        return Point(rect.x + rect.w / 2, rect.y + rect.h / 2)


class Blobs:
    def __init__(self, table: CodeTable, re_label: bool = True) -> None:
        self.__blob: Dict[int, Blob] = dict()
        self.__parser(table, re_label)

    def __len__(self) -> int:
        return len(self.__blob)

    def __repr__(self) -> str:
        return "\n".join(str(blob) for blob in self.__blob.values())

    def __getitem__(self, label: int) -> Blob:
        return self.__blob.get(label, Blob([]))

    def __iter__(self) -> Iterator[Tuple[int, Blob]]:
        for item in self.__blob.items():
            yield item

    @property
    def blob(self) -> Dict[int, Blob]:
        return self.__blob

    def __parser(self, table: CodeTable, re_label: bool) -> None:
        new_label: int = 0
        limit: int = max([record.label for record in table], default=-1) + 1

        for label in range(limit):
            blob_data: List[Record] = table[label]
            if not blob_data:
                continue

            if re_label:
                blob_data[0].label = new_label
                result_blob = Blob(blob_data)
                self.__blob[new_label] = result_blob
                new_label += 1
            else:
                self.__blob[label] = Blob(blob_data)

