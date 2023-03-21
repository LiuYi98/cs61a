import doctest




def fn():
    """
    >>> fn()
    5
    """
    return 5

if __name__ == "__main__":
    doctest.testmod()