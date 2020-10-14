# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\f\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\2\2\3\2\2\2")
        buf.write("\2\n\2\4\3\2\2\2\4\5\7\64\2\2\5\6\7\7\2\2\6\7\7:\2\2\7")
        buf.write("\b\7@\2\2\b\t\7\n\2\2\t\n\7\2\2\3\n\3\3\2\2\2\2")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'['", "']'", "':'", "'.'", 
                     "','", "';'", "'{'", "'}'", "'+'", "'+.'", "'-'", "'-.'", 
                     "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", "'&&'", 
                     "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'", "'Body'", 
                     "'Break'", "'Continue'", "'Do'", "'Else'", "'ElseIf'", 
                     "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", 
                     "'Function'", "'If'", "'Parameter'", "'Return'", "'Then'", 
                     "'Var'", "'While'", "'True'", "'False'", "'EndDo'" ]

    symbolicNames = [ "<INVALID>", "LP", "RP", "LB", "RB", "COLON", "DOT", 
                      "COMMA", "SEMI", "LCB", "RCB", "ADDOP", "ADDF", "SUBOP", 
                      "SUBF", "MULOP", "MULF", "DIVOP", "DIVF", "MODOP", 
                      "NOT", "CONJ", "DISJ", "EQ", "NEQ", "LT", "GT", "LTE", 
                      "GTE", "NEQF", "LTF", "GTF", "LTEF", "GTEF", "BODY", 
                      "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", 
                      "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", 
                      "IF", "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", 
                      "TRUE", "FALSE", "ENDDO", "INTERGER", "ID", "WS", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "UNTERMINATED_COMMENT", "REAL" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    LP=1
    RP=2
    LB=3
    RB=4
    COLON=5
    DOT=6
    COMMA=7
    SEMI=8
    LCB=9
    RCB=10
    ADDOP=11
    ADDF=12
    SUBOP=13
    SUBF=14
    MULOP=15
    MULF=16
    DIVOP=17
    DIVF=18
    MODOP=19
    NOT=20
    CONJ=21
    DISJ=22
    EQ=23
    NEQ=24
    LT=25
    GT=26
    LTE=27
    GTE=28
    NEQF=29
    LTF=30
    GTF=31
    LTEF=32
    GTEF=33
    BODY=34
    BREAK=35
    CONTINUE=36
    DO=37
    ELSE=38
    ELSEIF=39
    ENDBODY=40
    ENDIF=41
    ENDFOR=42
    ENDWHILE=43
    FOR=44
    FUNCTION=45
    IF=46
    PARAMETER=47
    RETURN=48
    THEN=49
    VAR=50
    WHILE=51
    TRUE=52
    FALSE=53
    ENDDO=54
    INTERGER=55
    ID=56
    WS=57
    ERROR_CHAR=58
    UNCLOSE_STRING=59
    ILLEGAL_ESCAPE=60
    UNTERMINATED_COMMENT=61
    REAL=62

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def REAL(self):
            return self.getToken(BKITParser.REAL, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(BKITParser.VAR)
            self.state = 3
            self.match(BKITParser.COLON)
            self.state = 4
            self.match(BKITParser.ID)
            self.state = 5
            self.match(BKITParser.REAL)
            self.state = 6
            self.match(BKITParser.SEMI)
            self.state = 7
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





