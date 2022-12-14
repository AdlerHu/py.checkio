def split_list(items: list) -> list:
    # your code here
    ans_list = []
    split = int(len(items)/2) if len(items) % 2 == 0 else int((len(items)+1)/2)
    ans_list.append(items[:split])
    ans_list.append(items[split:])
    return ans_list


if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6, 7]))
    # print(split_list([]))


    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")