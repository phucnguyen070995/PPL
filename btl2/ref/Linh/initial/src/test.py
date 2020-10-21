from  functools import reduce

from abc import ABC, abstractmethod
from typing import List

def merge(lst):
    l = []
    for x in lst: 
        if type(x) == list: 
            l+= x
        else : 
            l+=[x]
    return l
def doublea(lst): 
    return [x*2 for x in lst]
def doubleb(lst):
    return [] if len(lst)==0 else [lst[0]] + doubleb(lst[1:])
def doublec(lst): 
    return (list(map((lambda x: 2*x), lst)))
def mergeA(lst):
    if len(lst)==0:
        return []
    else: 
        return lst[0]+ mergeA(lst[1:]) if type(lst[0])== list else [lst[0]]+ mergeA(lst[1:])
def mergeB(lst):
    return reduce((lambda x,y: x+y), lst)
lst = [[1], [2,3,4], 2,3]

print(len(test))