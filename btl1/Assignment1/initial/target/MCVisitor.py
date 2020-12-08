# Generated from main/mc/parser/MC.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#func_decl.
    def visitFunc_decl(self, ctx:MCParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#func_type.
    def visitFunc_type(self, ctx:MCParser.Func_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#func_name.
    def visitFunc_name(self, ctx:MCParser.Func_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#one_para.
    def visitOne_para(self, ctx:MCParser.One_paraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#block_statement.
    def visitBlock_statement(self, ctx:MCParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#var_decl.
    def visitVar_decl(self, ctx:MCParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#one_variable.
    def visitOne_variable(self, ctx:MCParser.One_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression_stm.
    def visitExpression_stm(self, ctx:MCParser.Expression_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#term1.
    def visitTerm1(self, ctx:MCParser.Term1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#term2.
    def visitTerm2(self, ctx:MCParser.Term2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#term3.
    def visitTerm3(self, ctx:MCParser.Term3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#term4.
    def visitTerm4(self, ctx:MCParser.Term4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#term5.
    def visitTerm5(self, ctx:MCParser.Term5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#term6.
    def visitTerm6(self, ctx:MCParser.Term6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#term7.
    def visitTerm7(self, ctx:MCParser.Term7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#term8.
    def visitTerm8(self, ctx:MCParser.Term8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#term9.
    def visitTerm9(self, ctx:MCParser.Term9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#operand.
    def visitOperand(self, ctx:MCParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#invocation.
    def visitInvocation(self, ctx:MCParser.InvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#array_input.
    def visitArray_input(self, ctx:MCParser.Array_inputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#array_output.
    def visitArray_output(self, ctx:MCParser.Array_outputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#statement.
    def visitStatement(self, ctx:MCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#if_stm.
    def visitIf_stm(self, ctx:MCParser.If_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#do_while_stm.
    def visitDo_while_stm(self, ctx:MCParser.Do_while_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#for_stm.
    def visitFor_stm(self, ctx:MCParser.For_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#break_stm.
    def visitBreak_stm(self, ctx:MCParser.Break_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#continue_stm.
    def visitContinue_stm(self, ctx:MCParser.Continue_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#return_stm.
    def visitReturn_stm(self, ctx:MCParser.Return_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#primitive_type.
    def visitPrimitive_type(self, ctx:MCParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#func_call.
    def visitFunc_call(self, ctx:MCParser.Func_callContext):
        return self.visitChildren(ctx)



del MCParser