def is_palindrome(string):
    """checks if word is is palindrome
    >>> is_palindrome("testing")
    False

    >>> is_palindrome("tacocat")
    True

    >>> is_palindrome("hannah")
    True
    """
    stripped = string.replace(" ", "")
    return stripped == stripped[::-1]
