def sort_lenght(x):
    h_lenght = 0
    new_names = []
    for stuffs in x:
        if len(stuffs) > len(new_names):
            new_names.append(stuffs)
        elif len(stuffs) < len(new_names):
            new_names.insert(stuffs)
    return new_names
