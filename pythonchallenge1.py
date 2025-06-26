from math import sqrt as s
def divide_or_square(x):
    if x % 5 == 0:
        return s(x)
    else:
        return x % 5
print(divide_or_square(10))
