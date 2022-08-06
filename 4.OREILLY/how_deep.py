from typing import Tuple


def how_deep(structure: Tuple) -> int:
    # your code here
    if not type(structure) == tuple:
        return 0
    if len(structure) == 0:
        return 1
    return 1 + max(how_deep(x) for x in structure)


if __name__ == '__main__':
    print("Example:")
    # print(how_deep((1, 2, 3)))
    print(how_deep((1, 2, (3,))))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert how_deep((1, 2, 3)) == 1
    assert how_deep((1, 2, (3,))) == 2
    assert how_deep((1, 2, (3, (4,)))) == 3
    assert how_deep(()) == 1
    assert how_deep(((),)) == 2
    assert how_deep((((),),)) == 3
    assert how_deep((1, (2,), (3,))) == 2
    assert how_deep((1, ((),), (3,))) == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")