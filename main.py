from typing import List
from irls import IRLS, NeighborType, Image
from test_data import TEST_IMG_DATA_1 as TEST_DATA


def main(image: List[List[int]]) -> None:
    img = Image(image)
    irls = IRLS(image, NeighborType.NEIGHBOR4)

    print(img)
    print(irls.image)

    data = irls.blobs
    print(data)
    print(len(data))

    for i, record in irls:
        print(i, record)


if __name__ == "__main__":
    main(TEST_DATA)
