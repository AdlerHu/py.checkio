def split_pairs(a: str):
    # your code here
    sth_list = [x for x in a]
    ans_list = []
    if len(sth_list) % 2 == 1:
        sth_list.append('_')

    for i in range(len(sth_list) -1):
        if i % 2 == 0:
            ans_list.append(sth_list[i] + sth_list[i+1])

    return ans_list


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abc')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")