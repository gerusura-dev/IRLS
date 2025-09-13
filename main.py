from typing import List
from irls import IRLS
from test_data import TEST_IMG_DATA_6 as TEST_DATA


def main(image: List[List[int]]) -> None:
    irls = IRLS(image)
    irls.op_image()

    data = irls.blobs
    print(data)
    print(len(data))


if __name__ == "__main__":
    main(TEST_DATA)
