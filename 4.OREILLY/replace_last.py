def replace_last(line: list) -> list:
    # your code here
    if len(line) > 0:
        line.insert(0, line.pop())
        return line
    return []


if __name__ == '__main__':

    # print('Example:')
    # print(replace_last([1, 2, 3, 4]))

    assert replace_last([2, 3, 4, 1]) == [1, 2, 3, 4]
    assert replace_last([1, 2, 3, 4]) == [4, 1, 2, 3]
    assert replace_last([1]) == [1]
    assert replace_last([]) == []

    print("The mission is done! Click 'Check Solution' to earn rewards!")