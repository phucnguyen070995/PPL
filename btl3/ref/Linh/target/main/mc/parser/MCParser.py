# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\61")
        buf.write("\u013e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \3\2\6\2B\n\2\r\2\16\2C\3\2\3\2\3\3\3")
        buf.write("\3\5\3J\n\3\3\4\3\4\3\4\3\4\3\4\3\4\7\4R\n\4\f\4\16\4")
        buf.write("U\13\4\5\4W\n\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\5")
        buf.write("\5b\n\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7n\n")
        buf.write("\7\3\b\3\b\7\br\n\b\f\b\16\bu\13\b\3\b\3\b\3\t\3\t\5\t")
        buf.write("{\n\t\3\n\3\n\3\n\3\n\7\n\u0081\n\n\f\n\16\n\u0084\13")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\5\13\u008d\n\13\3")
        buf.write("\f\3\f\3\f\3\f\3\f\5\f\u0094\n\f\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\7\r\u009c\n\r\f\r\16\r\u009f\13\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\7\16\u00a7\n\16\f\16\16\16\u00aa\13\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\5\17\u00b1\n\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\5\20\u00b8\n\20\3\21\3\21\3\21\3\21\3\21\3")
        buf.write("\21\7\21\u00c0\n\21\f\21\16\21\u00c3\13\21\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\7\22\u00cb\n\22\f\22\16\22\u00ce\13")
        buf.write("\22\3\23\3\23\3\23\5\23\u00d3\n\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\5\24\u00db\n\24\3\25\3\25\3\25\3\25\3\25\5")
        buf.write("\25\u00e2\n\25\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u00ea")
        buf.write("\n\26\3\27\3\27\3\27\3\27\3\27\7\27\u00f1\n\27\f\27\16")
        buf.write("\27\u00f4\13\27\5\27\u00f6\n\27\3\27\3\27\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\5\30\u010c\n\30\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\5\31\u011c\n\31\3\32\3\32\6\32\u0120\n\32\r\32\16")
        buf.write("\32\u0121\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36")
        buf.write("\5\36\u0138\n\36\3\37\3\37\3 \3 \3 \2\6\30\32 \"!\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>\2\b\4\2\24\24\34\34\4\2\25\26\35\36\4\2\20\20")
        buf.write("\30\30\4\2\21\21\31\32\4\2\22\22\30\30\4\2\13\13\r\17")
        buf.write("\2\u0144\2A\3\2\2\2\4I\3\2\2\2\6K\3\2\2\2\ba\3\2\2\2\n")
        buf.write("c\3\2\2\2\fm\3\2\2\2\16o\3\2\2\2\20z\3\2\2\2\22|\3\2\2")
        buf.write("\2\24\u008c\3\2\2\2\26\u0093\3\2\2\2\30\u0095\3\2\2\2")
        buf.write("\32\u00a0\3\2\2\2\34\u00b0\3\2\2\2\36\u00b7\3\2\2\2 \u00b9")
        buf.write("\3\2\2\2\"\u00c4\3\2\2\2$\u00d2\3\2\2\2&\u00da\3\2\2\2")
        buf.write("(\u00e1\3\2\2\2*\u00e9\3\2\2\2,\u00eb\3\2\2\2.\u010b\3")
        buf.write("\2\2\2\60\u011b\3\2\2\2\62\u011d\3\2\2\2\64\u0126\3\2")
        buf.write("\2\2\66\u0130\3\2\2\28\u0132\3\2\2\2:\u0137\3\2\2\2<\u0139")
        buf.write("\3\2\2\2>\u013b\3\2\2\2@B\5\4\3\2A@\3\2\2\2BC\3\2\2\2")
        buf.write("CA\3\2\2\2CD\3\2\2\2DE\3\2\2\2EF\7\2\2\3F\3\3\2\2\2GJ")
        buf.write("\5\22\n\2HJ\5\6\4\2IG\3\2\2\2IH\3\2\2\2J\5\3\2\2\2KL\5")
        buf.write("\b\5\2LM\5\n\6\2MV\7#\2\2NS\5\f\7\2OP\7&\2\2PR\5\f\7\2")
        buf.write("QO\3\2\2\2RU\3\2\2\2SQ\3\2\2\2ST\3\2\2\2TW\3\2\2\2US\3")
        buf.write("\2\2\2VN\3\2\2\2VW\3\2\2\2WX\3\2\2\2XY\7$\2\2YZ\5\16\b")
        buf.write("\2Z\7\3\2\2\2[b\5<\37\2\\]\5<\37\2]^\7\37\2\2^_\7 \2\2")
        buf.write("_b\3\2\2\2`b\7\f\2\2a[\3\2\2\2a\\\3\2\2\2a`\3\2\2\2b\t")
        buf.write("\3\2\2\2cd\7*\2\2d\13\3\2\2\2ef\5<\37\2fg\7*\2\2gn\3\2")
        buf.write("\2\2hi\5<\37\2ij\7*\2\2jk\7\37\2\2kl\7 \2\2ln\3\2\2\2")
        buf.write("me\3\2\2\2mh\3\2\2\2n\r\3\2\2\2os\7!\2\2pr\5\20\t\2qp")
        buf.write("\3\2\2\2ru\3\2\2\2sq\3\2\2\2st\3\2\2\2tv\3\2\2\2us\3\2")
        buf.write("\2\2vw\7\"\2\2w\17\3\2\2\2x{\5\22\n\2y{\5.\30\2zx\3\2")
        buf.write("\2\2zy\3\2\2\2{\21\3\2\2\2|}\5<\37\2}\u0082\5\24\13\2")
        buf.write("~\177\7&\2\2\177\u0081\5\24\13\2\u0080~\3\2\2\2\u0081")
        buf.write("\u0084\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0083\3\2\2\2")
        buf.write("\u0083\u0085\3\2\2\2\u0084\u0082\3\2\2\2\u0085\u0086\7")
        buf.write("%\2\2\u0086\23\3\2\2\2\u0087\u008d\7*\2\2\u0088\u0089")
        buf.write("\7*\2\2\u0089\u008a\7\37\2\2\u008a\u008b\7)\2\2\u008b")
        buf.write("\u008d\7 \2\2\u008c\u0087\3\2\2\2\u008c\u0088\3\2\2\2")
        buf.write("\u008d\25\3\2\2\2\u008e\u008f\5\30\r\2\u008f\u0090\7\27")
        buf.write("\2\2\u0090\u0091\5\26\f\2\u0091\u0094\3\2\2\2\u0092\u0094")
        buf.write("\5\30\r\2\u0093\u008e\3\2\2\2\u0093\u0092\3\2\2\2\u0094")
        buf.write("\27\3\2\2\2\u0095\u0096\b\r\1\2\u0096\u0097\5\32\16\2")
        buf.write("\u0097\u009d\3\2\2\2\u0098\u0099\f\4\2\2\u0099\u009a\7")
        buf.write("\23\2\2\u009a\u009c\5\32\16\2\u009b\u0098\3\2\2\2\u009c")
        buf.write("\u009f\3\2\2\2\u009d\u009b\3\2\2\2\u009d\u009e\3\2\2\2")
        buf.write("\u009e\31\3\2\2\2\u009f\u009d\3\2\2\2\u00a0\u00a1\b\16")
        buf.write("\1\2\u00a1\u00a2\5\34\17\2\u00a2\u00a8\3\2\2\2\u00a3\u00a4")
        buf.write("\f\4\2\2\u00a4\u00a5\7\33\2\2\u00a5\u00a7\5\34\17\2\u00a6")
        buf.write("\u00a3\3\2\2\2\u00a7\u00aa\3\2\2\2\u00a8\u00a6\3\2\2\2")
        buf.write("\u00a8\u00a9\3\2\2\2\u00a9\33\3\2\2\2\u00aa\u00a8\3\2")
        buf.write("\2\2\u00ab\u00ac\5\36\20\2\u00ac\u00ad\t\2\2\2\u00ad\u00ae")
        buf.write("\5\36\20\2\u00ae\u00b1\3\2\2\2\u00af\u00b1\5\36\20\2\u00b0")
        buf.write("\u00ab\3\2\2\2\u00b0\u00af\3\2\2\2\u00b1\35\3\2\2\2\u00b2")
        buf.write("\u00b3\5 \21\2\u00b3\u00b4\t\3\2\2\u00b4\u00b5\5 \21\2")
        buf.write("\u00b5\u00b8\3\2\2\2\u00b6\u00b8\5 \21\2\u00b7\u00b2\3")
        buf.write("\2\2\2\u00b7\u00b6\3\2\2\2\u00b8\37\3\2\2\2\u00b9\u00ba")
        buf.write("\b\21\1\2\u00ba\u00bb\5\"\22\2\u00bb\u00c1\3\2\2\2\u00bc")
        buf.write("\u00bd\f\4\2\2\u00bd\u00be\t\4\2\2\u00be\u00c0\5\"\22")
        buf.write("\2\u00bf\u00bc\3\2\2\2\u00c0\u00c3\3\2\2\2\u00c1\u00bf")
        buf.write("\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2!\3\2\2\2\u00c3\u00c1")
        buf.write("\3\2\2\2\u00c4\u00c5\b\22\1\2\u00c5\u00c6\5$\23\2\u00c6")
        buf.write("\u00cc\3\2\2\2\u00c7\u00c8\f\4\2\2\u00c8\u00c9\t\5\2\2")
        buf.write("\u00c9\u00cb\5$\23\2\u00ca\u00c7\3\2\2\2\u00cb\u00ce\3")
        buf.write("\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd#")
        buf.write("\3\2\2\2\u00ce\u00cc\3\2\2\2\u00cf\u00d0\t\6\2\2\u00d0")
        buf.write("\u00d3\5$\23\2\u00d1\u00d3\5&\24\2\u00d2\u00cf\3\2\2\2")
        buf.write("\u00d2\u00d1\3\2\2\2\u00d3%\3\2\2\2\u00d4\u00d5\5(\25")
        buf.write("\2\u00d5\u00d6\7\37\2\2\u00d6\u00d7\5\26\f\2\u00d7\u00d8")
        buf.write("\7 \2\2\u00d8\u00db\3\2\2\2\u00d9\u00db\5(\25\2\u00da")
        buf.write("\u00d4\3\2\2\2\u00da\u00d9\3\2\2\2\u00db\'\3\2\2\2\u00dc")
        buf.write("\u00dd\7#\2\2\u00dd\u00de\5\26\f\2\u00de\u00df\7$\2\2")
        buf.write("\u00df\u00e2\3\2\2\2\u00e0\u00e2\5*\26\2\u00e1\u00dc\3")
        buf.write("\2\2\2\u00e1\u00e0\3\2\2\2\u00e2)\3\2\2\2\u00e3\u00ea")
        buf.write("\7\'\2\2\u00e4\u00ea\7(\2\2\u00e5\u00ea\7)\2\2\u00e6\u00ea")
        buf.write("\7.\2\2\u00e7\u00ea\7*\2\2\u00e8\u00ea\5,\27\2\u00e9\u00e3")
        buf.write("\3\2\2\2\u00e9\u00e4\3\2\2\2\u00e9\u00e5\3\2\2\2\u00e9")
        buf.write("\u00e6\3\2\2\2\u00e9\u00e7\3\2\2\2\u00e9\u00e8\3\2\2\2")
        buf.write("\u00ea+\3\2\2\2\u00eb\u00ec\7*\2\2\u00ec\u00f5\7#\2\2")
        buf.write("\u00ed\u00f2\5\26\f\2\u00ee\u00ef\7&\2\2\u00ef\u00f1\5")
        buf.write("\26\f\2\u00f0\u00ee\3\2\2\2\u00f1\u00f4\3\2\2\2\u00f2")
        buf.write("\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f6\3\2\2\2")
        buf.write("\u00f4\u00f2\3\2\2\2\u00f5\u00ed\3\2\2\2\u00f5\u00f6\3")
        buf.write("\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f8\7$\2\2\u00f8-\3")
        buf.write("\2\2\2\u00f9\u010c\5\60\31\2\u00fa\u00fb\5\62\32\2\u00fb")
        buf.write("\u00fc\7%\2\2\u00fc\u010c\3\2\2\2\u00fd\u010c\5\64\33")
        buf.write("\2\u00fe\u00ff\5\66\34\2\u00ff\u0100\7%\2\2\u0100\u010c")
        buf.write("\3\2\2\2\u0101\u0102\58\35\2\u0102\u0103\7%\2\2\u0103")
        buf.write("\u010c\3\2\2\2\u0104\u0105\5:\36\2\u0105\u0106\7%\2\2")
        buf.write("\u0106\u010c\3\2\2\2\u0107\u0108\5\26\f\2\u0108\u0109")
        buf.write("\7%\2\2\u0109\u010c\3\2\2\2\u010a\u010c\5\16\b\2\u010b")
        buf.write("\u00f9\3\2\2\2\u010b\u00fa\3\2\2\2\u010b\u00fd\3\2\2\2")
        buf.write("\u010b\u00fe\3\2\2\2\u010b\u0101\3\2\2\2\u010b\u0104\3")
        buf.write("\2\2\2\u010b\u0107\3\2\2\2\u010b\u010a\3\2\2\2\u010c/")
        buf.write("\3\2\2\2\u010d\u010e\7\3\2\2\u010e\u010f\7#\2\2\u010f")
        buf.write("\u0110\5\26\f\2\u0110\u0111\7$\2\2\u0111\u0112\5.\30\2")
        buf.write("\u0112\u011c\3\2\2\2\u0113\u0114\7\3\2\2\u0114\u0115\7")
        buf.write("#\2\2\u0115\u0116\5\26\f\2\u0116\u0117\7$\2\2\u0117\u0118")
        buf.write("\5.\30\2\u0118\u0119\7\4\2\2\u0119\u011a\5.\30\2\u011a")
        buf.write("\u011c\3\2\2\2\u011b\u010d\3\2\2\2\u011b\u0113\3\2\2\2")
        buf.write("\u011c\61\3\2\2\2\u011d\u011f\7\5\2\2\u011e\u0120\5.\30")
        buf.write("\2\u011f\u011e\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u011f")
        buf.write("\3\2\2\2\u0121\u0122\3\2\2\2\u0122\u0123\3\2\2\2\u0123")
        buf.write("\u0124\7\6\2\2\u0124\u0125\5\26\f\2\u0125\63\3\2\2\2\u0126")
        buf.write("\u0127\7\7\2\2\u0127\u0128\7#\2\2\u0128\u0129\5\26\f\2")
        buf.write("\u0129\u012a\7%\2\2\u012a\u012b\5\26\f\2\u012b\u012c\7")
        buf.write("%\2\2\u012c\u012d\5\26\f\2\u012d\u012e\7$\2\2\u012e\u012f")
        buf.write("\5.\30\2\u012f\65\3\2\2\2\u0130\u0131\7\b\2\2\u0131\67")
        buf.write("\3\2\2\2\u0132\u0133\7\t\2\2\u01339\3\2\2\2\u0134\u0138")
        buf.write("\7\n\2\2\u0135\u0136\7\n\2\2\u0136\u0138\5\26\f\2\u0137")
        buf.write("\u0134\3\2\2\2\u0137\u0135\3\2\2\2\u0138;\3\2\2\2\u0139")
        buf.write("\u013a\t\7\2\2\u013a=\3\2\2\2\u013b\u013c\3\2\2\2\u013c")
        buf.write("?\3\2\2\2\35CISVamsz\u0082\u008c\u0093\u009d\u00a8\u00b0")
        buf.write("\u00b7\u00c1\u00cc\u00d2\u00da\u00e1\u00e9\u00f2\u00f5")
        buf.write("\u010b\u011b\u0121\u0137")
        return buf.getvalue()


class MCParser ( Parser ):

    grammarFileName = "MC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'do'", "'while'", "'for'", 
                     "'break'", "'continue'", "'return'", "'int'", "'void'", 
                     "'boolean'", "'float'", "'string'", "'+'", "'*'", "'!'", 
                     "'||'", "'!='", "'<'", "'<='", "'='", "'-'", "'/'", 
                     "'%'", "'&&'", "'=='", "'>'", "'>='", "'['", "']'", 
                     "'{'", "'}'", "'('", "')'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INTTYPE", "VOIDTYPE", "BOOLTYPE", "FLOATTYPE", 
                      "STRINGTYPE", "ADD", "MUL", "NOT", "OR", "NEQ", "LESS", 
                      "ELESS", "ASSIGN", "SUB", "DIV", "MOD", "AND", "EQ", 
                      "GREAT", "EGREAT", "LS", "RS", "LB", "RB", "LP", "RP", 
                      "SEMI", "CM", "BOOLLIT", "FLOATLIT", "INTLIT", "ID", 
                      "WS", "BLOCKCOMMENT", "LINECOMMENT", "STRINGLIT", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_func_decl = 2
    RULE_func_type = 3
    RULE_func_name = 4
    RULE_one_para = 5
    RULE_block_statement = 6
    RULE_statements = 7
    RULE_var_decl = 8
    RULE_one_variable = 9
    RULE_expression_stm = 10
    RULE_term1 = 11
    RULE_term2 = 12
    RULE_term3 = 13
    RULE_term4 = 14
    RULE_term5 = 15
    RULE_term6 = 16
    RULE_term7 = 17
    RULE_term8 = 18
    RULE_term9 = 19
    RULE_operand = 20
    RULE_invocation = 21
    RULE_statement = 22
    RULE_if_stm = 23
    RULE_do_while_stm = 24
    RULE_for_stm = 25
    RULE_break_stm = 26
    RULE_continue_stm = 27
    RULE_return_stm = 28
    RULE_primitive_type = 29
    RULE_func_call = 30

    ruleNames =  [ "program", "decl", "func_decl", "func_type", "func_name", 
                   "one_para", "block_statement", "statements", "var_decl", 
                   "one_variable", "expression_stm", "term1", "term2", "term3", 
                   "term4", "term5", "term6", "term7", "term8", "term9", 
                   "operand", "invocation", "statement", "if_stm", "do_while_stm", 
                   "for_stm", "break_stm", "continue_stm", "return_stm", 
                   "primitive_type", "func_call" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    INTTYPE=9
    VOIDTYPE=10
    BOOLTYPE=11
    FLOATTYPE=12
    STRINGTYPE=13
    ADD=14
    MUL=15
    NOT=16
    OR=17
    NEQ=18
    LESS=19
    ELESS=20
    ASSIGN=21
    SUB=22
    DIV=23
    MOD=24
    AND=25
    EQ=26
    GREAT=27
    EGREAT=28
    LS=29
    RS=30
    LB=31
    RB=32
    LP=33
    RP=34
    SEMI=35
    CM=36
    BOOLLIT=37
    FLOATLIT=38
    INTLIT=39
    ID=40
    WS=41
    BLOCKCOMMENT=42
    LINECOMMENT=43
    STRINGLIT=44
    UNCLOSE_STRING=45
    ILLEGAL_ESCAPE=46
    ERROR_CHAR=47

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

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.DeclContext)
            else:
                return self.getTypedRuleContext(MCParser.DeclContext,i)


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
            self.state = 63 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 62
                self.decl()
                self.state = 65 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTTYPE) | (1 << MCParser.VOIDTYPE) | (1 << MCParser.BOOLTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE))) != 0)):
                    break

            self.state = 67
            self.match(MCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MCParser.Var_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(MCParser.Func_declContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MCParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.func_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_type(self):
            return self.getTypedRuleContext(MCParser.Func_typeContext,0)


        def func_name(self):
            return self.getTypedRuleContext(MCParser.Func_nameContext,0)


        def LP(self):
            return self.getToken(MCParser.LP, 0)

        def RP(self):
            return self.getToken(MCParser.RP, 0)

        def block_statement(self):
            return self.getTypedRuleContext(MCParser.Block_statementContext,0)


        def one_para(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.One_paraContext)
            else:
                return self.getTypedRuleContext(MCParser.One_paraContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.CM)
            else:
                return self.getToken(MCParser.CM, i)

        def getRuleIndex(self):
            return MCParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = MCParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.func_type()
            self.state = 74
            self.func_name()
            self.state = 75
            self.match(MCParser.LP)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTTYPE) | (1 << MCParser.BOOLTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE))) != 0):
                self.state = 76
                self.one_para()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MCParser.CM:
                    self.state = 77
                    self.match(MCParser.CM)
                    self.state = 78
                    self.one_para()
                    self.state = 83
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 86
            self.match(MCParser.RP)
            self.state = 87
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MCParser.Primitive_typeContext,0)


        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def VOIDTYPE(self):
            return self.getToken(MCParser.VOIDTYPE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_func_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_type" ):
                return visitor.visitFunc_type(self)
            else:
                return visitor.visitChildren(self)




    def func_type(self):

        localctx = MCParser.Func_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_func_type)
        try:
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.primitive_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.primitive_type()
                self.state = 91
                self.match(MCParser.LS)
                self.state = 92
                self.match(MCParser.RS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self.match(MCParser.VOIDTYPE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def getRuleIndex(self):
            return MCParser.RULE_func_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_name" ):
                return visitor.visitFunc_name(self)
            else:
                return visitor.visitChildren(self)




    def func_name(self):

        localctx = MCParser.Func_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_func_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(MCParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class One_paraContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MCParser.Primitive_typeContext,0)


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def getRuleIndex(self):
            return MCParser.RULE_one_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOne_para" ):
                return visitor.visitOne_para(self)
            else:
                return visitor.visitChildren(self)




    def one_para(self):

        localctx = MCParser.One_paraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_one_para)
        try:
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.primitive_type()
                self.state = 100
                self.match(MCParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.primitive_type()
                self.state = 103
                self.match(MCParser.ID)
                self.state = 104
                self.match(MCParser.LS)
                self.state = 105
                self.match(MCParser.RS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StatementsContext)
            else:
                return self.getTypedRuleContext(MCParser.StatementsContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = MCParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(MCParser.LB)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.T__0) | (1 << MCParser.T__2) | (1 << MCParser.T__4) | (1 << MCParser.T__5) | (1 << MCParser.T__6) | (1 << MCParser.T__7) | (1 << MCParser.INTTYPE) | (1 << MCParser.BOOLTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE) | (1 << MCParser.NOT) | (1 << MCParser.SUB) | (1 << MCParser.LB) | (1 << MCParser.LP) | (1 << MCParser.BOOLLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.INTLIT) | (1 << MCParser.ID) | (1 << MCParser.STRINGLIT))) != 0):
                self.state = 110
                self.statements()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 116
            self.match(MCParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(MCParser.Var_declContext,0)


        def statement(self):
            return self.getTypedRuleContext(MCParser.StatementContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = MCParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_statements)
        try:
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.INTTYPE, MCParser.BOOLTYPE, MCParser.FLOATTYPE, MCParser.STRINGTYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.var_decl()
                pass
            elif token in [MCParser.T__0, MCParser.T__2, MCParser.T__4, MCParser.T__5, MCParser.T__6, MCParser.T__7, MCParser.NOT, MCParser.SUB, MCParser.LB, MCParser.LP, MCParser.BOOLLIT, MCParser.FLOATLIT, MCParser.INTLIT, MCParser.ID, MCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.statement()
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


    class Var_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MCParser.Primitive_typeContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def one_variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.One_variableContext)
            else:
                return self.getTypedRuleContext(MCParser.One_variableContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.CM)
            else:
                return self.getToken(MCParser.CM, i)

        def getRuleIndex(self):
            return MCParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = MCParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.primitive_type()

            self.state = 123
            self.one_variable()
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.CM:
                self.state = 124
                self.match(MCParser.CM)
                self.state = 125
                self.one_variable()
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 131
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class One_variableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def getRuleIndex(self):
            return MCParser.RULE_one_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOne_variable" ):
                return visitor.visitOne_variable(self)
            else:
                return visitor.visitChildren(self)




    def one_variable(self):

        localctx = MCParser.One_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_one_variable)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.match(MCParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.match(MCParser.ID)
                self.state = 135
                self.match(MCParser.LS)
                self.state = 136
                self.match(MCParser.INTLIT)
                self.state = 137
                self.match(MCParser.RS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term1(self):
            return self.getTypedRuleContext(MCParser.Term1Context,0)


        def ASSIGN(self):
            return self.getToken(MCParser.ASSIGN, 0)

        def expression_stm(self):
            return self.getTypedRuleContext(MCParser.Expression_stmContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_expression_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_stm" ):
                return visitor.visitExpression_stm(self)
            else:
                return visitor.visitChildren(self)




    def expression_stm(self):

        localctx = MCParser.Expression_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expression_stm)
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.term1(0)
                self.state = 141
                self.match(MCParser.ASSIGN)
                self.state = 142
                self.expression_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.term1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Term1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term2(self):
            return self.getTypedRuleContext(MCParser.Term2Context,0)


        def term1(self):
            return self.getTypedRuleContext(MCParser.Term1Context,0)


        def OR(self):
            return self.getToken(MCParser.OR, 0)

        def getRuleIndex(self):
            return MCParser.RULE_term1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm1" ):
                return visitor.visitTerm1(self)
            else:
                return visitor.visitChildren(self)



    def term1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Term1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_term1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.term2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 155
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Term1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term1)
                    self.state = 150
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 151
                    self.match(MCParser.OR)
                    self.state = 152
                    self.term2(0) 
                self.state = 157
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Term2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term3(self):
            return self.getTypedRuleContext(MCParser.Term3Context,0)


        def term2(self):
            return self.getTypedRuleContext(MCParser.Term2Context,0)


        def AND(self):
            return self.getToken(MCParser.AND, 0)

        def getRuleIndex(self):
            return MCParser.RULE_term2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm2" ):
                return visitor.visitTerm2(self)
            else:
                return visitor.visitChildren(self)



    def term2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Term2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_term2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.term3()
            self._ctx.stop = self._input.LT(-1)
            self.state = 166
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Term2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term2)
                    self.state = 161
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 162
                    self.match(MCParser.AND)
                    self.state = 163
                    self.term3() 
                self.state = 168
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Term3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term4(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Term4Context)
            else:
                return self.getTypedRuleContext(MCParser.Term4Context,i)


        def EQ(self):
            return self.getToken(MCParser.EQ, 0)

        def NEQ(self):
            return self.getToken(MCParser.NEQ, 0)

        def getRuleIndex(self):
            return MCParser.RULE_term3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm3" ):
                return visitor.visitTerm3(self)
            else:
                return visitor.visitChildren(self)




    def term3(self):

        localctx = MCParser.Term3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_term3)
        self._la = 0 # Token type
        try:
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.term4()
                self.state = 170
                _la = self._input.LA(1)
                if not(_la==MCParser.NEQ or _la==MCParser.EQ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 171
                self.term4()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.term4()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Term4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term5(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Term5Context)
            else:
                return self.getTypedRuleContext(MCParser.Term5Context,i)


        def LESS(self):
            return self.getToken(MCParser.LESS, 0)

        def ELESS(self):
            return self.getToken(MCParser.ELESS, 0)

        def GREAT(self):
            return self.getToken(MCParser.GREAT, 0)

        def EGREAT(self):
            return self.getToken(MCParser.EGREAT, 0)

        def getRuleIndex(self):
            return MCParser.RULE_term4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm4" ):
                return visitor.visitTerm4(self)
            else:
                return visitor.visitChildren(self)




    def term4(self):

        localctx = MCParser.Term4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_term4)
        self._la = 0 # Token type
        try:
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.term5(0)
                self.state = 177
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.LESS) | (1 << MCParser.ELESS) | (1 << MCParser.GREAT) | (1 << MCParser.EGREAT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 178
                self.term5(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.term5(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Term5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term6(self):
            return self.getTypedRuleContext(MCParser.Term6Context,0)


        def term5(self):
            return self.getTypedRuleContext(MCParser.Term5Context,0)


        def ADD(self):
            return self.getToken(MCParser.ADD, 0)

        def SUB(self):
            return self.getToken(MCParser.SUB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_term5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm5" ):
                return visitor.visitTerm5(self)
            else:
                return visitor.visitChildren(self)



    def term5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Term5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_term5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.term6(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 191
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Term5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term5)
                    self.state = 186
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 187
                    _la = self._input.LA(1)
                    if not(_la==MCParser.ADD or _la==MCParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 188
                    self.term6(0) 
                self.state = 193
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Term6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term7(self):
            return self.getTypedRuleContext(MCParser.Term7Context,0)


        def term6(self):
            return self.getTypedRuleContext(MCParser.Term6Context,0)


        def DIV(self):
            return self.getToken(MCParser.DIV, 0)

        def MUL(self):
            return self.getToken(MCParser.MUL, 0)

        def MOD(self):
            return self.getToken(MCParser.MOD, 0)

        def getRuleIndex(self):
            return MCParser.RULE_term6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm6" ):
                return visitor.visitTerm6(self)
            else:
                return visitor.visitChildren(self)



    def term6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Term6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_term6, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.term7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 202
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Term6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term6)
                    self.state = 197
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 198
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.MUL) | (1 << MCParser.DIV) | (1 << MCParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 199
                    self.term7() 
                self.state = 204
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Term7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term7(self):
            return self.getTypedRuleContext(MCParser.Term7Context,0)


        def SUB(self):
            return self.getToken(MCParser.SUB, 0)

        def NOT(self):
            return self.getToken(MCParser.NOT, 0)

        def term8(self):
            return self.getTypedRuleContext(MCParser.Term8Context,0)


        def getRuleIndex(self):
            return MCParser.RULE_term7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm7" ):
                return visitor.visitTerm7(self)
            else:
                return visitor.visitChildren(self)




    def term7(self):

        localctx = MCParser.Term7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_term7)
        self._la = 0 # Token type
        try:
            self.state = 208
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.NOT, MCParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                _la = self._input.LA(1)
                if not(_la==MCParser.NOT or _la==MCParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 206
                self.term7()
                pass
            elif token in [MCParser.LP, MCParser.BOOLLIT, MCParser.FLOATLIT, MCParser.INTLIT, MCParser.ID, MCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.term8()
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


    class Term8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term9(self):
            return self.getTypedRuleContext(MCParser.Term9Context,0)


        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def expression_stm(self):
            return self.getTypedRuleContext(MCParser.Expression_stmContext,0)


        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def getRuleIndex(self):
            return MCParser.RULE_term8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm8" ):
                return visitor.visitTerm8(self)
            else:
                return visitor.visitChildren(self)




    def term8(self):

        localctx = MCParser.Term8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_term8)
        try:
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.term9()

                self.state = 211
                self.match(MCParser.LS)
                self.state = 212
                self.expression_stm()
                self.state = 213
                self.match(MCParser.RS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.term9()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Term9Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MCParser.LP, 0)

        def expression_stm(self):
            return self.getTypedRuleContext(MCParser.Expression_stmContext,0)


        def RP(self):
            return self.getToken(MCParser.RP, 0)

        def operand(self):
            return self.getTypedRuleContext(MCParser.OperandContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_term9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm9" ):
                return visitor.visitTerm9(self)
            else:
                return visitor.visitChildren(self)




    def term9(self):

        localctx = MCParser.Term9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_term9)
        try:
            self.state = 223
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.match(MCParser.LP)
                self.state = 219
                self.expression_stm()
                self.state = 220
                self.match(MCParser.RP)
                pass
            elif token in [MCParser.BOOLLIT, MCParser.FLOATLIT, MCParser.INTLIT, MCParser.ID, MCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.operand()
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


    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLLIT(self):
            return self.getToken(MCParser.BOOLLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MCParser.FLOATLIT, 0)

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MCParser.STRINGLIT, 0)

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def invocation(self):
            return self.getTypedRuleContext(MCParser.InvocationContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = MCParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_operand)
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.match(MCParser.BOOLLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.match(MCParser.FLOATLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 227
                self.match(MCParser.INTLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 228
                self.match(MCParser.STRINGLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 229
                self.match(MCParser.ID)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 230
                self.invocation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InvocationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LP(self):
            return self.getToken(MCParser.LP, 0)

        def RP(self):
            return self.getToken(MCParser.RP, 0)

        def expression_stm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Expression_stmContext)
            else:
                return self.getTypedRuleContext(MCParser.Expression_stmContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.CM)
            else:
                return self.getToken(MCParser.CM, i)

        def getRuleIndex(self):
            return MCParser.RULE_invocation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInvocation" ):
                return visitor.visitInvocation(self)
            else:
                return visitor.visitChildren(self)




    def invocation(self):

        localctx = MCParser.InvocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_invocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(MCParser.ID)
            self.state = 234
            self.match(MCParser.LP)
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.NOT) | (1 << MCParser.SUB) | (1 << MCParser.LP) | (1 << MCParser.BOOLLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.INTLIT) | (1 << MCParser.ID) | (1 << MCParser.STRINGLIT))) != 0):
                self.state = 235
                self.expression_stm()
                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MCParser.CM:
                    self.state = 236
                    self.match(MCParser.CM)
                    self.state = 237
                    self.expression_stm()
                    self.state = 242
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 245
            self.match(MCParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_stm(self):
            return self.getTypedRuleContext(MCParser.If_stmContext,0)


        def do_while_stm(self):
            return self.getTypedRuleContext(MCParser.Do_while_stmContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def for_stm(self):
            return self.getTypedRuleContext(MCParser.For_stmContext,0)


        def break_stm(self):
            return self.getTypedRuleContext(MCParser.Break_stmContext,0)


        def continue_stm(self):
            return self.getTypedRuleContext(MCParser.Continue_stmContext,0)


        def return_stm(self):
            return self.getTypedRuleContext(MCParser.Return_stmContext,0)


        def expression_stm(self):
            return self.getTypedRuleContext(MCParser.Expression_stmContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(MCParser.Block_statementContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MCParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_statement)
        try:
            self.state = 265
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.if_stm()
                pass
            elif token in [MCParser.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.do_while_stm()
                self.state = 249
                self.match(MCParser.SEMI)
                pass
            elif token in [MCParser.T__4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 251
                self.for_stm()
                pass
            elif token in [MCParser.T__5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 252
                self.break_stm()
                self.state = 253
                self.match(MCParser.SEMI)
                pass
            elif token in [MCParser.T__6]:
                self.enterOuterAlt(localctx, 5)
                self.state = 255
                self.continue_stm()
                self.state = 256
                self.match(MCParser.SEMI)
                pass
            elif token in [MCParser.T__7]:
                self.enterOuterAlt(localctx, 6)
                self.state = 258
                self.return_stm()
                self.state = 259
                self.match(MCParser.SEMI)
                pass
            elif token in [MCParser.NOT, MCParser.SUB, MCParser.LP, MCParser.BOOLLIT, MCParser.FLOATLIT, MCParser.INTLIT, MCParser.ID, MCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 7)
                self.state = 261
                self.expression_stm()
                self.state = 262
                self.match(MCParser.SEMI)
                pass
            elif token in [MCParser.LB]:
                self.enterOuterAlt(localctx, 8)
                self.state = 264
                self.block_statement()
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


    class If_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MCParser.LP, 0)

        def expression_stm(self):
            return self.getTypedRuleContext(MCParser.Expression_stmContext,0)


        def RP(self):
            return self.getToken(MCParser.RP, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StatementContext)
            else:
                return self.getTypedRuleContext(MCParser.StatementContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_if_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stm" ):
                return visitor.visitIf_stm(self)
            else:
                return visitor.visitChildren(self)




    def if_stm(self):

        localctx = MCParser.If_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_if_stm)
        try:
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.match(MCParser.T__0)
                self.state = 268
                self.match(MCParser.LP)
                self.state = 269
                self.expression_stm()
                self.state = 270
                self.match(MCParser.RP)
                self.state = 271
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.match(MCParser.T__0)
                self.state = 274
                self.match(MCParser.LP)
                self.state = 275
                self.expression_stm()
                self.state = 276
                self.match(MCParser.RP)
                self.state = 277
                self.statement()
                self.state = 278
                self.match(MCParser.T__1)
                self.state = 279
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_stm(self):
            return self.getTypedRuleContext(MCParser.Expression_stmContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StatementContext)
            else:
                return self.getTypedRuleContext(MCParser.StatementContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_do_while_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_stm" ):
                return visitor.visitDo_while_stm(self)
            else:
                return visitor.visitChildren(self)




    def do_while_stm(self):

        localctx = MCParser.Do_while_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_do_while_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(MCParser.T__2)
            self.state = 285 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 284
                self.statement()
                self.state = 287 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.T__0) | (1 << MCParser.T__2) | (1 << MCParser.T__4) | (1 << MCParser.T__5) | (1 << MCParser.T__6) | (1 << MCParser.T__7) | (1 << MCParser.NOT) | (1 << MCParser.SUB) | (1 << MCParser.LB) | (1 << MCParser.LP) | (1 << MCParser.BOOLLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.INTLIT) | (1 << MCParser.ID) | (1 << MCParser.STRINGLIT))) != 0)):
                    break

            self.state = 289
            self.match(MCParser.T__3)
            self.state = 290
            self.expression_stm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MCParser.LP, 0)

        def expression_stm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Expression_stmContext)
            else:
                return self.getTypedRuleContext(MCParser.Expression_stmContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.SEMI)
            else:
                return self.getToken(MCParser.SEMI, i)

        def RP(self):
            return self.getToken(MCParser.RP, 0)

        def statement(self):
            return self.getTypedRuleContext(MCParser.StatementContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_for_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stm" ):
                return visitor.visitFor_stm(self)
            else:
                return visitor.visitChildren(self)




    def for_stm(self):

        localctx = MCParser.For_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_for_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(MCParser.T__4)
            self.state = 293
            self.match(MCParser.LP)
            self.state = 294
            self.expression_stm()
            self.state = 295
            self.match(MCParser.SEMI)
            self.state = 296
            self.expression_stm()
            self.state = 297
            self.match(MCParser.SEMI)
            self.state = 298
            self.expression_stm()
            self.state = 299
            self.match(MCParser.RP)
            self.state = 300
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MCParser.RULE_break_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stm" ):
                return visitor.visitBreak_stm(self)
            else:
                return visitor.visitChildren(self)




    def break_stm(self):

        localctx = MCParser.Break_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_break_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(MCParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MCParser.RULE_continue_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stm" ):
                return visitor.visitContinue_stm(self)
            else:
                return visitor.visitChildren(self)




    def continue_stm(self):

        localctx = MCParser.Continue_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_continue_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(MCParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_stm(self):
            return self.getTypedRuleContext(MCParser.Expression_stmContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_return_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stm" ):
                return visitor.visitReturn_stm(self)
            else:
                return visitor.visitChildren(self)




    def return_stm(self):

        localctx = MCParser.Return_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_return_stm)
        try:
            self.state = 309
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.match(MCParser.T__7)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 307
                self.match(MCParser.T__7)
                self.state = 308
                self.expression_stm()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(MCParser.INTTYPE, 0)

        def BOOLTYPE(self):
            return self.getToken(MCParser.BOOLTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(MCParser.FLOATTYPE, 0)

        def STRINGTYPE(self):
            return self.getToken(MCParser.STRINGTYPE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = MCParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTTYPE) | (1 << MCParser.BOOLTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MCParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = MCParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.term1_sempred
        self._predicates[12] = self.term2_sempred
        self._predicates[15] = self.term5_sempred
        self._predicates[16] = self.term6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def term1_sempred(self, localctx:Term1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def term2_sempred(self, localctx:Term2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def term5_sempred(self, localctx:Term5Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def term6_sempred(self, localctx:Term6Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




