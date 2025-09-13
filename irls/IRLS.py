from typing import List, Optional
from irls.Tables.CodeTable import Run, CodeTable, NeighborType
from irls.Tables.ConnectTable import ConnectTable
from irls.Tables.Blobs import Blobs


class IRLS:
    def __init__(self, image: List[List[int]], neighbor = NeighborType.NEIGHBOR4, re_label: bool = True) -> None:
        self.__neighbor = neighbor
        self.__image = image
        self.__blobs = self.__search(re_label)

    @property
    def blobs(self) -> Blobs:
        return self.__blobs

    def op_image(self) -> None:
        print()
        for run in self.__image:
            line = "".join(map(str, run)).replace("0", "⬛️").replace("1", "⬜️")
            print(f"    {line}")
        print()

    def __search(self, re_label: bool) -> Blobs:
        table = CodeTable(self.__neighbor)
        image = [[0] + run + [0] for run in self.__image]

        record: Optional[Run] = None

        for y, run in enumerate(image):
            for x, (left, right) in enumerate(zip(run[:-1], run[1:])):
                scan = left + right
                if scan == 1:
                    if record:
                        record.xe = x - 1
                        table.append(record)
                        record = None
                    else:
                        record = Run(temp=len(table), y=y, xs=x, xe=x)

        return Blobs(self.__labeling(table), re_label)

    def __labeling(self, code_table: CodeTable) -> CodeTable:
        table = ConnectTable()
        latest = 0

        def new_label(targets: List[Run]) -> None:
            nonlocal latest
            for target in targets:
                target.label = latest
                latest += 1

        for y in range(code_table.max_y + 1):
            records = code_table.get_y(y)

            if not records:
                continue

            if not y:
                new_label(records)
                continue

            pre_records = code_table.get_y(y - 1)

            if not pre_records:
                new_label(records)
                continue

            for record in records:
                for pre_record in pre_records:
                    if pre_record.is_neighbor(record, self.__neighbor.dilation):
                        if record.label is None:
                            record.label = pre_record.label
                        else:
                            table.append(record.label, pre_record.label)
                    else:
                        if record.label is None:
                            new_label([record])
                            continue

        return self.__connect(code_table, table)

    @staticmethod
    def __connect(code_table: CodeTable, connect: ConnectTable) -> CodeTable:
        while len(connect):
            old, new = connect.pop()
            for record in code_table[old]:
                record.label = new

            connect.replace(old, new)

        return code_table
