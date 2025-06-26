def duplicate(x):
    non_duplicate = []
    for stuffs in x:
        if stuffs in non_duplicate:
            return f"{stuffs} is a duplicate"
        else:
            non_duplicate.append(stuffs)
            pass
    else:
        return "No duplicate"
