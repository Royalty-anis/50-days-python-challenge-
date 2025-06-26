string_words =  ['1','3','5']

def convert_add(x):
    converted = []
    total = 0
    for nums in x:
        converted.append(int(nums))
        total += int(nums)
    return total 
