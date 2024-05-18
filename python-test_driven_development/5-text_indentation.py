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

    text = text.strip()
    if not text:
        print()

    char = 0

    while char < len(text):
        print(text[char], end="")
        if (text[char] in ".?:"):
            print("\n")
            while char + 1 < len(text) and text[char + 1] == " ":
                char += 1
        char += 1
