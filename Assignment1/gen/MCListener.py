# Generated from /home/lin/0-PPL/Assignment/initial/src/main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete listener for a parse tree produced by MCParser.
class MCListener(ParseTreeListener):

    # Enter a parse tree produced by MCParser#program.
    def enterProgram(self, ctx:MCParser.ProgramContext):
        pass

    # Exit a parse tree produced by MCParser#program.
    def exitProgram(self, ctx:MCParser.ProgramContext):
        pass


    # Enter a parse tree produced by MCParser#manyDecls.
    def enterManyDecls(self, ctx:MCParser.ManyDeclsContext):
        pass

    # Exit a parse tree produced by MCParser#manyDecls.
    def exitManyDecls(self, ctx:MCParser.ManyDeclsContext):
        pass


    # Enter a parse tree produced by MCParser#decl.
    def enterDecl(self, ctx:MCParser.DeclContext):
        pass

    # Exit a parse tree produced by MCParser#decl.
    def exitDecl(self, ctx:MCParser.DeclContext):
        pass


    # Enter a parse tree produced by MCParser#func_decl.
    def enterFunc_decl(self, ctx:MCParser.Func_declContext):
        pass

    # Exit a parse tree produced by MCParser#func_decl.
    def exitFunc_decl(self, ctx:MCParser.Func_declContext):
        pass


    # Enter a parse tree produced by MCParser#func_type.
    def enterFunc_type(self, ctx:MCParser.Func_typeContext):
        pass

    # Exit a parse tree produced by MCParser#func_type.
    def exitFunc_type(self, ctx:MCParser.Func_typeContext):
        pass


    # Enter a parse tree produced by MCParser#func_name.
    def enterFunc_name(self, ctx:MCParser.Func_nameContext):
        pass

    # Exit a parse tree produced by MCParser#func_name.
    def exitFunc_name(self, ctx:MCParser.Func_nameContext):
        pass


    # Enter a parse tree produced by MCParser#para_list.
    def enterPara_list(self, ctx:MCParser.Para_listContext):
        pass

    # Exit a parse tree produced by MCParser#para_list.
    def exitPara_list(self, ctx:MCParser.Para_listContext):
        pass


    # Enter a parse tree produced by MCParser#one_para.
    def enterOne_para(self, ctx:MCParser.One_paraContext):
        pass

    # Exit a parse tree produced by MCParser#one_para.
    def exitOne_para(self, ctx:MCParser.One_paraContext):
        pass


    # Enter a parse tree produced by MCParser#block_statement.
    def enterBlock_statement(self, ctx:MCParser.Block_statementContext):
        pass

    # Exit a parse tree produced by MCParser#block_statement.
    def exitBlock_statement(self, ctx:MCParser.Block_statementContext):
        pass


    # Enter a parse tree produced by MCParser#var_decl.
    def enterVar_decl(self, ctx:MCParser.Var_declContext):
        pass

    # Exit a parse tree produced by MCParser#var_decl.
    def exitVar_decl(self, ctx:MCParser.Var_declContext):
        pass


    # Enter a parse tree produced by MCParser#var_list.
    def enterVar_list(self, ctx:MCParser.Var_listContext):
        pass

    # Exit a parse tree produced by MCParser#var_list.
    def exitVar_list(self, ctx:MCParser.Var_listContext):
        pass


    # Enter a parse tree produced by MCParser#one_variable.
    def enterOne_variable(self, ctx:MCParser.One_variableContext):
        pass

    # Exit a parse tree produced by MCParser#one_variable.
    def exitOne_variable(self, ctx:MCParser.One_variableContext):
        pass


    # Enter a parse tree produced by MCParser#statement.
    def enterStatement(self, ctx:MCParser.StatementContext):
        pass

    # Exit a parse tree produced by MCParser#statement.
    def exitStatement(self, ctx:MCParser.StatementContext):
        pass


    # Enter a parse tree produced by MCParser#if_stm.
    def enterIf_stm(self, ctx:MCParser.If_stmContext):
        pass

    # Exit a parse tree produced by MCParser#if_stm.
    def exitIf_stm(self, ctx:MCParser.If_stmContext):
        pass


    # Enter a parse tree produced by MCParser#do_while_stm.
    def enterDo_while_stm(self, ctx:MCParser.Do_while_stmContext):
        pass

    # Exit a parse tree produced by MCParser#do_while_stm.
    def exitDo_while_stm(self, ctx:MCParser.Do_while_stmContext):
        pass


    # Enter a parse tree produced by MCParser#for_stm.
    def enterFor_stm(self, ctx:MCParser.For_stmContext):
        pass

    # Exit a parse tree produced by MCParser#for_stm.
    def exitFor_stm(self, ctx:MCParser.For_stmContext):
        pass


    # Enter a parse tree produced by MCParser#break_stm.
    def enterBreak_stm(self, ctx:MCParser.Break_stmContext):
        pass

    # Exit a parse tree produced by MCParser#break_stm.
    def exitBreak_stm(self, ctx:MCParser.Break_stmContext):
        pass


    # Enter a parse tree produced by MCParser#continue_stm.
    def enterContinue_stm(self, ctx:MCParser.Continue_stmContext):
        pass

    # Exit a parse tree produced by MCParser#continue_stm.
    def exitContinue_stm(self, ctx:MCParser.Continue_stmContext):
        pass


    # Enter a parse tree produced by MCParser#return_stm.
    def enterReturn_stm(self, ctx:MCParser.Return_stmContext):
        pass

    # Exit a parse tree produced by MCParser#return_stm.
    def exitReturn_stm(self, ctx:MCParser.Return_stmContext):
        pass


    # Enter a parse tree produced by MCParser#expression_stm.
    def enterExpression_stm(self, ctx:MCParser.Expression_stmContext):
        pass

    # Exit a parse tree produced by MCParser#expression_stm.
    def exitExpression_stm(self, ctx:MCParser.Expression_stmContext):
        pass


    # Enter a parse tree produced by MCParser#term1.
    def enterTerm1(self, ctx:MCParser.Term1Context):
        pass

    # Exit a parse tree produced by MCParser#term1.
    def exitTerm1(self, ctx:MCParser.Term1Context):
        pass


    # Enter a parse tree produced by MCParser#term2.
    def enterTerm2(self, ctx:MCParser.Term2Context):
        pass

    # Exit a parse tree produced by MCParser#term2.
    def exitTerm2(self, ctx:MCParser.Term2Context):
        pass


    # Enter a parse tree produced by MCParser#term3.
    def enterTerm3(self, ctx:MCParser.Term3Context):
        pass

    # Exit a parse tree produced by MCParser#term3.
    def exitTerm3(self, ctx:MCParser.Term3Context):
        pass


    # Enter a parse tree produced by MCParser#term4.
    def enterTerm4(self, ctx:MCParser.Term4Context):
        pass

    # Exit a parse tree produced by MCParser#term4.
    def exitTerm4(self, ctx:MCParser.Term4Context):
        pass


    # Enter a parse tree produced by MCParser#term5.
    def enterTerm5(self, ctx:MCParser.Term5Context):
        pass

    # Exit a parse tree produced by MCParser#term5.
    def exitTerm5(self, ctx:MCParser.Term5Context):
        pass


    # Enter a parse tree produced by MCParser#term6.
    def enterTerm6(self, ctx:MCParser.Term6Context):
        pass

    # Exit a parse tree produced by MCParser#term6.
    def exitTerm6(self, ctx:MCParser.Term6Context):
        pass


    # Enter a parse tree produced by MCParser#term7.
    def enterTerm7(self, ctx:MCParser.Term7Context):
        pass

    # Exit a parse tree produced by MCParser#term7.
    def exitTerm7(self, ctx:MCParser.Term7Context):
        pass


    # Enter a parse tree produced by MCParser#term8.
    def enterTerm8(self, ctx:MCParser.Term8Context):
        pass

    # Exit a parse tree produced by MCParser#term8.
    def exitTerm8(self, ctx:MCParser.Term8Context):
        pass


    # Enter a parse tree produced by MCParser#term9.
    def enterTerm9(self, ctx:MCParser.Term9Context):
        pass

    # Exit a parse tree produced by MCParser#term9.
    def exitTerm9(self, ctx:MCParser.Term9Context):
        pass


    # Enter a parse tree produced by MCParser#operand.
    def enterOperand(self, ctx:MCParser.OperandContext):
        pass

    # Exit a parse tree produced by MCParser#operand.
    def exitOperand(self, ctx:MCParser.OperandContext):
        pass


    # Enter a parse tree produced by MCParser#invocation.
    def enterInvocation(self, ctx:MCParser.InvocationContext):
        pass

    # Exit a parse tree produced by MCParser#invocation.
    def exitInvocation(self, ctx:MCParser.InvocationContext):
        pass


    # Enter a parse tree produced by MCParser#array_input.
    def enterArray_input(self, ctx:MCParser.Array_inputContext):
        pass

    # Exit a parse tree produced by MCParser#array_input.
    def exitArray_input(self, ctx:MCParser.Array_inputContext):
        pass


    # Enter a parse tree produced by MCParser#array_output.
    def enterArray_output(self, ctx:MCParser.Array_outputContext):
        pass

    # Exit a parse tree produced by MCParser#array_output.
    def exitArray_output(self, ctx:MCParser.Array_outputContext):
        pass


    # Enter a parse tree produced by MCParser#array_element.
    def enterArray_element(self, ctx:MCParser.Array_elementContext):
        pass

    # Exit a parse tree produced by MCParser#array_element.
    def exitArray_element(self, ctx:MCParser.Array_elementContext):
        pass


    # Enter a parse tree produced by MCParser#primitive_type.
    def enterPrimitive_type(self, ctx:MCParser.Primitive_typeContext):
        pass

    # Exit a parse tree produced by MCParser#primitive_type.
    def exitPrimitive_type(self, ctx:MCParser.Primitive_typeContext):
        pass


    # Enter a parse tree produced by MCParser#func_call.
    def enterFunc_call(self, ctx:MCParser.Func_callContext):
        pass

    # Exit a parse tree produced by MCParser#func_call.
    def exitFunc_call(self, ctx:MCParser.Func_callContext):
        pass


