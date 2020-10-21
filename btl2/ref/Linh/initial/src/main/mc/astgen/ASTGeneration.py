# StudentID 1710169
# Nguyen Van Hoai Linh
from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):
    def visitProgram(self,ctx:MCParser.ProgramContext):
        lst = []
        for x in ctx.decl():
            lst+= self.visit(x)
        return Program(lst)
    def visitDecl(self, ctx:MCParser.DeclContext):
        return self.visit(ctx.var_decl()) if ctx.var_decl() else [self.visit(ctx.func_decl())]
    def visitVar_decl(self, ctx:MCParser.Var_declContext):
        lst = []
        for x in ctx.one_variable():
            if x.getChildCount()==1:
                a = self.visit(ctx.primitive_type())
            else: 
                a = ArrayType( int(x.INTLIT().getText()),self.visit(ctx.primitive_type()))
            lst = lst + [VarDecl(x.ID().getText(),a)]
        return lst

    def visitPrimitive_type(self, ctx:MCParser.Primitive_typeContext):
        if ctx.INTTYPE():
            return IntType()
        if ctx.BOOLTYPE():
            return BoolType()
        if ctx.FLOATTYPE():
            return FloatType()
        if ctx.STRINGTYPE():
            return StringType()

    def visitFunc_decl(self, ctx:MCParser.Func_declContext): 
        name = self.visit(ctx.func_name())
        param=[]
        if ctx.one_para(0): 
            for x in ctx.one_para():
                param += [self.visit(x)]
        returnType = self.visit(ctx.func_type())
        body = self.visit(ctx.block_statement())
        return FuncDecl(name, param, returnType, body)
    def visitFunc_name(self, ctx:MCParser.Func_nameContext): 
        return Id(ctx.ID().getText())
    def visitFunc_type(self,ctx:MCParser.Func_typeContext):
        if ctx.VOIDTYPE(): 
            return VoidType()
        elif ctx.LS():  
            return ArrayPointerType(self.visit(ctx.primitive_type()))
        else:
            return self.visit(ctx.primitive_type())
        
    def visitOne_para(self, ctx:MCParser.One_paraContext):
        if ctx.LS():
            Type = ArrayPointerType(self.visit(ctx.primitive_type()))
        else:  
            Type = self.visit(ctx.primitive_type())
        return VarDecl(ctx.ID().getText(), Type)
    def visitBlock_statement(self, ctx:MCParser.Block_statementContext):
        lst= []
        if (ctx.statements()): 
            for x in ctx.statements(): 
                lst+= self.visit(x)
        return Block(lst)
    def visitStatements(self, ctx:MCParser.StatementsContext): 
        if ctx.var_decl(): 
            return self.visit(ctx.var_decl())
        elif ctx.statement():
            return [self.visit(ctx.statement())]
    def visitStatement(self, ctx:MCParser.StatementContext):
        if ctx.if_stm(): 
            return  self.visit(ctx.if_stm())
        if ctx.do_while_stm(): 
            return self.visit(ctx.do_while_stm())
        if ctx.for_stm(): 
            return self.visit(ctx.for_stm())
        if ctx.break_stm():
            return self.visit(ctx.break_stm())
        if ctx.continue_stm(): 
            return self.visit(ctx.continue_stm())
        if ctx.return_stm():
            return self.visit(ctx.return_stm())
        if ctx.expression_stm(): 
            return self.visit(ctx.expression_stm())
        if ctx.block_statement(): 
            return self.visit(ctx.block_statement())
    def visitIf_stm(self, ctx: MCParser.If_stmContext):
        expr = self.visit(ctx.expression_stm())
        thenStmt = self.visit(ctx.statement(0))
        if ctx.statement(1): 
            elseStmt = self.visit(ctx.statement(1)) 
            return If(expr, thenStmt, elseStmt)
        else: return If(expr, thenStmt, None)
    def visitDo_while_stm(self, ctx: MCParser.Do_while_stmContext):
        sl = []
        for x in ctx.statement():
            sl+= [self.visit(x)] # sl: list(stmt)
        exp = self.visit(ctx.expression_stm()) # exp: Expr
        return Dowhile(sl,exp)
    def visitFor_stm(self, ctx: MCParser.For_stmContext): 
        expr1 = self.visit(ctx.expression_stm(0))
        expr2 = self.visit(ctx.expression_stm(1))
        expr3 = self.visit(ctx.expression_stm(2))
        loop  = self.visit(ctx.statement())
        return For(expr1,expr2,expr3, loop)
    def visitBreak_stm(self, ctx: MCParser.Break_stmContext):
        return Break()
    def visitContinue_stm(self, ctx: MCParser.Continue_stmContext): 
        return Continue()
    def visitReturn_stm(self, ctx: MCParser.Return_stmContext): 
        return Return(self.visit(ctx.expression_stm())) if ctx.expression_stm() else Return()
    #op:string
    #left:Expr
    #right: Expr
    def visitExpression_stm(self, ctx: MCParser.Expression_stmContext):
        return BinaryOp(ctx.ASSIGN().getText(), self.visit(ctx.term1()), self.visit(ctx.expression_stm())) if (ctx.ASSIGN()) else self.visit(ctx.term1())
    def visitTerm1(self,ctx: MCParser.Term1Context):
        return BinaryOp(ctx.OR().getText(), self.visit(ctx.term1()), self.visit(ctx.term2())) if ctx.OR() else self.visit(ctx.term2())
    def visitTerm2(self,ctx:MCParser.Term2Context): 
        return BinaryOp(ctx.AND().getText(), self.visit(ctx.term2()), self.visit(ctx.term3())) if ctx.AND() else self.visit(ctx.term3())
    def visitTerm3(self, ctx: MCParser.Term3Context): 
        if ctx.getChildCount() ==3: 
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.term4(0)), self.visit(ctx.term4(1)))
        else: return self.visit(ctx.term4(0))
    def visitTerm4(self, ctx: MCParser.Term4Context): 
        if ctx.getChildCount()==3: 
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.term5(0)), self.visit(ctx.term5(1))) 
        else: return self.visit(ctx.term5(0))
    def visitTerm5(self,ctx:MCParser.Term5Context): 
        if ctx.getChildCount()==3: 
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.term5()), self.visit(ctx.term6())) 
        else: return self.visit(ctx.term6())
    def visitTerm6(self, ctx:MCParser.Term6Context): 
        if ctx.getChildCount()==3: 
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.term6()), self.visit(ctx.term7())) 
        else: return self.visit(ctx.term7())
    #UnaryOp 
    #op: String
    #body: Expr
    def visitTerm7(self, ctx:MCParser.Term7Context): 
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.term7()))
        else: 
            return self.visit(ctx.term8())
    def visitTerm8(self,ctx:MCParser.Term8Context): 
        if ctx.LS(): 
            return ArrayCell(self.visit(ctx.term9()), self.visit(ctx.expression_stm()))
        else: 
            return self.visit(ctx.term9())
    def visitTerm9(self,ctx:MCParser.Term9Context): 
        if ctx.LP(): 
            return self.visit(ctx.expression_stm())
        else: 
            return self.visit(ctx.operand())
    def visitOperand(self, ctx: MCParser.OperandContext): 
        if ctx.BOOLLIT(): 
            return BooleanLiteral(ctx.BOOLLIT())
        elif ctx.FLOATLIT(): 
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.INTLIT(): 
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.STRINGLIT(): 
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.ID(): 
            return Id(ctx.ID().getText())
        else: 
            return self.visit(ctx.invocation())
    def visitInvocation(self, ctx: MCParser.InvocationContext): 
        lst = []
        if ctx.expression_stm():
            for x in ctx.expression_stm():
                lst+= [self.visit(x)]
        return CallExpr(Id(ctx.ID().getText()), lst) 