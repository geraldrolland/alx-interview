#!/usr/bin/python3


def canUnlockAll(boxes: Boxes) -> bool:
    """
    boxes: a list of list
    """
    BoxSize: int = len(boxes)
    if BoxSize > 0:
        listKeys: list[int] = [0]
        i: int = 0
        while i < BoxSize:
            if i in listKeys:
                for j in boxes[i]:
                    k: int = 0
                    while k < BoxSize:
                        if j == k:
                            if k not in listKeys:
                                listKeys.append(k)
                                if j < i:
                                    i = j - 1
                                break
                        k += 1
            i += 1
        return BoxSize == len(listKeys)
