lst = [1,2,3,4,5]
def double1(lst):
    return [ele*2 for ele in lst]
print(double1(lst))

idx = 0
def double2(lst):
    global idx
    if idx == len(lst):
        return lst
    else:
        lst[idx] = lst[idx]*2
        idx += 1
        return double2(lst)
print(double2(lst))

lst = [1,2,3,4,5]
def double3(lst):
    return list(map(lambda ele: ele*2, lst))
print(double3(lst))