from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class Count(MCVisitor):
    # program: vardecls EOF;
    def visitProgram(self,ctx:MCParser.ProgramContext):
        # EOF is also considered as a node
        return 1 + self.visit(ctx.vardecls())


    # mctype: INTTYPE | FLOATTYPE | ARRAY LB INTLIT RB OF mctype ;
    def visitMctype(self,ctx:MCParser.MctypeContext):
        if ctx.getChildCount() == 6:
            return 5 + self.visit(ctx.mctype()) # return number of leaf nodes from the third right hand side
        else:
            return 1 # return number of leaf nodes from the first or second right hand side

    # vardecls: vardecl vardecls | vardecl ;
    def visitVardecls(self,ctx:MCParser.VardeclsContext):
        if ctx.getChildCount() == 2:
            return self.visit(ctx.vardecl()) + self.visit(ctx.vardecls())# return number of leaf nodes from the first right hand side
        else:
            return self.visit(ctx.vardecl())# return number of leaf nodes from the first right hand side
  	
    # vardecl: mctype ids SEMI ;
    def visitVardecl(self,ctx:MCParser.VardeclContext):
        return 1 + self.visit(ctx.ids()) + self.visit(ctx.mctype())

    # ids: ID (COMMA ID)* ;
    def visitIds(self,ctx:MCParser.IdsContext):
        return ctx.getChildCount()
 

