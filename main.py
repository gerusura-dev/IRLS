import math
from typing import List
from irls import IRLS, NeighborType, Image
from test_data import TEST_IMG_DATA_1 as TEST_DATA


def main(image: List[List[int]]) -> None:
    img = Image(image)
    irls = IRLS(image, NeighborType.NEIGHBOR4)

    print(img)
    print(irls.image)
    print(irls.blobs[2])
    print(irls.blobs[2].label)
    print(irls.blobs[2].rect)
    print(irls.blobs[2].area)
    print(irls.blobs[2].cor)
    print(irls.blobs[2].cog)
    print(irls.blobs[2].theta * 180 / math.pi)


if __name__ == "__main__":
    main(TEST_DATA)
