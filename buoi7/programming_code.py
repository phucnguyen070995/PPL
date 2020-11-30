class StaticCheck(Visitor):

    def visitBinOp(self,ctx:BinOp,o):
        operator = ctx.op
        lexp = self.visit(ctx.e1,[])
        rexp = self.visit(ctx.e2,[])
def visitId(self,ctx:Id,o:object):
        if ctx.name not in o:
            raise UndeclaredIdentifier(ctx.name)
        return ctx.name        if operator in ['+', '-', '*']:
            if type(lexp) is IntLit and type(rexp) is IntLit:
                return IntType()
            if type(lexp) is FloatLit and type(rexp) is FloatLit:
                return FloatType()
            if type(lexp) is FloatLit and type(rexp) is IntLit:
                return FloatType()
            if type(lexp) is IntLit and type(rexp) is FloatLit:
                return FloatType()
            raise TypeMismatchInExpression(ctx)
                
        
    def visitUnOp(self,ctx:UnOp,o):
        pass

    def visitIntLit(self,ctx:IntLit,o):
        return IntLit(ctx.val)
        
    def visitFloatLit(self,ctx,o):
        return FloatLit(ctx.val)
        
    def visitBoolLit(self,ctx,o):
        return BoolLit(ctx.val)
    
#Cau 1
class StaticCheck(Visitor):

    def visitBinOp(self,ctx:BinOp,o):
        operator = ctx.op
        lexp = self.visit(ctx.e1,[])
        rexp = self.visit(ctx.e2,[])
        if operator in ['+', '-', '*']:
            if any([x is BoolLit for x in [type(lexp), type(rexp)]]):
                raise TypeMismatchInExpression(ctx)
            if any([x is FloatLit for x in [type(lexp), type(rexp)]]):
                return FloatLit(ctx)
            return IntLit(ctx)
        if operator == '/':
            if any([x is BoolLit for x in [type(lexp), type(rexp)]]):
                raise TypeMismatchInExpression(ctx)
            return FloatLit(ctx)
        if operator in ['&&', '||']:
            if all([x is BoolLit for x in [type(lexp), type(rexp)]]):
                return BoolLit(ctx)
            raise TypeMismatchInExpression(ctx)
        if operator in ['>', '<', '==', '!=']:
            if type(lexp) == type(rexp):
                return BoolLit(ctx)
            raise TypeMismatchInExpression(ctx)
        raise TypeMismatchInExpression(ctx)
            
    def visitUnOp(self,ctx:UnOp,o):
        operator = ctx.op
        exp = self.visit(ctx.e,[])
        if operator == '!':
            if type(exp) is BoolLit:
                return BoolLit(ctx)
            raise TypeMismatchInExpression(ctx)
        if operator == '-':
            if type(exp) is BoolLit:
                raise TypeMismatchInExpression(ctx)
            if type(exp) is IntLit:
                return IntLit(ctx)
            if type(exp) is FloatLit:
                return FloatLit(ctx)
        raise TypeMismatchInExpression(ctx)
        

    def visitIntLit(self,ctx:IntLit,o):
        return IntLit(ctx.val)
        
    def visitFloatLit(self,ctx,o):
        return FloatLit(ctx.val)
        
    def visitBoolLit(self,ctx,o):
        return BoolLit(ctx.val)


#Cau2 (sai)
class StaticCheck(Visitor):
    def visitProgram(self,ctx:Program,o):
        o = [self.visit(x,[]) for x in ctx.decl]
        self.visit(ctx.exp,o)
        
    def visitVarDecl(self,ctx:VarDecl,o):
        return (ctx.name, type(ctx.typ))
    
    def visitBinOp(self,ctx:BinOp,o):
        operator = ctx.op
        o_name = [x[0] for x in o]
        lexp = self.visit(ctx.e1,o_name)
        rexp = self.visit(ctx.e2,o_name)
        if type(lexp) is str:
            idx = o_name.index(lexp)
            lexp = o[idx][1]
            if lexp == BoolType:
                lexp == type(BoolLit(0))
            elif lexp == FloatType:
                lexp == type(FloatLit(0))
            elif lexp == IntType:
                lexp == type(IntLit(0))
        else:
            lexp = type(lexp)
        if type(rexp) is str:
            idx = o_name.index(name)
            rexp = o[idx][1]
            if rexp == BoolType:
                rexp == type(BoolLit(0))
            elif rexp == FloatType:
                rexp == type(FloatLit(0))
            elif rexp == IntType:
                rexp == type(IntLit(0))
        else:
            rexp = type(rexp)
        if operator in ['+', '-', '*']:
            if any([x is BoolLit for x in [lexp, rexp]]):
                raise TypeMismatchInExpression(ctx)
            if any([x is FloatLit for x in [lexp, rexp]]):
                return FloatLit(ctx)
            return IntLit(ctx)
        if operator == '/':
            if any([x is BoolLit for x in [lexp, rexp]]):
                raise TypeMismatchInExpression(ctx)
            return FloatLit(ctx)
        if operator in ['&&', '||']:
            if all([x is BoolLit for x in [lexp, rexp]]):
                return BoolLit(ctx)
            raise TypeMismatchInExpression(ctx)
        if operator in ['>', '<', '==', '!=']:
            if lexp == rexp:
                return BoolLit(ctx)
            raise TypeMismatchInExpression(ctx)
        raise TypeMismatchInExpression(ctx)
            
    def visitUnOp(self,ctx:UnOp,o):
        operator = ctx.op
        exp = self.visit(ctx.e1,o_name)
        if type(exp) is str:
            o_name = [x[0] for x in o]
            idx = o_name.index(name)
            exp = o[idx][1]
            if exp == BoolType:
                exp == type(BoolLit(0))
            elif exp == FloatType:
                exp == type(FloatLit(0))
            elif exp == IntType:
                exp == type(IntLit(0))
        else:
            exp = type(self.visit(ctx.e,[]))
        if operator == '!':
            if exp is BoolLit:
                return BoolLit(ctx)
            raise TypeMismatchInExpression(ctx)
        if operator == '-':
            if exp is BoolLit:
                raise TypeMismatchInExpression(ctx)
            if exp is IntLit:
                return IntLit(ctx)
            if exp is FloatLit:
                return FloatLit(ctx)
        raise TypeMismatchInExpression(ctx)
        

    def visitIntLit(self,ctx:IntLit,o):
        return IntLit(ctx.val)
        
    def visitFloatLit(self,ctx,o):
        return FloatLit(ctx.val)
        
    def visitBoolLit(self,ctx,o):
        return BoolLit(ctx.val)
    
    def visitId(self,ctx:Id,o:object):
        if ctx.name not in o:
            raise UndeclaredIdentifier(ctx.name)
        return ctx.name
        
        
#cau2 (sua)     
from functools import reduce
class StaticCheck(Visitor):
    
    def visitProgram(self,ctx:Program,o):
        varList = reduce(lambda acc,x: acc + self.visit(x,acc), ctx.decl, [] )
        #print(varList)
        return Program(varList, self.visit(ctx.exp, varList))
        
        
    def visitVarDecl(self,ctx:VarDecl,o):
        #print(ctx.typ)
        return [(ctx.name, ctx.typ)]
        
    def visitBinOp(self,ctx:BinOp,o): 
        e1 = self.visit(ctx.e1,o)
        e2 = self.visit(ctx.e2,o)
        
        if ctx.op in ['+','-','*']:
            
            if (type(e1) == BoolLit or type(e2) == BoolLit):
                raise TypeMismatchInExpression(ctx)
            elif(type(e1) == FloatLit or type(e2) == FloatLit):
                return FloatLit(ctx)
            else:
                return IntLit(ctx)
        elif ctx.op == '/':
            if (type(e1) == BoolLit or type(e2) == BoolLit):
                raise TypeMismatchInExpression(ctx)
            else:
                return FloatLit(ctx)
        elif ctx.op in ['||', '&&']:
            if (type(e1) != BoolLit or type(e2) != BoolLit):
                raise TypeMismatchInExpression(ctx)
            else:
                return BoolLit(ctx)
        elif ctx.op in ['>', '<', '==', '!=']:
            if (type(e1) != type(e2)):
                raise TypeMismatchInExpression(ctx)
            else:
                return BoolLit(ctx)
                
    def visitUnOp(self,ctx:UnOp,o):
        e = self.visit(ctx.e, o)
        if ctx.op == '!':
            if type(e) !=  BoolLit:
                raise TypeMismatchInExpression(ctx)
            else:
                return BoolLit(ctx)
        elif ctx.op == '-':
            if type(e) == BoolLit:
                raise TypeMismatchInExpression(ctx)
            elif type(e) == FloatLit:
                return FloatLit(ctx)
            elif type(e) == IntLit:
                return IntLit(ctx)
    def visitIntLit(self,ctx:IntLit,o): 
        return IntLit(ctx.val)

    def visitFloatLit(self,ctx,o): 
        return FloatLit(ctx.val)

    def visitBoolLit(self,ctx,o): 
        return BoolLit(ctx.val)
        
    def visitId(self,ctx,o):
        for vardecl in o:
            if ctx.name == vardecl[0]:
                if type(vardecl[1]) == BoolType:
                    return BoolLit(0)
                elif type(vardecl[1]) == IntType:
                    return IntLit(0)
                elif type(vardecl[1]) == FloatType:
                    return FloatLit(0)
                    
        #if ctx.name in o:
        #    return ctx.typ
        #else:
        raise UndeclaredIdentifier(ctx.name)
#cau 2 (sua tu bai 1)
class StaticCheck(Visitor):
    def visitProgram(self,ctx:Program,o):
        o = [self.visit(x,[]) for x in ctx.decl]
        return Program(o, self.visit(ctx.exp,o))
        
        
    def visitVarDecl(self,ctx:VarDecl,o):
        return (ctx.name, ctx.typ)
        
    def visitBinOp(self,ctx:BinOp,o):
        operator = ctx.op
        lexp = self.visit(ctx.e1,o)
        rexp = self.visit(ctx.e2,o)
        if operator in ['+', '-', '*']:
            if any([x is BoolLit for x in [type(lexp), type(rexp)]]):
                raise TypeMismatchInExpression(ctx)
            if any([x is FloatLit for x in [type(lexp), type(rexp)]]):
                return FloatLit(ctx)
            return IntLit(ctx)
        if operator == '/':
            if any([x is BoolLit for x in [type(lexp), type(rexp)]]):
                raise TypeMismatchInExpression(ctx)
            return FloatLit(ctx)
        if operator in ['&&', '||']:
            if all([x is BoolLit for x in [type(lexp), type(rexp)]]):
                return BoolLit(ctx)
            raise TypeMismatchInExpression(ctx)
        if operator in ['>', '<', '==', '!=']:
            if type(lexp) == type(rexp):
                return BoolLit(ctx)
            raise TypeMismatchInExpression(ctx)
        raise TypeMismatchInExpression(ctx)
            
    def visitUnOp(self,ctx:UnOp,o):
        operator = ctx.op
        exp = self.visit(ctx.e,o)
        if operator == '!':
            if type(exp) is BoolLit:
                return BoolLit(ctx)
            raise TypeMismatchInExpression(ctx)
        if operator == '-':
            if type(exp) is BoolLit:
                raise TypeMismatchInExpression(ctx)
            if type(exp) is IntLit:
                return IntLit(ctx)
            if type(exp) is FloatLit:
                return FloatLit(ctx)
        raise TypeMismatchInExpression(ctx)
        

    def visitIntLit(self,ctx:IntLit,o):
        return IntLit(ctx.val)
        
    def visitFloatLit(self,ctx,o):
        return FloatLit(ctx.val)
        
    def visitBoolLit(self,ctx,o):
        return BoolLit(ctx.val)
        
    def visitId(self,ctx,o):
        for vardecl in o:
            if ctx.name == vardecl[0]:
                if type(vardecl[1]) == BoolType:
                    return BoolLit(0)
                elif type(vardecl[1]) == IntType:
                    return IntLit(0)
                elif type(vardecl[1]) == FloatType:
                    return FloatLit(0)
        raise UndeclaredIdentifier(ctx.name)

#cau 3 (tu lam)
from functools import reduce
class StaticCheck(Visitor):
    def visitProgram(self,ctx:Program,o):
        o = [self.visit(x,[]) for x in ctx.decl]
        reduce(lambda acc, x: acc + self.visit(x,acc), ctx.stmts,o)  
        
    def visitVarDecl(self,ctx:VarDecl,o):
        return (ctx.name, None)
        
    def visitAssign(self,ctx:Assign,o):
        rtype = self.visit(ctx.lhs,o)
        ltype = self.visit(ctx.rhs,o)
        if type(ltype) == str:
            if type(rtype) == str:
                raise TypeCannotBeInferred(ctx)
            for i in range(len(o)):
            	if o[i][0] == ltype:
            		x[i][1] = rtype
            		break
            return o
        if ltype != rtype:
            raise TypeMismatchInStatement(ctx)


    def visitBinOp(self,ctx:BinOp,o):
        operator = ctx.op
        lexp = self.visit(ctx.e1,o)
        rexp = self.visit(ctx.e2,o)
        if operator in ['+', '-', '*','/']:
            if any([(x is BoolLit or x is FloatLit) for x in [type(lexp), type(rexp)]]):
                raise TypeMismatchInExpression(ctx)
            return IntLit(ctx)
        if operator in ['+.', '-.', '*.','/.']:
            if any([(x is BoolLit or x is IntLit) for x in [type(lexp), type(rexp)]]):
                raise TypeMismatchInExpression(ctx)
            return FloatLit(ctx)
        if operator in ['>', '=']:
            if any([(x is BoolLit or x is FloatLit) for x in [type(lexp), type(rexp)]]):
                raise TypeMismatchInExpression(ctx)
            return BoolLit(ctx)
        if operator in ['>.', '=.']:
            if any([(x is BoolLit or x is IntLit) for x in [type(lexp), type(rexp)]]):
                raise TypeMismatchInExpression(ctx)
            return BoolLit(ctx)
        if operator in ['&&', '||', '>b', '=b']:
            if any([(x is FloatLit or x is IntLit) for x in [type(lexp), type(rexp)]]):
                raise TypeMismatchInExpression(ctx)
            return BoolLit(ctx)
        raise TypeMismatchInExpression(ctx)
            
    def visitUnOp(self,ctx:UnOp,o):
        operator = ctx.op
        exp = self.visit(ctx.e,o)
        if operator == '!':
            if type(exp) is BoolLit:
                return BoolLit(ctx)
            raise TypeMismatchInExpression(ctx)
        if operator == '-.':
            if type(exp) is FloatLit:
                return FloatLit(ctx)
        if operator == '-':
            if type(exp) is IntLit:
                return IntLit(ctx)
        if operator == 'i2f':
            if type(exp) is IntLit:
                return FloatLit(ctx)
        if operator == 'floor':
            if type(exp) is FloatLit:
                return IntLit(ctx)
        raise TypeMismatchInExpression(ctx)
        

    def visitIntLit(self,ctx:IntLit,o):
        return IntLit(ctx.val)
        
    def visitFloatLit(self,ctx,o):
        return FloatLit(ctx.val)
        
    def visitBoolLit(self,ctx,o):
        return BoolLit(ctx.val)
        
    def visitId(self,ctx,o):
        for vardecl in o:
            if ctx.name == vardecl[0]:
                return ctx.name
        raise UndeclaredIdentifier(ctx.name)

Program([VarDecl("x"),VarDecl("y"),VarDecl("z")],
	[Assign(Id("x"),
		BinOp(">b",BinOp("&&",Id("x"),Id("y")),BinOp("||",BoolLit(False),BinOp(">",Id("z"),IntLit(3))))),
	Assign(Id("z"),Id("x"))])


