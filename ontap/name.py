from functools import reduce
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o:object):
        o = [[],[]]
        [self.visit(x,o) for x in ctx.decl]
        
    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o[1]:
            raise RedeclaredVariable(ctx.name)
        o[1] += [ctx.name]
        if ctx.name not in o[0]:
            o[0] += [ctx.name]

    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name in o[1]:
            raise RedeclaredConstant(ctx.name)
        o[1] += [ctx.name]
        if ctx.name not in o[0]:
            o[0] += [ctx.name]
        
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if ctx.name in o[1]:
            raise RedeclaredFunction(ctx.name)
        o[1] += [ctx.name]
        if ctx.name not in o[0]:
            o[0] += [ctx.name]
        o1 = [o[0].copy(),[]]
        [self.visit(x,o1) for x in ctx.param + ctx.body[0]]
        [self.visit(x,o1[0]) for x in ctx.body[1]]

    def visitIntType(self,ctx:IntType,o:object):
        return IntType()

    def visitFloatType(self,ctx:FloatType,o:object):
        return FloatType()

    def visitIntLit(self,ctx:IntLit,o:object):
        return ctx.val
        
    def visitId(self,ctx:Id,o:object):
        if ctx.name not in o:
            raise UndeclaredIdentifier(ctx.name)





Program(
        [VarDecl("b",IntType())
        ,FuncDecl("a",
                [VarDecl("m",FloatType())
                ,VarDecl("b",IntType())
                ,VarDecl("d",FloatType())],

                ([ConstDecl("c",IntLit(3))
                ,FuncDecl("foo",
                        [VarDecl("x",IntType())]
                        ,([VarDecl("y",IntType()),
                            VarDecl("z",IntType())]
                        ,[Id("y"),Id("x"),Id("foo"),Id("c"),Id("m"),Id("a")])
                )
                ],
                [Id("foo"),Id("d"),Id("z")])
        )])




from functools import reduce
class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o:object):
        o = ({},{})
        [self.visit(x,o) for x in ctx.decl]
        
    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o[1]:
            raise RedeclaredVariable(ctx.name)
        o[1][ctx.name] = ctx.name
        if ctx.name not in o[0]:
            o[0][ctx.name] = ctx.name

    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name in o[1]:
            raise RedeclaredConstant(ctx.name)
        o[1][ctx.name] = ctx.name
        if ctx.name not in o[0]:
            o[0][ctx.name] = ctx.name
        
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if ctx.name in o[1]:
            raise RedeclaredFunction(ctx.name)
        o[1][ctx.name] = ctx.name
        if ctx.name not in o[0]:
            o[0][ctx.name] = ctx.name
        o2 = o[0]
        o1 = (o2,{})
        [self.visit(x,o1) for x in ctx.param + ctx.body[0]]
        print(o)
        [self.visit(x,o[0]) for x in ctx.body[1]]

    def visitIntType(self,ctx:IntType,o:object):
        return IntType()

    def visitFloatType(self,ctx:FloatType,o:object):
        return FloatType()

    def visitIntLit(self,ctx:IntLit,o:object):
        return ctx.val
        
    def visitId(self,ctx:Id,o:object):
        if ctx.name not in o:
            raise UndeclaredIdentifier(ctx.name)