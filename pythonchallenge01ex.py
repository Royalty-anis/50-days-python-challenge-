def longest_value(x):
    total_len = 0
    longest_val = None
    for things in x:
        if len(x[things]) > total_len:
            total_len = len(x[things])
            longest_val = x[things]
        elif len(x[things]) == total_len:
            pass

    return longest_val
