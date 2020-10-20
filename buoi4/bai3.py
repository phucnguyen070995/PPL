from functools import reduce

lst = [1,9,3,4,5,6,7,8,9,10]

def lessThan1(num, lst):
    return [item for item in lst if item < num]
print(lessThan1(9,lst))

res = []
def lessThan2(num, lst):
    global res
    if len(lst) == 0:
        return res
    else:
        if lst[0] < num:
            res += [lst[0]]
        return lessThan2(num, lst[1:])
print(lessThan2(9,lst))

def flatten3(num, lst):
    res = []
    return list(filter(lambda x: x < num, lst))
print(flatten3(9, lst))