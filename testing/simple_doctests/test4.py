def capitalize(string):
    """capitalizing the word

    >>> capitalize("cat")
    'Cat'

    >>> capitalize("dog")
    'Dog'

    >>> capitalize("matthew")
    'matthew'
    """
    return string[:1].upper() + string[1:]
