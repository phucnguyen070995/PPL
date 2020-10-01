# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("p\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\6\7\6-\n\6\f\6\16\6\60\13\6\3\7\3\7\3\7")
        buf.write("\3\7\7\7\66\n\7\f\7\16\79\13\7\3\7\3\7\3\b\6\b>\n\b\r")
        buf.write("\b\16\b?\3\b\3\b\6\bD\n\b\r\b\16\bE\3\b\3\b\5\bJ\n\b\3")
        buf.write("\b\3\b\3\b\5\bO\n\b\5\bQ\n\b\5\bS\n\b\3\b\6\bV\n\b\r\b")
        buf.write("\16\bW\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\13\3\f\6\fc\n")
        buf.write("\f\r\f\16\fd\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20")
        buf.write("\3\20\2\2\21\3\2\5\2\7\2\t\2\13\3\r\4\17\5\21\6\23\7\25")
        buf.write("\b\27\t\31\n\33\13\35\f\37\r\3\2\b\3\2c|\3\2\62;\3\2)")
        buf.write(")\4\2GGgg\4\2--//\5\2\13\f\17\17\"\"\2w\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\3!\3\2\2\2\5#\3\2\2\2\7%\3\2\2\2\t")
        buf.write("\'\3\2\2\2\13)\3\2\2\2\r\61\3\2\2\2\17=\3\2\2\2\21Y\3")
        buf.write("\2\2\2\23[\3\2\2\2\25]\3\2\2\2\27b\3\2\2\2\31h\3\2\2\2")
        buf.write("\33j\3\2\2\2\35l\3\2\2\2\37n\3\2\2\2!\"\t\2\2\2\"\4\3")
        buf.write("\2\2\2#$\t\3\2\2$\6\3\2\2\2%&\7)\2\2&\b\3\2\2\2\'(\7\60")
        buf.write("\2\2(\n\3\2\2\2).\5\3\2\2*-\5\3\2\2+-\5\5\3\2,*\3\2\2")
        buf.write("\2,+\3\2\2\2-\60\3\2\2\2.,\3\2\2\2./\3\2\2\2/\f\3\2\2")
        buf.write("\2\60.\3\2\2\2\61\67\7)\2\2\62\66\n\4\2\2\63\64\7)\2\2")
        buf.write("\64\66\7)\2\2\65\62\3\2\2\2\65\63\3\2\2\2\669\3\2\2\2")
        buf.write("\67\65\3\2\2\2\678\3\2\2\28:\3\2\2\29\67\3\2\2\2:;\7)")
        buf.write("\2\2;\16\3\2\2\2<>\5\5\3\2=<\3\2\2\2>?\3\2\2\2?=\3\2\2")
        buf.write("\2?@\3\2\2\2@R\3\2\2\2AC\5\t\5\2BD\5\5\3\2CB\3\2\2\2D")
        buf.write("E\3\2\2\2EC\3\2\2\2EF\3\2\2\2FG\3\2\2\2GI\t\5\2\2HJ\t")
        buf.write("\6\2\2IH\3\2\2\2IJ\3\2\2\2JS\3\2\2\2KQ\5\t\5\2LN\t\5\2")
        buf.write("\2MO\t\6\2\2NM\3\2\2\2NO\3\2\2\2OQ\3\2\2\2PK\3\2\2\2P")
        buf.write("L\3\2\2\2QS\3\2\2\2RA\3\2\2\2RP\3\2\2\2SU\3\2\2\2TV\5")
        buf.write("\5\3\2UT\3\2\2\2VW\3\2\2\2WU\3\2\2\2WX\3\2\2\2X\20\3\2")
        buf.write("\2\2YZ\7=\2\2Z\22\3\2\2\2[\\\7<\2\2\\\24\3\2\2\2]^\7X")
        buf.write("\2\2^_\7c\2\2_`\7t\2\2`\26\3\2\2\2ac\t\7\2\2ba\3\2\2\2")
        buf.write("cd\3\2\2\2db\3\2\2\2de\3\2\2\2ef\3\2\2\2fg\b\f\2\2g\30")
        buf.write("\3\2\2\2hi\13\2\2\2i\32\3\2\2\2jk\13\2\2\2k\34\3\2\2\2")
        buf.write("lm\13\2\2\2m\36\3\2\2\2no\13\2\2\2o \3\2\2\2\17\2,.\65")
        buf.write("\67?EINPRWd\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    STRING = 2
    REAL = 3
    SEMI = 4
    COLON = 5
    VAR = 6
    WS = 7
    ERROR_CHAR = 8
    UNCLOSE_STRING = 9
    ILLEGAL_ESCAPE = 10
    UNTERMINATED_COMMENT = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "':'", "'Var'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "STRING", "REAL", "SEMI", "COLON", "VAR", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "Letter", "Number", "SINGLEQUOTE", "DOT", "ID", "STRING", 
                  "REAL", "SEMI", "COLON", "VAR", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


