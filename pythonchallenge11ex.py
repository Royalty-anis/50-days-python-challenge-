def swap_value(x):
    temp = x[0]
    x[0] = x[-1]
    x[-1] = temp
    return x
