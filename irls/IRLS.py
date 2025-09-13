from copy import deepcopy
from typing import List, Tuple, Optional, Iterator
from irls.Types import Image, Run, Record, NeighborType
from irls.Tables import Blobs, CodeTable, ConnectTable, TransferTable


class IRLS:
    def __init__(self, image: List[List[int]], neighbor = NeighborType.NEIGHBOR4) -> None:
        self.__neighbor = neighbor
        self.__blobs, self.__image = self.__search(deepcopy(image))

    def __iter__(self) -> Iterator[Tuple[int, Record]]:
        for record in self.blobs:
            yield record

    def __getitem__(self, label: int) -> Optional[Record]:
        return self.blobs[label]

    @property
    def blobs(self) -> Blobs:
        return self.__blobs

    @property
    def image(self) -> Image:
        return self.__image

    def __get_image(self):
        pass

    def __search(self, image_org: List[List[int]]) -> Tuple[Blobs, Image]:
        table = CodeTable(self.__neighbor)
        image = [[0] + run + [0] for run in image_org]

        record: Optional[Run] = None

        for y, run in enumerate(image):
            for x, (left, right) in enumerate(zip(run[:-1], run[1:])):
                if left + right == 1:
                    if record is not None:
                        record.xe = x - 1
                        table.append(record)
                        record = None
                    else:
                        record = Run(temp=len(table), y=y, xs=x, xe=-1)

        self.__labeling(table)

        for run in table:
            image_org[run.y][run.xs:run.xe + 1] = [run.label for _ in range(len(run))]

        return Blobs(table), Image(image_org)

    def __labeling(self, code_table: CodeTable) -> None:
        table = ConnectTable()
        latest = 1

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

        self.__connect(code_table, table)

    @staticmethod
    def __connect(code_table: CodeTable, connect: ConnectTable) -> None:
        table = TransferTable(code_table.max_label)

        for old, new in connect:
            table.append(old, new)

        for run in code_table:
            run.label = table[run.label]
