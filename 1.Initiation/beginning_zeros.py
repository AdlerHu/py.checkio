def beginning_zeros(a: str) -> int:
    # your code here
    ans = 0
    for i in [x for x in str(a)]:
        if i == '0':
            ans += 1 
        else:
            break
    return ans


if __name__ == '__main__':
    print('Example:')
    print(beginning_zeros('001001'))

    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4

    print("The mission is done! Click 'Check Solution' to earn rewards!")