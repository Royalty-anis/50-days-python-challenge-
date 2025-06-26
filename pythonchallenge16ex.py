Nested_list = [[12, 34, 56, 67], [34, 68, 78]]
def unpack(x):
    output = []
    for stuff in x:
        for i in stuff:
            if i in output:
                pass
            else:
                output.append(i)
    return output
print(unpack(Nested_list))
