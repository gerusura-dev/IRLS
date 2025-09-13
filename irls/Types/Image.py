from typing import List, Iterator


class Image:
    def __init__(self, image: List[List[int]]) -> None:
        self.image = image

    def __repr__(self) -> str:
        src = ""
        for row in self.image:
            src += "".join(map(str, row)) + "\n"
        return src

    def __iter__(self) -> Iterator[List[int]]:
        for row in self.image:
            yield row
