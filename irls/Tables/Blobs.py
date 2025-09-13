from typing import List, Dict, Tuple, Optional, Iterator
from irls.Types import Run, Record
from irls.Tables import CodeTable


class Blobs:
    def __init__(self, table: CodeTable) -> None:
        self.record: Dict[int, Record] = dict()
        self.__parser(table)

    def __len__(self) -> int:
        return len(self.record)

    def __repr__(self) -> str:
        return "\n".join(str(blob) for blob in self.record.values())

    def __getitem__(self, label: int) -> Optional[Record]:
        return self.record.get(label, None)

    def __iter__(self) -> Iterator[Tuple[int, Record]]:
        for item in self.record.items():
            yield item

    def __parser(self, table: CodeTable) -> None:
        limit: int = max([run.label for run in table], default=-1) + 1

        for label in range(limit):
            blob_data: List[Run] = table[label]
            if not blob_data:
                continue

            self.record[label] = Record(blob_data)
