# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#program_part.
    def visitProgram_part(self, ctx:BKITParser.Program_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_dec.
    def visitVar_dec(self, ctx:BKITParser.Var_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#variable_list.
    def visitVariable_list(self, ctx:BKITParser.Variable_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#scalar_variable.
    def visitScalar_variable(self, ctx:BKITParser.Scalar_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#composite_variable.
    def visitComposite_variable(self, ctx:BKITParser.Composite_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#composite_var_name.
    def visitComposite_var_name(self, ctx:BKITParser.Composite_var_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_dec.
    def visitFunc_dec(self, ctx:BKITParser.Func_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#params.
    def visitParams(self, ctx:BKITParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#param_list.
    def visitParam_list(self, ctx:BKITParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_body.
    def visitFunc_body(self, ctx:BKITParser.Func_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression_stm.
    def visitExpression_stm(self, ctx:BKITParser.Expression_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#term1.
    def visitTerm1(self, ctx:BKITParser.Term1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#term2.
    def visitTerm2(self, ctx:BKITParser.Term2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#term3.
    def visitTerm3(self, ctx:BKITParser.Term3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#term4.
    def visitTerm4(self, ctx:BKITParser.Term4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#term5.
    def visitTerm5(self, ctx:BKITParser.Term5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#term6.
    def visitTerm6(self, ctx:BKITParser.Term6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#term7.
    def visitTerm7(self, ctx:BKITParser.Term7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#operand.
    def visitOperand(self, ctx:BKITParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_operators.
    def visitIndex_operators(self, ctx:BKITParser.Index_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#callee.
    def visitCallee(self, ctx:BKITParser.CalleeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#parameter_callee.
    def visitParameter_callee(self, ctx:BKITParser.Parameter_calleeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#type_coercions.
    def visitType_coercions(self, ctx:BKITParser.Type_coercionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statement_list.
    def visitStatement_list(self, ctx:BKITParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statement_part.
    def visitStatement_part(self, ctx:BKITParser.Statement_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assign_stm.
    def visitAssign_stm(self, ctx:BKITParser.Assign_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_stm.
    def visitIf_stm(self, ctx:BKITParser.If_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#elseif_else.
    def visitElseif_else(self, ctx:BKITParser.Elseif_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#elseif_one.
    def visitElseif_one(self, ctx:BKITParser.Elseif_oneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#else_one.
    def visitElse_one(self, ctx:BKITParser.Else_oneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_stm.
    def visitFor_stm(self, ctx:BKITParser.For_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_stm.
    def visitReturn_stm(self, ctx:BKITParser.Return_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_stm.
    def visitWhile_stm(self, ctx:BKITParser.While_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#do_while_stm.
    def visitDo_while_stm(self, ctx:BKITParser.Do_while_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#break_stm.
    def visitBreak_stm(self, ctx:BKITParser.Break_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continue_stm.
    def visitContinue_stm(self, ctx:BKITParser.Continue_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_stm.
    def visitCall_stm(self, ctx:BKITParser.Call_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#multiplying.
    def visitMultiplying(self, ctx:BKITParser.MultiplyingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#adding.
    def visitAdding(self, ctx:BKITParser.AddingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#logical.
    def visitLogical(self, ctx:BKITParser.LogicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#relational.
    def visitRelational(self, ctx:BKITParser.RelationalContext):
        return self.visitChildren(ctx)



del BKITParser