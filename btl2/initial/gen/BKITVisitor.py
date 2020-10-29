# Generated from /Users/mac/Phuc/PPL/btl2/initial/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
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


    # Visit a parse tree produced by BKITParser#vardecls.
    def visitVardecls(self, ctx:BKITParser.VardeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#vardecltail.
    def visitVardecltail(self, ctx:BKITParser.VardecltailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#vardecl.
    def visitVardecl(self, ctx:BKITParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#mptype.
    def visitMptype(self, ctx:BKITParser.MptypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#ids.
    def visitIds(self, ctx:BKITParser.IdsContext):
        return self.visitChildren(ctx)



del BKITParser