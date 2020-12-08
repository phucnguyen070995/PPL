from abc import ABC, abstractmethod , ABCMeta
class AST(ABC):
    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

class Type(AST): 
    _metaclass__ = ABCMeta
    pass
class IntType(Type):
    def __str__(self):
        return "IntType"
class FloatType(Type): 
    pass
a = FloatType()
lst = [[1,2,3], [4,5,6]]
print([i for x in lst for i in x])