def word_index(x):
    max_len = 0
    index = -1
    for stuffs in x:
        if len(stuffs) > max_len:
            max_len = len(stuffs)
            index += 1
        elif len(stuffs) == max_len:
            pass
        else:
            return 0
    return index
