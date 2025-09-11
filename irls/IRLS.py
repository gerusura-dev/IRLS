from typing import List, Optional
from .CodeTable import Record, CodeTable, NeighborType
from .ConnectTable import ConnectTable
from .Blobs import Blobs


class IRLS:
    def __init__(self, image: List[List[int]], neighbor: NeighborType = NeighborType.NEIGHBOR4, re_label: bool = True) -> None:
        self.__neighbor = neighbor
        self.__image = image
        self.__table = self.__search()
        self.__labeling()
        self.__blobs = Blobs(self.__table, re_label)

    @property
    def blobs(self) -> Blobs:
        return self.__blobs

    def op_image(self) -> None:
        print()
        for run in self.__image:
            line = "".join(map(str, run)).replace("0", "⬛️").replace("1", "⬜️")
            print(f"    {line}")
        print()

    def __search(self) -> CodeTable:
        table = CodeTable(self.__neighbor)
        image = [[0] + run + [0] for run in self.__image]

        record: Optional[Record] = None

        for y, run in enumerate(image):
            for x, (left, right) in enumerate(zip(run[:-1], run[1:])):
                scan = left + right
                if scan == 1:
                    if record:
                        table.append(record)
                        record = None
                    else:
                        record = Record(temp=len(table), y=y, xs=x, xe=x)
                elif scan == 2:
                    record.xe += 1

        return table

    def __labeling(self) -> None:
        table = ConnectTable()
        latest = 0

        def new_label(targets: List[Record]) -> None:
            nonlocal latest
            for target in targets:
                target.label = latest
                latest += 1

        for y in range(self.__table.max_y + 1):
            records = self.__table.get_y(y)

            if not records:
                continue

            if not y:
                new_label(records)
                continue

            pre_records = self.__table.get_y(y - 1)

            if not pre_records:
                new_label(records)
                continue

            for record in records:
                for pre_record in pre_records:
                    if pre_record.is_neighbor(record, self.__neighbor.dilation):
                        if record.label == -1:
                            record.label = pre_record.label
                        else:
                            table.append(record.label, pre_record.label)
                    else:
                        if record.label == -1:
                            new_label([record])
                            continue

        self.__connect(table)

    def __connect(self, connect: ConnectTable) -> None:
        while len(connect):
            old, new = connect.pop()
            for record in self.__table[old]:
                record.label = new

            connect.replace(old, new)
