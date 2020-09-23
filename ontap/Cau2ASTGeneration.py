from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):

    # program: vardecls EOF;
    def visitProgram(self,ctx:MCParser.ProgramContext):
        return Program(self.visit(ctx.vardecls())) # return a Program object
    
    # vardecls: vardecl vardecls | vardecl ;
    def visitVardecls(self,ctx:MCParser.VardeclsContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.vardecl())]+ self.visit(ctx.vardecls()) # return the list of VarDecl for the first right hand side
        else:
            return [self.visit(ctx.vardecl())] # return the list of VarDecl for the second right hand side  

    # vardecl: mctype ids ;
    def visitVardecl(self,ctx:MCParser.VardeclContext):
        return VarDecl(self.visit(ctx.mctype()), self.visit(ctx.ids())) # return VarDecl object
  
  	# mctype: INTTYPE | FLOATTYPE ;
    def visitMctype(self,ctx:MCParser.MctypeContext):
        if ctx.INTTYPE():
            return IntType()
        return FloatType() # return IntType() or FloatType()

    # ids: ID (COMMA ID)* ;
    def visitIds(self,ctx:MCParser.IdsContext):
        return [x.getText() for x in ctx.ID()]# return the list of identifier's lexemes