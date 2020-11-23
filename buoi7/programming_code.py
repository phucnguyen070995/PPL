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


#Cau2
class StaticCheck(Visitor):
    def visitProgram(self,ctx:Program,o):
        o = [self.visit(x,[]) for x in ctx.decl]
        self.visit(ctx.exp,o)
        
    def visitVarDecl(self,ctx:VarDecl,o):
        return (ctx.name, ctx.typ)
    
    def visitBinOp(self,ctx:BinOp,o):
        operator = ctx.op
        o_name = [x[0] for x in o]
        lexp = self.visit(ctx.e1,o_name)
        rexp = self.visit(ctx.e2,o_name)
        if type(lexp) is str or type(rexp) is str:
            if type(lexp) is str:
                idx = o_name.index(lexp)
                lexp = o[idx][1]
            if type(ctx.e2) is Id:
                idx = o_name.index(name)
                rexp = o[idx][1]
        else:
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
        exp = []
        if type(ctx.e) is Id:
            name = self.visit(ctx.e,[])
            o_name = [x[0] for x in o]
            if name not in o_name:
                raise UndeclaredIdentifier(name)
            idx = o_name.index(name)
            exp = o[idx][1]
        else:
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
    
    def visitId(self,ctx:Id,o:object):
        if ctx.name not in o:
            raise UndeclaredIdentifier(ctx.name)
        return ctx.name