#!/usr/bin/python3
"""
This function prints out text
Returns:
text to stdout
"""


def text_indentation(text):
    """print text"""
    list_l = ['.', ':', '?', ]
    string = ""
    if not isinstance(text, (str)):
        raise TypeError('text must be a string')
    for char in text:
        string = string + char
        if char in list_l:
            string = string.strip()
            print(string)
            print()
            string = ""
    string = string.strip()
    print(string, end="")
