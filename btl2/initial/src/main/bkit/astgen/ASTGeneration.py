from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

from functools import reduce
class ASTGeneration(BKITVisitor):
    def visitProgram(self, ctx: BKITParser.ProgramContext):
        return self.visit(ctx.exp())

    def visitExp(self, ctx: BKITParser.ExpContext):
        return reduce(lambda acc, ele: Binary(ele[0].getText(), self.visit(ele[1]), acc), [[ctx.ASSIGN()[i], ctx.term()[i]] for i in range(len(ctx.ASSIGN()))][::-1], self.visit(ctx.term()[-1]))

    def visitTerm(self, ctx: BKITParser.TermContext):
        if ctx.getChildCount() == 3:
            return Binary(ctx.getChild(1).getText(), self.visit(ctx.factor(0)), self.visit(ctx.factor(1)))
        else:
            return self.visit(ctx.factor(0))

    def visitFactor(self, ctx: BKITParser.FactorContext):
        return reduce(lambda acc, ele: Binary(ele[0].getText(), acc, self.visit(ele[1])), [[ctx.ANDOR()[i], ctx.operand()[i+1]] for i in range(len(ctx.ANDOR()))], self.visit(ctx.operand()[0]))

    def visitOperand(self, ctx: BKITParser.OperandContext):
        if ctx.BOOLIT():
            return BooleanLiteral(ctx.BOOLIT().getText())
        elif ctx.INTLIT():
            return IntLiteral(ctx.INTLIT().getText())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.exp())



    

