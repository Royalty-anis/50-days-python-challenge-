def only_floats(x,y):
    if isinstance(x,float) and isinstance(y,float):
        return 2
    elif isinstance(x,float) or isinstance(y,float):
        return 1
    else:
        return 0
