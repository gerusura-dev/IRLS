from typing import List, Dict, Tuple, Iterator
from irls.Types import Record
from .CodeTable import Run, CodeTable


class Blobs:
    def __init__(self, table: CodeTable, re_label: bool = False) -> None:
        self.record: Dict[int, Record] = dict()
        self.__parser(table, re_label)

    def __len__(self) -> int:
        return len(self.record)

    def __repr__(self) -> str:
        return "\n".join(str(blob) for blob in self.record.values())

    def __getitem__(self, label: int) -> Record:
        return self.record.get(label, Record([]))

    def __iter__(self) -> Iterator[Tuple[int, Record]]:
        for item in self.record.items():
            yield item

    def __parser(self, table: CodeTable, re_label: bool) -> None:
        new_label: int = 0
        limit: int = max([run.label for run in table], default=-1) + 1

        for label in range(limit):
            blob_data: List[Run] = table[label]
            if not blob_data:
                continue

            if re_label:
                blob_data[0].label = new_label
                result_blob = Record(blob_data)
                self.record[new_label] = result_blob
                new_label += 1
            else:
                self.record[label] = Record(blob_data)

