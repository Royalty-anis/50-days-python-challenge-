names = ["kerry", "dickson", "John", "Mary","carol", "Rose", "adam"]
stuffs = []
for name in names:
    if name[0].islower():
        stuffs.append(name)
    else:
        pass
stuffs.sort(reverse=True)
tuples = tuple(stuffs)
