#!/usr/bin/python3
"""
A function that prints text with 2 new lines after each of these chars: . ? :
"""
def text_indentation(text):
    """
    Args:
        text (str): The input text.
        result = the changed text
    Raises:
        TypeError: If text is not a string.
    Prints:
        The modified text with 2 new lines after each '.', '?', and ':'.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in {'.', '?', ':'}:
            result += "\n\n"
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        i += 1

    lines = result.split('\n')
    stripped_lines = [line.strip() for line in lines]
    cleaned_result = '\n'.join(stripped_lines)

    print(cleaned_result)
