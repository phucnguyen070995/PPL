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
        print('vardecl', o)

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
        print('param', dict_param)
        print('o1', o1)
        print('o', o)
        o[0][ctx.name] = dict_param
        o[1][ctx.name] = dict_param
        print('o', o)

        for keys, values in o[1].items():
            if keys not in o1[1]:
                o1[1][keys] = values
        print('o1', o1)
        print('o', o)
        env2 = [self.visit(x,o1) for x in ctx.local]
        stmt = [self.visit(x,o1) for x in ctx.stmts]
        print('o1', o1)
        print('o', o)
        print('funcdecl',o)

    def visitCallStmt(self,ctx:CallStmt,o):
        print('callstmt',o)
        if ctx.name not in o[1]:
            raise UndeclaredIdentifier(ctx.name)
        elif len(ctx.args) != len(o[1][ctx.name]):
            raise TypeMismatchInStatement(ctx)
        for i in range(len(ctx.args)):
            print(i)
            arg = self.visit(ctx.args[i],o[0])
            print('arg',arg)
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
            print(o)
        print('callstmt',o)

    def visitAssign(self,ctx:Assign,o):
        print('ass',o)
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
        print('ass',o)
        for keys, values in o[1].items():
            if type(values) == dict:
                for k, v in values.items():
                    if o[1][keys][k] not in ['int', 'float', 'bool']:
                        o[1][keys][k] = o[1][v]
        print('ass',o)

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
