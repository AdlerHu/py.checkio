def max_digit(a: int) -> int:
    # your code here
    ans = 0
    for x in [x for x in str(a)]:
        if int(x) > ans:
            ans = int(x)
    return ans


if __name__ == '__main__':
    print('Example:')
    print(max_digit(6347))

    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1

    print("The mission is done! Click 'Check Solution' to earn rewards!")