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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3L")
        buf.write("\u0188\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\3\2\3\2\3\2\6\2X\n\2\r\2\16")
        buf.write("\2Y\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\5\4e\n\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\5\4l\n\4\3\5\3\5\3\5\3\5\5\5r\n\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\5\6y\n\6\3\7\3\7\3\7\3\7\6\7\177\n\7\r")
        buf.write("\7\16\7\u0080\3\b\3\b\3\b\3\b\3\b\5\b\u0088\n\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\n\3\n\5\n\u0092\n\n\3\n\3\n\3\n\3")
        buf.write("\n\5\n\u0098\n\n\3\13\3\13\3\13\3\13\7\13\u009e\n\13\f")
        buf.write("\13\16\13\u00a1\13\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\5\f\u00ab\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u00b4")
        buf.write("\n\r\f\r\16\r\u00b7\13\r\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\7\16\u00c0\n\16\f\16\16\16\u00c3\13\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\7\17\u00cc\n\17\f\17\16\17\u00cf")
        buf.write("\13\17\3\20\3\20\3\20\5\20\u00d4\n\20\3\21\3\21\3\21\5")
        buf.write("\21\u00d9\n\21\3\22\3\22\3\22\3\22\3\22\7\22\u00e0\n\22")
        buf.write("\f\22\16\22\u00e3\13\22\3\23\3\23\3\23\3\23\3\23\5\23")
        buf.write("\u00ea\n\23\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u00f2\n")
        buf.write("\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25")
        buf.write("\u00fd\n\25\3\26\3\26\5\26\u0101\n\26\3\26\3\26\3\26\5")
        buf.write("\26\u0106\n\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\5\27")
        buf.write("\u010f\n\27\3\30\3\30\3\31\3\31\3\31\3\31\5\31\u0117\n")
        buf.write("\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\5\32\u0128\n\32\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\5\34\u0137\n\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3")
        buf.write("\35\5\35\u0141\n\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3!")
        buf.write("\3!\3!\5!\u015d\n!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5")
        buf.write("\"\u0168\n\"\3\"\3\"\3#\3#\3#\3#\3#\5#\u0171\n#\3#\3#")
        buf.write("\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3)\3)")
        buf.write("\3*\3*\3*\2\6\30\32\34\"+\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR\2\t\4\2B")
        buf.write("DFF\3\2\27\30\3\2\3\n\3\2\31\35\3\2\25\30\3\2\37 \3\2")
        buf.write("!+\2\u018f\2W\3\2\2\2\4]\3\2\2\2\6k\3\2\2\2\bq\3\2\2\2")
        buf.write("\nx\3\2\2\2\fz\3\2\2\2\16\u0082\3\2\2\2\20\u008b\3\2\2")
        buf.write("\2\22\u0097\3\2\2\2\24\u0099\3\2\2\2\26\u00aa\3\2\2\2")
        buf.write("\30\u00ac\3\2\2\2\32\u00b8\3\2\2\2\34\u00c4\3\2\2\2\36")
        buf.write("\u00d3\3\2\2\2 \u00d8\3\2\2\2\"\u00da\3\2\2\2$\u00e9\3")
        buf.write("\2\2\2&\u00f1\3\2\2\2(\u00fc\3\2\2\2*\u0100\3\2\2\2,\u010e")
        buf.write("\3\2\2\2.\u0110\3\2\2\2\60\u0116\3\2\2\2\62\u0127\3\2")
        buf.write("\2\2\64\u0129\3\2\2\2\66\u012e\3\2\2\28\u0140\3\2\2\2")
        buf.write(":\u0142\3\2\2\2<\u0147\3\2\2\2>\u014a\3\2\2\2@\u015c\3")
        buf.write("\2\2\2B\u0160\3\2\2\2D\u016b\3\2\2\2F\u0176\3\2\2\2H\u0179")
        buf.write("\3\2\2\2J\u017c\3\2\2\2L\u017f\3\2\2\2N\u0181\3\2\2\2")
        buf.write("P\u0183\3\2\2\2R\u0185\3\2\2\2TX\5\4\3\2UX\5\16\b\2VX")
        buf.write("\5\60\31\2WT\3\2\2\2WU\3\2\2\2WV\3\2\2\2XY\3\2\2\2YW\3")
        buf.write("\2\2\2YZ\3\2\2\2Z[\3\2\2\2[\\\7\2\2\3\\\3\3\2\2\2]^\7")
        buf.write("=\2\2^_\7\17\2\2_`\5\6\4\2`a\7\22\2\2a\5\3\2\2\2be\5\b")
        buf.write("\5\2ce\5\n\6\2db\3\2\2\2dc\3\2\2\2ef\3\2\2\2fg\7\21\2")
        buf.write("\2gh\5\6\4\2hl\3\2\2\2il\5\b\5\2jl\5\n\6\2kd\3\2\2\2k")
        buf.write("i\3\2\2\2kj\3\2\2\2l\7\3\2\2\2mn\7G\2\2no\7,\2\2or\t\2")
        buf.write("\2\2pr\7G\2\2qm\3\2\2\2qp\3\2\2\2r\t\3\2\2\2st\5\f\7\2")
        buf.write("tu\7,\2\2uv\7E\2\2vy\3\2\2\2wy\5\f\7\2xs\3\2\2\2xw\3\2")
        buf.write("\2\2y\13\3\2\2\2z~\7G\2\2{|\7\r\2\2|}\7B\2\2}\177\7\16")
        buf.write("\2\2~{\3\2\2\2\177\u0080\3\2\2\2\u0080~\3\2\2\2\u0080")
        buf.write("\u0081\3\2\2\2\u0081\r\3\2\2\2\u0082\u0083\78\2\2\u0083")
        buf.write("\u0087\7\17\2\2\u0084\u0088\7G\2\2\u0085\u0086\7G\2\2")
        buf.write("\u0086\u0088\5\20\t\2\u0087\u0084\3\2\2\2\u0087\u0085")
        buf.write("\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008a\5\24\13\2\u008a")
        buf.write("\17\3\2\2\2\u008b\u008c\7:\2\2\u008c\u008d\7\17\2\2\u008d")
        buf.write("\u008e\5\22\n\2\u008e\21\3\2\2\2\u008f\u0092\7G\2\2\u0090")
        buf.write("\u0092\5\f\7\2\u0091\u008f\3\2\2\2\u0091\u0090\3\2\2\2")
        buf.write("\u0092\u0093\3\2\2\2\u0093\u0094\7\21\2\2\u0094\u0098")
        buf.write("\5\22\n\2\u0095\u0098\7G\2\2\u0096\u0098\5\f\7\2\u0097")
        buf.write("\u0091\3\2\2\2\u0097\u0095\3\2\2\2\u0097\u0096\3\2\2\2")
        buf.write("\u0098\23\3\2\2\2\u0099\u009a\7-\2\2\u009a\u009f\7\17")
        buf.write("\2\2\u009b\u009e\5\4\3\2\u009c\u009e\5\60\31\2\u009d\u009b")
        buf.write("\3\2\2\2\u009d\u009c\3\2\2\2\u009e\u00a1\3\2\2\2\u009f")
        buf.write("\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a2\3\2\2\2")
        buf.write("\u00a1\u009f\3\2\2\2\u00a2\u00a3\7\63\2\2\u00a3\u00a4")
        buf.write("\7\20\2\2\u00a4\25\3\2\2\2\u00a5\u00a6\5\30\r\2\u00a6")
        buf.write("\u00a7\5R*\2\u00a7\u00a8\5\30\r\2\u00a8\u00ab\3\2\2\2")
        buf.write("\u00a9\u00ab\5\30\r\2\u00aa\u00a5\3\2\2\2\u00aa\u00a9")
        buf.write("\3\2\2\2\u00ab\27\3\2\2\2\u00ac\u00ad\b\r\1\2\u00ad\u00ae")
        buf.write("\5\32\16\2\u00ae\u00b5\3\2\2\2\u00af\u00b0\f\4\2\2\u00b0")
        buf.write("\u00b1\5P)\2\u00b1\u00b2\5\32\16\2\u00b2\u00b4\3\2\2\2")
        buf.write("\u00b3\u00af\3\2\2\2\u00b4\u00b7\3\2\2\2\u00b5\u00b3\3")
        buf.write("\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\31\3\2\2\2\u00b7\u00b5")
        buf.write("\3\2\2\2\u00b8\u00b9\b\16\1\2\u00b9\u00ba\5\34\17\2\u00ba")
        buf.write("\u00c1\3\2\2\2\u00bb\u00bc\f\4\2\2\u00bc\u00bd\5N(\2\u00bd")
        buf.write("\u00be\5\34\17\2\u00be\u00c0\3\2\2\2\u00bf\u00bb\3\2\2")
        buf.write("\2\u00c0\u00c3\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2")
        buf.write("\3\2\2\2\u00c2\33\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4\u00c5")
        buf.write("\b\17\1\2\u00c5\u00c6\5\36\20\2\u00c6\u00cd\3\2\2\2\u00c7")
        buf.write("\u00c8\f\4\2\2\u00c8\u00c9\5L\'\2\u00c9\u00ca\5\36\20")
        buf.write("\2\u00ca\u00cc\3\2\2\2\u00cb\u00c7\3\2\2\2\u00cc\u00cf")
        buf.write("\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce")
        buf.write("\35\3\2\2\2\u00cf\u00cd\3\2\2\2\u00d0\u00d1\7\36\2\2\u00d1")
        buf.write("\u00d4\5\36\20\2\u00d2\u00d4\5 \21\2\u00d3\u00d0\3\2\2")
        buf.write("\2\u00d3\u00d2\3\2\2\2\u00d4\37\3\2\2\2\u00d5\u00d6\t")
        buf.write("\3\2\2\u00d6\u00d9\5 \21\2\u00d7\u00d9\5\"\22\2\u00d8")
        buf.write("\u00d5\3\2\2\2\u00d8\u00d7\3\2\2\2\u00d9!\3\2\2\2\u00da")
        buf.write("\u00db\b\22\1\2\u00db\u00dc\5$\23\2\u00dc\u00e1\3\2\2")
        buf.write("\2\u00dd\u00de\f\4\2\2\u00de\u00e0\5(\25\2\u00df\u00dd")
        buf.write("\3\2\2\2\u00e0\u00e3\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1")
        buf.write("\u00e2\3\2\2\2\u00e2#\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e4")
        buf.write("\u00e5\7\13\2\2\u00e5\u00e6\5\26\f\2\u00e6\u00e7\7\f\2")
        buf.write("\2\u00e7\u00ea\3\2\2\2\u00e8\u00ea\5&\24\2\u00e9\u00e4")
        buf.write("\3\2\2\2\u00e9\u00e8\3\2\2\2\u00ea%\3\2\2\2\u00eb\u00f2")
        buf.write("\7F\2\2\u00ec\u00f2\7C\2\2\u00ed\u00f2\7B\2\2\u00ee\u00f2")
        buf.write("\7D\2\2\u00ef\u00f2\7G\2\2\u00f0\u00f2\5*\26\2\u00f1\u00eb")
        buf.write("\3\2\2\2\u00f1\u00ec\3\2\2\2\u00f1\u00ed\3\2\2\2\u00f1")
        buf.write("\u00ee\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f0\3\2\2\2")
        buf.write("\u00f2\'\3\2\2\2\u00f3\u00f4\7\r\2\2\u00f4\u00f5\5\26")
        buf.write("\f\2\u00f5\u00f6\7\16\2\2\u00f6\u00f7\5(\25\2\u00f7\u00fd")
        buf.write("\3\2\2\2\u00f8\u00f9\7\r\2\2\u00f9\u00fa\5\26\f\2\u00fa")
        buf.write("\u00fb\7\16\2\2\u00fb\u00fd\3\2\2\2\u00fc\u00f3\3\2\2")
        buf.write("\2\u00fc\u00f8\3\2\2\2\u00fd)\3\2\2\2\u00fe\u0101\7G\2")
        buf.write("\2\u00ff\u0101\5.\30\2\u0100\u00fe\3\2\2\2\u0100\u00ff")
        buf.write("\3\2\2\2\u0101\u0105\3\2\2\2\u0102\u0106\7\13\2\2\u0103")
        buf.write("\u0104\7\13\2\2\u0104\u0106\5,\27\2\u0105\u0102\3\2\2")
        buf.write("\2\u0105\u0103\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0108")
        buf.write("\7\f\2\2\u0108+\3\2\2\2\u0109\u010a\5\26\f\2\u010a\u010b")
        buf.write("\7\21\2\2\u010b\u010c\5,\27\2\u010c\u010f\3\2\2\2\u010d")
        buf.write("\u010f\5\26\f\2\u010e\u0109\3\2\2\2\u010e\u010d\3\2\2")
        buf.write("\2\u010f-\3\2\2\2\u0110\u0111\t\4\2\2\u0111/\3\2\2\2\u0112")
        buf.write("\u0113\5\62\32\2\u0113\u0114\5\60\31\2\u0114\u0117\3\2")
        buf.write("\2\2\u0115\u0117\5\62\32\2\u0116\u0112\3\2\2\2\u0116\u0115")
        buf.write("\3\2\2\2\u0117\61\3\2\2\2\u0118\u0128\5\66\34\2\u0119")
        buf.write("\u0128\5\64\33\2\u011a\u011b\5D#\2\u011b\u011c\7\22\2")
        buf.write("\2\u011c\u0128\3\2\2\2\u011d\u0128\5> \2\u011e\u0128\5")
        buf.write("F$\2\u011f\u0128\5H%\2\u0120\u0128\5@!\2\u0121\u0128\5")
        buf.write("B\"\2\u0122\u0128\5D#\2\u0123\u0128\5J&\2\u0124\u0125")
        buf.write("\5\26\f\2\u0125\u0126\7\22\2\2\u0126\u0128\3\2\2\2\u0127")
        buf.write("\u0118\3\2\2\2\u0127\u0119\3\2\2\2\u0127\u011a\3\2\2\2")
        buf.write("\u0127\u011d\3\2\2\2\u0127\u011e\3\2\2\2\u0127\u011f\3")
        buf.write("\2\2\2\u0127\u0120\3\2\2\2\u0127\u0121\3\2\2\2\u0127\u0122")
        buf.write("\3\2\2\2\u0127\u0123\3\2\2\2\u0127\u0124\3\2\2\2\u0128")
        buf.write("\63\3\2\2\2\u0129\u012a\5\26\f\2\u012a\u012b\7,\2\2\u012b")
        buf.write("\u012c\5\26\f\2\u012c\u012d\7\22\2\2\u012d\65\3\2\2\2")
        buf.write("\u012e\u012f\79\2\2\u012f\u0136\5\26\f\2\u0130\u0131\7")
        buf.write("<\2\2\u0131\u0137\5\60\31\2\u0132\u0133\7<\2\2\u0133\u0134")
        buf.write("\5\60\31\2\u0134\u0135\58\35\2\u0135\u0137\3\2\2\2\u0136")
        buf.write("\u0130\3\2\2\2\u0136\u0132\3\2\2\2\u0137\u0138\3\2\2\2")
        buf.write("\u0138\u0139\7\64\2\2\u0139\u013a\7\20\2\2\u013a\67\3")
        buf.write("\2\2\2\u013b\u013c\5:\36\2\u013c\u013d\58\35\2\u013d\u0141")
        buf.write("\3\2\2\2\u013e\u0141\5:\36\2\u013f\u0141\5<\37\2\u0140")
        buf.write("\u013b\3\2\2\2\u0140\u013e\3\2\2\2\u0140\u013f\3\2\2\2")
        buf.write("\u01419\3\2\2\2\u0142\u0143\7\62\2\2\u0143\u0144\5\26")
        buf.write("\f\2\u0144\u0145\7<\2\2\u0145\u0146\5\60\31\2\u0146;\3")
        buf.write("\2\2\2\u0147\u0148\7\61\2\2\u0148\u0149\5\60\31\2\u0149")
        buf.write("=\3\2\2\2\u014a\u014b\7\67\2\2\u014b\u014c\7\13\2\2\u014c")
        buf.write("\u014d\7G\2\2\u014d\u014e\7,\2\2\u014e\u014f\7B\2\2\u014f")
        buf.write("\u0150\7\21\2\2\u0150\u0151\5\26\f\2\u0151\u0152\7\21")
        buf.write("\2\2\u0152\u0153\5\26\f\2\u0153\u0154\7\f\2\2\u0154\u0155")
        buf.write("\7\60\2\2\u0155\u0156\5\60\31\2\u0156\u0157\7\65\2\2\u0157")
        buf.write("\u0158\7\20\2\2\u0158?\3\2\2\2\u0159\u015d\7;\2\2\u015a")
        buf.write("\u015b\7;\2\2\u015b\u015d\5\26\f\2\u015c\u0159\3\2\2\2")
        buf.write("\u015c\u015a\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u015f\7")
        buf.write("\22\2\2\u015fA\3\2\2\2\u0160\u0161\7>\2\2\u0161\u0162")
        buf.write("\5\26\f\2\u0162\u0167\7\60\2\2\u0163\u0164\5\60\31\2\u0164")
        buf.write("\u0165\7\66\2\2\u0165\u0168\3\2\2\2\u0166\u0168\7\66\2")
        buf.write("\2\u0167\u0163\3\2\2\2\u0167\u0166\3\2\2\2\u0168\u0169")
        buf.write("\3\2\2\2\u0169\u016a\7\20\2\2\u016aC\3\2\2\2\u016b\u0170")
        buf.write("\7\60\2\2\u016c\u016d\5\60\31\2\u016d\u016e\7>\2\2\u016e")
        buf.write("\u0171\3\2\2\2\u016f\u0171\7>\2\2\u0170\u016c\3\2\2\2")
        buf.write("\u0170\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0173\5")
        buf.write("\26\f\2\u0173\u0174\7A\2\2\u0174\u0175\7\20\2\2\u0175")
        buf.write("E\3\2\2\2\u0176\u0177\7.\2\2\u0177\u0178\7\22\2\2\u0178")
        buf.write("G\3\2\2\2\u0179\u017a\7/\2\2\u017a\u017b\7\22\2\2\u017b")
        buf.write("I\3\2\2\2\u017c\u017d\5*\26\2\u017d\u017e\7\22\2\2\u017e")
        buf.write("K\3\2\2\2\u017f\u0180\t\5\2\2\u0180M\3\2\2\2\u0181\u0182")
        buf.write("\t\6\2\2\u0182O\3\2\2\2\u0183\u0184\t\7\2\2\u0184Q\3\2")
        buf.write("\2\2\u0185\u0186\t\b\2\2\u0186S\3\2\2\2\"WYdkqx\u0080")
        buf.write("\u0087\u0091\u0097\u009d\u009f\u00aa\u00b5\u00c1\u00cd")
        buf.write("\u00d3\u00d8\u00e1\u00e9\u00f1\u00fc\u0100\u0105\u010e")
        buf.write("\u0116\u0127\u0136\u0140\u015c\u0167\u0170")
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
                     "'True'", "'False'", "'EndDo'" ]

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
                      "TRUE", "FALSE", "ENDDO", "INTERGER", "FLOAT", "STRING", 
                      "ARRAY", "BOOLEAN", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_var_dec = 1
    RULE_variable_list = 2
    RULE_scalar_variable = 3
    RULE_composite_variable = 4
    RULE_composite_var_name = 5
    RULE_func_dec = 6
    RULE_params = 7
    RULE_param_list = 8
    RULE_func_body = 9
    RULE_expression_stm = 10
    RULE_term1 = 11
    RULE_term2 = 12
    RULE_term3 = 13
    RULE_term4 = 14
    RULE_term5 = 15
    RULE_term6 = 16
    RULE_term7 = 17
    RULE_operand = 18
    RULE_index_operators = 19
    RULE_callee = 20
    RULE_parameter_callee = 21
    RULE_type_coercions = 22
    RULE_statement_list = 23
    RULE_statement_part = 24
    RULE_assign_stm = 25
    RULE_if_stm = 26
    RULE_elseif_else = 27
    RULE_elseif_one = 28
    RULE_else_one = 29
    RULE_for_stm = 30
    RULE_return_stm = 31
    RULE_while_stm = 32
    RULE_do_while_stm = 33
    RULE_break_stm = 34
    RULE_continue_stm = 35
    RULE_call_stm = 36
    RULE_multiplying = 37
    RULE_adding = 38
    RULE_logical = 39
    RULE_relational = 40

    ruleNames =  [ "program", "var_dec", "variable_list", "scalar_variable", 
                   "composite_variable", "composite_var_name", "func_dec", 
                   "params", "param_list", "func_body", "expression_stm", 
                   "term1", "term2", "term3", "term4", "term5", "term6", 
                   "term7", "operand", "index_operators", "callee", "parameter_callee", 
                   "type_coercions", "statement_list", "statement_part", 
                   "assign_stm", "if_stm", "elseif_else", "elseif_one", 
                   "else_one", "for_stm", "return_stm", "while_stm", "do_while_stm", 
                   "break_stm", "continue_stm", "call_stm", "multiplying", 
                   "adding", "logical", "relational" ]

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
    TRUE=61
    FALSE=62
    ENDDO=63
    INTERGER=64
    FLOAT=65
    STRING=66
    ARRAY=67
    BOOLEAN=68
    ID=69
    WS=70
    ERROR_CHAR=71
    UNCLOSE_STRING=72
    ILLEGAL_ESCAPE=73
    UNTERMINATED_COMMENT=74

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def var_dec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_decContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_decContext,i)


        def func_dec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Func_decContext)
            else:
                return self.getTypedRuleContext(BKITParser.Func_decContext,i)


        def statement_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Statement_listContext)
            else:
                return self.getTypedRuleContext(BKITParser.Statement_listContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 85
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.VAR]:
                    self.state = 82
                    self.var_dec()
                    pass
                elif token in [BKITParser.FUNCTION]:
                    self.state = 83
                    self.func_dec()
                    pass
                elif token in [BKITParser.T__0, BKITParser.T__1, BKITParser.T__2, BKITParser.T__3, BKITParser.T__4, BKITParser.T__5, BKITParser.T__6, BKITParser.T__7, BKITParser.LP, BKITParser.SUBOP, BKITParser.SUBF, BKITParser.NOT, BKITParser.BREAK, BKITParser.CONTINUE, BKITParser.DO, BKITParser.FOR, BKITParser.IF, BKITParser.RETURN, BKITParser.WHILE, BKITParser.INTERGER, BKITParser.FLOAT, BKITParser.STRING, BKITParser.BOOLEAN, BKITParser.ID]:
                    self.state = 84
                    self.statement_list()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 87 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.T__0) | (1 << BKITParser.T__1) | (1 << BKITParser.T__2) | (1 << BKITParser.T__3) | (1 << BKITParser.T__4) | (1 << BKITParser.T__5) | (1 << BKITParser.T__6) | (1 << BKITParser.T__7) | (1 << BKITParser.LP) | (1 << BKITParser.SUBOP) | (1 << BKITParser.SUBF) | (1 << BKITParser.NOT) | (1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.FUNCTION) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.VAR) | (1 << BKITParser.WHILE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (BKITParser.INTERGER - 64)) | (1 << (BKITParser.FLOAT - 64)) | (1 << (BKITParser.STRING - 64)) | (1 << (BKITParser.BOOLEAN - 64)) | (1 << (BKITParser.ID - 64)))) != 0)):
                    break

            self.state = 89
            self.match(BKITParser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_var_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(BKITParser.VAR)
            self.state = 92
            self.match(BKITParser.COLON)
            self.state = 93
            self.variable_list()
            self.state = 94
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
        self.enterRule(localctx, 4, self.RULE_variable_list)
        try:
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 96
                    self.scalar_variable()
                    pass

                elif la_ == 2:
                    self.state = 97
                    self.composite_variable()
                    pass


                self.state = 100
                self.match(BKITParser.COMMA)
                self.state = 101
                self.variable_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.scalar_variable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 104
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
        self.enterRule(localctx, 6, self.RULE_scalar_variable)
        self._la = 0 # Token type
        try:
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.match(BKITParser.ID)
                self.state = 108
                self.match(BKITParser.ASSIG)
                self.state = 109
                _la = self._input.LA(1)
                if not(((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (BKITParser.INTERGER - 64)) | (1 << (BKITParser.FLOAT - 64)) | (1 << (BKITParser.STRING - 64)) | (1 << (BKITParser.BOOLEAN - 64)))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
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
        self.enterRule(localctx, 8, self.RULE_composite_variable)
        try:
            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.composite_var_name()
                self.state = 114
                self.match(BKITParser.ASSIG)
                self.state = 115
                self.match(BKITParser.ARRAY)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
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

        def LB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LB)
            else:
                return self.getToken(BKITParser.LB, i)

        def INTERGER(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.INTERGER)
            else:
                return self.getToken(BKITParser.INTERGER, i)

        def RB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RB)
            else:
                return self.getToken(BKITParser.RB, i)

        def getRuleIndex(self):
            return BKITParser.RULE_composite_var_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComposite_var_name" ):
                return visitor.visitComposite_var_name(self)
            else:
                return visitor.visitChildren(self)




    def composite_var_name(self):

        localctx = BKITParser.Composite_var_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_composite_var_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(BKITParser.ID)
            self.state = 124 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 121
                self.match(BKITParser.LB)
                self.state = 122
                self.match(BKITParser.INTERGER)
                self.state = 123
                self.match(BKITParser.RB)
                self.state = 126 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.LB):
                    break

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
        self.enterRule(localctx, 12, self.RULE_func_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(BKITParser.FUNCTION)
            self.state = 129
            self.match(BKITParser.COLON)
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 130
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.state = 131
                self.match(BKITParser.ID)
                self.state = 132
                self.params()
                pass


            self.state = 135
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
        self.enterRule(localctx, 14, self.RULE_params)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(BKITParser.PARAMETER)
            self.state = 138
            self.match(BKITParser.COLON)
            self.state = 139
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
        self.enterRule(localctx, 16, self.RULE_param_list)
        try:
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 141
                    self.match(BKITParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 142
                    self.composite_var_name()
                    pass


                self.state = 145
                self.match(BKITParser.COMMA)
                self.state = 146
                self.param_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.match(BKITParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 148
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

        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def var_dec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_decContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_decContext,i)


        def statement_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Statement_listContext)
            else:
                return self.getTypedRuleContext(BKITParser.Statement_listContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_func_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_body" ):
                return visitor.visitFunc_body(self)
            else:
                return visitor.visitChildren(self)




    def func_body(self):

        localctx = BKITParser.Func_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_func_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(BKITParser.BODY)
            self.state = 152
            self.match(BKITParser.COLON)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.T__0) | (1 << BKITParser.T__1) | (1 << BKITParser.T__2) | (1 << BKITParser.T__3) | (1 << BKITParser.T__4) | (1 << BKITParser.T__5) | (1 << BKITParser.T__6) | (1 << BKITParser.T__7) | (1 << BKITParser.LP) | (1 << BKITParser.SUBOP) | (1 << BKITParser.SUBF) | (1 << BKITParser.NOT) | (1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.VAR) | (1 << BKITParser.WHILE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (BKITParser.INTERGER - 64)) | (1 << (BKITParser.FLOAT - 64)) | (1 << (BKITParser.STRING - 64)) | (1 << (BKITParser.BOOLEAN - 64)) | (1 << (BKITParser.ID - 64)))) != 0):
                self.state = 155
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.VAR]:
                    self.state = 153
                    self.var_dec()
                    pass
                elif token in [BKITParser.T__0, BKITParser.T__1, BKITParser.T__2, BKITParser.T__3, BKITParser.T__4, BKITParser.T__5, BKITParser.T__6, BKITParser.T__7, BKITParser.LP, BKITParser.SUBOP, BKITParser.SUBF, BKITParser.NOT, BKITParser.BREAK, BKITParser.CONTINUE, BKITParser.DO, BKITParser.FOR, BKITParser.IF, BKITParser.RETURN, BKITParser.WHILE, BKITParser.INTERGER, BKITParser.FLOAT, BKITParser.STRING, BKITParser.BOOLEAN, BKITParser.ID]:
                    self.state = 154
                    self.statement_list()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 160
            self.match(BKITParser.ENDBODY)
            self.state = 161
            self.match(BKITParser.DOT)
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
        self.enterRule(localctx, 20, self.RULE_expression_stm)
        try:
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.term1(0)
                self.state = 164
                self.relational()
                self.state = 165
                self.term1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
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
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_term1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.term2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 179
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Term1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term1)
                    self.state = 173
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 174
                    self.logical()
                    self.state = 175
                    self.term2(0) 
                self.state = 181
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
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_term2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.term3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 191
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Term2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term2)
                    self.state = 185
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 186
                    self.adding()
                    self.state = 187
                    self.term3(0) 
                self.state = 193
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
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_term3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.term4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 203
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Term3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term3)
                    self.state = 197
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 198
                    self.multiplying()
                    self.state = 199
                    self.term4() 
                self.state = 205
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
        self.enterRule(localctx, 28, self.RULE_term4)
        try:
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.match(BKITParser.NOT)
                self.state = 207
                self.term4()
                pass
            elif token in [BKITParser.T__0, BKITParser.T__1, BKITParser.T__2, BKITParser.T__3, BKITParser.T__4, BKITParser.T__5, BKITParser.T__6, BKITParser.T__7, BKITParser.LP, BKITParser.SUBOP, BKITParser.SUBF, BKITParser.INTERGER, BKITParser.FLOAT, BKITParser.STRING, BKITParser.BOOLEAN, BKITParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
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
        self.enterRule(localctx, 30, self.RULE_term5)
        self._la = 0 # Token type
        try:
            self.state = 214
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.SUBOP, BKITParser.SUBF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                _la = self._input.LA(1)
                if not(_la==BKITParser.SUBOP or _la==BKITParser.SUBF):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 212
                self.term5()
                pass
            elif token in [BKITParser.T__0, BKITParser.T__1, BKITParser.T__2, BKITParser.T__3, BKITParser.T__4, BKITParser.T__5, BKITParser.T__6, BKITParser.T__7, BKITParser.LP, BKITParser.INTERGER, BKITParser.FLOAT, BKITParser.STRING, BKITParser.BOOLEAN, BKITParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
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


        def index_operators(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorsContext,0)


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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_term6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.term7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 223
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Term6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term6)
                    self.state = 219
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 220
                    self.index_operators() 
                self.state = 225
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
        self.enterRule(localctx, 34, self.RULE_term7)
        try:
            self.state = 231
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.match(BKITParser.LP)
                self.state = 227
                self.expression_stm()
                self.state = 228
                self.match(BKITParser.RP)
                pass
            elif token in [BKITParser.T__0, BKITParser.T__1, BKITParser.T__2, BKITParser.T__3, BKITParser.T__4, BKITParser.T__5, BKITParser.T__6, BKITParser.T__7, BKITParser.INTERGER, BKITParser.FLOAT, BKITParser.STRING, BKITParser.BOOLEAN, BKITParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
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

        def BOOLEAN(self):
            return self.getToken(BKITParser.BOOLEAN, 0)

        def FLOAT(self):
            return self.getToken(BKITParser.FLOAT, 0)

        def INTERGER(self):
            return self.getToken(BKITParser.INTERGER, 0)

        def STRING(self):
            return self.getToken(BKITParser.STRING, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

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
        self.enterRule(localctx, 36, self.RULE_operand)
        try:
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.match(BKITParser.BOOLEAN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.match(BKITParser.FLOAT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 235
                self.match(BKITParser.INTERGER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 236
                self.match(BKITParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 237
                self.match(BKITParser.ID)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 238
                self.callee()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def expression_stm(self):
            return self.getTypedRuleContext(BKITParser.Expression_stmContext,0)


        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def index_operators(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_index_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators" ):
                return visitor.visitIndex_operators(self)
            else:
                return visitor.visitChildren(self)




    def index_operators(self):

        localctx = BKITParser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_index_operators)
        try:
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.match(BKITParser.LB)
                self.state = 242
                self.expression_stm()
                self.state = 243
                self.match(BKITParser.RB)
                self.state = 244
                self.index_operators()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
                self.match(BKITParser.LB)
                self.state = 247
                self.expression_stm()
                self.state = 248
                self.match(BKITParser.RB)
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
        self.enterRule(localctx, 40, self.RULE_callee)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ID]:
                self.state = 252
                self.match(BKITParser.ID)
                pass
            elif token in [BKITParser.T__0, BKITParser.T__1, BKITParser.T__2, BKITParser.T__3, BKITParser.T__4, BKITParser.T__5, BKITParser.T__6, BKITParser.T__7]:
                self.state = 253
                self.type_coercions()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 259
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 256
                self.match(BKITParser.LP)
                pass

            elif la_ == 2:
                self.state = 257
                self.match(BKITParser.LP)
                self.state = 258
                self.parameter_callee()
                pass


            self.state = 261
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
        self.enterRule(localctx, 42, self.RULE_parameter_callee)
        try:
            self.state = 268
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.expression_stm()
                self.state = 264
                self.match(BKITParser.COMMA)
                self.state = 265
                self.parameter_callee()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
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
        self.enterRule(localctx, 44, self.RULE_type_coercions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
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
        self.enterRule(localctx, 46, self.RULE_statement_list)
        try:
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.statement_part()
                self.state = 273
                self.statement_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
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


        def expression_stm(self):
            return self.getTypedRuleContext(BKITParser.Expression_stmContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_statement_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_part" ):
                return visitor.visitStatement_part(self)
            else:
                return visitor.visitChildren(self)




    def statement_part(self):

        localctx = BKITParser.Statement_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_statement_part)
        try:
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.if_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
                self.assign_stm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 280
                self.do_while_stm()
                self.state = 281
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 283
                self.for_stm()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 284
                self.break_stm()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 285
                self.continue_stm()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 286
                self.return_stm()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 287
                self.while_stm()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 288
                self.do_while_stm()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 289
                self.call_stm()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 290
                self.expression_stm()
                self.state = 291
                self.match(BKITParser.SEMI)
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
        self.enterRule(localctx, 50, self.RULE_assign_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.expression_stm()
            self.state = 296
            self.match(BKITParser.ASSIG)
            self.state = 297
            self.expression_stm()
            self.state = 298
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


        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

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
        self.enterRule(localctx, 52, self.RULE_if_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(BKITParser.IF)
            self.state = 301
            self.expression_stm()
            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 302
                self.match(BKITParser.THEN)
                self.state = 303
                self.statement_list()
                pass

            elif la_ == 2:
                self.state = 304
                self.match(BKITParser.THEN)
                self.state = 305
                self.statement_list()
                self.state = 306
                self.elseif_else()
                pass


            self.state = 310
            self.match(BKITParser.ENDIF)
            self.state = 311
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
        self.enterRule(localctx, 54, self.RULE_elseif_else)
        try:
            self.state = 318
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.elseif_one()
                self.state = 314
                self.elseif_else()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
                self.elseif_one()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 317
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
        self.enterRule(localctx, 56, self.RULE_elseif_one)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(BKITParser.ELSEIF)
            self.state = 321
            self.expression_stm()
            self.state = 322
            self.match(BKITParser.THEN)
            self.state = 323
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
        self.enterRule(localctx, 58, self.RULE_else_one)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(BKITParser.ELSE)
            self.state = 326
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
        self.enterRule(localctx, 60, self.RULE_for_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(BKITParser.FOR)
            self.state = 329
            self.match(BKITParser.LP)
            self.state = 330
            self.match(BKITParser.ID)
            self.state = 331
            self.match(BKITParser.ASSIG)
            self.state = 332
            self.match(BKITParser.INTERGER)
            self.state = 333
            self.match(BKITParser.COMMA)
            self.state = 334
            self.expression_stm()
            self.state = 335
            self.match(BKITParser.COMMA)
            self.state = 336
            self.expression_stm()
            self.state = 337
            self.match(BKITParser.RP)
            self.state = 338
            self.match(BKITParser.DO)
            self.state = 339
            self.statement_list()
            self.state = 340
            self.match(BKITParser.ENDFOR)
            self.state = 341
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
        self.enterRule(localctx, 62, self.RULE_return_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 343
                self.match(BKITParser.RETURN)
                pass

            elif la_ == 2:
                self.state = 344
                self.match(BKITParser.RETURN)
                self.state = 345
                self.expression_stm()
                pass


            self.state = 348
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
        self.enterRule(localctx, 64, self.RULE_while_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(BKITParser.WHILE)
            self.state = 351
            self.expression_stm()
            self.state = 352
            self.match(BKITParser.DO)
            self.state = 357
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.T__0, BKITParser.T__1, BKITParser.T__2, BKITParser.T__3, BKITParser.T__4, BKITParser.T__5, BKITParser.T__6, BKITParser.T__7, BKITParser.LP, BKITParser.SUBOP, BKITParser.SUBF, BKITParser.NOT, BKITParser.BREAK, BKITParser.CONTINUE, BKITParser.DO, BKITParser.FOR, BKITParser.IF, BKITParser.RETURN, BKITParser.WHILE, BKITParser.INTERGER, BKITParser.FLOAT, BKITParser.STRING, BKITParser.BOOLEAN, BKITParser.ID]:
                self.state = 353
                self.statement_list()
                self.state = 354
                self.match(BKITParser.ENDWHILE)
                pass
            elif token in [BKITParser.ENDWHILE]:
                self.state = 356
                self.match(BKITParser.ENDWHILE)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 359
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
        self.enterRule(localctx, 66, self.RULE_do_while_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(BKITParser.DO)
            self.state = 366
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 362
                self.statement_list()
                self.state = 363
                self.match(BKITParser.WHILE)
                pass

            elif la_ == 2:
                self.state = 365
                self.match(BKITParser.WHILE)
                pass


            self.state = 368
            self.expression_stm()
            self.state = 369
            self.match(BKITParser.ENDDO)
            self.state = 370
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
        self.enterRule(localctx, 68, self.RULE_break_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.match(BKITParser.BREAK)
            self.state = 373
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
        self.enterRule(localctx, 70, self.RULE_continue_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.match(BKITParser.CONTINUE)
            self.state = 376
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
        self.enterRule(localctx, 72, self.RULE_call_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.callee()
            self.state = 379
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
        self.enterRule(localctx, 74, self.RULE_multiplying)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
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
        self.enterRule(localctx, 76, self.RULE_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
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
        self.enterRule(localctx, 78, self.RULE_logical)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
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
        self.enterRule(localctx, 80, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
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
        self._predicates[11] = self.term1_sempred
        self._predicates[12] = self.term2_sempred
        self._predicates[13] = self.term3_sempred
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
         

    def term3_sempred(self, localctx:Term3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def term6_sempred(self, localctx:Term6Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




