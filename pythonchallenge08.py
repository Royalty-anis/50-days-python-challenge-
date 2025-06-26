def odd_even(num):
    even_num = 0
    odd_num = 0
    num.sort()
    for nums in num:
        if nums % 2 == 0:
            even_num = nums
        else:
            pass

    return even_num - num[0]
