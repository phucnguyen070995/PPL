def lstSquare(n):
    if n == 1:
        return [1]
    else: 
        return lstSquare(n-1) + [n*n]
print(lstSquare(3))
# def dist(lst,n):
#     return list(map(lambda ele: (ele, n), lst))

def dist(lst,n):
    return list(map(lambda ele: (ele, n), lst))
def flatten2(lst):
    if len(lst) == 0:
        return []
    else:
        return lst[0] + flatten2(lst[1:])
print(dist([1,2,3,4],4))

def dist(lst,n):
    if len(lst) == 0:
        return []
    else:
        return [(lst[0],n)] + dist(lst[1:],n)
print(dist([1,2,3,4],4))
