def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    result = [True if isinstance(l, list) else False for l in lst]
    if result.count(False) > 0:
        return False
    else: return True
