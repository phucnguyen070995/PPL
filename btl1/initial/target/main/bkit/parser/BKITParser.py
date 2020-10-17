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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3J")
        buf.write("\u0196\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\5\3a\n\3\3\3\3\3\3\3\3\3\3\3\5\3h\n\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\5\3\5\5\5q\n\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\5\5x\n\5\3\6\3\6\3\6\3\6\5\6~\n\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\5\7\u0085\n\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\5\t\u008e")
        buf.write("\n\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\5\13\u0099")
        buf.write("\n\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\5\r\u00a3\n\r")
        buf.write("\3\r\3\r\3\r\3\r\5\r\u00a9\n\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\5\16\u00b4\n\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\5\17\u00bd\n\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\5\20\u00c4\n\20\3\21\3\21\3\21\3\21\3\21\3\21\3")
        buf.write("\21\7\21\u00cd\n\21\f\21\16\21\u00d0\13\21\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\7\22\u00d9\n\22\f\22\16\22\u00dc")
        buf.write("\13\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\7\23\u00e5\n")
        buf.write("\23\f\23\16\23\u00e8\13\23\3\24\3\24\3\24\5\24\u00ed\n")
        buf.write("\24\3\25\3\25\3\25\5\25\u00f2\n\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\7\26\u00fc\n\26\f\26\16\26\u00ff")
        buf.write("\13\26\3\27\3\27\3\27\3\27\3\27\5\27\u0106\n\27\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\5\30\u010f\n\30\3\31\3\31")
        buf.write("\5\31\u0113\n\31\3\31\3\31\3\31\5\31\u0118\n\31\3\31\3")
        buf.write("\31\3\32\3\32\3\32\3\32\3\32\5\32\u0121\n\32\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\5\34\u0129\n\34\3\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u0137")
        buf.write("\n\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\5\37\u0145\n\37\3\37\3\37\3\37\3 \3 \3 \3 ")
        buf.write("\3 \5 \u014f\n \3!\3!\3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\5$\u016b\n")
        buf.write("$\3$\3$\3%\3%\3%\3%\3%\3%\3%\5%\u0176\n%\3%\3%\3&\3&\3")
        buf.write("&\3&\3&\5&\u017f\n&\3&\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3")
        buf.write(")\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3-\2\6 \"$*.\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write(">@BDFHJLNPRTVX\2\t\4\2@BDD\3\2\27\30\3\2\3\n\3\2\31\35")
        buf.write("\3\2\25\30\3\2\37 \3\2!+\2\u019c\2Z\3\2\2\2\4g\3\2\2\2")
        buf.write("\6i\3\2\2\2\bw\3\2\2\2\n}\3\2\2\2\f\u0084\3\2\2\2\16\u0086")
        buf.write("\3\2\2\2\20\u008d\3\2\2\2\22\u008f\3\2\2\2\24\u0093\3")
        buf.write("\2\2\2\26\u009c\3\2\2\2\30\u00a8\3\2\2\2\32\u00aa\3\2")
        buf.write("\2\2\34\u00bc\3\2\2\2\36\u00c3\3\2\2\2 \u00c5\3\2\2\2")
        buf.write("\"\u00d1\3\2\2\2$\u00dd\3\2\2\2&\u00ec\3\2\2\2(\u00f1")
        buf.write("\3\2\2\2*\u00f3\3\2\2\2,\u0105\3\2\2\2.\u010e\3\2\2\2")
        buf.write("\60\u0112\3\2\2\2\62\u0120\3\2\2\2\64\u0122\3\2\2\2\66")
        buf.write("\u0128\3\2\2\28\u0136\3\2\2\2:\u0138\3\2\2\2<\u013d\3")
        buf.write("\2\2\2>\u014e\3\2\2\2@\u0150\3\2\2\2B\u0155\3\2\2\2D\u0158")
        buf.write("\3\2\2\2F\u016a\3\2\2\2H\u016e\3\2\2\2J\u0179\3\2\2\2")
        buf.write("L\u0184\3\2\2\2N\u0187\3\2\2\2P\u018a\3\2\2\2R\u018d\3")
        buf.write("\2\2\2T\u018f\3\2\2\2V\u0191\3\2\2\2X\u0193\3\2\2\2Z[")
        buf.write("\5\4\3\2[\\\7\2\2\3\\\3\3\2\2\2]a\5\6\4\2^a\5\24\13\2")
        buf.write("_a\5\66\34\2`]\3\2\2\2`^\3\2\2\2`_\3\2\2\2ab\3\2\2\2b")
        buf.write("c\5\4\3\2ch\3\2\2\2dh\5\6\4\2eh\5\24\13\2fh\5\66\34\2")
        buf.write("g`\3\2\2\2gd\3\2\2\2ge\3\2\2\2gf\3\2\2\2h\5\3\2\2\2ij")
        buf.write("\7=\2\2jk\7\17\2\2kl\5\b\5\2lm\7\22\2\2m\7\3\2\2\2nq\5")
        buf.write("\n\6\2oq\5\f\7\2pn\3\2\2\2po\3\2\2\2qr\3\2\2\2rs\7\21")
        buf.write("\2\2st\5\b\5\2tx\3\2\2\2ux\5\n\6\2vx\5\f\7\2wp\3\2\2\2")
        buf.write("wu\3\2\2\2wv\3\2\2\2x\t\3\2\2\2yz\7E\2\2z{\7,\2\2{~\t")
        buf.write("\2\2\2|~\7E\2\2}y\3\2\2\2}|\3\2\2\2~\13\3\2\2\2\177\u0080")
        buf.write("\5\16\b\2\u0080\u0081\7,\2\2\u0081\u0082\7C\2\2\u0082")
        buf.write("\u0085\3\2\2\2\u0083\u0085\5\16\b\2\u0084\177\3\2\2\2")
        buf.write("\u0084\u0083\3\2\2\2\u0085\r\3\2\2\2\u0086\u0087\7E\2")
        buf.write("\2\u0087\u0088\5\20\t\2\u0088\17\3\2\2\2\u0089\u008a\5")
        buf.write("\22\n\2\u008a\u008b\5\20\t\2\u008b\u008e\3\2\2\2\u008c")
        buf.write("\u008e\5\22\n\2\u008d\u0089\3\2\2\2\u008d\u008c\3\2\2")
        buf.write("\2\u008e\21\3\2\2\2\u008f\u0090\7\r\2\2\u0090\u0091\7")
        buf.write("@\2\2\u0091\u0092\7\16\2\2\u0092\23\3\2\2\2\u0093\u0094")
        buf.write("\78\2\2\u0094\u0098\7\17\2\2\u0095\u0099\7E\2\2\u0096")
        buf.write("\u0097\7E\2\2\u0097\u0099\5\26\f\2\u0098\u0095\3\2\2\2")
        buf.write("\u0098\u0096\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b\5")
        buf.write("\32\16\2\u009b\25\3\2\2\2\u009c\u009d\7:\2\2\u009d\u009e")
        buf.write("\7\17\2\2\u009e\u009f\5\30\r\2\u009f\27\3\2\2\2\u00a0")
        buf.write("\u00a3\7E\2\2\u00a1\u00a3\5\16\b\2\u00a2\u00a0\3\2\2\2")
        buf.write("\u00a2\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a5\7")
        buf.write("\21\2\2\u00a5\u00a9\5\30\r\2\u00a6\u00a9\7E\2\2\u00a7")
        buf.write("\u00a9\5\16\b\2\u00a8\u00a2\3\2\2\2\u00a8\u00a6\3\2\2")
        buf.write("\2\u00a8\u00a7\3\2\2\2\u00a9\31\3\2\2\2\u00aa\u00b3\7")
        buf.write("-\2\2\u00ab\u00ac\7\17\2\2\u00ac\u00b4\5\34\17\2\u00ad")
        buf.write("\u00ae\7\17\2\2\u00ae\u00b4\5\66\34\2\u00af\u00b0\7\17")
        buf.write("\2\2\u00b0\u00b1\5\34\17\2\u00b1\u00b2\5\66\34\2\u00b2")
        buf.write("\u00b4\3\2\2\2\u00b3\u00ab\3\2\2\2\u00b3\u00ad\3\2\2\2")
        buf.write("\u00b3\u00af\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b6\7")
        buf.write("\63\2\2\u00b6\u00b7\7\20\2\2\u00b7\33\3\2\2\2\u00b8\u00b9")
        buf.write("\5\6\4\2\u00b9\u00ba\5\34\17\2\u00ba\u00bd\3\2\2\2\u00bb")
        buf.write("\u00bd\5\6\4\2\u00bc\u00b8\3\2\2\2\u00bc\u00bb\3\2\2\2")
        buf.write("\u00bd\35\3\2\2\2\u00be\u00bf\5 \21\2\u00bf\u00c0\5X-")
        buf.write("\2\u00c0\u00c1\5 \21\2\u00c1\u00c4\3\2\2\2\u00c2\u00c4")
        buf.write("\5 \21\2\u00c3\u00be\3\2\2\2\u00c3\u00c2\3\2\2\2\u00c4")
        buf.write("\37\3\2\2\2\u00c5\u00c6\b\21\1\2\u00c6\u00c7\5\"\22\2")
        buf.write("\u00c7\u00ce\3\2\2\2\u00c8\u00c9\f\4\2\2\u00c9\u00ca\5")
        buf.write("V,\2\u00ca\u00cb\5\"\22\2\u00cb\u00cd\3\2\2\2\u00cc\u00c8")
        buf.write("\3\2\2\2\u00cd\u00d0\3\2\2\2\u00ce\u00cc\3\2\2\2\u00ce")
        buf.write("\u00cf\3\2\2\2\u00cf!\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d1")
        buf.write("\u00d2\b\22\1\2\u00d2\u00d3\5$\23\2\u00d3\u00da\3\2\2")
        buf.write("\2\u00d4\u00d5\f\4\2\2\u00d5\u00d6\5T+\2\u00d6\u00d7\5")
        buf.write("$\23\2\u00d7\u00d9\3\2\2\2\u00d8\u00d4\3\2\2\2\u00d9\u00dc")
        buf.write("\3\2\2\2\u00da\u00d8\3\2\2\2\u00da\u00db\3\2\2\2\u00db")
        buf.write("#\3\2\2\2\u00dc\u00da\3\2\2\2\u00dd\u00de\b\23\1\2\u00de")
        buf.write("\u00df\5&\24\2\u00df\u00e6\3\2\2\2\u00e0\u00e1\f\4\2\2")
        buf.write("\u00e1\u00e2\5R*\2\u00e2\u00e3\5&\24\2\u00e3\u00e5\3\2")
        buf.write("\2\2\u00e4\u00e0\3\2\2\2\u00e5\u00e8\3\2\2\2\u00e6\u00e4")
        buf.write("\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7%\3\2\2\2\u00e8\u00e6")
        buf.write("\3\2\2\2\u00e9\u00ea\7\36\2\2\u00ea\u00ed\5&\24\2\u00eb")
        buf.write("\u00ed\5(\25\2\u00ec\u00e9\3\2\2\2\u00ec\u00eb\3\2\2\2")
        buf.write("\u00ed\'\3\2\2\2\u00ee\u00ef\t\3\2\2\u00ef\u00f2\5(\25")
        buf.write("\2\u00f0\u00f2\5*\26\2\u00f1\u00ee\3\2\2\2\u00f1\u00f0")
        buf.write("\3\2\2\2\u00f2)\3\2\2\2\u00f3\u00f4\b\26\1\2\u00f4\u00f5")
        buf.write("\5,\27\2\u00f5\u00fd\3\2\2\2\u00f6\u00f7\f\4\2\2\u00f7")
        buf.write("\u00f8\7\r\2\2\u00f8\u00f9\5\36\20\2\u00f9\u00fa\7\16")
        buf.write("\2\2\u00fa\u00fc\3\2\2\2\u00fb\u00f6\3\2\2\2\u00fc\u00ff")
        buf.write("\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe")
        buf.write("+\3\2\2\2\u00ff\u00fd\3\2\2\2\u0100\u0101\7\13\2\2\u0101")
        buf.write("\u0102\5\36\20\2\u0102\u0103\7\f\2\2\u0103\u0106\3\2\2")
        buf.write("\2\u0104\u0106\5.\30\2\u0105\u0100\3\2\2\2\u0105\u0104")
        buf.write("\3\2\2\2\u0106-\3\2\2\2\u0107\u010f\7E\2\2\u0108\u010f")
        buf.write("\7A\2\2\u0109\u010f\7@\2\2\u010a\u010f\7B\2\2\u010b\u010f")
        buf.write("\7D\2\2\u010c\u010f\7C\2\2\u010d\u010f\5\60\31\2\u010e")
        buf.write("\u0107\3\2\2\2\u010e\u0108\3\2\2\2\u010e\u0109\3\2\2\2")
        buf.write("\u010e\u010a\3\2\2\2\u010e\u010b\3\2\2\2\u010e\u010c\3")
        buf.write("\2\2\2\u010e\u010d\3\2\2\2\u010f/\3\2\2\2\u0110\u0113")
        buf.write("\7E\2\2\u0111\u0113\5\64\33\2\u0112\u0110\3\2\2\2\u0112")
        buf.write("\u0111\3\2\2\2\u0113\u0117\3\2\2\2\u0114\u0118\7\13\2")
        buf.write("\2\u0115\u0116\7\13\2\2\u0116\u0118\5\62\32\2\u0117\u0114")
        buf.write("\3\2\2\2\u0117\u0115\3\2\2\2\u0118\u0119\3\2\2\2\u0119")
        buf.write("\u011a\7\f\2\2\u011a\61\3\2\2\2\u011b\u011c\5\36\20\2")
        buf.write("\u011c\u011d\7\21\2\2\u011d\u011e\5\62\32\2\u011e\u0121")
        buf.write("\3\2\2\2\u011f\u0121\5\36\20\2\u0120\u011b\3\2\2\2\u0120")
        buf.write("\u011f\3\2\2\2\u0121\63\3\2\2\2\u0122\u0123\t\4\2\2\u0123")
        buf.write("\65\3\2\2\2\u0124\u0125\58\35\2\u0125\u0126\5\66\34\2")
        buf.write("\u0126\u0129\3\2\2\2\u0127\u0129\58\35\2\u0128\u0124\3")
        buf.write("\2\2\2\u0128\u0127\3\2\2\2\u0129\67\3\2\2\2\u012a\u0137")
        buf.write("\5<\37\2\u012b\u0137\5:\36\2\u012c\u012d\5J&\2\u012d\u012e")
        buf.write("\7\22\2\2\u012e\u0137\3\2\2\2\u012f\u0137\5D#\2\u0130")
        buf.write("\u0137\5L\'\2\u0131\u0137\5N(\2\u0132\u0137\5F$\2\u0133")
        buf.write("\u0137\5H%\2\u0134\u0137\5J&\2\u0135\u0137\5P)\2\u0136")
        buf.write("\u012a\3\2\2\2\u0136\u012b\3\2\2\2\u0136\u012c\3\2\2\2")
        buf.write("\u0136\u012f\3\2\2\2\u0136\u0130\3\2\2\2\u0136\u0131\3")
        buf.write("\2\2\2\u0136\u0132\3\2\2\2\u0136\u0133\3\2\2\2\u0136\u0134")
        buf.write("\3\2\2\2\u0136\u0135\3\2\2\2\u01379\3\2\2\2\u0138\u0139")
        buf.write("\5\36\20\2\u0139\u013a\7,\2\2\u013a\u013b\5\36\20\2\u013b")
        buf.write("\u013c\7\22\2\2\u013c;\3\2\2\2\u013d\u013e\79\2\2\u013e")
        buf.write("\u013f\5\36\20\2\u013f\u0144\7<\2\2\u0140\u0145\5\66\34")
        buf.write("\2\u0141\u0142\5\66\34\2\u0142\u0143\5> \2\u0143\u0145")
        buf.write("\3\2\2\2\u0144\u0140\3\2\2\2\u0144\u0141\3\2\2\2\u0145")
        buf.write("\u0146\3\2\2\2\u0146\u0147\7\64\2\2\u0147\u0148\7\20\2")
        buf.write("\2\u0148=\3\2\2\2\u0149\u014a\5@!\2\u014a\u014b\5> \2")
        buf.write("\u014b\u014f\3\2\2\2\u014c\u014f\5@!\2\u014d\u014f\5B")
        buf.write("\"\2\u014e\u0149\3\2\2\2\u014e\u014c\3\2\2\2\u014e\u014d")
        buf.write("\3\2\2\2\u014f?\3\2\2\2\u0150\u0151\7\62\2\2\u0151\u0152")
        buf.write("\5\36\20\2\u0152\u0153\7<\2\2\u0153\u0154\5\66\34\2\u0154")
        buf.write("A\3\2\2\2\u0155\u0156\7\61\2\2\u0156\u0157\5\66\34\2\u0157")
        buf.write("C\3\2\2\2\u0158\u0159\7\67\2\2\u0159\u015a\7\13\2\2\u015a")
        buf.write("\u015b\7E\2\2\u015b\u015c\7,\2\2\u015c\u015d\7@\2\2\u015d")
        buf.write("\u015e\7\21\2\2\u015e\u015f\5\36\20\2\u015f\u0160\7\21")
        buf.write("\2\2\u0160\u0161\5\36\20\2\u0161\u0162\7\f\2\2\u0162\u0163")
        buf.write("\7\60\2\2\u0163\u0164\5\66\34\2\u0164\u0165\7\65\2\2\u0165")
        buf.write("\u0166\7\20\2\2\u0166E\3\2\2\2\u0167\u016b\7;\2\2\u0168")
        buf.write("\u0169\7;\2\2\u0169\u016b\5\36\20\2\u016a\u0167\3\2\2")
        buf.write("\2\u016a\u0168\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016d")
        buf.write("\7\22\2\2\u016dG\3\2\2\2\u016e\u016f\7>\2\2\u016f\u0170")
        buf.write("\5\36\20\2\u0170\u0175\7\60\2\2\u0171\u0172\5\66\34\2")
        buf.write("\u0172\u0173\7\66\2\2\u0173\u0176\3\2\2\2\u0174\u0176")
        buf.write("\7\66\2\2\u0175\u0171\3\2\2\2\u0175\u0174\3\2\2\2\u0176")
        buf.write("\u0177\3\2\2\2\u0177\u0178\7\20\2\2\u0178I\3\2\2\2\u0179")
        buf.write("\u017e\7\60\2\2\u017a\u017b\5\66\34\2\u017b\u017c\7>\2")
        buf.write("\2\u017c\u017f\3\2\2\2\u017d\u017f\7>\2\2\u017e\u017a")
        buf.write("\3\2\2\2\u017e\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180")
        buf.write("\u0181\5\36\20\2\u0181\u0182\7?\2\2\u0182\u0183\7\20\2")
        buf.write("\2\u0183K\3\2\2\2\u0184\u0185\7.\2\2\u0185\u0186\7\22")
        buf.write("\2\2\u0186M\3\2\2\2\u0187\u0188\7/\2\2\u0188\u0189\7\22")
        buf.write("\2\2\u0189O\3\2\2\2\u018a\u018b\5\60\31\2\u018b\u018c")
        buf.write("\7\22\2\2\u018cQ\3\2\2\2\u018d\u018e\t\5\2\2\u018eS\3")
        buf.write("\2\2\2\u018f\u0190\t\6\2\2\u0190U\3\2\2\2\u0191\u0192")
        buf.write("\t\7\2\2\u0192W\3\2\2\2\u0193\u0194\t\b\2\2\u0194Y\3\2")
        buf.write("\2\2!`gpw}\u0084\u008d\u0098\u00a2\u00a8\u00b3\u00bc\u00c3")
        buf.write("\u00ce\u00da\u00e6\u00ec\u00f1\u00fd\u0105\u010e\u0112")
        buf.write("\u0117\u0120\u0128\u0136\u0144\u014e\u016a\u0175\u017e")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int_of_float'", "'float_of_int'", "'int_of_string'", 
                     "'string_of_int'", "'float_of_string'", "'string_of_float'", 
                     "'bool_of_string'", "'string_of_bool'", "'('", "')'", 
                     "'['", "']'", "':'", "'.'", "','", "';'", "'{'", "'}'", 
                     "'+'", "'+.'", "'-'", "'-.'", "'*'", "'*.'", "'\\'", 
                     "'\\.'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", 
                     "'<'", "'>'", "'<='", "'>='", "'=/='", "'<.'", "'>.'", 
                     "'<=.'", "'>=.'", "'='", "'Body'", "'Break'", "'Continue'", 
                     "'Do'", "'Else'", "'ElseIf'", "'EndBody'", "'EndIf'", 
                     "'EndFor'", "'EndWhile'", "'For'", "'Function'", "'If'", 
                     "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
                     "'EndDo'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "LP", "RP", "LB", "RB", "COLON", "DOT", 
                      "COMMA", "SEMI", "LCB", "RCB", "ADDOP", "ADDF", "SUBOP", 
                      "SUBF", "MULOP", "MULF", "DIVOP", "DIVF", "MODOP", 
                      "NOT", "AND", "OR", "EQ", "NEQ", "LT", "GT", "LTE", 
                      "GTE", "NEQF", "LTF", "GTF", "LTEF", "GTEF", "ASSIG", 
                      "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", 
                      "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", 
                      "IF", "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", 
                      "ENDDO", "INTERGER", "FLOAT", "STRING", "ARRAY", "BOOLEAN", 
                      "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_program_part = 1
    RULE_var_dec = 2
    RULE_variable_list = 3
    RULE_scalar_variable = 4
    RULE_composite_variable = 5
    RULE_composite_var_name = 6
    RULE_many_demension = 7
    RULE_one_demension = 8
    RULE_func_dec = 9
    RULE_params = 10
    RULE_param_list = 11
    RULE_func_body = 12
    RULE_var_dec_list = 13
    RULE_expression_stm = 14
    RULE_term1 = 15
    RULE_term2 = 16
    RULE_term3 = 17
    RULE_term4 = 18
    RULE_term5 = 19
    RULE_term6 = 20
    RULE_term7 = 21
    RULE_operand = 22
    RULE_callee = 23
    RULE_parameter_callee = 24
    RULE_type_coercions = 25
    RULE_statement_list = 26
    RULE_statement_part = 27
    RULE_assign_stm = 28
    RULE_if_stm = 29
    RULE_elseif_else = 30
    RULE_elseif_one = 31
    RULE_else_one = 32
    RULE_for_stm = 33
    RULE_return_stm = 34
    RULE_while_stm = 35
    RULE_do_while_stm = 36
    RULE_break_stm = 37
    RULE_continue_stm = 38
    RULE_call_stm = 39
    RULE_multiplying = 40
    RULE_adding = 41
    RULE_logical = 42
    RULE_relational = 43

    ruleNames =  [ "program", "program_part", "var_dec", "variable_list", 
                   "scalar_variable", "composite_variable", "composite_var_name", 
                   "many_demension", "one_demension", "func_dec", "params", 
                   "param_list", "func_body", "var_dec_list", "expression_stm", 
                   "term1", "term2", "term3", "term4", "term5", "term6", 
                   "term7", "operand", "callee", "parameter_callee", "type_coercions", 
                   "statement_list", "statement_part", "assign_stm", "if_stm", 
                   "elseif_else", "elseif_one", "else_one", "for_stm", "return_stm", 
                   "while_stm", "do_while_stm", "break_stm", "continue_stm", 
                   "call_stm", "multiplying", "adding", "logical", "relational" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    LP=9
    RP=10
    LB=11
    RB=12
    COLON=13
    DOT=14
    COMMA=15
    SEMI=16
    LCB=17
    RCB=18
    ADDOP=19
    ADDF=20
    SUBOP=21
    SUBF=22
    MULOP=23
    MULF=24
    DIVOP=25
    DIVF=26
    MODOP=27
    NOT=28
    AND=29
    OR=30
    EQ=31
    NEQ=32
    LT=33
    GT=34
    LTE=35
    GTE=36
    NEQF=37
    LTF=38
    GTF=39
    LTEF=40
    GTEF=41
    ASSIG=42
    BODY=43
    BREAK=44
    CONTINUE=45
    DO=46
    ELSE=47
    ELSEIF=48
    ENDBODY=49
    ENDIF=50
    ENDFOR=51
    ENDWHILE=52
    FOR=53
    FUNCTION=54
    IF=55
    PARAMETER=56
    RETURN=57
    THEN=58
    VAR=59
    WHILE=60
    ENDDO=61
    INTERGER=62
    FLOAT=63
    STRING=64
    ARRAY=65
    BOOLEAN=66
    ID=67
    WS=68
    ERROR_CHAR=69
    UNCLOSE_STRING=70
    ILLEGAL_ESCAPE=71
    UNTERMINATED_COMMENT=72

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def program_part(self):
            return self.getTypedRuleContext(BKITParser.Program_partContext,0)


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
            self.state = 88
            self.program_part()
            self.state = 89
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Program_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def program_part(self):
            return self.getTypedRuleContext(BKITParser.Program_partContext,0)


        def var_dec(self):
            return self.getTypedRuleContext(BKITParser.Var_decContext,0)


        def func_dec(self):
            return self.getTypedRuleContext(BKITParser.Func_decContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_program_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram_part" ):
                return visitor.visitProgram_part(self)
            else:
                return visitor.visitChildren(self)




    def program_part(self):

        localctx = BKITParser.Program_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_program_part)
        try:
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.VAR]:
                    self.state = 91
                    self.var_dec()
                    pass
                elif token in [BKITParser.FUNCTION]:
                    self.state = 92
                    self.func_dec()
                    pass
                elif token in [BKITParser.T__0, BKITParser.T__1, BKITParser.T__2, BKITParser.T__3, BKITParser.T__4, BKITParser.T__5, BKITParser.T__6, BKITParser.T__7, BKITParser.LP, BKITParser.SUBOP, BKITParser.SUBF, BKITParser.NOT, BKITParser.BREAK, BKITParser.CONTINUE, BKITParser.DO, BKITParser.FOR, BKITParser.IF, BKITParser.RETURN, BKITParser.WHILE, BKITParser.INTERGER, BKITParser.FLOAT, BKITParser.STRING, BKITParser.ARRAY, BKITParser.BOOLEAN, BKITParser.ID]:
                    self.state = 93
                    self.statement_list()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 96
                self.program_part()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.var_dec()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 99
                self.func_dec()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 100
                self.statement_list()
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

        def variable_list(self):
            return self.getTypedRuleContext(BKITParser.Variable_listContext,0)


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
        self.enterRule(localctx, 4, self.RULE_var_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(BKITParser.VAR)
            self.state = 104
            self.match(BKITParser.COLON)
            self.state = 105
            self.variable_list()
            self.state = 106
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def variable_list(self):
            return self.getTypedRuleContext(BKITParser.Variable_listContext,0)


        def scalar_variable(self):
            return self.getTypedRuleContext(BKITParser.Scalar_variableContext,0)


        def composite_variable(self):
            return self.getTypedRuleContext(BKITParser.Composite_variableContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_variable_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_list" ):
                return visitor.visitVariable_list(self)
            else:
                return visitor.visitChildren(self)




    def variable_list(self):

        localctx = BKITParser.Variable_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variable_list)
        try:
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 108
                    self.scalar_variable()
                    pass

                elif la_ == 2:
                    self.state = 109
                    self.composite_variable()
                    pass


                self.state = 112
                self.match(BKITParser.COMMA)
                self.state = 113
                self.variable_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.scalar_variable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 116
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
        self.enterRule(localctx, 8, self.RULE_scalar_variable)
        self._la = 0 # Token type
        try:
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.match(BKITParser.ID)
                self.state = 120
                self.match(BKITParser.ASSIG)
                self.state = 121
                _la = self._input.LA(1)
                if not(((((_la - 62)) & ~0x3f) == 0 and ((1 << (_la - 62)) & ((1 << (BKITParser.INTERGER - 62)) | (1 << (BKITParser.FLOAT - 62)) | (1 << (BKITParser.STRING - 62)) | (1 << (BKITParser.BOOLEAN - 62)))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 122
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

        def ARRAY(self):
            return self.getToken(BKITParser.ARRAY, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_composite_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComposite_variable" ):
                return visitor.visitComposite_variable(self)
            else:
                return visitor.visitChildren(self)




    def composite_variable(self):

        localctx = BKITParser.Composite_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_composite_variable)
        try:
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.composite_var_name()
                self.state = 126
                self.match(BKITParser.ASSIG)
                self.state = 127
                self.match(BKITParser.ARRAY)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
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
        self.enterRule(localctx, 12, self.RULE_composite_var_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(BKITParser.ID)
            self.state = 133
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
        self.enterRule(localctx, 14, self.RULE_many_demension)
        try:
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.one_demension()
                self.state = 136
                self.many_demension()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
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
        self.enterRule(localctx, 16, self.RULE_one_demension)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(BKITParser.LB)
            self.state = 142
            self.match(BKITParser.INTERGER)
            self.state = 143
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

        def func_body(self):
            return self.getTypedRuleContext(BKITParser.Func_bodyContext,0)


        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def params(self):
            return self.getTypedRuleContext(BKITParser.ParamsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_dec" ):
                return visitor.visitFunc_dec(self)
            else:
                return visitor.visitChildren(self)




    def func_dec(self):

        localctx = BKITParser.Func_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_func_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(BKITParser.FUNCTION)
            self.state = 146
            self.match(BKITParser.COLON)
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 147
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.state = 148
                self.match(BKITParser.ID)
                self.state = 149
                self.params()
                pass


            self.state = 152
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
        self.enterRule(localctx, 20, self.RULE_params)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(BKITParser.PARAMETER)
            self.state = 155
            self.match(BKITParser.COLON)
            self.state = 156
            self.param_list()
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

        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def param_list(self):
            return self.getTypedRuleContext(BKITParser.Param_listContext,0)


        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def composite_var_name(self):
            return self.getTypedRuleContext(BKITParser.Composite_var_nameContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = BKITParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_param_list)
        try:
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 158
                    self.match(BKITParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 159
                    self.composite_var_name()
                    pass


                self.state = 162
                self.match(BKITParser.COMMA)
                self.state = 163
                self.param_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.match(BKITParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 165
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

        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def var_dec_list(self):
            return self.getTypedRuleContext(BKITParser.Var_dec_listContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_body" ):
                return visitor.visitFunc_body(self)
            else:
                return visitor.visitChildren(self)




    def func_body(self):

        localctx = BKITParser.Func_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_func_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(BKITParser.BODY)
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 169
                self.match(BKITParser.COLON)
                self.state = 170
                self.var_dec_list()
                pass

            elif la_ == 2:
                self.state = 171
                self.match(BKITParser.COLON)
                self.state = 172
                self.statement_list()
                pass

            elif la_ == 3:
                self.state = 173
                self.match(BKITParser.COLON)
                self.state = 174
                self.var_dec_list()
                self.state = 175
                self.statement_list()
                pass


            self.state = 179
            self.match(BKITParser.ENDBODY)
            self.state = 180
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_dec_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_dec(self):
            return self.getTypedRuleContext(BKITParser.Var_decContext,0)


        def var_dec_list(self):
            return self.getTypedRuleContext(BKITParser.Var_dec_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_dec_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_dec_list" ):
                return visitor.visitVar_dec_list(self)
            else:
                return visitor.visitChildren(self)




    def var_dec_list(self):

        localctx = BKITParser.Var_dec_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_var_dec_list)
        try:
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.var_dec()
                self.state = 183
                self.var_dec_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.var_dec()
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

        def term1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Term1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Term1Context,i)


        def relational(self):
            return self.getTypedRuleContext(BKITParser.RelationalContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_expression_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_stm" ):
                return visitor.visitExpression_stm(self)
            else:
                return visitor.visitChildren(self)




    def expression_stm(self):

        localctx = BKITParser.Expression_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expression_stm)
        try:
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
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
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_term1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.term2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 204
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
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
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_term2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.term3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 216
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
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
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_term3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.term4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 228
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
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
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
        self.enterRule(localctx, 36, self.RULE_term4)
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
            elif token in [BKITParser.T__0, BKITParser.T__1, BKITParser.T__2, BKITParser.T__3, BKITParser.T__4, BKITParser.T__5, BKITParser.T__6, BKITParser.T__7, BKITParser.LP, BKITParser.SUBOP, BKITParser.SUBF, BKITParser.INTERGER, BKITParser.FLOAT, BKITParser.STRING, BKITParser.ARRAY, BKITParser.BOOLEAN, BKITParser.ID]:
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
        self.enterRule(localctx, 38, self.RULE_term5)
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
            elif token in [BKITParser.T__0, BKITParser.T__1, BKITParser.T__2, BKITParser.T__3, BKITParser.T__4, BKITParser.T__5, BKITParser.T__6, BKITParser.T__7, BKITParser.LP, BKITParser.INTERGER, BKITParser.FLOAT, BKITParser.STRING, BKITParser.ARRAY, BKITParser.BOOLEAN, BKITParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                self.term6(0)
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


        def term6(self):
            return self.getTypedRuleContext(BKITParser.Term6Context,0)


        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def expression_stm(self):
            return self.getTypedRuleContext(BKITParser.Expression_stmContext,0)


        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_term6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm6" ):
                return visitor.visitTerm6(self)
            else:
                return visitor.visitChildren(self)



    def term6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Term6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_term6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.term7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 251
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Term6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term6)
                    self.state = 244
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 245
                    self.match(BKITParser.LB)
                    self.state = 246
                    self.expression_stm()
                    self.state = 247
                    self.match(BKITParser.RB) 
                self.state = 253
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def expression_stm(self):
            return self.getTypedRuleContext(BKITParser.Expression_stmContext,0)


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
        self.enterRule(localctx, 42, self.RULE_term7)
        try:
            self.state = 259
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.match(BKITParser.LP)
                self.state = 255
                self.expression_stm()
                self.state = 256
                self.match(BKITParser.RP)
                pass
            elif token in [BKITParser.T__0, BKITParser.T__1, BKITParser.T__2, BKITParser.T__3, BKITParser.T__4, BKITParser.T__5, BKITParser.T__6, BKITParser.T__7, BKITParser.INTERGER, BKITParser.FLOAT, BKITParser.STRING, BKITParser.ARRAY, BKITParser.BOOLEAN, BKITParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 258
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

        def ARRAY(self):
            return self.getToken(BKITParser.ARRAY, 0)

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
        self.enterRule(localctx, 44, self.RULE_operand)
        try:
            self.state = 268
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
                self.match(BKITParser.FLOAT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 263
                self.match(BKITParser.INTERGER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 264
                self.match(BKITParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 265
                self.match(BKITParser.BOOLEAN)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 266
                self.match(BKITParser.ARRAY)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 267
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

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def type_coercions(self):
            return self.getTypedRuleContext(BKITParser.Type_coercionsContext,0)


        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def parameter_callee(self):
            return self.getTypedRuleContext(BKITParser.Parameter_calleeContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_callee

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallee" ):
                return visitor.visitCallee(self)
            else:
                return visitor.visitChildren(self)




    def callee(self):

        localctx = BKITParser.CalleeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_callee)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ID]:
                self.state = 270
                self.match(BKITParser.ID)
                pass
            elif token in [BKITParser.T__0, BKITParser.T__1, BKITParser.T__2, BKITParser.T__3, BKITParser.T__4, BKITParser.T__5, BKITParser.T__6, BKITParser.T__7]:
                self.state = 271
                self.type_coercions()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 274
                self.match(BKITParser.LP)
                pass

            elif la_ == 2:
                self.state = 275
                self.match(BKITParser.LP)
                self.state = 276
                self.parameter_callee()
                pass


            self.state = 279
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

        def expression_stm(self):
            return self.getTypedRuleContext(BKITParser.Expression_stmContext,0)


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
        self.enterRule(localctx, 48, self.RULE_parameter_callee)
        try:
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.expression_stm()
                self.state = 282
                self.match(BKITParser.COMMA)
                self.state = 283
                self.parameter_callee()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 285
                self.expression_stm()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_coercionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKITParser.RULE_type_coercions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_coercions" ):
                return visitor.visitType_coercions(self)
            else:
                return visitor.visitChildren(self)




    def type_coercions(self):

        localctx = BKITParser.Type_coercionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_type_coercions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.T__0) | (1 << BKITParser.T__1) | (1 << BKITParser.T__2) | (1 << BKITParser.T__3) | (1 << BKITParser.T__4) | (1 << BKITParser.T__5) | (1 << BKITParser.T__6) | (1 << BKITParser.T__7))) != 0)):
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
        self.enterRule(localctx, 52, self.RULE_statement_list)
        try:
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.statement_part()
                self.state = 291
                self.statement_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.statement_part()
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


        def do_while_stm(self):
            return self.getTypedRuleContext(BKITParser.Do_while_stmContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

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
        self.enterRule(localctx, 54, self.RULE_statement_part)
        try:
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.if_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.assign_stm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 298
                self.do_while_stm()
                self.state = 299
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 301
                self.for_stm()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 302
                self.break_stm()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 303
                self.continue_stm()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 304
                self.return_stm()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 305
                self.while_stm()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 306
                self.do_while_stm()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 307
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

        def expression_stm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Expression_stmContext)
            else:
                return self.getTypedRuleContext(BKITParser.Expression_stmContext,i)


        def ASSIG(self):
            return self.getToken(BKITParser.ASSIG, 0)

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
        self.enterRule(localctx, 56, self.RULE_assign_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.expression_stm()
            self.state = 311
            self.match(BKITParser.ASSIG)
            self.state = 312
            self.expression_stm()
            self.state = 313
            self.match(BKITParser.SEMI)
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

        def expression_stm(self):
            return self.getTypedRuleContext(BKITParser.Expression_stmContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def elseif_else(self):
            return self.getTypedRuleContext(BKITParser.Elseif_elseContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_if_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stm" ):
                return visitor.visitIf_stm(self)
            else:
                return visitor.visitChildren(self)




    def if_stm(self):

        localctx = BKITParser.If_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_if_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(BKITParser.IF)
            self.state = 316
            self.expression_stm()
            self.state = 317
            self.match(BKITParser.THEN)
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 318
                self.statement_list()
                pass

            elif la_ == 2:
                self.state = 319
                self.statement_list()
                self.state = 320
                self.elseif_else()
                pass


            self.state = 324
            self.match(BKITParser.ENDIF)
            self.state = 325
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_elseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elseif_one(self):
            return self.getTypedRuleContext(BKITParser.Elseif_oneContext,0)


        def elseif_else(self):
            return self.getTypedRuleContext(BKITParser.Elseif_elseContext,0)


        def else_one(self):
            return self.getTypedRuleContext(BKITParser.Else_oneContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_elseif_else

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_else" ):
                return visitor.visitElseif_else(self)
            else:
                return visitor.visitChildren(self)




    def elseif_else(self):

        localctx = BKITParser.Elseif_elseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_elseif_else)
        try:
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.elseif_one()
                self.state = 328
                self.elseif_else()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
                self.elseif_one()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 331
                self.else_one()
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

        def expression_stm(self):
            return self.getTypedRuleContext(BKITParser.Expression_stmContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

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
        self.enterRule(localctx, 62, self.RULE_elseif_one)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(BKITParser.ELSEIF)
            self.state = 335
            self.expression_stm()
            self.state = 336
            self.match(BKITParser.THEN)
            self.state = 337
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
        self.enterRule(localctx, 64, self.RULE_else_one)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.match(BKITParser.ELSE)
            self.state = 340
            self.statement_list()
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

        def INTERGER(self):
            return self.getToken(BKITParser.INTERGER, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def expression_stm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Expression_stmContext)
            else:
                return self.getTypedRuleContext(BKITParser.Expression_stmContext,i)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

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
        self.enterRule(localctx, 66, self.RULE_for_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(BKITParser.FOR)
            self.state = 343
            self.match(BKITParser.LP)
            self.state = 344
            self.match(BKITParser.ID)
            self.state = 345
            self.match(BKITParser.ASSIG)
            self.state = 346
            self.match(BKITParser.INTERGER)
            self.state = 347
            self.match(BKITParser.COMMA)
            self.state = 348
            self.expression_stm()
            self.state = 349
            self.match(BKITParser.COMMA)
            self.state = 350
            self.expression_stm()
            self.state = 351
            self.match(BKITParser.RP)
            self.state = 352
            self.match(BKITParser.DO)
            self.state = 353
            self.statement_list()
            self.state = 354
            self.match(BKITParser.ENDFOR)
            self.state = 355
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

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def expression_stm(self):
            return self.getTypedRuleContext(BKITParser.Expression_stmContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_return_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stm" ):
                return visitor.visitReturn_stm(self)
            else:
                return visitor.visitChildren(self)




    def return_stm(self):

        localctx = BKITParser.Return_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_return_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 357
                self.match(BKITParser.RETURN)
                pass

            elif la_ == 2:
                self.state = 358
                self.match(BKITParser.RETURN)
                self.state = 359
                self.expression_stm()
                pass


            self.state = 362
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

        def expression_stm(self):
            return self.getTypedRuleContext(BKITParser.Expression_stmContext,0)


        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_while_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stm" ):
                return visitor.visitWhile_stm(self)
            else:
                return visitor.visitChildren(self)




    def while_stm(self):

        localctx = BKITParser.While_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_while_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.match(BKITParser.WHILE)
            self.state = 365
            self.expression_stm()
            self.state = 366
            self.match(BKITParser.DO)
            self.state = 371
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.T__0, BKITParser.T__1, BKITParser.T__2, BKITParser.T__3, BKITParser.T__4, BKITParser.T__5, BKITParser.T__6, BKITParser.T__7, BKITParser.LP, BKITParser.SUBOP, BKITParser.SUBF, BKITParser.NOT, BKITParser.BREAK, BKITParser.CONTINUE, BKITParser.DO, BKITParser.FOR, BKITParser.IF, BKITParser.RETURN, BKITParser.WHILE, BKITParser.INTERGER, BKITParser.FLOAT, BKITParser.STRING, BKITParser.ARRAY, BKITParser.BOOLEAN, BKITParser.ID]:
                self.state = 367
                self.statement_list()
                self.state = 368
                self.match(BKITParser.ENDWHILE)
                pass
            elif token in [BKITParser.ENDWHILE]:
                self.state = 370
                self.match(BKITParser.ENDWHILE)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 373
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

        def expression_stm(self):
            return self.getTypedRuleContext(BKITParser.Expression_stmContext,0)


        def ENDDO(self):
            return self.getToken(BKITParser.ENDDO, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_do_while_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_stm" ):
                return visitor.visitDo_while_stm(self)
            else:
                return visitor.visitChildren(self)




    def do_while_stm(self):

        localctx = BKITParser.Do_while_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_do_while_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.match(BKITParser.DO)
            self.state = 380
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 376
                self.statement_list()
                self.state = 377
                self.match(BKITParser.WHILE)
                pass

            elif la_ == 2:
                self.state = 379
                self.match(BKITParser.WHILE)
                pass


            self.state = 382
            self.expression_stm()
            self.state = 383
            self.match(BKITParser.ENDDO)
            self.state = 384
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
        self.enterRule(localctx, 74, self.RULE_break_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.match(BKITParser.BREAK)
            self.state = 387
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
        self.enterRule(localctx, 76, self.RULE_continue_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.match(BKITParser.CONTINUE)
            self.state = 390
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
        self.enterRule(localctx, 78, self.RULE_call_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.callee()
            self.state = 393
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
        self.enterRule(localctx, 80, self.RULE_multiplying)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
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
        self.enterRule(localctx, 82, self.RULE_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
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
        self.enterRule(localctx, 84, self.RULE_logical)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
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
        self.enterRule(localctx, 86, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[15] = self.term1_sempred
        self._predicates[16] = self.term2_sempred
        self._predicates[17] = self.term3_sempred
        self._predicates[20] = self.term6_sempred
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
         

    def term6_sempred(self, localctx:Term6Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




