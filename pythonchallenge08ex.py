def zero_last(x):
    for num in x:
        if num == 0:
            x.remove(num)
            x.append(num)
        elif 0 not in x:
            x.sort()
    return x
