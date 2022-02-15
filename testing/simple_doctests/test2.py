def single_letter_count(string, letter):
    """checks how many letters are in the word
    >>> single_letter_count("Hello world", "h")
    1

    >>> single_letter_count("Hello world", "z")
    0

    >>> single_letter_count("Hello world", "l")
    3
    """
    return string.lower().count(letter.lower())
