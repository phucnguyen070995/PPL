class StaticCheck(Visitor):
    def visitProgram(self,ctx:Program,o):
        o = [{}, {}]
        vardecl = [self.visit(x,o) for x in ctx.decl]
        stmt = [self.visit(x,o) for x in ctx.stmts]

    def visitVarDecl(self,ctx:VarDecl,o):
        if ctx.name in o[0]:
            raise Redeclared(ctx)
        o[0][ctx.name] = ctx.name
        if ctx.name not in o[1]:
            o[1][ctx.name] = ctx.name

    def visitFuncDecl(self,ctx:FuncDecl,o):
        if ctx.name in o[0]:
            raise Redeclared(ctx)
        o1 = [{},{}]
        env = [self.visit(x,o1) for x in ctx.param]
        dict_param = {}
        for i in range(len(o1[0])):
            dict_param[i] = o1[0][ctx.name][i]
        o[0][ctx.name] = dict_param
        if ctx.name not in o[1]:
            o[1][ctx.name] = dict_param

        for keys, values in o[1].items():
            if keys not in o1[1]:
                o1[1][keys] = values
        
        env2 = [self.visit(x,o1) for x in ctx.local]
        stmt = [self.visit(x,o1) for x in ctx.local]
        for keys, values in o1[1].items():
            if keys in o and o[keys] == keys:
                o[0][keys] = values

    def visitCallStmt(self,ctx:CallStmt,o):
        if ctx.name not in o[1]:
            raise UndeclaredIdentifier(ctx.name)
        elif len(ctx.args) != len(o[0][ctx.name]):
            raise TypeMismatchInStatement(ctx)

        for i in range(len(ctx.args)):
            if o[0][ctx.name][i] not in ['int', 'float', 'bool']:
                o[0][ctx.name][i] = self.visit(ctx.args[i],o[0])
            elif o[0][ctx.name][i] != self.visit(ctx.args[i],o[0]):
                raise TypeMismatchInStatement(ctx)

    def visitAssign(self,ctx:Assign,o):
        rtype = self.visit(ctx.rhs,o[1])
        ltype = self.visit(ctx.lhs,o[1])
        if ltype not in ['int', 'float', 'bool']:
            if rtype not in ['int', 'float', 'bool']:
                raise TypeCannotBeInferred(ctx)
            o[ltype] = rtype
            ltype = rtype
        if rtype not in ['int', 'float', 'bool']:
            o[rtype] = ltype
            rtype = ltype
        if ltype != rtype:
            raise TypeMismatchInStatement(ctx)

    def visitIntLit(self,ctx:IntLit,o):
        return 'int'
        
    def visitFloatLit(self,ctx,o):
        return 'float'
        
    def visitBoolLit(self,ctx,o):
        return 'bool'
        
    def visitId(self,ctx,o):
        if ctx.name in o:
            return o[ctx.name]
        raise UndeclaredIdentifier(ctx.name)