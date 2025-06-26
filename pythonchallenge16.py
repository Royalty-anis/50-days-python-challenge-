list_add = [[2, 4, 5, 6], [2, 3, 5, 6]]
def sum_list(x):
    total = 0
    for i in x:
        for stuff in i:
            total += stuff
    return total
print(sum_list(list_add))
