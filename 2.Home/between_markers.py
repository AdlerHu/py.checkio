def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here
    start = text.index(begin) + len(begin) if begin in text else 0
    end = text.index(end) if end in text else len(text)
    return text[start:end]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi'
    assert between_markers('No <hi>', '>', '<') == ''
    print('Wow, you are doing pretty good. Time to check it!')