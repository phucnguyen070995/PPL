
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

@dataclass
class cVariable:
    local: List[Symbol]
    isVariable: bool = True
    nonLocal: List[Symbol] = None


@dataclass
class cExp:
    local: List[Symbol]
    nonLocal: List[Symbol]
    isFunction: bool = False
    inferType: Type = Unknown()
    callStmt: Stmt = None


@dataclass
class cStmt:
    nonLocal: List[Symbol]
    currentFunc: Symbol


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

    # def visitProgram(self,ast, c):
    #     [self.visit(x,c) for x in ast.decl]
    def lookup(self,name,lst,func):
        for x in lst:
            if name == func(x):
                return x
        return None

    def visitProgram(self, ast: Program, c):

        # check redeclare in global, get all symbol
        for decl in ast.decl:
            if type(decl) is VarDecl:
                c.append(self.visit(decl, cVariable(c, True)))
            else:
                if self.lookup(decl.name.name, c, lambda x: x.name) is not None:
                    raise Redeclared(Function(), decl.name.name)
                param_list = [self.visit(varDecl, cVariable([], False, [])) for varDecl in
                              decl.param]  # list Symbol, not check Redeclare
                c.append(Symbol(decl.name.name, MType([sym.mtype for sym in param_list], Unknown())))

        for decl in ast.decl:
            if type(decl) is FuncDecl:
                self.visit(decl, c)
        #check main function
        #globl_env = reduce(lambda x,y: x + [self.visit(y,x)], ast.decl, StaticChecker.global_envi) #create global enviroment, check name only
        globl_env = [self.visit(x,c) for x in ast.decl]+ StaticChecker.global_envi
        mainFunc = self.lookup("main", filter(lambda x: type(x.mtype) == MType, globl_env), lambda x: x.name)
        if mainFunc is None:
             raise NoEntryPoint()

    def visitVarDecl(self, ast: VarDecl, c: cVariable):
        if self.lookup(ast.variable.name, c.local, lambda x: x.name) is not None:
            raise Redeclared(Variable() if c.isVariable else Parameter(), ast.variable.name)
        if len(ast.varDimen) > 0:  # array type
            if type(ast.varInit) is ArrayType:

                return Symbol(ast.variable.name,
                          ArrayType(ast.varDimen, self.visit(ast.varInit, c) if ast.varInit else Unknown()))
        else:  # prim type
            return Symbol(ast.variable.name, self.visit(ast.varInit, c) if ast.varInit else Unknown())


    def visitFuncDecl(self, ast: FuncDecl, c):  # c: global_envi
        local = []  # env: new list
        for param in ast.param:
            local.append(self.visit(param, cVariable(local, False, c)))
        for decl in ast.body[0]:  # list VarDecl
            local.append(self.visit(decl, cVariable(local, True, c)))

        currentFunc = self.lookup(ast.name.name, self.global_envi, lambda x: x.name)
        for stmt in ast.body[1]:
            print(1)
            self.visit(stmt, cStmt(local + c, currentFunc))

    def visitIf(self, ast: If, c: cStmt):
        for tup in ast.ifthenStmt:
            if type(self.visit(tup[0], cExp([], c.nonLocal, inferType=BoolType(), callStmt=ast))) is not BoolType:
                raise TypeMismatchInStatement(ast)
            local = []
            for decl in tup[1]:  # List[VarDecl]
                local.append(self.visit(decl, cVariable(local, True, c.nonLocal)))
            for stmt in tup[2]:
                self.visit(stmt, cStmt(local + c.nonLocal, c.currentFunc))  # visit Stmt

        tup = ast.elseStmt
        if tup:
            local = []
            for decl in tup[0]:
                local.append(self.visit(decl, cVariable(local, True, c.nonLocal)))
            for stmt in tup[1]:
                self.visit(stmt, cStmt(local + c.nonLocal, c.currentFunc))  # visit Stmt

    def visitFor(self, ast: For, c: cStmt):
        exp1 = self.visit(ast.expr1, cExp([], c.nonLocal, inferType=IntType(), callStmt=ast))
        exp2 = self.visit(ast.expr2, cExp([], c.nonLocal, inferType=BoolType(), callStmt=ast))
        exp3 = self.visit(ast.expr3, cExp([], c.nonLocal, inferType=IntType(), callStmt=ast))

        if type(exp1) is not IntType or type(exp2) is not BoolType or type(exp3) is not IntType:
            raise TypeMismatchInStatement(ast)

        idx1 = self.visit(ast.idx1, cExp([], c.nonLocal, False, inferType=IntType(), callStmt=ast))
        #idx2 = self.visit(ast.idx2, cExp([], c.nonLocal, False, inferType=IntType(), callStmt=ast))
        #####
        if type(idx1) is not IntType : #or type(idx2) is not IntType:
            raise TypeMismatchInStatement(ast)
        local = []
        for decl in ast.loop[0]:
            local.append(self.visit(decl, cVariable(local, True, c.nonLocal)))
        for stmt in ast.loop[1]:
            self.visit(stmt, cStmt(local + c.nonLocal, c.currentFunc))


    def visitDowhile(self, ast: Dowhile, c: cStmt):
        exp = self.visit(ast.exp, cExp([], c.nonLocal, inferType=BoolType(), callStmt=ast))
        if type(exp) is not BoolType:
            raise TypeMismatchInStatement(ast)

        local = []
        for decl in ast.sl[0]:
            local.append(self.visit(decl, cVariable(local, True, c.nonLocal)))
        for stmt in ast.sl[1]:
            self.visit(stmt, cStmt(local + c.nonLocal, c.currentFunc))

    def visitWhile(self, ast: While, c: cStmt):
        exp = self.visit(ast.exp, cExp([], c.nonLocal, inferType=BoolType(), callStmt=ast))
        if type(exp) is not BoolType:
            raise TypeMismatchInStatement(ast)

        local = []
        for decl in ast.sl[0]:
            local.append(self.visit(decl, cVariable(local, True, c.nonLocal)))
        for stmt in ast.sl[1]:
            self.visit(stmt, cStmt(local + c.nonLocal, c.currentFunc))

    def visitAssign(self, ast: Assign, c: cStmt):
        try:
            # infer from rhs to lhs
            rhs = self.visit(ast.rhs, cExp([], c.nonLocal, False, callStmt=ast))
            lhs = self.visit(ast.lhs, cExp([], c.nonLocal, False, inferType=rhs, callStmt=ast))

        except TypeCannotBeInferred:
            # if rhs cannot be resolved, infer from lhs to rhs
            lhs = self.visit(ast.lhs, cExp([], c.nonLocal, False, callStmt=ast))
            rhs = self.visit(ast.rhs, cExp([], c.nonLocal, False, inferType=lhs, callStmt=ast))

        if type(rhs) is VoidType:
            raise TypeMismatchInStatement(ast)
        if type(lhs) is VoidType or type(lhs) is not type(rhs):
            raise TypeMismatchInStatement(ast)

    def visitCallStmt(self, ast: CallStmt, c: cStmt):
        print(2)
        method = self.visit(ast.method,
                            cExp([], c.nonLocal, isFunction=True, inferType=VoidType(), callStmt=ast))  # MType
        # elif type(method.restype) is not VoidType:
        #     raise TypeMismatchInStatement(ast)
        if len(ast.param) != len(method.intype):
            raise TypeMismatchInStatement(ast)

        for i in range(len(ast.param)):  # check type param
            declarationParam = method.intype[i]
            actualParam = self.visit(ast.param[i], cExp([], c.nonLocal, False, inferType=declarationParam, callStmt=ast))
            if type(declarationParam) is Unknown:
                method.intype[i] = actualParam
            elif type(actualParam) is not type(declarationParam):
                raise TypeMismatchInStatement(ast)

    def visitReturn(self, ast: Return, c: cStmt):
        resType = c.currentFunc.mtype.restype
        if ast.expr:  # return with Exp
            if type(resType) is VoidType:
                raise TypeMismatchInStatement(ast)
            exp = self.visit(ast.expr, cExp([], c.nonLocal, False, resType, ast))  # return Exp
            if type(resType) is Unknown:
                c.currentFunc.mtype.restype = exp
            elif type(exp) is not type(resType):
                raise TypeMismatchInStatement(ast)
        else:  # return with no Exp
            if type(resType) is Unknown:
                c.currentFunc.mtype.restype = VoidType()
            elif type(resType) is not VoidType:
                raise TypeMismatchInStatement(ast)

    def visitBreak(self, ast: Break, c: cExp):
        pass

    def visitContinue(self, ast:Continue, c:cExp):
        pass

    def visitArrayCell(self, ast: ArrayCell, c: cExp):
        arr = self.visit(ast.arr, cExp(c.local, c.nonLocal, inferType=c.inferType, callStmt=c.callStmt))  # arr -> ArrayType
        if type(arr) is not ArrayType or len(ast.idx) != len(arr.dimen):
            raise TypeMismatchInExpression(ast)

        idx_list = [self.visit(idx, cExp(c.local, c.nonLocal, False, IntType())) for idx in ast.idx] # ast.indx : List[Exp] -> List[Type]
        if not all([type(x) is IntType for x in idx_list]):
            raise TypeMismatchInExpression(ast)
        return arr.eletype

    def visitId(self, ast: Id, c: cExp):
        symbol = self.lookup(ast.name, c.local, lambda x: x.name)
        if symbol is None:  # find in local -> not found -> find in nonLocal
            symbol = self.lookup(ast.name, c.nonLocal, lambda x: x.name)
            if symbol is None:  # not found in nonLocal -> raise Exception
                raise Undeclared(Function() if c.isFunction else Identifier(), ast.name)
        # find a Symbol, but not a function for Call Stmt/Func
        if c.isFunction and type(symbol.mtype) is not MType:
            raise Undeclared(Function(), ast.name)

        if type(symbol.mtype) is Unknown:
            if type(c.inferType) is Unknown:
                raise TypeCannotBeInferred(c.callStmt)
            symbol.mtype = c.inferType
        elif type(symbol.mtype) is ArrayType and type(symbol.mtype.eletype) is Unknown:
            if type(c.inferType)is Unknown:
                raise TypeCannotBeInferred(c.callStmt)
            symbol.mtype.eletype = c.inferType
        elif type(symbol.mtype) is MType and type(symbol.mtype.restype) is Unknown:
            if type(c.inferType) is Unknown:
                raise TypeCannotBeInferred(c.callStmt)
            symbol.mtype.restype = c.inferType

        return symbol.mtype


    def visitCallExpr(self, ast: CallExpr, c: cExp):
        print(3)
        print('-------------')
        print(c)
        print('------------------------')
        method = self.visit(ast.method, cExp(c.local, c.nonLocal, isFunction=True, inferType=c.inferType))  # MType -> declaration
        if type(method) is Unknown:
            method.restype = c.inferType

        if len(method.intype) != len(ast.param):
            raise TypeMismatchInExpression(ast)

        for i in range(len(ast.param)):
            declarationType = method.intype[i]
            actualType = self.visit(ast.param[i], cExp(c.local, c.nonLocal, inferType=declarationType, callStmt=c.callStmt))
            if type(declarationType) is Unknown:
                method.intype[i] = actualType
            elif type(declarationType) is not type(actualType):
                raise TypeMismatchInExpression(ast)
        return method.restype


    def visitBinaryOp(self, ast: BinaryOp, c: cExp):
        typ = IntType() if ast.op in ('-', '+', '*', '\\', '%', '==', '!=', '<', '>', '<=', '>=') \
            else FloatType() if ast.op in ('-.', '+.', '*.', '\\.', '=/=', '<.', '>.', '<=.', '>=.') \
            else BoolType() 
        left = self.visit(ast.left, cExp(local=c.local, nonLocal=c.nonLocal, isFunction=False, inferType=typ,
                                         callStmt=c.callStmt))
        right = self.visit(ast.right, cExp(local=c.local, nonLocal=c.nonLocal, isFunction=False, inferType=typ,
                                           callStmt=c.callStmt))
        if type(typ) is not type(left) or type(typ) is not type(right):
            raise TypeMismatchInExpression(ast)

        return BoolType() if ast.op in ('==', '!=', '<', '>', '<=', '>=', '<.', '>.', '<=.', '>=.') else typ


    def visitUnaryOp(self, ast: UnaryOp, c: cExp):
        typ = IntType() if ast.op == '-' else FloatType() if ast.op == '-.' else BoolType() 
        body = self.visit(ast.body, cExp(local=c.local, nonLocal=c.nonLocal, isFunction=False, inferType=typ,
                                         callStmt=c.callStmt))
        if type(typ) is not type(body):
            raise TypeMismatchInExpression(ast)

        return typ

    # int, string, .....
    def visitFloatLiteral(self, ast, c):
        return FloatType()

    def visitIntLiteral(self, ast, c):
        return IntType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    def visitStringLiteral(self, ast, c):
        return StringType()


    def visitArrayLiteral(self, ast, c):
        pass


        
    # def checkArrLit(self,arr1, arr2):
    #     if type(arr1) == type(arr2):
    #         if type(arr1) != ArrayType :
    #             return True
    #         if len(arr1.dimen) == len(arr2.dimen) :
    #             for i in range(len(arr1.dimen)):
    #                 if (arr1.dimen[i])!= (arr2.dimen[i]):
    #                     return False
    #         if (type(arr1.eletype) == type(arr2.eletype)) :
    #             return True
    #     return False
    # def visitArrayLiteral(self, ast, c):
    #     lit =ast.value
    #     eletype = [self.visit(x,c).mtype for x in lit]
    #     checkSame = all(self.checkArrLit(eletype[0],x) for x in eletype)
    #     if checkSame is False :
    #         raise TypeMismatchInExpression(ast)
    #     mtype= ArrayType([len(lit)] ,eletype[0].mtype.eletype if type(eletype[0])== ArrayType else eletype[0] )
    #     if type(eletype[0])== ArrayType:
    #         mtype.dimen+=eletype[0].dimen 
        
    #     return Symbol(None,mtype)