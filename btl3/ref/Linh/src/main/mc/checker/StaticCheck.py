
"""
 * @author Nguyen Van Hoai Linh - ID: 1710169
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype
        self.isInvoked = False
    def accept(self,v,param):
        return v.visitMType(self,param)

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name  = name
        self.mtype = mtype
        self.value = value


class StaticChecker(BaseVisitor,Utils):

    global_envi = [
    Symbol("getInt",  MType([]          ,IntType())),
    Symbol("putIntLn",MType([IntType()] ,VoidType())), 
    Symbol("putInt",  MType([IntType()] ,VoidType())),
    Symbol("getFloat",MType([]         ,FloatType())),
    Symbol('putFloat',MType([FloatType()],VoidType())), 
    Symbol('putFloatLn',MType([FloatType()],VoidType())), 
    Symbol('putBool', MType([BoolType()],VoidType())), 
    Symbol('putBoolLn', MType([BoolType()],VoidType())),
    Symbol('putString', MType([StringType()], VoidType())), 
    Symbol('putStringLn', MType([StringType()], VoidType())), 
    Symbol('putLn', MType([], VoidType()))
    ]

    
    def lst(self,l): 
        a = []
        for x in l: 
            a += [[i.name for i in x ]]
        print(a)
    def lst_global(self,l):
        print([x.name for x in l[len(l)-1]])
    def flatten(self, l): 
        return [i for x in l for i in x ]
    def __init__(self,ast):
        
        #print(ast)
        #print()
        self.ast = ast
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast, c): 
        # Get All Global Name 
        global_e = []
        for x in ast.decl: 
            if (type(x) is VarDecl): 
                if self.lookup(x.variable, StaticChecker.global_envi + global_e, lambda x: x.name): 
                    raise Redeclared(Variable(), x.variable)
                else: 
                    global_e+= [Symbol(x.variable, x.varType)]
            else: 
                if self.lookup(x.name.name, StaticChecker.global_envi + global_e, lambda x: x.name): 
                    raise Redeclared(Function(), x.name.name)
                global_e+= [Symbol(x.name.name, MType([y.varType for y in x.param], x.returnType))]
        #self.lst([StaticChecker.global_envi + global_e] )
        # No Entry Point 
        name = [x.name for x in StaticChecker.global_envi + global_e if type(x.mtype) is MType]
        if "main" not in name: raise NoEntryPoint()
        lstFunc = []
        for x in ast.decl: 
            if (type(x) is FuncDecl): 
                lstFunc +=[ self.visit(x, ([StaticChecker.global_envi + global_e], True)) ]
        # UnreachableFunction                
        a = [ [i.mtype.isInvoked for i in x]for x in lstFunc]
        b = reduce (lambda x,y: [x[i] or y[i] for i in range(len(x))], a)
        if False in b: 
            raise UnreachableFunction(lstFunc[0][b.index(False)].name)
        return StaticChecker.global_envi


    def visitFuncDecl(self,ast, c): 
        returnType = self.visit(ast.returnType,True)
        # Redeclared Parameter
        try: 
            paramLst = reduce(lambda x, y: [x[0]+ self.visit(y, (x,True ))], ast.param,[[]])
        except Redeclared as e: 
            raise Redeclared(Parameter(), e.n)

        # GotoBlock
        #a = reduce(lambda x,y: [x[0] + self.visitMember(y,x),x[1]] ,ast.body.member, paramLst+ [c[0]])
        # use for check type Return  
        lstCheck = [returnType, 0, "NoUseForAnything", "callExprNotFound", 
                    Symbol(ast.name.name, MType([y.varType for y in ast.param], ast.returnType))
                    ]
        checkReturn =0
        d = c[0]
        x = paramLst + [d[0]]
        for y in ast.body.member: 
            temp = self.visit(y,(x, lstCheck ))
            if type(y) is If or type(y) is Dowhile or type(y) is Return or type(y) is Block: 
                checkReturn = checkReturn or temp
            if type(y) is not VarDecl: temp = []
            x = [x[0]+temp] +d
        if type(returnType) is not VoidType:
            if checkReturn==0: 
                raise FunctionNotReturn(ast.name.name)
        a = list(filter(lambda x: type(x.mtype) is  MType and x.name != 'main', d[0][11:]))
        return a
    def visitVarDecl(self, ast, c): 
        d = c[0]
        if self.lookup(ast.variable, d[0], lambda x: x.name ): 
            raise Redeclared(Variable(), ast.variable)
        
        return [Symbol(ast.variable, ast.varType)]
    ############ BLOCK ##############
    
    
    def visitBlock(self, ast,c): 
        checkReturn = 0
        d = c[0]
        x = [[]]+ d
        for y in ast.member:
            temp = self.visit(y,(x, c[1]))
            if type(y) is If or type(y) is Dowhile or type(y) is Return or type(y) is Block: 
                checkReturn = checkReturn or temp
            if type(y) is not VarDecl: temp = []
            x = [x[0] + temp]+d
        
        return checkReturn

    ############ visitStmt ##########
    def visitIf(self, ast,c): 
        # Initialized 
        thenStmt = 0; elseStmt = 0;
        expr = self.visit(ast.expr,c)
        if(type(expr) is not BoolType):
            raise TypeMismatchInStatement(ast)
        thenStmt = self.visit(ast.thenStmt,c)
        if ast.elseStmt is not None:
            elseStmt = self.visit(ast.elseStmt,c)  
        else: 
            return 0
            
        
        if (type(thenStmt) is int and type(elseStmt) is int):
            return thenStmt * elseStmt
        else: return 0

    def visitFor(self, ast, c):
        expr1 = self.visit(ast.expr1,c)
        expr2 = self.visit(ast.expr2,c)
        expr3 = self.visit(ast.expr3,c)
        (c[1])[1] += 1
        loop  = self.visit(ast.loop, c)
        (c[1])[1] -= 1
        if not (type(expr1) is IntType and type(expr2) is BoolType and type(expr3) is IntType): 
            raise TypeMismatchInStatement(ast)
        return 0
    def visitDowhile(self, ast,c): 
        checkReturn = 0 
        exp = self.visit(ast.exp, c)
        if not (type(exp) is BoolType): 
            raise TypeMismatchInStatement(ast)
        (c[1])[1] +=1
        for x in ast.sl: 
            temp = self.visit(x,c)
            if type(x) is If or type(x) is Dowhile or type(x) is Return or type(x) is Block:
                checkReturn  = checkReturn or temp
        (c[1])[1] -=1
            
        return checkReturn
    def visitBreak(self, ast,c): 
        if (c[1])[1] == 0:
            raise BreakNotInLoop()
    def visitContinue(self, ast,c): 
        if (c[1])[1] == 0:
            raise ContinueNotInLoop()
    def visitReturn(self, ast,c):
        functionType = (c[1])[0]
        returnType = self.visit(ast.expr,c) if ast.expr is not None else None
        if (type(functionType) is VoidType): 
            if( returnType is not None): 
                raise TypeMismatchInStatement(ast)
        else:
            left = functionType; right = returnType
            #print(left)
            if type(left) in [IntType, BoolType, StringType]: 
                if not type(left) is type(right): 
                    raise TypeMismatchInStatement(ast)
            elif type(left) is FloatType: 
                if not type(right) in [FloatType, IntType]:
                    raise TypeMismatchInStatement(ast)
            elif type(left) is ArrayPointerType: 
                if not type(right) in [ArrayPointerType, ArrayType]: 
                    raise TypeMismatchInStatement(ast)
                elif not (type(self.visit(left.eleType,c)) is type(self.visit(right.eleType,c))):
                    raise TypeMismatchInStatement(ast)     
        
        return 1
    ########### _end_visitStmt_ #####
    ########### visitExpr ###########
    # def visit LHS
    def visitId(self, ast,c): 
        a = (list(filter(lambda x: x.name == ast.name, self.flatten(c[0]))))
        if a == []: 
            if c[1][3] =="callExprFound":
                raise Undeclared( Function(), ast.name)
            else: raise Undeclared( Identifier(), ast.name)
        else: 
            if c[1][3] =="callExprFound":
                if a[0].name != c[1][4].name :
                    a[0].mtype.isInvoked = True;
            return self.visit(a[0].mtype,c)
    def visitArrayCell(self, ast,c):
        E1 = (self.visit(ast.arr,c))
        E2 = (self.visit(ast.idx,c))
        cond1 = (type(E1) is ArrayType or type(E1)  is ArrayPointerType)         
        cond2 = type(E2) is IntType
        if not (cond1 and cond2): 
            raise TypeMismatchInExpression(ast)
        return E1.eleType
    def visitMType(self,ast,c):
        return ast
    # def visitLiteral
    

    def visitCallExpr(self, ast, c): 
        c[1][3] = "callExprFound"
        method = self.visit(ast.method,c) # inside method has info of function
        if (type(method) is not MType): 
            raise TypeMismatchInExpression(ast) 
        formalPar = method.partype
        c[1][3] = "callExprNotFound"
        param = [self.visit(x,c) for x in ast.param]
        if len(formalPar) != len(param): 
            raise TypeMismatchInExpression(ast)
        elif len(param)!=0 : 
            for i in range(len(param)): 
                left = formalPar[i]; right = param[i]
                if type(left) in [IntType, BoolType, StringType]: 
                    if type(left) is not type(right): 
                        raise TypeMismatchInExpression(ast)
                elif type(left) is FloatType: 
                    if not type(right) in [FloatType, IntType]:
                        raise TypeMismatchInExpression(ast)
                elif type(left) is ArrayPointerType: 
                    if not type(right) in [ArrayPointerType, ArrayType]:
                        raise TypeMismatchInExpression(ast)
                    elif not (type(self.visit(left.eleType,c)) is type(self.visit(right.eleType,c))):
                        raise TypeMismatchInExpression(ast)
        return method.rettype
    def visitBinaryOp(self, ast,c): 
        op = ast.op
        left = self.visit(ast.left, c)
        right = self.visit(ast.right, c)
        if op in ["+", "-", "*", "/"]: 
            if type(left) in [IntType, FloatType] and type(right) in [IntType, FloatType]:
                if(type(left) is FloatType or type(right) is FloatType): 
                    return FloatType()
                else: return IntType()
            else: raise TypeMismatchInExpression(ast)
        if op is "%": 
            if type(left) is IntType and type(right) is IntType: 
                return IntType()
            else: raise TypeMismatchInExpression(ast) 
        if op in ["<", "<=", ">", ">="]: 
            if (type(left) in [IntType, FloatType] and type(right) in [IntType, FloatType]):
                return BoolType()
            else: raise TypeMismatchInExpression(ast)
        if op in ["==", "!="]:
            if type(left) is type(right) and type(left) in [IntType, BoolType]:
                return BoolType()
            else: raise TypeMismatchInExpression(ast)
        if op in ["&&" , "||"]: 
            if type(left) is BoolType and type(right) is BoolType: 
                return BoolType()
            else: raise TypeMismatchInExpression(ast)
        if op is "=": 
            # if type(left)  not in [IntType, FloatType, StringType, BoolType, MType]: 
            #     raise TypeMismatchInExpression(ast)

            # if type(ast.left) not in [Id, ArrayCell]:
            #     raise NotLeftValue(ast.left)
            # elif type(left) not in [BoolType, IntType, FloatType, StringType, MType]:
            #     raise NotLeftValue(ast.left)
            
            # if type(left) in [IntType, BoolType, StringType]:
            #     if type(left) is not type(right):
            #         raise TypeMismatchInExpression(ast)
            #     else:  return type(left)()
            # elif type(left) is FloatType: 
            #     if not type(right) in [FloatType, IntType]:
            #         raise TypeMismatchInExpression(ast)
            #     else:  return type(left)()
            if type(ast.left) not in [Id, ArrayCell]:
                raise NotLeftValue(ast.left)

            if type(left) in [VoidType, ArrayPointerType, ArrayType, MType]: 
                raise TypeMismatchInExpression(ast)
            else: 
                if type(left) in [IntType, BoolType, StringType]:
                    if type(right) is not type(left):
                        raise TypeMismatchInExpression(ast)
                    else: return type(left)() 
                elif type(left) is FloatType: 
                    if not type(right) in [FloatType, IntType]:
                        raise TypeMismatchInExpression(ast)
                    else: return FloatType()
            
            
            

    def visitUnaryOp(self, ast, c): 
        op = ast.op
        body = self.visit(ast.body,c)
        if op is "-" : 
            if type(body) in [IntType, FloatType]: 
                return type(body)()
            else: raise TypeMismatchInExpression(ast)
        if op is "!": 
            if type(body) is BoolType: 
                return BoolType()
            else: raise TypeMismatchInExpression(ast)
    ########### end_visitExpr #######


    ############ TYPE ###############
    def visitIntLiteral(self, ast,c): 
        return IntType()
    def visitFloatLiteral(self, ast, c): 
        return FloatType()
    def visitStringLiteral(self, ast, c) : 
        return StringType()
    def visitBooleanLiteral(self, ast, c): 
        return BoolType()
    def visitIntType(self, ast,c): 
        return IntType()
    def visitBoolType(self, ast,c): 
        return BoolType()
    def visitFloatType(self, ast, c): 
        return FloatType()
    def visitStringType(self, ast, c) : 
        return StringType()
    def visitVoidType(self,ast,c):
        return VoidType()
    def visitArrayPointerType(self, ast,c):
        return ArrayPointerType(self.visit(ast.eleType,c))
    def visitArrayType(self, ast,c): 
        #return ArrayType(ast.dimen, self.visit(ast.eleType, c))
        return ArrayPointerType(self.visit(ast.eleType,c))        
    #################################

