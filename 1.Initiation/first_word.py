def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here    
    return text.split(' ')[0]

print('Example:')
print(first_word("Hello world"))
print(first_word("Hello"))