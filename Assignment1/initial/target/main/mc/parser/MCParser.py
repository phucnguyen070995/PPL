# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("\35\4\2\t\2\4\3\t\3\4\4\t\4\3\2\6\2\n\n\2\r\2\16\2\13")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5")
        buf.write("\4\33\n\4\3\4\2\2\5\2\4\6\2\2\2\35\2\t\3\2\2\2\4\17\3")
        buf.write("\2\2\2\6\32\3\2\2\2\b\n\5\4\3\2\t\b\3\2\2\2\n\13\3\2\2")
        buf.write("\2\13\t\3\2\2\2\13\f\3\2\2\2\f\r\3\2\2\2\r\16\7\2\2\3")
        buf.write("\16\3\3\2\2\2\17\20\5\6\4\2\20\21\7\b\2\2\21\22\5\6\4")
        buf.write("\2\22\5\3\2\2\2\23\33\7\n\2\2\24\33\7\3\2\2\25\33\7\4")
        buf.write("\2\2\26\27\7\5\2\2\27\30\5\4\3\2\30\31\7\6\2\2\31\33\3")
        buf.write("\2\2\2\32\23\3\2\2\2\32\24\3\2\2\2\32\25\3\2\2\2\32\26")
        buf.write("\3\2\2\2\33\7\3\2\2\2\4\13\32")
        return buf.getvalue()


class MCParser ( Parser ):

    grammarFileName = "MC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "INTLIT", "BOOLIT", "LB", "RB", "ANDOR", 
                      "ASSIGN", "COMPARE", "ID", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_exp = 1
    RULE_operand = 2

    ruleNames =  [ "program", "exp", "operand" ]

    EOF = Token.EOF
    INTLIT=1
    BOOLIT=2
    LB=3
    RB=4
    ANDOR=5
    ASSIGN=6
    COMPARE=7
    ID=8
    WS=9
    ERROR_CHAR=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MCParser.EOF, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ExpContext)
            else:
                return self.getTypedRuleContext(MCParser.ExpContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.exp()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTLIT) | (1 << MCParser.BOOLIT) | (1 << MCParser.LB) | (1 << MCParser.ID))) != 0)):
                    break

            self.state = 11
            self.match(MCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.OperandContext)
            else:
                return self.getTypedRuleContext(MCParser.OperandContext,i)


        def ASSIGN(self):
            return self.getToken(MCParser.ASSIGN, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = MCParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.operand()
            self.state = 14
            self.match(MCParser.ASSIGN)
            self.state = 15
            self.operand()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def BOOLIT(self):
            return self.getToken(MCParser.BOOLIT, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = MCParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_operand)
        try:
            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.match(MCParser.ID)
                pass
            elif token in [MCParser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.match(MCParser.INTLIT)
                pass
            elif token in [MCParser.BOOLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 19
                self.match(MCParser.BOOLIT)
                pass
            elif token in [MCParser.LB]:
                self.enterOuterAlt(localctx, 4)
                self.state = 20
                self.match(MCParser.LB)
                self.state = 21
                self.exp()
                self.state = 22
                self.match(MCParser.RB)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





