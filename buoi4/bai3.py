from functools import reduce

lst = [1,9,3,4,5,6,7,8,9,10]

def lessThan1(num, lst):
    return [item for item in lst if item < num]
print(lessThan1(9,lst))

def lessThan2(num, lst):
    if len(lst) == 0:
        return []
    if lst[0] < num:
        return [lst[0]] + lessThan2(num, lst[1:])
    return lessThan2(num, lst[1:])
print(lessThan2(9,lst))

def lessThan3(num, lst):
    return list(filter(lambda x: x < num, lst))
print(lessThan3(9, lst))