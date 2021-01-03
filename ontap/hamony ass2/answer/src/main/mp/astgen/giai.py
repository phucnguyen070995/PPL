from functools import reduce

class ASTGeneration(Q1Visitor):
	def visitProg(self, ctx: Q1Parser.ProgContext):
		return Program([self.visit(x) for x in ctx.stmt])

	def visitStmt(self, ctx:Q1Parser.StmtContext):
		return Stmt(Id(ctx.ID().getText()), self.visit(ctx.exp()))

	def visitExp(self, ctx:Q1Parser.ExpContext):
		if ctx.ADDOP():
			merge = [(ctx.ADDOP(i), ctx.term(i + 1)) for in range(len(ctx.ADDOP()))]
			return reduce(lambda x,y: Add(x, self.visit(y[1])) if y[0] == '+' else Minus(x, self.visit(y[1])), merge, self.visit(ctx.term(0)))
		return self.visit(ctx.term(0))

	def visitExp(self, ctx:Q1Parse.ExpContext):
		if ctx.ASSIGN():
			lterm = ctx.term()[::-1]
			lAssign = ctx.ASSIGN()[::-1]
			merge = list(zip(lterm[1:],lAssign))
			return reduce(lambda x, y: Binary(y[1].getText(),self.visit(y[0]),x),merge,self.visit(lterm[0]))
		return self.
																	             

	def visitTerm(self, ctx:Q1Paerser.Term):
		if ctx.term() == 3:
			if ctx.MULOP().getText() == '*':
				return Mul(self.visit(ctx.term()), self.visit(ctx.fact))
			return Div(self.visit(ctx.term()), self.visit(ctx.fact))
		return self.visit(ctx.fact)

	def visitFact(self, ctx:Q1Parser.FactContext):
		if ctx.ID():
			return Id(ctx.ID().getText())
		elif ctx.INTLIT();
			return Intlit(ctx.INTLIT().getText())
		elif ctx.FLOATLIT();
			return Floatlit(ctx.FLOATLIT().getText())
		return self.visit(ctx.exp())
