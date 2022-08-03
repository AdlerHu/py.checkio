def second_index(text: str, symbol: str):
    """
        returns the second index of a symbol in a given text
    """
    # your code here
    result_list = [i for i in range(len(text)) if text.startswith(symbol, i)]
    return result_list[1] if len(result_list) >1 else None


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3
    assert second_index("find the river", "e") == 12
    assert second_index("hi", " ") is None
    assert second_index("hi mayor", " ") is None
    assert second_index("hi mr Mayor", " ") == 5
    print('You are awesome! All tests are done! Go Check it!')