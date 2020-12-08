
"""
 * @author nhphung
"""
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import * 
from Visitor import *
from StaticError import *
from functools import *

class Type(ABC):
    __metaclass__ = ABCMeta
    pass
class Prim(Type):
    __metaclass__ = ABCMeta
    pass
class IntType(Prim):
    pass
class FloatType(Prim):
    pass
class StringType(Prim):
    pass
class BoolType(Prim):
    pass
class VoidType(Type):
    pass
class Unknown(Type):
    pass

@dataclass
class ArrayType(Type):
    dimen:List[int]
    eletype: Type

@dataclass
class MType:
    intype:List[Type]
    restype:Type

@dataclass
class Symbol:
    name: str
    mtype:Type

class StaticChecker(BaseVisitor):
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [
Symbol("int_of_float",MType([FloatType()],IntType())),
Symbol("float_of_int",MType([IntType()],FloatType())),
Symbol("int_of_string",MType([StringType()],IntType())),
Symbol("string_of_int",MType([IntType()],StringType())),
Symbol("float_of_string",MType([StringType()],FloatType())),
Symbol("string_of_float",MType([FloatType()],StringType())),
Symbol("bool_of_string",MType([StringType()],BoolType())),
Symbol("string_of_bool",MType([BoolType()],StringType())),
Symbol("read",MType([],StringType())),
Symbol("printLn",MType([],VoidType())),
Symbol("printStr",MType([StringType()],VoidType())),
Symbol("printStrLn",MType([StringType()],VoidType()))]                           
   
    def check(self):
        return self.visit(self.ast,self.global_envi)

    def visitProgram(self,ast, c):
        [self.visit(x,c) for x in ast.decl]

    








    # class Dowhile(Stmt):
    # sl:Tuple[List[VarDecl],List[Stmt]]
    # exp: Expr
    def visitDowhile(self, ast, c):
        try:
            expr = self.visit(ast.exp, (c[0], BoolType()))
        except TypeCannotBeInferred:
            raise TypeCannotBeInferred(ast)
        if type(expr) is not BoolType:
            raise TypeMismatchInStatement(ast)

        varLocal = []
        varLocal = reduce(lambda acc, x: self.visit(x, acc), ast.sl[0], varLocal)
        [self.visit(x, (varLocal + c[0], VoidType(), c[2])) for x in ast.sl[1]]

    # class For(Stmt):
    # idx1: Id
    # expr1:Expr
    # expr2:Expr boolType
    # idx2: Id
    # expr3:Expr
    # loop: Tuple[List[VarDecl],List[Stmt]]
    def visitFor(self, ast, c):
        try:
            e1 = self.visit(ast.idx1, (c[0], IntType()))
            e2 = self.visit(ast.expr1, (c[0], IntType()))
            e3 = self.visit(ast.expr2, (c[0], BoolType()))
            e4 = self.visit(ast.idx2, (c[0], IntType()))
            e5 = self.visit(ast.expr3, (c[0], IntType()))
        except TypeCannotBeInferred:
            raise TypeCannotBeInferred(ast)
        if type(e1) is not IntType:
            raise TypeMismatchInStatement(ast)

        if type(e2) is not IntType:
            raise TypeMismatchInStatement(ast)

        if type(e3) is not BoolType:
            raise TypeMismatchInStatement(ast)

        if type(e4) is not IntType:
            raise TypeMismatchInStatement(ast)

        if type(e5) is not IntType:
            raise TypeMismatchInStatement(ast)

        varLocal = []
        varLocal = reduce(lambda acc, x: self.visit(x, acc), ast.loop[0], varLocal)
        [self.visit(x, (varLocal + c[0], VoidType(), c[2])) for x in ast.loop[1]]


    # class Return(Stmt):
    # expr:Expr # None if no expression
    def visitReturn(self, ast, c):
        reType = VoidType() 

        if ast.expr:
            try:
                reType = self.visit(ast.expr, (c[0], Unknown()))
            except TypeCannotBeInferred:
                raise TypeCannotBeInferred(ast)

        if type(reType) is Unknown:
            raise TypeCannotBeInferred(ast)

        if type(c[2].mtype.restype) is Unknown:
            c[2].mtype.restype = reType

        if type(c[2].mtype.restype) is not type(reType):
            raise TypeMismatchInStatement(ast)


    def visitId(self, ast, c):
        idName = ast.name
        typeId = self.lookup(idName, c[0], lambda x: x.name)
        if typeId == None:
            raise Undeclared(Identifier(), idName)

        if type(typeId.mtype) is Unknown and type(c[1]) is not Unknown and type(c[1]) is not ArrayType:
            typeId.mtype = c[1]

        return typeId.mtype

    def visitIntLiteral(self, ast, c):
        return IntType()

    def visitFloatLiteral(self, ast, c):
        return FloatType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    def visitStringLiteral(self, ast, c):
        return StringType()





        
