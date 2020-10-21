from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *
from functools import reduce

class ASTGeneration(BKITVisitor):
    # program: varDeclarList functionList EOF
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        listvar = self.visit(ctx.varDeclarList())
        listfunc = self.visit(ctx.functionList())
        return Program(listvar + listfunc)

    # varDeclarList : noNullVarDeclarList | ;
    def visitVarDeclarList(self, ctx:BKITParser.VarDeclarListContext):
        if ctx.noNullVarDeclarList():
            return self.visit(ctx.noNullVarDeclarList())
        else:
            return []

    # noNullVarDeclarList: varDeclar noNullVarDeclarList| varDeclar;
    def visitNoNullVarDeclarList(self, ctx:BKITParser.NoNullVarDeclarListContext):
        varDeclar = self.visit(ctx.varDeclar())
        if ctx.noNullVarDeclarList():
            noNullVarDeclList = self.visit(ctx.noNullVarDeclarList())
            return varDeclar + noNullVarDeclList
        else:
            return varDeclar

            
    # varDeclar: VAR COLON varList SEMI
    def visitVarDeclar(self, ctx:BKITParser.VarDeclarContext):
        return self.visit(ctx.varList())

    # varList : var CM varList| var
    def visitVarList(self, ctx:BKITParser.VarListContext):
        var = self.visit(ctx.var())
        if ctx.varList():
            varList = self.visit(ctx.varList())
            return [var] + varList
        return [var]

    # var: nonInit| init
    def visitVar(self, ctx:BKITParser.VarContext):
        if ctx.nonInit():
            return self.visit(ctx.nonInit())
        else:
            return self.visit(ctx.init())

    # nonInit: ID| declarArray
    def visitNonInit(self, ctx:BKITParser.NonInitContext):
        if ctx.ID():
            id = Id(ctx.ID().getText())
            return VarDecl(id,[],None)
        else:
            return self.visit(ctx.declarArray())

    # init: ID EQUAL literals| declarArray EQUAL literals
    def visitInit(self, ctx:BKITParser.InitContext):
        if ctx.ID():
            id = Id(ctx.ID().getText())
            literals = self.visit(ctx.literals())
            return VarDecl(id,[],literals)
        else:
            declarArray = self.visit(ctx.declarArray())
            declarArray.varInit = self.visit(ctx.literals())
            return declarArray



    # literals: INTLIT| FLOATLIT| BOOLLIT| STRINGLIT
    def visitLiterals(self, ctx:BKITParser.LiteralsContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText(),0))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.BOOLLIT():
            return BooleanLiteral(ctx.BOOLLIT().getText() == "True")
        else:
            return StringLiteral(ctx.STRINGLIT().getText())

    # declarArray: ID arrayOper
    def visitDeclarArray(self, ctx:BKITParser.DeclarArrayContext):
        return VarDecl(Id(ctx.ID().getText()), self.visit(ctx.arrayOper()), None)

    # List(int)
    # arrayOper: LSB INTLIT RSB| LSB INTLIT RSB arrayOper
    def visitArrayOper(self, ctx:BKITParser.ArrayOperContext):
        intlit = int(ctx.INTLIT().getText(), 0)
        if ctx.getChildCount() == 3:
            return [intlit]
        else:
            return [intlit] + self.visit(ctx.arrayOper())

    #Object ArrayCell
    # elmexp: ID indexOper
    def visitElmexp(self, ctx:BKITParser.ElmexpContext):
        return ArrayCell(Id(ctx.ID().getText()), self.visit(ctx.indexOper()))

    #list(expression)
    # indexOper: LSB expression RSB| LSB expression RSB indexOper
    def visitIndexOper(self, ctx:BKITParser.IndexOperContext):
        expression = self.visit(ctx.expression())
        if ctx.getChildCount() == 3:
            return [expression]
        return [expression] + self.visit(ctx.indexOper())

    #return list
    # functionList: nonNullFunctionList| ;
    def visitFunctionList(self, ctx:BKITParser.FunctionListContext):
        if ctx.nonNullFunctionList():
            return self.visit(ctx.nonNullFunctionList())
        return []
       
    #return list funcDeclar
    # nonNullFunctionList: funcDeclar nonNullFunctionList| funcDeclar
    def visitNonNullFunctionList(self, ctx:BKITParser.NonNullFunctionListContext):
        funcDeclar = self.visit(ctx.funcDeclar())
        if ctx.getChildCount() == 1:
            return [funcDeclar]
        return [funcDeclar] + self.visit(ctx.nonNullFunctionList())
       
    # body: Tuple[List[VarDecl],List[Stmt]]
    # funcDeclar: FUNCTION COLON ID PARAMETER COLON pramList bodyFunc| FUNCTION COLON ID bodyFunc
    def visitFuncDeclar(self, ctx:BKITParser.FuncDeclarContext):
        name = Id(ctx.ID().getText())
        body = self.visit(ctx.bodyFunc())
        if ctx.PARAMETER():
            param = self.visit(ctx.pramList())
            return FuncDecl(name, param, body)
        return FuncDecl(name, [], body)
       

    # pramList: nonInit CM pramList| nonInit
    def visitPramList(self, ctx:BKITParser.PramListContext):
        param = self.visit(ctx.nonInit())
        if ctx.CM():
            return [param] + self.visit(ctx.pramList())
        return [param]       

    # bodyFunc: BEGINFUNC statemtList  ENDFUNC
    def visitBodyFunc(self, ctx:BKITParser.BodyFuncContext):
        return self.visit(ctx.statemtList())   

    # statemtList: varDeclarList otherStatementList
    def visitStatemtList(self, ctx:BKITParser.StatemtListContext):
        return (self.visit(ctx.varDeclarList()),self.visit(ctx.otherStatementList()))


    # otherStatementList: noNullOtherStatementList| ;
    def visitOtherStatementList(self, ctx:BKITParser.OtherStatementListContext):
        if ctx.noNullOtherStatementList():
            return self.visit(ctx.noNullOtherStatementList())
        return [] 


    # noNullOtherStatementList: otherStatement noNullOtherStatementList| otherStatement
    def visitNoNullOtherStatementList(self, ctx:BKITParser.NoNullOtherStatementListContext):
        otherStatement = self.visit(ctx.otherStatement())
        if ctx.noNullOtherStatementList():
            return [otherStatement] + self.visit(ctx.noNullOtherStatementList())
        return [otherStatement]

    # otherStatement: assignstm| ifStm| forStm| whileStm|doWhileStm| breakStm| continueStm| callStm| returnstm
    def visitOtherStatement(self, ctx:BKITParser.OtherStatementContext):
        return self.visit(ctx.getChild(0)) 
      

    # assignstm: variable EQUAL expression SEMI
    def visitAssignstm(self, ctx:BKITParser.AssignstmContext):
        return Assign(self.visit(ctx.variable()), self.visit(ctx.expression()))
       

    # variable: ID| elmexp
    def visitVariable(self, ctx:BKITParser.VariableContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.elmexp())

    # expression: expression EQINT expression2| expression NOTEQINT expression2| expression LESS expression2
    # | expression GREATER expression2| expression LESSEQINT expression2| expression GREATEREQINT expression2
    # | expression NOTEQF expression2| expression LESSF expression2| expression GREATERF expression2
    # | expression LESSEQF expression2| expression GREATEREQF expression2| expression2
    def visitExpression(self, ctx:BKITParser.ExpressionContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expression()), self.visit(ctx.expression2()))
        return self.visit(ctx.expression2())

    # class BinaryOp(Expr):
    # op:str
    # left:Expr
    # right:Expr
    # expression2: expression2 CONJ expression3| expression2 DISJ expression3| expression3 
    def visitExpression2(self, ctx:BKITParser.Expression2Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expression2()), self.visit(ctx.expression3()))
        return self.visit(ctx.expression3())

    # expression3
    # : expression3 ADDINT expression4
    # | expression3 ADDF expression4
    # | expression3 SUBINT expression4
    # | expression3 SUBF expression4
    # | expression4
    # ;
    def visitExpression3(self, ctx:BKITParser.Expression3Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expression3()), self.visit(ctx.expression4()))
        return self.visit(ctx.expression4())

    # expression4
    # : expression4 MULINT expression5
    # | expression4 MULF expression5
    # | expression4 DIVINT expression5
    # | expression4 DIVF expression5
    # | expression4 REINT expression5
    # | expression5
    # ;
    def visitExpression4(self, ctx:BKITParser.Expression4Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expression4()), self.visit(ctx.expression5()))
        return self.visit(ctx.expression5())

    # expression5
    # : NEG expression5
    # | expression6
    # ;
    # class UnaryOp(Expr):
    # op:str
    # body:Expr
    def visitExpression5(self, ctx:BKITParser.Expression5Context):
        if ctx.NEG():
            return UnaryOp(ctx.NEG().getText(), self.visit(ctx.expression5()))
        return self.visit(ctx.expression6())

    # expression6
    # : SUBINT expression6
    # | SUBF expression6
    # | expression7
    # ;
    def visitExpression6(self, ctx:BKITParser.Expression6Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.expression6()))
        return self.visit(ctx.expression7())

    # expression7
    # : ID
    # | literals
    # | LP expression RP
    # | elmexp
    # | callfunc
    # ;
    def visitExpression7(self, ctx:BKITParser.Expression7Context):
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.literals():
            return self.visit(ctx.literals())
        if ctx.expression():
            return self.visit(ctx.expression())
        if ctx.elmexp():
            return self.visit(ctx.elmexp())
        # self.visit(ctx.callfunc()) return a tubple 
        return CallExpr(*self.visit(ctx.callfunc()))
        # 
    # callfunc
    # : ID LP expList RP
    # ;
    def visitCallfunc(self, ctx:BKITParser.CallfuncContext):
        return (Id(ctx.ID().getText()), self.visit(ctx.expList()))
        # return CallStmt(Id(ctx.ID().getText()), self.visit(ctx.expList()))

    # expList
    # : nonNullExpList
    # | 
    # ;
    def visitExpList(self, ctx:BKITParser.ExpListContext):
        if ctx.nonNullExpList():
            return self.visit(ctx.nonNullExpList())
        return []

    # nonNullExpList
    # : expression CM nonNullExpList
    # | expression
    # ;
    def visitNonNullExpList(self, ctx:BKITParser.NonNullExpListContext):
        exp = self.visit(ctx.expression())
        if ctx.nonNullExpList():
            return [exp] + self.visit(ctx.nonNullExpList())
        return [exp]

    # If(Stmt):
    # """Expr is the condition, 
    #     List[VarDecl] is the list of declaration in the beginning of Then branch, empty list if no declaration
    #     List[Stmt] is the list of statement after the declaration in Then branch, empty list if no statement
    # """
    # ifthenStmt:List[Tuple[Expr,List[VarDecl],List[Stmt]]]
    # elseStmt:Tuple[List[VarDecl],List[Stmt]] # for Else branch, empty list if no Else

    # ifStm
    # : IF expression THEN statemtList (ELSEIF expression THEN statemtList)* (ELSE statemtList)? ENDIF DOT
    def visitIfStm(self, ctx:BKITParser.IfStmContext):
        exp = ctx.expression()
        statemtList = ctx.statemtList()
        if ctx.ELSE():
            expstmtList = list(zip(exp, statemtList[:-1]))
            stmtThen = [(self.visit(i[0]), *self.visit(i[1])) for i in expstmtList]
            stmtElse = self.visit(statemtList[-1])
            return If(stmtThen, stmtElse)
        expstmtList = list(zip(exp, statemtList))
        stmtThen = [(self.visit(i[0]), *self.visit(i[1])) for i in expstmtList]
        stmtElse = ([],[])
        return If(stmtThen, stmtElse)


    # For(Stmt):
    # idx1: Id
    # expr1:Expr
    # expr2:Expr
    # idx2: Id
    # expr3:Expr
    # loop: Tuple[List[VarDecl],List[Stmt]]

    # forStm
    # : FOR LP ID EQUAL expression CM expression CM ID EQUAL expression RP DO statemtList ENDFOR DOT
    # ;
    def visitForStm(self, ctx:BKITParser.ForStmContext):
        return For(
                Id(ctx.ID(0).getText()), 
                self.visit(ctx.expression(0)), 
                self.visit(ctx.expression(1)),
                Id(ctx.ID(1).getText()), 
                self.visit(ctx.expression(2)), 
                self.visit(ctx.statemtList())
            )

    #  While(Stmt):
    # exp: Expr
    # sl:Tuple[List[VarDecl],List[Stmt]]
    # whileStm
    # : WHILE expression DO statemtList ENDWHILE DOT
    # ;
    def visitWhileStm(self, ctx:BKITParser.WhileStmContext):
        return While(self.visit(ctx.expression()), self.visit(ctx.statemtList()))


    # Dowhile(Stmt):
    # sl:Tuple[List[VarDecl],List[Stmt]]
    # exp: Expr
    # doWhileStm
    # : DO statemtList WHILE expression SEMI
    # ;
    def visitDoWhileStm(self, ctx:BKITParser.DoWhileStmContext):
        return Dowhile(self.visit(ctx.statemtList()), self.visit(ctx.expression()))

     # breakStm
    # : BREAK SEMI
    # ;
    def visitBreakStm(self, ctx:BKITParser.BreakStmContext):
        return Break()

    # continueStm
    # : CONTINUE SEMI
    def visitContinueStm(self, ctx:BKITParser.ContinueStmContext):
        return Continue()

    # callStm
    # : callfunc SEMI
    # return CallStmt
    def visitCallStm(self, ctx:BKITParser.CallStmContext):
        return CallStmt(*self.visit(ctx.callfunc())) 

    # returnstm
    # : RETURN expression SEMI
        # | RETURN SEMI
    # ;
    def visitReturnstm(self, ctx:BKITParser.ReturnstmContext):
        if ctx.expression():
            return Return(self.visit(ctx.expression()))
        return Return(None)


