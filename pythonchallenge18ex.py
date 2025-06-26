def add_reverse(x,y):
    total = 0
    z= []
    for num_x in x:
        z.append(num_x + y[total])
        total += 1
    z.reverse()
    return z
