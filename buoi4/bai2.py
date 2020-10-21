from functools import reduce

lst1 = [1,2,3,4,5]
lst2 = ['a','b','c']
lst3 = [1.1,2.2,3.3,4.4,5.5]
lst = [lst1, lst2, lst3]

def flatten1(lst):
    return [cell for ele in lst for cell in ele]
print(flatten1(lst))

def flatten2(lst):
    if len(lst) == 0:
        return []
    else:
        return lst[0] + flatten2(lst[1:])
print(flatten2(lst))

lst = [lst1, lst2, lst3]
def flatten3(lst):
    return list(reduce(lambda x,y: x+y,lst,[]))
print(flatten3(lst))