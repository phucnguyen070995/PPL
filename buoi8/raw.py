class StaticCheck(Visitor):
    def visitProgram(self,ctx:Program,o):
        o = [{}, {}]
        vardecl = [self.visit(x,o) for x in ctx.decl]
        stmt = [self.visit(x,o) for x in ctx.stmts]

    def visitVarDecl(self,ctx:VarDecl,o):
        if ctx.name in o[0]:
            raise Redeclared(ctx)
        o[0][ctx.name] = ctx.name
        o[1][ctx.name] = ctx.name

    def visitFuncDecl(self,ctx:FuncDecl,o):
        if ctx.name in o[0]:
            raise Redeclared(ctx)
        o1 = [{},{}]
        env = [self.visit(x,o1) for x in ctx.param]
        dict_param = {}
        i = 0
        for values in o1[1].values():
            dict_param[i] = values
            i += 1
        o[0][ctx.name] = dict_param
        o[1][ctx.name] = dict_param

        for keys, values in o[1].items():
            if keys not in o1[1]:
                o1[1][keys] = values
        
        env2 = [self.visit(x,o1) for x in ctx.local]
        stmt = [self.visit(x,o1) for x in ctx.stmts]
        
        for keys, values in o1[1].items():
            if keys in o[0] and keys not in o1[0] and o[0][keys] == keys:
                o[0][keys] = values
                o[1][keys] = values
            elif keys in o[0] and type(values) == dict:
                o[0][keys] = values
                o[1][keys] = values

    def visitCallStmt(self,ctx:CallStmt,o):
        if ctx.name not in o[1]:
            raise UndeclaredIdentifier(ctx.name)
        elif len(ctx.args) != len(o[1][ctx.name]):
            raise TypeMismatchInStatement(ctx)
        for i in range(len(ctx.args)):
            arg = self.visit(ctx.args[i],o[0])
            if arg not in ['int', 'float', 'bool']:
                if o[0][ctx.name][i] not in ['int', 'float', 'bool']:
                    raise TypeCannotBeInferred(ctx)
                elif arg in o[0]:
                    o[0][arg] = o[0][ctx.name][i]
                    o[1][arg] = o[0][ctx.name][i]

            elif o[0][ctx.name][i] not in ['int', 'float', 'bool']:
                o[0][ctx.name][i] = arg
            elif arg != o[0][ctx.name][i]:
                raise TypeMismatchInStatement(ctx)

    def visitAssign(self,ctx:Assign,o):
        rtype = self.visit(ctx.rhs,o[1])
        ltype = self.visit(ctx.lhs,o[1])
        if ltype not in ['int', 'float', 'bool']:
            if rtype not in ['int', 'float', 'bool']:
                raise TypeCannotBeInferred(ctx)
            o[1][ltype] = rtype
            o[0][ltype] = rtype
        elif rtype not in ['int', 'float', 'bool']:
            o[1][rtype] = ltype
            o[0][rtype] = ltype
        elif ltype != rtype:
            raise TypeMismatchInStatement(ctx)
        for keys, values in o[1].items():
            if type(values) == dict:
                for k, v in values.items():
                    if o[1][keys][k] not in ['int', 'float', 'bool']:
                        o[1][keys][k] = o[1][v]

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
