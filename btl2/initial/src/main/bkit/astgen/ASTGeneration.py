from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

from functools import reduce
class ASTGeneration(BKITVisitor):

    # program:            var_dec_many func_dec_many EOF
    #                 | var_dec_many EOF
    #                 | func_dec_many EOF
    #                 | EOF;
    def visitProgram(self, ctx: BKITParser.ProgramContext):
        return Program(self.visit(ctx.var_dec_many()) + self.visit(ctx.func_dec_many()))

    # var_dec_many:       var_dec var_dec_many
    #                 | var_dec
    #                 | ;
    def visitVar_dec_many(self, ctx: BKITParser.Var_dec_manyContext):
        if ctx.getChildCount() == 2:
            return self.visit(ctx.var_dec()) + self.visit(ctx.var_dec_many())
        elif ctx.getChildCount() == 1:
            return self.visit(ctx.var_dec())
        return []
    
    # func_dec_many:      func_dec func_dec_many
    #                 | func_dec
    #                 | ;
    def visitFunc_dec_many(self, ctx: BKITParser.Func_dec_manyContext):
        if ctx.getChildCount() == 2:
            return self.visit(ctx.func_dec()) + self.visit(ctx.func_dec_many())
        elif ctx.getChildCount() == 1:
            return self.visit(ctx.func_dec())
        return []

#-------------------------------Variable declaration---------------------------------

    # var_dec:            VAR COLON variable_list SEMI;
    def visitVar_dec(self, ctx:BKITParser.Var_decContext):
        return self.visit(ctx.variable_list())

    # var_list:           var_one COMMA var_list
    #                     | var_one;
    def visitVar_list(self, ctx: BKITParser.Var_listContext):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.var_one()) + self.visit(ctx.var_list())
        return self.visit(ctx.var_one())
    
    # var_one:            scalar_variable | composite_variable;
    def visitVar_one(self, ctx: BKITParser.Var_oneContext):
        if ctx.scalar_variable():
            return [self.visit(ctx.scalar_variable())]
        return [self.visit(ctx.composite_variable())]

    # scalar_variable:    ID ASSIG (INTERGER | FLOAT | BOOLEAN | STRING)
    #                     | ID;
    def visitScalar_variable(self, ctx:BKITParser.Scalar_variableContext):
        if ctx.INTERGER():
            return VarDecl(Id(ctx.ID().getText()),[],IntLiteral(int(ctx.INTERGER().getText(),0)))
        elif ctx.FLOAT():
            return VarDecl(Id(ctx.ID().getText()),[],FloatLiteral(float(ctx.FLOAT().getText())))
        elif ctx.BOOLEAN():
            return VarDecl(Id(ctx.ID().getText()),[],BooleanLiteral(ctx.BOOLEAN().getText() == 'True'))
        elif ctx.STRING():
            return VarDecl(Id(ctx.ID().getText()),[],StringLiteral(ctx.STRING().getText()))
        return VarDecl(Id(ctx.ID().getText()),[],None)
    

    # composite_variable: composite_var_name ASSIG ARRAY
    #                     | composite_var_name;
    def visitComposite_variable(self, ctx:BKITParser.Composite_variableContext):
        if ctx.getChildCount() == 3:
            composite_var_name = self.visit(ctx.composite_var_name())
            composite_var_name.varInit = ArrayLiteral(ctx.ARRAY().getText())
            return composite_var_name
        return self.visit(ctx.composite_var_name())

    # composite_var_name: ID many_demension;
    def visitComposite_var_name(self, ctx:BKITParser.Composite_var_nameContext):
        return VarDecl(Id(ctx.ID().getText()), self.visit(ctx.many_demension()), None)

    # many_demension:     one_demension many_demension
    #                     | one_demension;
    def visitMany_demension(self, ctx:BKITParser.Many_demensionContext):
        if ctx.getChildCount() == 2:
            return self.visit(ctx.one_demension()) + self.visit(ctx.many_demension())
        return self.visit(ctx.one_demension())

    # one_demension:      LB INTERGER RB;
    def visitOne_demension(self, ctx:BKITParser.One_demensionContext):
        return [int(ctx.INTERGER().getText(), 0)]

#-------------------------------Function declaration---------------------------------

    # func_dec:           FUNCTION COLON ID params func_body;
    def visitFunc_dec(self, ctx:BKITParser.Func_decContext):
        return FuncDecl(Id(ctx.ID().getText()), self.visit(ctx.params()), self.visit(ctx.func_body()))

    # params:             PARAMETER COLON param_list
    #                     | ;
    def visitParams(self, ctx:BKITParser.ParamsContext):
        if ctx.param_list():
            return self.visit(ctx.param_list())
        return []

    # param_list:         param_one COMMA param_list
    #                     | param_one;
    def visitParam_list(self, ctx:BKITParser.Param_listContext):
        param = self.visit(ctx.param_one())
        if ctx.COMMA():
            return [param] + self.visit(ctx.param_list())
        return [param]

    # param_one:          ID | composite_var_name;
    def visitParam_one(self, ctx:BKITParser.Param_oneContext):
        if ctx.ID():
            return VarDecl(Id(ctx.ID().getText()),[],None)
        return self.visit(ctx.composite_var_name())

    # func_body:          BODY COLON var_dec_many statement_list ENDBODY DOT;
    def visitFunc_body(self, ctx:BKITParser.Func_bodyContext):
        return (self.visit(ctx.var_dec_many()),self.visit(ctx.statement_list()))

#-------------------------------Expressions---------------------------------

    # expression:         term1 relational term1 | term1;
    def visitExpression(self, ctx:BKITParser.ExpressionContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(self.visit(ctx.relational(), self.visit(ctx.term1(0)), self.visit(ctx.term1(1))))
        return self.visit(ctx.term1(0))

    # term1:              term1 logical term2 | term2;
    def visitTerm1(self, ctx:BKITParser.Term1Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(self.visit(ctx.logical(), self.visit(ctx.term1()), self.visit(ctx.term2())))
        return self.visit(ctx.term2())

    # term2:              term2 adding term3 | term3;
    def visitTerm2(self, ctx:BKITParser.Term2Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(self.visit(ctx.adding(), self.visit(ctx.term2()), self.visit(ctx.term3())))
        return self.visit(ctx.term3())

    # term3:              term3 multiplying term4 | term4;
    def visitTerm3(self, ctx:BKITParser.Term3Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(self.visit(ctx.multiplying(), self.visit(ctx.term3()), self.visit(ctx.term4())))
        return self.visit(ctx.term4())

    # term4:              NOT term4 | term5;
    def visitTerm4(self, ctx:BKITParser.Term4Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.NOT().getText(), self.visit(ctx.term4()))
        return self.visit(ctx.term5())

    # term5:              (SUBOP | SUBF) term5 | term6;
    def visitTerm5(self, ctx:BKITParser.Term5Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.term5()))
        return self.visit(ctx.term6())

    # term6:              term6 LB expression RB | term7;


    # term7:              (LP expression RP) | operand;
    def visitTerm7(self, ctx:BKITParser.Term7Context):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.expression())
        return self.visit(ctx.operand())

    # operand:            ID | FLOAT | INTERGER | STRING | BOOLEAN | ARRAY | callee;
    def visitOperand(self, ctx:BKITParser.OperandContext):
        if ctx.callee():
            return self.visit(ctx.callee())
        elif ctx.INTERGER():
            return VarDecl(Id(ctx.ID().getText()),[],IntLiteral(int(ctx.INTERGER().getText(),0)))
        elif ctx.FLOAT():
            return VarDecl(Id(ctx.ID().getText()),[],FloatLiteral(float(ctx.FLOAT().getText())))
        elif ctx.BOOLEAN():
            return VarDecl(Id(ctx.ID().getText()),[],BooleanLiteral(ctx.BOOLEAN().getText() == 'True'))
        elif ctx.STRING():
            return VarDecl(Id(ctx.ID().getText()),[],StringLiteral(ctx.STRING().getText()))
        elif ctx.ID():
            return VarDecl(Id(ctx.ID().getText()),[],None)
        return ArrayLiteral(ctx.ARRAY().getText())

#-------------------------------Call function---------------------------------

    # callee:             ID LP parameter_callee RP;
    def visitCallee(self, ctx:BKITParser.CalleeContext):
        return CallExpr(Id(ctx.ID().getText()), self.visit(ctx.parameter_callee()))

    # parameter_callee:   expression COMMA parameter_callee
    #                 | expression
    #                 | ;
    def visitParameter_callee(self, ctx:BKITParser.Parameter_calleeContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.expression())] + self.visit(ctx.parameter_callee())
        elif ctx.getChildCount() == 1:
            return [self.visit(ctx.expression())]
        return []
    
#-------------------------------Statement---------------------------------

    # statement_list:     statement_part statement_list
    #                     | statement_part
    #                     | ;
    def visitStatement_list(self, ctx:BKITParser.Statement_listContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.statement_part())] + self.visit(ctx.statement_list())
        elif ctx.getChildCount() == 1:
            return [self.visit(ctx.statement_part())]
        return []

    # statement_part:     if_stm
    #                     | assign_stm
    #                     | for_stm
    #                     | break_stm
    #                     | continue_stm
    #                     | return_stm
    #                     | while_stm
    #                     | do_while_stm
    #                     | call_stm;
    def visitStatement_part(self, ctx:BKITParser.Statement_partContext):
        if ctx.if_stm():
            return self.visit(ctx.if_stm())
        elif ctx.assign_stm():
            return self.visit(ctx.assign_stm())
        elif ctx.for_stm():
            return self.visit(ctx.for_stm())
        elif ctx.break_stm():
            return self.visit(ctx.break_stm())
        elif ctx.continue_stm():
            return self.visit(ctx.continue_stm())
        elif ctx.return_stm():
            return self.visit(ctx.return_stm())
        elif ctx.while_stm():
            return self.visit(ctx.while_stm())
        elif ctx.do_while_stm():
            return self.visit(ctx.do_while_stm())
        return self.visit(ctx.call_stm())

#-------------------------------Assignment Statement---------------------------------

    # assign_stm:         assign SEMI;
    def visitAssign_stm(self, ctx:BKITParser.Assign_stmContext):
        return self.visit(ctx.assign())

    # assign:             ID (many_index | ) ASSIG expression;
    def visitAssign(self, ctx:BKITParser.AssignContext):
        if ctx.many_index():
            return Assign(ArrayCell(Id(ctx.ID().getText()), self.visit(ctx.many_index())), self.visit(ctx.expression()))
        return Assign(Id(ctx.ID().getText()), self.visit(ctx.expression()))

    # many_index:         one_index many_index
    #                     | one_index;
    def visitMany_index(self, ctx:BKITParser.Many_indexContext):
        if ctx.getChildCount() == 2:
            return self.visit(ctx.one_index()) + self.visit(ctx.many_index())
        return self.visit(ctx.one_index())

    # one_index:          LB expression RB;
    def visitOne_index(self, ctx:BKITParser.One_indexContext):
        return [self.visit(ctx.expression())]






    

    

