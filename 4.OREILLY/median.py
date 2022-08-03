from typing import List

def checkio(data: List[int]):

    #replace this for solution
    sorted_list = sorted(data, reverse=False)
    if len(data) %2 == 1:
        medium = int((len(data) -1) / 2)
        return sorted_list[medium]
    else:
        medium1 = int((len(data) -2 )/ 2)
        return (sorted_list[medium1] + sorted_list[medium1 + 1]) / 2


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio([3, 6, 20, 99, 10, 15]))

    # assert checkio([1, 2, 3, 4, 5]) == 3
    # assert checkio([3, 1, 2, 5, 3]) == 3
    # assert checkio([1, 300, 2, 200, 1]) == 2
    # assert checkio([3, 6, 20, 99, 10, 15]) == 12.5
    # print("Start the long test")
    # assert checkio(list(range(1000000))) == 499999.5
    # print("Coding complete? Click 'Check' to earn cool rewards!")