def between_markers(text: str, start: str, end: str) -> str:
    # your code here
    return text[text.index(start) + 1 : text.index(end)]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    assert between_markers('What is >apple<', '>', '<') == 'apple'
    assert between_markers('What is [apple]', '[', ']') == 'apple'
    assert between_markers('What is ><', '>', '<') == ''
    assert between_markers('[an apple]', '[', ']') == 'an apple'

    print("The mission is done! Click 'Check Solution' to earn rewards!")