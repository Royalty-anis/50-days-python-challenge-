def equal_strings(x,y):
    temp1 = []
    temp2 = []
    for i in x:
        temp1.append(i)
    for stuffs in y:
        temp2.append(stuffs)
    temp1.sort(),temp2.sort()
    if temp1 == temp2:
        return True
    else:
        return False
