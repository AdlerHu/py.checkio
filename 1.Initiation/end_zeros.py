def end_zeros(a: int) -> int:
    # your code here

    reverse_list = [x for x in str(a)][::-1]
    ans = 0

    for i in reverse_list:
        if i == '0':
            ans += 1 
        else:
            break
    return ans


print('Example:')
print(end_zeros(101))

# assert end_zeros(0) == 1
# assert end_zeros(1) == 0
# assert end_zeros(10) == 1
# assert end_zeros(101) == 0
# assert end_zeros(245) == 0
# assert end_zeros(100100) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")