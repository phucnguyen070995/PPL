lst = [1,2,3,4,5]
def double1(lst):
    return [ele*2 for ele in lst]
print(double1(lst))

def double2(lst):
    if len(lst) == 0:
        return []
    else:
        return double2(lst[:-1]) + [lst[-1]*2]
print(double2(lst))

lst = [1,2,3,4,5]
def double3(lst):
    return list(map(lambda ele: ele*2, lst))
print(double3(lst))