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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u01c5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\5\3n\n\3\3\4\3\4\3\4\3\4\3\4\5\4u\n\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\5\6\u0081\n\6")
        buf.write("\3\7\3\7\5\7\u0085\n\7\3\b\3\b\3\b\3\b\5\b\u008b\n\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\5\t\u0092\n\t\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\5\13\u009b\n\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\16\5\16\u00ab\n\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\5\17\u00b2\n\17\3\20\3\20\5\20\u00b6")
        buf.write("\n\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\5\22\u00c4\n\22\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\3\23\7\23\u00cd\n\23\f\23\16\23\u00d0\13\23\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\7\24\u00d9\n\24\f\24\16\24")
        buf.write("\u00dc\13\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u00e5")
        buf.write("\n\25\f\25\16\25\u00e8\13\25\3\26\3\26\3\26\5\26\u00ed")
        buf.write("\n\26\3\27\3\27\3\27\5\27\u00f2\n\27\3\30\3\30\3\30\3")
        buf.write("\30\3\30\7\30\u00f9\n\30\f\30\16\30\u00fc\13\30\3\31\3")
        buf.write("\31\3\31\3\31\3\31\5\31\u0103\n\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\5\32\u010c\n\32\3\33\3\33\3\33\3\33\3")
        buf.write("\33\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0119\n\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\5\35\u0120\n\35\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\5\36\u012b\n\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \5 \u0133\n \3 \3 \3 \3!\3!\3!\3!\5!\u013c")
        buf.write("\n!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3$\3")
        buf.write("$\3$\3$\3$\5$\u0151\n$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3")
        buf.write("&\5&\u015e\n&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\5(\u0173\n(\3(\3(\3")
        buf.write(")\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3+\3+\3")
        buf.write("+\3,\3,\3,\3-\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3")
        buf.write("\62\3\62\3\62\3\62\7\62\u019c\n\62\f\62\16\62\u019f\13")
        buf.write("\62\3\62\3\62\3\62\7\62\u01a4\n\62\f\62\16\62\u01a7\13")
        buf.write("\62\3\62\3\62\3\62\7\62\u01ac\n\62\f\62\16\62\u01af\13")
        buf.write("\62\3\62\3\62\3\62\7\62\u01b4\n\62\f\62\16\62\u01b7\13")
        buf.write("\62\3\62\3\62\3\62\7\62\u01bc\n\62\f\62\16\62\u01bf\13")
        buf.write("\62\5\62\u01c1\n\62\3\62\3\62\3\62\2\5$&(\63\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write(">@BDFHJLNPRTVXZ\\^`b\2\b\3\28;\3\2\17\20\3\2\21\25\3\2")
        buf.write("\r\20\3\2\27\30\3\2\31#\2\u01c8\2d\3\2\2\2\4m\3\2\2\2")
        buf.write("\6t\3\2\2\2\bv\3\2\2\2\n\u0080\3\2\2\2\f\u0084\3\2\2\2")
        buf.write("\16\u008a\3\2\2\2\20\u0091\3\2\2\2\22\u0093\3\2\2\2\24")
        buf.write("\u009a\3\2\2\2\26\u009c\3\2\2\2\30\u00a0\3\2\2\2\32\u00aa")
        buf.write("\3\2\2\2\34\u00b1\3\2\2\2\36\u00b5\3\2\2\2 \u00b7\3\2")
        buf.write("\2\2\"\u00c3\3\2\2\2$\u00c5\3\2\2\2&\u00d1\3\2\2\2(\u00dd")
        buf.write("\3\2\2\2*\u00ec\3\2\2\2,\u00f1\3\2\2\2.\u00f3\3\2\2\2")
        buf.write("\60\u0102\3\2\2\2\62\u010b\3\2\2\2\64\u010d\3\2\2\2\66")
        buf.write("\u0118\3\2\2\28\u011f\3\2\2\2:\u012a\3\2\2\2<\u012c\3")
        buf.write("\2\2\2>\u012f\3\2\2\2@\u013b\3\2\2\2B\u013d\3\2\2\2D\u0141")
        buf.write("\3\2\2\2F\u0150\3\2\2\2H\u0152\3\2\2\2J\u015d\3\2\2\2")
        buf.write("L\u015f\3\2\2\2N\u016f\3\2\2\2P\u0176\3\2\2\2R\u017e\3")
        buf.write("\2\2\2T\u0186\3\2\2\2V\u0189\3\2\2\2X\u018c\3\2\2\2Z\u018f")
        buf.write("\3\2\2\2\\\u0191\3\2\2\2^\u0193\3\2\2\2`\u0195\3\2\2\2")
        buf.write("b\u0197\3\2\2\2de\5\4\3\2ef\5\6\4\2fg\7\2\2\3g\3\3\2\2")
        buf.write("\2hi\5\b\5\2ij\5\4\3\2jn\3\2\2\2kn\5\b\5\2ln\3\2\2\2m")
        buf.write("h\3\2\2\2mk\3\2\2\2ml\3\2\2\2n\5\3\2\2\2op\5\30\r\2pq")
        buf.write("\5\6\4\2qu\3\2\2\2ru\5\30\r\2su\3\2\2\2to\3\2\2\2tr\3")
        buf.write("\2\2\2ts\3\2\2\2u\7\3\2\2\2vw\7\65\2\2wx\7\7\2\2xy\5\n")
        buf.write("\6\2yz\7\n\2\2z\t\3\2\2\2{|\5\f\7\2|}\7\t\2\2}~\5\n\6")
        buf.write("\2~\u0081\3\2\2\2\177\u0081\5\f\7\2\u0080{\3\2\2\2\u0080")
        buf.write("\177\3\2\2\2\u0081\13\3\2\2\2\u0082\u0085\5\16\b\2\u0083")
        buf.write("\u0085\5\20\t\2\u0084\u0082\3\2\2\2\u0084\u0083\3\2\2")
        buf.write("\2\u0085\r\3\2\2\2\u0086\u0087\7<\2\2\u0087\u0088\7$\2")
        buf.write("\2\u0088\u008b\t\2\2\2\u0089\u008b\7<\2\2\u008a\u0086")
        buf.write("\3\2\2\2\u008a\u0089\3\2\2\2\u008b\17\3\2\2\2\u008c\u008d")
        buf.write("\5\22\n\2\u008d\u008e\7$\2\2\u008e\u008f\5b\62\2\u008f")
        buf.write("\u0092\3\2\2\2\u0090\u0092\5\22\n\2\u0091\u008c\3\2\2")
        buf.write("\2\u0091\u0090\3\2\2\2\u0092\21\3\2\2\2\u0093\u0094\7")
        buf.write("<\2\2\u0094\u0095\5\24\13\2\u0095\23\3\2\2\2\u0096\u0097")
        buf.write("\5\26\f\2\u0097\u0098\5\24\13\2\u0098\u009b\3\2\2\2\u0099")
        buf.write("\u009b\5\26\f\2\u009a\u0096\3\2\2\2\u009a\u0099\3\2\2")
        buf.write("\2\u009b\25\3\2\2\2\u009c\u009d\7\5\2\2\u009d\u009e\7")
        buf.write("8\2\2\u009e\u009f\7\6\2\2\u009f\27\3\2\2\2\u00a0\u00a1")
        buf.write("\7\60\2\2\u00a1\u00a2\7\7\2\2\u00a2\u00a3\7<\2\2\u00a3")
        buf.write("\u00a4\5\32\16\2\u00a4\u00a5\5 \21\2\u00a5\31\3\2\2\2")
        buf.write("\u00a6\u00a7\7\62\2\2\u00a7\u00a8\7\7\2\2\u00a8\u00ab")
        buf.write("\5\34\17\2\u00a9\u00ab\3\2\2\2\u00aa\u00a6\3\2\2\2\u00aa")
        buf.write("\u00a9\3\2\2\2\u00ab\33\3\2\2\2\u00ac\u00ad\5\36\20\2")
        buf.write("\u00ad\u00ae\7\t\2\2\u00ae\u00af\5\34\17\2\u00af\u00b2")
        buf.write("\3\2\2\2\u00b0\u00b2\5\36\20\2\u00b1\u00ac\3\2\2\2\u00b1")
        buf.write("\u00b0\3\2\2\2\u00b2\35\3\2\2\2\u00b3\u00b6\7<\2\2\u00b4")
        buf.write("\u00b6\5\22\n\2\u00b5\u00b3\3\2\2\2\u00b5\u00b4\3\2\2")
        buf.write("\2\u00b6\37\3\2\2\2\u00b7\u00b8\7%\2\2\u00b8\u00b9\7\7")
        buf.write("\2\2\u00b9\u00ba\5\4\3\2\u00ba\u00bb\58\35\2\u00bb\u00bc")
        buf.write("\7+\2\2\u00bc\u00bd\7\b\2\2\u00bd!\3\2\2\2\u00be\u00bf")
        buf.write("\5$\23\2\u00bf\u00c0\5`\61\2\u00c0\u00c1\5$\23\2\u00c1")
        buf.write("\u00c4\3\2\2\2\u00c2\u00c4\5$\23\2\u00c3\u00be\3\2\2\2")
        buf.write("\u00c3\u00c2\3\2\2\2\u00c4#\3\2\2\2\u00c5\u00c6\b\23\1")
        buf.write("\2\u00c6\u00c7\5&\24\2\u00c7\u00ce\3\2\2\2\u00c8\u00c9")
        buf.write("\f\4\2\2\u00c9\u00ca\5^\60\2\u00ca\u00cb\5&\24\2\u00cb")
        buf.write("\u00cd\3\2\2\2\u00cc\u00c8\3\2\2\2\u00cd\u00d0\3\2\2\2")
        buf.write("\u00ce\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf%\3\2\2")
        buf.write("\2\u00d0\u00ce\3\2\2\2\u00d1\u00d2\b\24\1\2\u00d2\u00d3")
        buf.write("\5(\25\2\u00d3\u00da\3\2\2\2\u00d4\u00d5\f\4\2\2\u00d5")
        buf.write("\u00d6\5\\/\2\u00d6\u00d7\5(\25\2\u00d7\u00d9\3\2\2\2")
        buf.write("\u00d8\u00d4\3\2\2\2\u00d9\u00dc\3\2\2\2\u00da\u00d8\3")
        buf.write("\2\2\2\u00da\u00db\3\2\2\2\u00db\'\3\2\2\2\u00dc\u00da")
        buf.write("\3\2\2\2\u00dd\u00de\b\25\1\2\u00de\u00df\5*\26\2\u00df")
        buf.write("\u00e6\3\2\2\2\u00e0\u00e1\f\4\2\2\u00e1\u00e2\5Z.\2\u00e2")
        buf.write("\u00e3\5*\26\2\u00e3\u00e5\3\2\2\2\u00e4\u00e0\3\2\2\2")
        buf.write("\u00e5\u00e8\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e7\3")
        buf.write("\2\2\2\u00e7)\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e9\u00ea")
        buf.write("\7\26\2\2\u00ea\u00ed\5*\26\2\u00eb\u00ed\5,\27\2\u00ec")
        buf.write("\u00e9\3\2\2\2\u00ec\u00eb\3\2\2\2\u00ed+\3\2\2\2\u00ee")
        buf.write("\u00ef\t\3\2\2\u00ef\u00f2\5,\27\2\u00f0\u00f2\5.\30\2")
        buf.write("\u00f1\u00ee\3\2\2\2\u00f1\u00f0\3\2\2\2\u00f2-\3\2\2")
        buf.write("\2\u00f3\u00fa\5\60\31\2\u00f4\u00f5\7\5\2\2\u00f5\u00f6")
        buf.write("\5\"\22\2\u00f6\u00f7\7\6\2\2\u00f7\u00f9\3\2\2\2\u00f8")
        buf.write("\u00f4\3\2\2\2\u00f9\u00fc\3\2\2\2\u00fa\u00f8\3\2\2\2")
        buf.write("\u00fa\u00fb\3\2\2\2\u00fb/\3\2\2\2\u00fc\u00fa\3\2\2")
        buf.write("\2\u00fd\u00fe\7\3\2\2\u00fe\u00ff\5\"\22\2\u00ff\u0100")
        buf.write("\7\4\2\2\u0100\u0103\3\2\2\2\u0101\u0103\5\62\32\2\u0102")
        buf.write("\u00fd\3\2\2\2\u0102\u0101\3\2\2\2\u0103\61\3\2\2\2\u0104")
        buf.write("\u010c\7<\2\2\u0105\u010c\79\2\2\u0106\u010c\78\2\2\u0107")
        buf.write("\u010c\7:\2\2\u0108\u010c\7;\2\2\u0109\u010c\5b\62\2\u010a")
        buf.write("\u010c\5\64\33\2\u010b\u0104\3\2\2\2\u010b\u0105\3\2\2")
        buf.write("\2\u010b\u0106\3\2\2\2\u010b\u0107\3\2\2\2\u010b\u0108")
        buf.write("\3\2\2\2\u010b\u0109\3\2\2\2\u010b\u010a\3\2\2\2\u010c")
        buf.write("\63\3\2\2\2\u010d\u010e\7<\2\2\u010e\u010f\7\3\2\2\u010f")
        buf.write("\u0110\5\66\34\2\u0110\u0111\7\4\2\2\u0111\65\3\2\2\2")
        buf.write("\u0112\u0113\5\"\22\2\u0113\u0114\7\t\2\2\u0114\u0115")
        buf.write("\5\66\34\2\u0115\u0119\3\2\2\2\u0116\u0119\5\"\22\2\u0117")
        buf.write("\u0119\3\2\2\2\u0118\u0112\3\2\2\2\u0118\u0116\3\2\2\2")
        buf.write("\u0118\u0117\3\2\2\2\u0119\67\3\2\2\2\u011a\u011b\5:\36")
        buf.write("\2\u011b\u011c\58\35\2\u011c\u0120\3\2\2\2\u011d\u0120")
        buf.write("\5:\36\2\u011e\u0120\3\2\2\2\u011f\u011a\3\2\2\2\u011f")
        buf.write("\u011d\3\2\2\2\u011f\u011e\3\2\2\2\u01209\3\2\2\2\u0121")
        buf.write("\u012b\5D#\2\u0122\u012b\5<\37\2\u0123\u012b\5L\'\2\u0124")
        buf.write("\u012b\5T+\2\u0125\u012b\5V,\2\u0126\u012b\5N(\2\u0127")
        buf.write("\u012b\5P)\2\u0128\u012b\5R*\2\u0129\u012b\5X-\2\u012a")
        buf.write("\u0121\3\2\2\2\u012a\u0122\3\2\2\2\u012a\u0123\3\2\2\2")
        buf.write("\u012a\u0124\3\2\2\2\u012a\u0125\3\2\2\2\u012a\u0126\3")
        buf.write("\2\2\2\u012a\u0127\3\2\2\2\u012a\u0128\3\2\2\2\u012a\u0129")
        buf.write("\3\2\2\2\u012b;\3\2\2\2\u012c\u012d\5> \2\u012d\u012e")
        buf.write("\7\n\2\2\u012e=\3\2\2\2\u012f\u0132\5\"\22\2\u0130\u0133")
        buf.write("\5@!\2\u0131\u0133\3\2\2\2\u0132\u0130\3\2\2\2\u0132\u0131")
        buf.write("\3\2\2\2\u0133\u0134\3\2\2\2\u0134\u0135\7$\2\2\u0135")
        buf.write("\u0136\5\"\22\2\u0136?\3\2\2\2\u0137\u0138\5B\"\2\u0138")
        buf.write("\u0139\5@!\2\u0139\u013c\3\2\2\2\u013a\u013c\5B\"\2\u013b")
        buf.write("\u0137\3\2\2\2\u013b\u013a\3\2\2\2\u013cA\3\2\2\2\u013d")
        buf.write("\u013e\7\5\2\2\u013e\u013f\5\"\22\2\u013f\u0140\7\6\2")
        buf.write("\2\u0140C\3\2\2\2\u0141\u0142\7\61\2\2\u0142\u0143\5\"")
        buf.write("\22\2\u0143\u0144\7\64\2\2\u0144\u0145\5\4\3\2\u0145\u0146")
        buf.write("\58\35\2\u0146\u0147\5F$\2\u0147\u0148\5J&\2\u0148\u0149")
        buf.write("\7,\2\2\u0149\u014a\7\b\2\2\u014aE\3\2\2\2\u014b\u014c")
        buf.write("\5H%\2\u014c\u014d\5F$\2\u014d\u0151\3\2\2\2\u014e\u0151")
        buf.write("\5H%\2\u014f\u0151\3\2\2\2\u0150\u014b\3\2\2\2\u0150\u014e")
        buf.write("\3\2\2\2\u0150\u014f\3\2\2\2\u0151G\3\2\2\2\u0152\u0153")
        buf.write("\7*\2\2\u0153\u0154\5\"\22\2\u0154\u0155\7\64\2\2\u0155")
        buf.write("\u0156\5\4\3\2\u0156\u0157\58\35\2\u0157I\3\2\2\2\u0158")
        buf.write("\u0159\7)\2\2\u0159\u015a\5\4\3\2\u015a\u015b\58\35\2")
        buf.write("\u015b\u015e\3\2\2\2\u015c\u015e\3\2\2\2\u015d\u0158\3")
        buf.write("\2\2\2\u015d\u015c\3\2\2\2\u015eK\3\2\2\2\u015f\u0160")
        buf.write("\7/\2\2\u0160\u0161\7\3\2\2\u0161\u0162\7<\2\2\u0162\u0163")
        buf.write("\7$\2\2\u0163\u0164\5\"\22\2\u0164\u0165\7\t\2\2\u0165")
        buf.write("\u0166\5\"\22\2\u0166\u0167\7\t\2\2\u0167\u0168\5\"\22")
        buf.write("\2\u0168\u0169\7\4\2\2\u0169\u016a\7(\2\2\u016a\u016b")
        buf.write("\5\4\3\2\u016b\u016c\58\35\2\u016c\u016d\7-\2\2\u016d")
        buf.write("\u016e\7\b\2\2\u016eM\3\2\2\2\u016f\u0172\7\63\2\2\u0170")
        buf.write("\u0173\3\2\2\2\u0171\u0173\5\"\22\2\u0172\u0170\3\2\2")
        buf.write("\2\u0172\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0175")
        buf.write("\7\n\2\2\u0175O\3\2\2\2\u0176\u0177\7\66\2\2\u0177\u0178")
        buf.write("\5\"\22\2\u0178\u0179\7(\2\2\u0179\u017a\5\4\3\2\u017a")
        buf.write("\u017b\58\35\2\u017b\u017c\7.\2\2\u017c\u017d\7\b\2\2")
        buf.write("\u017dQ\3\2\2\2\u017e\u017f\7(\2\2\u017f\u0180\5\4\3\2")
        buf.write("\u0180\u0181\58\35\2\u0181\u0182\7\66\2\2\u0182\u0183")
        buf.write("\5\"\22\2\u0183\u0184\7\67\2\2\u0184\u0185\7\b\2\2\u0185")
        buf.write("S\3\2\2\2\u0186\u0187\7&\2\2\u0187\u0188\7\n\2\2\u0188")
        buf.write("U\3\2\2\2\u0189\u018a\7\'\2\2\u018a\u018b\7\n\2\2\u018b")
        buf.write("W\3\2\2\2\u018c\u018d\5\64\33\2\u018d\u018e\7\n\2\2\u018e")
        buf.write("Y\3\2\2\2\u018f\u0190\t\4\2\2\u0190[\3\2\2\2\u0191\u0192")
        buf.write("\t\5\2\2\u0192]\3\2\2\2\u0193\u0194\t\6\2\2\u0194_\3\2")
        buf.write("\2\2\u0195\u0196\t\7\2\2\u0196a\3\2\2\2\u0197\u01c0\7")
        buf.write("\13\2\2\u0198\u019d\78\2\2\u0199\u019a\7\t\2\2\u019a\u019c")
        buf.write("\78\2\2\u019b\u0199\3\2\2\2\u019c\u019f\3\2\2\2\u019d")
        buf.write("\u019b\3\2\2\2\u019d\u019e\3\2\2\2\u019e\u01c1\3\2\2\2")
        buf.write("\u019f\u019d\3\2\2\2\u01a0\u01a5\79\2\2\u01a1\u01a2\7")
        buf.write("\t\2\2\u01a2\u01a4\79\2\2\u01a3\u01a1\3\2\2\2\u01a4\u01a7")
        buf.write("\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6")
        buf.write("\u01c1\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a8\u01ad\7:\2\2")
        buf.write("\u01a9\u01aa\7\t\2\2\u01aa\u01ac\7:\2\2\u01ab\u01a9\3")
        buf.write("\2\2\2\u01ac\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae")
        buf.write("\3\2\2\2\u01ae\u01c1\3\2\2\2\u01af\u01ad\3\2\2\2\u01b0")
        buf.write("\u01b5\7;\2\2\u01b1\u01b2\7\t\2\2\u01b2\u01b4\7;\2\2\u01b3")
        buf.write("\u01b1\3\2\2\2\u01b4\u01b7\3\2\2\2\u01b5\u01b3\3\2\2\2")
        buf.write("\u01b5\u01b6\3\2\2\2\u01b6\u01c1\3\2\2\2\u01b7\u01b5\3")
        buf.write("\2\2\2\u01b8\u01bd\5b\62\2\u01b9\u01ba\7\t\2\2\u01ba\u01bc")
        buf.write("\5b\62\2\u01bb\u01b9\3\2\2\2\u01bc\u01bf\3\2\2\2\u01bd")
        buf.write("\u01bb\3\2\2\2\u01bd\u01be\3\2\2\2\u01be\u01c1\3\2\2\2")
        buf.write("\u01bf\u01bd\3\2\2\2\u01c0\u0198\3\2\2\2\u01c0\u01a0\3")
        buf.write("\2\2\2\u01c0\u01a8\3\2\2\2\u01c0\u01b0\3\2\2\2\u01c0\u01b8")
        buf.write("\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c3\7\f\2\2\u01c3")
        buf.write("c\3\2\2\2#mt\u0080\u0084\u008a\u0091\u009a\u00aa\u00b1")
        buf.write("\u00b5\u00c3\u00ce\u00da\u00e6\u00ec\u00f1\u00fa\u0102")
        buf.write("\u010b\u0118\u011f\u012a\u0132\u013b\u0150\u015d\u0172")
        buf.write("\u019d\u01a5\u01ad\u01b5\u01bd\u01c0")
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
                     "'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'", "'='", "'Body'", 
                     "'Break'", "'Continue'", "'Do'", "'Else'", "'ElseIf'", 
                     "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", 
                     "'Function'", "'If'", "'Parameter'", "'Return'", "'Then'", 
                     "'Var'", "'While'", "'EndDo'" ]

    symbolicNames = [ "<INVALID>", "LP", "RP", "LB", "RB", "COLON", "DOT", 
                      "COMMA", "SEMI", "LCB", "RCB", "ADDOP", "ADDF", "SUBOP", 
                      "SUBF", "MULOP", "MULF", "DIVOP", "DIVF", "MODOP", 
                      "NOT", "AND", "OR", "EQ", "NEQ", "LT", "GT", "LTE", 
                      "GTE", "NEQF", "LTF", "GTF", "LTEF", "GTEF", "ASSIG", 
                      "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", 
                      "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", 
                      "IF", "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", 
                      "ENDDO", "INTERGER", "FLOAT", "STRING", "BOOLEAN", 
                      "ID", "WS", "COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_var_dec_many = 1
    RULE_func_dec_many = 2
    RULE_var_dec = 3
    RULE_var_list = 4
    RULE_var_one = 5
    RULE_scalar_variable = 6
    RULE_composite_variable = 7
    RULE_composite_var_name = 8
    RULE_many_demension = 9
    RULE_one_demension = 10
    RULE_func_dec = 11
    RULE_params = 12
    RULE_param_list = 13
    RULE_param_one = 14
    RULE_func_body = 15
    RULE_expression = 16
    RULE_term1 = 17
    RULE_term2 = 18
    RULE_term3 = 19
    RULE_term4 = 20
    RULE_term5 = 21
    RULE_term6 = 22
    RULE_term7 = 23
    RULE_operand = 24
    RULE_callee = 25
    RULE_parameter_callee = 26
    RULE_statement_list = 27
    RULE_statement_part = 28
    RULE_assign_stm = 29
    RULE_assign = 30
    RULE_many_index = 31
    RULE_one_index = 32
    RULE_if_stm = 33
    RULE_elseif = 34
    RULE_elseif_one = 35
    RULE_else_one = 36
    RULE_for_stm = 37
    RULE_return_stm = 38
    RULE_while_stm = 39
    RULE_do_while_stm = 40
    RULE_break_stm = 41
    RULE_continue_stm = 42
    RULE_call_stm = 43
    RULE_multiplying = 44
    RULE_adding = 45
    RULE_logical = 46
    RULE_relational = 47
    RULE_array = 48

    ruleNames =  [ "program", "var_dec_many", "func_dec_many", "var_dec", 
                   "var_list", "var_one", "scalar_variable", "composite_variable", 
                   "composite_var_name", "many_demension", "one_demension", 
                   "func_dec", "params", "param_list", "param_one", "func_body", 
                   "expression", "term1", "term2", "term3", "term4", "term5", 
                   "term6", "term7", "operand", "callee", "parameter_callee", 
                   "statement_list", "statement_part", "assign_stm", "assign", 
                   "many_index", "one_index", "if_stm", "elseif", "elseif_one", 
                   "else_one", "for_stm", "return_stm", "while_stm", "do_while_stm", 
                   "break_stm", "continue_stm", "call_stm", "multiplying", 
                   "adding", "logical", "relational", "array" ]

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
    AND=21
    OR=22
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
    ASSIG=34
    BODY=35
    BREAK=36
    CONTINUE=37
    DO=38
    ELSE=39
    ELSEIF=40
    ENDBODY=41
    ENDIF=42
    ENDFOR=43
    ENDWHILE=44
    FOR=45
    FUNCTION=46
    IF=47
    PARAMETER=48
    RETURN=49
    THEN=50
    VAR=51
    WHILE=52
    ENDDO=53
    INTERGER=54
    FLOAT=55
    STRING=56
    BOOLEAN=57
    ID=58
    WS=59
    COMMENT=60
    ERROR_CHAR=61
    UNCLOSE_STRING=62
    ILLEGAL_ESCAPE=63
    UNTERMINATED_COMMENT=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_dec_many(self):
            return self.getTypedRuleContext(BKITParser.Var_dec_manyContext,0)


        def func_dec_many(self):
            return self.getTypedRuleContext(BKITParser.Func_dec_manyContext,0)


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
            self.state = 98
            self.var_dec_many()
            self.state = 99
            self.func_dec_many()
            self.state = 100
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_dec_manyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_dec(self):
            return self.getTypedRuleContext(BKITParser.Var_decContext,0)


        def var_dec_many(self):
            return self.getTypedRuleContext(BKITParser.Var_dec_manyContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_dec_many

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_dec_many" ):
                return visitor.visitVar_dec_many(self)
            else:
                return visitor.visitChildren(self)




    def var_dec_many(self):

        localctx = BKITParser.Var_dec_manyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_var_dec_many)
        try:
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.var_dec()
                self.state = 103
                self.var_dec_many()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.var_dec()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_dec_manyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_dec(self):
            return self.getTypedRuleContext(BKITParser.Func_decContext,0)


        def func_dec_many(self):
            return self.getTypedRuleContext(BKITParser.Func_dec_manyContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_dec_many

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_dec_many" ):
                return visitor.visitFunc_dec_many(self)
            else:
                return visitor.visitChildren(self)




    def func_dec_many(self):

        localctx = BKITParser.Func_dec_manyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_func_dec_many)
        try:
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.func_dec()
                self.state = 110
                self.func_dec_many()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.func_dec()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def var_list(self):
            return self.getTypedRuleContext(BKITParser.Var_listContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_var_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_dec" ):
                return visitor.visitVar_dec(self)
            else:
                return visitor.visitChildren(self)




    def var_dec(self):

        localctx = BKITParser.Var_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(BKITParser.VAR)
            self.state = 117
            self.match(BKITParser.COLON)
            self.state = 118
            self.var_list()
            self.state = 119
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_one(self):
            return self.getTypedRuleContext(BKITParser.Var_oneContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def var_list(self):
            return self.getTypedRuleContext(BKITParser.Var_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_list" ):
                return visitor.visitVar_list(self)
            else:
                return visitor.visitChildren(self)




    def var_list(self):

        localctx = BKITParser.Var_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_list)
        try:
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.var_one()
                self.state = 122
                self.match(BKITParser.COMMA)
                self.state = 123
                self.var_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.var_one()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_oneContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_variable(self):
            return self.getTypedRuleContext(BKITParser.Scalar_variableContext,0)


        def composite_variable(self):
            return self.getTypedRuleContext(BKITParser.Composite_variableContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_one

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_one" ):
                return visitor.visitVar_one(self)
            else:
                return visitor.visitChildren(self)




    def var_one(self):

        localctx = BKITParser.Var_oneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var_one)
        try:
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.scalar_variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.composite_variable()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_variableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ASSIG(self):
            return self.getToken(BKITParser.ASSIG, 0)

        def INTERGER(self):
            return self.getToken(BKITParser.INTERGER, 0)

        def FLOAT(self):
            return self.getToken(BKITParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(BKITParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKITParser.STRING, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_scalar_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_variable" ):
                return visitor.visitScalar_variable(self)
            else:
                return visitor.visitChildren(self)




    def scalar_variable(self):

        localctx = BKITParser.Scalar_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_scalar_variable)
        self._la = 0 # Token type
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.match(BKITParser.ID)
                self.state = 133
                self.match(BKITParser.ASSIG)
                self.state = 134
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.INTERGER) | (1 << BKITParser.FLOAT) | (1 << BKITParser.STRING) | (1 << BKITParser.BOOLEAN))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.match(BKITParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Composite_variableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def composite_var_name(self):
            return self.getTypedRuleContext(BKITParser.Composite_var_nameContext,0)


        def ASSIG(self):
            return self.getToken(BKITParser.ASSIG, 0)

        def array(self):
            return self.getTypedRuleContext(BKITParser.ArrayContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_composite_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComposite_variable" ):
                return visitor.visitComposite_variable(self)
            else:
                return visitor.visitChildren(self)




    def composite_variable(self):

        localctx = BKITParser.Composite_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_composite_variable)
        try:
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.composite_var_name()
                self.state = 139
                self.match(BKITParser.ASSIG)
                self.state = 140
                self.array()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.composite_var_name()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Composite_var_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def many_demension(self):
            return self.getTypedRuleContext(BKITParser.Many_demensionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_composite_var_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComposite_var_name" ):
                return visitor.visitComposite_var_name(self)
            else:
                return visitor.visitChildren(self)




    def composite_var_name(self):

        localctx = BKITParser.Composite_var_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_composite_var_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(BKITParser.ID)
            self.state = 146
            self.many_demension()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_demensionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def one_demension(self):
            return self.getTypedRuleContext(BKITParser.One_demensionContext,0)


        def many_demension(self):
            return self.getTypedRuleContext(BKITParser.Many_demensionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_many_demension

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_demension" ):
                return visitor.visitMany_demension(self)
            else:
                return visitor.visitChildren(self)




    def many_demension(self):

        localctx = BKITParser.Many_demensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_many_demension)
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.one_demension()
                self.state = 149
                self.many_demension()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.one_demension()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class One_demensionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def INTERGER(self):
            return self.getToken(BKITParser.INTERGER, 0)

        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_one_demension

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOne_demension" ):
                return visitor.visitOne_demension(self)
            else:
                return visitor.visitChildren(self)




    def one_demension(self):

        localctx = BKITParser.One_demensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_one_demension)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(BKITParser.LB)
            self.state = 155
            self.match(BKITParser.INTERGER)
            self.state = 156
            self.match(BKITParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_decContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def params(self):
            return self.getTypedRuleContext(BKITParser.ParamsContext,0)


        def func_body(self):
            return self.getTypedRuleContext(BKITParser.Func_bodyContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_dec" ):
                return visitor.visitFunc_dec(self)
            else:
                return visitor.visitChildren(self)




    def func_dec(self):

        localctx = BKITParser.Func_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_func_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(BKITParser.FUNCTION)
            self.state = 159
            self.match(BKITParser.COLON)
            self.state = 160
            self.match(BKITParser.ID)
            self.state = 161
            self.params()
            self.state = 162
            self.func_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def param_list(self):
            return self.getTypedRuleContext(BKITParser.Param_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = BKITParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_params)
        try:
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.PARAMETER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.match(BKITParser.PARAMETER)
                self.state = 165
                self.match(BKITParser.COLON)
                self.state = 166
                self.param_list()
                pass
            elif token in [BKITParser.BODY]:
                self.enterOuterAlt(localctx, 2)

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


    class Param_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_one(self):
            return self.getTypedRuleContext(BKITParser.Param_oneContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def param_list(self):
            return self.getTypedRuleContext(BKITParser.Param_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = BKITParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_param_list)
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.param_one()
                self.state = 171
                self.match(BKITParser.COMMA)
                self.state = 172
                self.param_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.param_one()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_oneContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def composite_var_name(self):
            return self.getTypedRuleContext(BKITParser.Composite_var_nameContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_param_one

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_one" ):
                return visitor.visitParam_one(self)
            else:
                return visitor.visitChildren(self)




    def param_one(self):

        localctx = BKITParser.Param_oneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_param_one)
        try:
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.composite_var_name()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def var_dec_many(self):
            return self.getTypedRuleContext(BKITParser.Var_dec_manyContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_func_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_body" ):
                return visitor.visitFunc_body(self)
            else:
                return visitor.visitChildren(self)




    def func_body(self):

        localctx = BKITParser.Func_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_func_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(BKITParser.BODY)
            self.state = 182
            self.match(BKITParser.COLON)
            self.state = 183
            self.var_dec_many()
            self.state = 184
            self.statement_list()
            self.state = 185
            self.match(BKITParser.ENDBODY)
            self.state = 186
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Term1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Term1Context,i)


        def relational(self):
            return self.getTypedRuleContext(BKITParser.RelationalContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = BKITParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expression)
        try:
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.term1(0)
                self.state = 189
                self.relational()
                self.state = 190
                self.term1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
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
            return self.getTypedRuleContext(BKITParser.Term2Context,0)


        def term1(self):
            return self.getTypedRuleContext(BKITParser.Term1Context,0)


        def logical(self):
            return self.getTypedRuleContext(BKITParser.LogicalContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_term1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm1" ):
                return visitor.visitTerm1(self)
            else:
                return visitor.visitChildren(self)



    def term1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Term1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_term1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.term2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 204
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Term1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term1)
                    self.state = 198
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 199
                    self.logical()
                    self.state = 200
                    self.term2(0) 
                self.state = 206
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
            return self.getTypedRuleContext(BKITParser.Term3Context,0)


        def term2(self):
            return self.getTypedRuleContext(BKITParser.Term2Context,0)


        def adding(self):
            return self.getTypedRuleContext(BKITParser.AddingContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_term2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm2" ):
                return visitor.visitTerm2(self)
            else:
                return visitor.visitChildren(self)



    def term2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Term2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_term2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.term3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 216
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Term2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term2)
                    self.state = 210
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 211
                    self.adding()
                    self.state = 212
                    self.term3(0) 
                self.state = 218
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

        def term4(self):
            return self.getTypedRuleContext(BKITParser.Term4Context,0)


        def term3(self):
            return self.getTypedRuleContext(BKITParser.Term3Context,0)


        def multiplying(self):
            return self.getTypedRuleContext(BKITParser.MultiplyingContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_term3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm3" ):
                return visitor.visitTerm3(self)
            else:
                return visitor.visitChildren(self)



    def term3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Term3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_term3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.term4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 228
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Term3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term3)
                    self.state = 222
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 223
                    self.multiplying()
                    self.state = 224
                    self.term4() 
                self.state = 230
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Term4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKITParser.NOT, 0)

        def term4(self):
            return self.getTypedRuleContext(BKITParser.Term4Context,0)


        def term5(self):
            return self.getTypedRuleContext(BKITParser.Term5Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_term4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm4" ):
                return visitor.visitTerm4(self)
            else:
                return visitor.visitChildren(self)




    def term4(self):

        localctx = BKITParser.Term4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_term4)
        try:
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.match(BKITParser.NOT)
                self.state = 232
                self.term4()
                pass
            elif token in [BKITParser.LP, BKITParser.LCB, BKITParser.SUBOP, BKITParser.SUBF, BKITParser.INTERGER, BKITParser.FLOAT, BKITParser.STRING, BKITParser.BOOLEAN, BKITParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.term5()
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


    class Term5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term5(self):
            return self.getTypedRuleContext(BKITParser.Term5Context,0)


        def SUBOP(self):
            return self.getToken(BKITParser.SUBOP, 0)

        def SUBF(self):
            return self.getToken(BKITParser.SUBF, 0)

        def term6(self):
            return self.getTypedRuleContext(BKITParser.Term6Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_term5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm5" ):
                return visitor.visitTerm5(self)
            else:
                return visitor.visitChildren(self)




    def term5(self):

        localctx = BKITParser.Term5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_term5)
        self._la = 0 # Token type
        try:
            self.state = 239
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.SUBOP, BKITParser.SUBF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                _la = self._input.LA(1)
                if not(_la==BKITParser.SUBOP or _la==BKITParser.SUBF):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 237
                self.term5()
                pass
            elif token in [BKITParser.LP, BKITParser.LCB, BKITParser.INTERGER, BKITParser.FLOAT, BKITParser.STRING, BKITParser.BOOLEAN, BKITParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                self.term6()
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


    class Term6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term7(self):
            return self.getTypedRuleContext(BKITParser.Term7Context,0)


        def LB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LB)
            else:
                return self.getToken(BKITParser.LB, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpressionContext,i)


        def RB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RB)
            else:
                return self.getToken(BKITParser.RB, i)

        def getRuleIndex(self):
            return BKITParser.RULE_term6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm6" ):
                return visitor.visitTerm6(self)
            else:
                return visitor.visitChildren(self)




    def term6(self):

        localctx = BKITParser.Term6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_term6)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.term7()
            self.state = 248
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 242
                    self.match(BKITParser.LB)
                    self.state = 243
                    self.expression()
                    self.state = 244
                    self.match(BKITParser.RB) 
                self.state = 250
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Term7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def operand(self):
            return self.getTypedRuleContext(BKITParser.OperandContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_term7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm7" ):
                return visitor.visitTerm7(self)
            else:
                return visitor.visitChildren(self)




    def term7(self):

        localctx = BKITParser.Term7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_term7)
        try:
            self.state = 256
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.match(BKITParser.LP)
                self.state = 252
                self.expression()
                self.state = 253
                self.match(BKITParser.RP)
                pass
            elif token in [BKITParser.LCB, BKITParser.INTERGER, BKITParser.FLOAT, BKITParser.STRING, BKITParser.BOOLEAN, BKITParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
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

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def FLOAT(self):
            return self.getToken(BKITParser.FLOAT, 0)

        def INTERGER(self):
            return self.getToken(BKITParser.INTERGER, 0)

        def STRING(self):
            return self.getToken(BKITParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(BKITParser.BOOLEAN, 0)

        def array(self):
            return self.getTypedRuleContext(BKITParser.ArrayContext,0)


        def callee(self):
            return self.getTypedRuleContext(BKITParser.CalleeContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = BKITParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_operand)
        try:
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.match(BKITParser.FLOAT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 260
                self.match(BKITParser.INTERGER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 261
                self.match(BKITParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 262
                self.match(BKITParser.BOOLEAN)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 263
                self.array()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 264
                self.callee()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CalleeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def parameter_callee(self):
            return self.getTypedRuleContext(BKITParser.Parameter_calleeContext,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_callee

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallee" ):
                return visitor.visitCallee(self)
            else:
                return visitor.visitChildren(self)




    def callee(self):

        localctx = BKITParser.CalleeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_callee)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(BKITParser.ID)
            self.state = 268
            self.match(BKITParser.LP)
            self.state = 269
            self.parameter_callee()
            self.state = 270
            self.match(BKITParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_calleeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def parameter_callee(self):
            return self.getTypedRuleContext(BKITParser.Parameter_calleeContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_parameter_callee

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_callee" ):
                return visitor.visitParameter_callee(self)
            else:
                return visitor.visitChildren(self)




    def parameter_callee(self):

        localctx = BKITParser.Parameter_calleeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_parameter_callee)
        try:
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.expression()
                self.state = 273
                self.match(BKITParser.COMMA)
                self.state = 274
                self.parameter_callee()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement_part(self):
            return self.getTypedRuleContext(BKITParser.Statement_partContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_statement_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_list" ):
                return visitor.visitStatement_list(self)
            else:
                return visitor.visitChildren(self)




    def statement_list(self):

        localctx = BKITParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_statement_list)
        try:
            self.state = 285
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.statement_part()
                self.state = 281
                self.statement_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self.statement_part()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_stm(self):
            return self.getTypedRuleContext(BKITParser.If_stmContext,0)


        def assign_stm(self):
            return self.getTypedRuleContext(BKITParser.Assign_stmContext,0)


        def for_stm(self):
            return self.getTypedRuleContext(BKITParser.For_stmContext,0)


        def break_stm(self):
            return self.getTypedRuleContext(BKITParser.Break_stmContext,0)


        def continue_stm(self):
            return self.getTypedRuleContext(BKITParser.Continue_stmContext,0)


        def return_stm(self):
            return self.getTypedRuleContext(BKITParser.Return_stmContext,0)


        def while_stm(self):
            return self.getTypedRuleContext(BKITParser.While_stmContext,0)


        def do_while_stm(self):
            return self.getTypedRuleContext(BKITParser.Do_while_stmContext,0)


        def call_stm(self):
            return self.getTypedRuleContext(BKITParser.Call_stmContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_statement_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_part" ):
                return visitor.visitStatement_part(self)
            else:
                return visitor.visitChildren(self)




    def statement_part(self):

        localctx = BKITParser.Statement_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_statement_part)
        try:
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.if_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
                self.assign_stm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 289
                self.for_stm()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 290
                self.break_stm()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 291
                self.continue_stm()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 292
                self.return_stm()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 293
                self.while_stm()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 294
                self.do_while_stm()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 295
                self.call_stm()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(BKITParser.AssignContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_assign_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stm" ):
                return visitor.visitAssign_stm(self)
            else:
                return visitor.visitChildren(self)




    def assign_stm(self):

        localctx = BKITParser.Assign_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_assign_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.assign()
            self.state = 299
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpressionContext,i)


        def ASSIG(self):
            return self.getToken(BKITParser.ASSIG, 0)

        def many_index(self):
            return self.getTypedRuleContext(BKITParser.Many_indexContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = BKITParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.expression()
            self.state = 304
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LB]:
                self.state = 302
                self.many_index()
                pass
            elif token in [BKITParser.ASSIG]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 306
            self.match(BKITParser.ASSIG)
            self.state = 307
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_indexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def one_index(self):
            return self.getTypedRuleContext(BKITParser.One_indexContext,0)


        def many_index(self):
            return self.getTypedRuleContext(BKITParser.Many_indexContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_many_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_index" ):
                return visitor.visitMany_index(self)
            else:
                return visitor.visitChildren(self)




    def many_index(self):

        localctx = BKITParser.Many_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_many_index)
        try:
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.one_index()
                self.state = 310
                self.many_index()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 312
                self.one_index()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class One_indexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_one_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOne_index" ):
                return visitor.visitOne_index(self)
            else:
                return visitor.visitChildren(self)




    def one_index(self):

        localctx = BKITParser.One_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_one_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(BKITParser.LB)
            self.state = 316
            self.expression()
            self.state = 317
            self.match(BKITParser.RB)
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

        def IF(self):
            return self.getToken(BKITParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def var_dec_many(self):
            return self.getTypedRuleContext(BKITParser.Var_dec_manyContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def elseif(self):
            return self.getTypedRuleContext(BKITParser.ElseifContext,0)


        def else_one(self):
            return self.getTypedRuleContext(BKITParser.Else_oneContext,0)


        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_if_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stm" ):
                return visitor.visitIf_stm(self)
            else:
                return visitor.visitChildren(self)




    def if_stm(self):

        localctx = BKITParser.If_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_if_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(BKITParser.IF)
            self.state = 320
            self.expression()
            self.state = 321
            self.match(BKITParser.THEN)
            self.state = 322
            self.var_dec_many()
            self.state = 323
            self.statement_list()
            self.state = 324
            self.elseif()
            self.state = 325
            self.else_one()
            self.state = 326
            self.match(BKITParser.ENDIF)
            self.state = 327
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseifContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elseif_one(self):
            return self.getTypedRuleContext(BKITParser.Elseif_oneContext,0)


        def elseif(self):
            return self.getTypedRuleContext(BKITParser.ElseifContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_elseif

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif" ):
                return visitor.visitElseif(self)
            else:
                return visitor.visitChildren(self)




    def elseif(self):

        localctx = BKITParser.ElseifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_elseif)
        try:
            self.state = 334
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 329
                self.elseif_one()
                self.state = 330
                self.elseif()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 332
                self.elseif_one()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_oneContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(BKITParser.ELSEIF, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def var_dec_many(self):
            return self.getTypedRuleContext(BKITParser.Var_dec_manyContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_elseif_one

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_one" ):
                return visitor.visitElseif_one(self)
            else:
                return visitor.visitChildren(self)




    def elseif_one(self):

        localctx = BKITParser.Elseif_oneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_elseif_one)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(BKITParser.ELSEIF)
            self.state = 337
            self.expression()
            self.state = 338
            self.match(BKITParser.THEN)
            self.state = 339
            self.var_dec_many()
            self.state = 340
            self.statement_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_oneContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def var_dec_many(self):
            return self.getTypedRuleContext(BKITParser.Var_dec_manyContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_else_one

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_one" ):
                return visitor.visitElse_one(self)
            else:
                return visitor.visitChildren(self)




    def else_one(self):

        localctx = BKITParser.Else_oneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_else_one)
        try:
            self.state = 347
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ELSE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
                self.match(BKITParser.ELSE)
                self.state = 343
                self.var_dec_many()
                self.state = 344
                self.statement_list()
                pass
            elif token in [BKITParser.ENDIF]:
                self.enterOuterAlt(localctx, 2)

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


    class For_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKITParser.FOR, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ASSIG(self):
            return self.getToken(BKITParser.ASSIG, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def var_dec_many(self):
            return self.getTypedRuleContext(BKITParser.Var_dec_manyContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def ENDFOR(self):
            return self.getToken(BKITParser.ENDFOR, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_for_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stm" ):
                return visitor.visitFor_stm(self)
            else:
                return visitor.visitChildren(self)




    def for_stm(self):

        localctx = BKITParser.For_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_for_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(BKITParser.FOR)
            self.state = 350
            self.match(BKITParser.LP)
            self.state = 351
            self.match(BKITParser.ID)
            self.state = 352
            self.match(BKITParser.ASSIG)
            self.state = 353
            self.expression()
            self.state = 354
            self.match(BKITParser.COMMA)
            self.state = 355
            self.expression()
            self.state = 356
            self.match(BKITParser.COMMA)
            self.state = 357
            self.expression()
            self.state = 358
            self.match(BKITParser.RP)
            self.state = 359
            self.match(BKITParser.DO)
            self.state = 360
            self.var_dec_many()
            self.state = 361
            self.statement_list()
            self.state = 362
            self.match(BKITParser.ENDFOR)
            self.state = 363
            self.match(BKITParser.DOT)
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

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_return_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stm" ):
                return visitor.visitReturn_stm(self)
            else:
                return visitor.visitChildren(self)




    def return_stm(self):

        localctx = BKITParser.Return_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_return_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(BKITParser.RETURN)
            self.state = 368
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.SEMI]:
                pass
            elif token in [BKITParser.LP, BKITParser.LCB, BKITParser.SUBOP, BKITParser.SUBF, BKITParser.NOT, BKITParser.INTERGER, BKITParser.FLOAT, BKITParser.STRING, BKITParser.BOOLEAN, BKITParser.ID]:
                self.state = 367
                self.expression()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 370
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def var_dec_many(self):
            return self.getTypedRuleContext(BKITParser.Var_dec_manyContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_while_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stm" ):
                return visitor.visitWhile_stm(self)
            else:
                return visitor.visitChildren(self)




    def while_stm(self):

        localctx = BKITParser.While_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_while_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.match(BKITParser.WHILE)
            self.state = 373
            self.expression()
            self.state = 374
            self.match(BKITParser.DO)
            self.state = 375
            self.var_dec_many()
            self.state = 376
            self.statement_list()
            self.state = 377
            self.match(BKITParser.ENDWHILE)
            self.state = 378
            self.match(BKITParser.DOT)
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

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def var_dec_many(self):
            return self.getTypedRuleContext(BKITParser.Var_dec_manyContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def ENDDO(self):
            return self.getToken(BKITParser.ENDDO, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_do_while_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_stm" ):
                return visitor.visitDo_while_stm(self)
            else:
                return visitor.visitChildren(self)




    def do_while_stm(self):

        localctx = BKITParser.Do_while_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_do_while_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(BKITParser.DO)
            self.state = 381
            self.var_dec_many()
            self.state = 382
            self.statement_list()
            self.state = 383
            self.match(BKITParser.WHILE)
            self.state = 384
            self.expression()
            self.state = 385
            self.match(BKITParser.ENDDO)
            self.state = 386
            self.match(BKITParser.DOT)
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

        def BREAK(self):
            return self.getToken(BKITParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_break_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stm" ):
                return visitor.visitBreak_stm(self)
            else:
                return visitor.visitChildren(self)




    def break_stm(self):

        localctx = BKITParser.Break_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_break_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(BKITParser.BREAK)
            self.state = 389
            self.match(BKITParser.SEMI)
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

        def CONTINUE(self):
            return self.getToken(BKITParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_continue_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stm" ):
                return visitor.visitContinue_stm(self)
            else:
                return visitor.visitChildren(self)




    def continue_stm(self):

        localctx = BKITParser.Continue_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_continue_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(BKITParser.CONTINUE)
            self.state = 392
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def callee(self):
            return self.getTypedRuleContext(BKITParser.CalleeContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_call_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stm" ):
                return visitor.visitCall_stm(self)
            else:
                return visitor.visitChildren(self)




    def call_stm(self):

        localctx = BKITParser.Call_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_call_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.callee()
            self.state = 395
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplyingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULOP(self):
            return self.getToken(BKITParser.MULOP, 0)

        def MULF(self):
            return self.getToken(BKITParser.MULF, 0)

        def DIVOP(self):
            return self.getToken(BKITParser.DIVOP, 0)

        def DIVF(self):
            return self.getToken(BKITParser.DIVF, 0)

        def MODOP(self):
            return self.getToken(BKITParser.MODOP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_multiplying

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplying" ):
                return visitor.visitMultiplying(self)
            else:
                return visitor.visitChildren(self)




    def multiplying(self):

        localctx = BKITParser.MultiplyingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_multiplying)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.MULOP) | (1 << BKITParser.MULF) | (1 << BKITParser.DIVOP) | (1 << BKITParser.DIVF) | (1 << BKITParser.MODOP))) != 0)):
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


    class AddingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADDOP(self):
            return self.getToken(BKITParser.ADDOP, 0)

        def ADDF(self):
            return self.getToken(BKITParser.ADDF, 0)

        def SUBOP(self):
            return self.getToken(BKITParser.SUBOP, 0)

        def SUBF(self):
            return self.getToken(BKITParser.SUBF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_adding

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdding" ):
                return visitor.visitAdding(self)
            else:
                return visitor.visitChildren(self)




    def adding(self):

        localctx = BKITParser.AddingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ADDOP) | (1 << BKITParser.ADDF) | (1 << BKITParser.SUBOP) | (1 << BKITParser.SUBF))) != 0)):
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


    class LogicalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(BKITParser.AND, 0)

        def OR(self):
            return self.getToken(BKITParser.OR, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_logical

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical" ):
                return visitor.visitLogical(self)
            else:
                return visitor.visitChildren(self)




    def logical(self):

        localctx = BKITParser.LogicalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_logical)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            _la = self._input.LA(1)
            if not(_la==BKITParser.AND or _la==BKITParser.OR):
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


    class RelationalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def NEQ(self):
            return self.getToken(BKITParser.NEQ, 0)

        def LT(self):
            return self.getToken(BKITParser.LT, 0)

        def GT(self):
            return self.getToken(BKITParser.GT, 0)

        def LTE(self):
            return self.getToken(BKITParser.LTE, 0)

        def GTE(self):
            return self.getToken(BKITParser.GTE, 0)

        def NEQF(self):
            return self.getToken(BKITParser.NEQF, 0)

        def LTF(self):
            return self.getToken(BKITParser.LTF, 0)

        def GTF(self):
            return self.getToken(BKITParser.GTF, 0)

        def LTEF(self):
            return self.getToken(BKITParser.LTEF, 0)

        def GTEF(self):
            return self.getToken(BKITParser.GTEF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_relational

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational" ):
                return visitor.visitRelational(self)
            else:
                return visitor.visitChildren(self)




    def relational(self):

        localctx = BKITParser.RelationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.EQ) | (1 << BKITParser.NEQ) | (1 << BKITParser.LT) | (1 << BKITParser.GT) | (1 << BKITParser.LTE) | (1 << BKITParser.GTE) | (1 << BKITParser.NEQF) | (1 << BKITParser.LTF) | (1 << BKITParser.GTF) | (1 << BKITParser.LTEF) | (1 << BKITParser.GTEF))) != 0)):
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


    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(BKITParser.LCB, 0)

        def RCB(self):
            return self.getToken(BKITParser.RCB, 0)

        def INTERGER(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.INTERGER)
            else:
                return self.getToken(BKITParser.INTERGER, i)

        def FLOAT(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.FLOAT)
            else:
                return self.getToken(BKITParser.FLOAT, i)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.STRING)
            else:
                return self.getToken(BKITParser.STRING, i)

        def BOOLEAN(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.BOOLEAN)
            else:
                return self.getToken(BKITParser.BOOLEAN, i)

        def array(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ArrayContext)
            else:
                return self.getTypedRuleContext(BKITParser.ArrayContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = BKITParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.match(BKITParser.LCB)
            self.state = 446
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.INTERGER]:
                self.state = 406
                self.match(BKITParser.INTERGER)
                self.state = 411
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 407
                    self.match(BKITParser.COMMA)
                    self.state = 408
                    self.match(BKITParser.INTERGER)
                    self.state = 413
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [BKITParser.FLOAT]:
                self.state = 414
                self.match(BKITParser.FLOAT)
                self.state = 419
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 415
                    self.match(BKITParser.COMMA)
                    self.state = 416
                    self.match(BKITParser.FLOAT)
                    self.state = 421
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [BKITParser.STRING]:
                self.state = 422
                self.match(BKITParser.STRING)
                self.state = 427
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 423
                    self.match(BKITParser.COMMA)
                    self.state = 424
                    self.match(BKITParser.STRING)
                    self.state = 429
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [BKITParser.BOOLEAN]:
                self.state = 430
                self.match(BKITParser.BOOLEAN)
                self.state = 435
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 431
                    self.match(BKITParser.COMMA)
                    self.state = 432
                    self.match(BKITParser.BOOLEAN)
                    self.state = 437
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [BKITParser.LCB]:
                self.state = 438
                self.array()
                self.state = 443
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 439
                    self.match(BKITParser.COMMA)
                    self.state = 440
                    self.array()
                    self.state = 445
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 448
            self.match(BKITParser.RCB)
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
        self._predicates[17] = self.term1_sempred
        self._predicates[18] = self.term2_sempred
        self._predicates[19] = self.term3_sempred
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
         

    def term3_sempred(self, localctx:Term3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




