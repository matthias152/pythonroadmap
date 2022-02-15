def number_compare(a, b):
    """checks which number is greater

    >>> number_compare(4, 5)
    'Second is greater'

    >>> number_compare(3, 1)
    'First is greater'
    """
    if a > b:
        return "First is greater"
    elif b > a:
        return "Second is greater"
    return "Numbers are equal"
