#Cau 1
from functools import reduce
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o:object): 
        reduce(lambda acc,x: acc+ self.visit(x,acc), ctx.decl,[])
        
        
    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o:
            raise RedeclaredDeclaration(ctx.name)
        return [ctx.name]

    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name in o:
            raise RedeclaredDeclaration(ctx.name)
        return [ctx.name]

    def visitIntType(self,ctx:IntType,o:object):
        return IntType()

    def visitFloatType(self,ctx:FloatType,o:object):
        return FloatType()

    def visitIntLit(self,ctx:IntLit,o:object):
        return ctx.val

#Cau 2
from functools import reduce
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o:object): 
        reduce(lambda acc,x: acc+ self.visit(x,acc), ctx.decl,[])
        
        
    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o:
            raise RedeclaredVariable(ctx.name)
        return [ctx.name]

    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name in o:
            raise RedeclaredConstant(ctx.name)
        return [ctx.name]

    def visitIntType(self,ctx:IntType,o:object):
        return IntType()

    def visitFloatType(self,ctx:FloatType,o:object):
        return FloatType()

    def visitIntLit(self,ctx:IntLit,o:object):
        return ctx.val

#Cau 3
from functools import reduce
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o:object): 
        reduce(lambda acc,x: acc+ self.visit(x,acc), ctx.decl,[])
        
        
    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o:
            raise RedeclaredVariable(ctx.name)
        return [ctx.name]

    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name in o:
            raise RedeclaredConstant(ctx.name)
        return [ctx.name]
        
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if ctx.name in o:
            raise RedeclaredFunction(ctx.name)
        reduce(lambda acc,x: acc+ self.visit(x,acc), ctx.param+ctx.body,[])
        return [ctx.name]
        

    def visitIntType(self,ctx:IntType,o:object):
        return IntType()

    def visitFloatType(self,ctx:FloatType,o:object):
        return FloatType()

    def visitIntLit(self,ctx:IntLit,o:object):
        return ctx.val
#Cau 4
from functools import reduce
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o:object): 
        var_cons_list = [x for x in ctx.decl if type(x) is not FuncDecl]
        var_cons_name = reduce(lambda acc,x: acc+ self.visit(x,acc), var_cons_list,[])

        func_list = [x for x in ctx.decl if type(x) is FuncDecl]
        func_name = [self.visit(x,0) for x in func_list]
        names = var_cons_name + func_name

        dict = {}
        for name in names:
            if name in dict:
                raise RedeclaredFunction(name)
            dict[name] = 1
        
        o = list(set(names + o))
        [self.visit(x,o) for x in func_list]
        
    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o:
            raise RedeclaredVariable(ctx.name)
        return [ctx.name]

    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name in o:
            raise RedeclaredConstant(ctx.name)
        return [ctx.name]
        
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if o == 0:
            return ctx.name
        var_cons_list = ctx.param + [x for x in ctx.body[0] if type(x) is not FuncDecl]
        var_cons_name = reduce(lambda acc,x: acc+ self.visit(x,acc), var_cons_list,[])

        func_list = [x for x in ctx.body[0] if type(x) is FuncDecl]
        func_name = [self.visit(x,0) for x in func_list]
        names = var_cons_name + func_name

        dict = {}
        for name in names:
            if name in dict:
                raise RedeclaredFunction(name)
            dict[name] = 1
        o = list(set(names + o))
        [self.visit(x,o) for x in ctx.body[1]]
        
        [self.visit(x,o) for x in func_list]
        return [ctx.name]
        
        

    def visitIntType(self,ctx:IntType,o:object):
        return IntType()

    def visitFloatType(self,ctx:FloatType,o:object):
        return FloatType()

    def visitIntLit(self,ctx:IntLit,o:object):
        return ctx.val
        
    def visitId(self,ctx:Id,o:object):
        if ctx.name not in o:
            raise UndeclaredIdentifier(ctx.name)
        return ctx.name


#Cau 4 (cach 2)
from functools import reduce
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o:object): 
        reduce(lambda acc,x: (acc[0] + self.visit(x,acc),acc[1] + self.visit(x,acc)), ctx.decl, ([],[]) )
        
        
    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o[0]:
            raise RedeclaredVariable(ctx.name)
        else:
            return [ctx.name]

    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name in o[0]:
            raise RedeclaredConstant(ctx.name)
        else:
            return [ctx.name]
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if ctx.name in o[0]:
            raise RedeclaredFunction(ctx.name)
        else:
            acc=  reduce(lambda acc,x: (acc[0]+ self.visit(x,acc),acc[1]+ self.visit(x,acc)), ctx.param+ctx.body[0], ([],[ctx.name]+o[1]))
            temp = [self.visit(x,acc[1]) for x in ctx.body[1]]
            return [ctx.name]

    def visitIntType(self,ctx:IntType,o:object):
        return IntType()

    def visitFloatType(self,ctx:FloatType,o:object):
        return FloatType()

    def visitIntLit(self,ctx:IntLit,o:object):
        return ctx.val
        
    def visitId(self,ctx:Id,o:object):
        if ctx.name in o:
            return ctx.name
        else:
            raise UndeclaredIdentifier(ctx.name)