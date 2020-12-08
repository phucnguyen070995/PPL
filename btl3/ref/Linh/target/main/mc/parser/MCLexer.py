# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\61")
        buf.write("\u01c1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\27\3\27")
        buf.write("\3\30\3\30\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3")
        buf.write("\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3&\5")
        buf.write("&\u0104\n&\3\'\3\'\3(\3(\3)\3)\3)\3)\3)\5)\u010f\n)\3")
        buf.write("*\6*\u0112\n*\r*\16*\u0113\3*\3*\7*\u0118\n*\f*\16*\u011b")
        buf.write("\13*\3*\7*\u011e\n*\f*\16*\u0121\13*\3*\3*\6*\u0125\n")
        buf.write("*\r*\16*\u0126\5*\u0129\n*\3+\6+\u012c\n+\r+\16+\u012d")
        buf.write("\3+\3+\6+\u0132\n+\r+\16+\u0133\3,\7,\u0137\n,\f,\16,")
        buf.write("\u013a\13,\3,\3,\6,\u013e\n,\r,\16,\u013f\3,\3,\6,\u0144")
        buf.write("\n,\r,\16,\u0145\3,\6,\u0149\n,\r,\16,\u014a\3,\3,\7,")
        buf.write("\u014f\n,\f,\16,\u0152\13,\3,\3,\6,\u0156\n,\r,\16,\u0157")
        buf.write("\5,\u015a\n,\3-\3-\3-\5-\u015f\n-\3.\6.\u0162\n.\r.\16")
        buf.write(".\u0163\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\62\3\62")
        buf.write("\3\63\3\63\7\63\u0172\n\63\f\63\16\63\u0175\13\63\3\64")
        buf.write("\6\64\u0178\n\64\r\64\16\64\u0179\3\64\3\64\3\65\3\65")
        buf.write("\3\65\3\66\3\66\3\66\3\67\3\67\3\67\38\38\78\u0189\n8")
        buf.write("\f8\168\u018c\138\38\38\38\38\39\39\79\u0194\n9\f9\16")
        buf.write("9\u0197\139\39\39\3:\3:\5:\u019d\n:\3;\3;\7;\u01a1\n;")
        buf.write("\f;\16;\u01a4\13;\3;\3;\3<\3<\3<\3<\3<\7<\u01ad\n<\f<")
        buf.write("\16<\u01b0\13<\3<\3<\3<\5<\u01b5\n<\3=\3=\7=\u01b9\n=")
        buf.write("\f=\16=\u01bc\13=\3=\3=\3>\3>\3\u018a\2?\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M\2O\2Q\2S\2U\2W\2")
        buf.write("Y([)]\2_\2a\2c\2e*g+i\2k\2m\2o,q-s\2u.w/y\60{\61\3\2\f")
        buf.write("\3\2\62;\4\2GGgg\t\2$$^^ddhhppttvv\13\2\f\f\17\17$$^^")
        buf.write("ddhhppttvv\3\2$$\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\16")
        buf.write("\17\"\"\4\2\f\f\17\17\7\2\2\13\r\16\20#%]_\u0101\2\u01d1")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2e\3\2\2\2\2g\3\2\2")
        buf.write("\2\2o\3\2\2\2\2q\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2")
        buf.write("\2\2\2{\3\2\2\2\3}\3\2\2\2\5\u0080\3\2\2\2\7\u0085\3\2")
        buf.write("\2\2\t\u0088\3\2\2\2\13\u008e\3\2\2\2\r\u0092\3\2\2\2")
        buf.write("\17\u0098\3\2\2\2\21\u00a1\3\2\2\2\23\u00a8\3\2\2\2\25")
        buf.write("\u00ac\3\2\2\2\27\u00b1\3\2\2\2\31\u00b9\3\2\2\2\33\u00bf")
        buf.write("\3\2\2\2\35\u00c6\3\2\2\2\37\u00c8\3\2\2\2!\u00ca\3\2")
        buf.write("\2\2#\u00cc\3\2\2\2%\u00cf\3\2\2\2\'\u00d2\3\2\2\2)\u00d4")
        buf.write("\3\2\2\2+\u00d7\3\2\2\2-\u00d9\3\2\2\2/\u00db\3\2\2\2")
        buf.write("\61\u00dd\3\2\2\2\63\u00df\3\2\2\2\65\u00e2\3\2\2\2\67")
        buf.write("\u00e5\3\2\2\29\u00e7\3\2\2\2;\u00ea\3\2\2\2=\u00ec\3")
        buf.write("\2\2\2?\u00ee\3\2\2\2A\u00f0\3\2\2\2C\u00f2\3\2\2\2E\u00f4")
        buf.write("\3\2\2\2G\u00f6\3\2\2\2I\u00f8\3\2\2\2K\u0103\3\2\2\2")
        buf.write("M\u0105\3\2\2\2O\u0107\3\2\2\2Q\u010e\3\2\2\2S\u0128\3")
        buf.write("\2\2\2U\u012b\3\2\2\2W\u0159\3\2\2\2Y\u015e\3\2\2\2[\u0161")
        buf.write("\3\2\2\2]\u0165\3\2\2\2_\u0167\3\2\2\2a\u016a\3\2\2\2")
        buf.write("c\u016d\3\2\2\2e\u016f\3\2\2\2g\u0177\3\2\2\2i\u017d\3")
        buf.write("\2\2\2k\u0180\3\2\2\2m\u0183\3\2\2\2o\u0186\3\2\2\2q\u0191")
        buf.write("\3\2\2\2s\u019c\3\2\2\2u\u019e\3\2\2\2w\u01b4\3\2\2\2")
        buf.write("y\u01b6\3\2\2\2{\u01bf\3\2\2\2}~\7k\2\2~\177\7h\2\2\177")
        buf.write("\4\3\2\2\2\u0080\u0081\7g\2\2\u0081\u0082\7n\2\2\u0082")
        buf.write("\u0083\7u\2\2\u0083\u0084\7g\2\2\u0084\6\3\2\2\2\u0085")
        buf.write("\u0086\7f\2\2\u0086\u0087\7q\2\2\u0087\b\3\2\2\2\u0088")
        buf.write("\u0089\7y\2\2\u0089\u008a\7j\2\2\u008a\u008b\7k\2\2\u008b")
        buf.write("\u008c\7n\2\2\u008c\u008d\7g\2\2\u008d\n\3\2\2\2\u008e")
        buf.write("\u008f\7h\2\2\u008f\u0090\7q\2\2\u0090\u0091\7t\2\2\u0091")
        buf.write("\f\3\2\2\2\u0092\u0093\7d\2\2\u0093\u0094\7t\2\2\u0094")
        buf.write("\u0095\7g\2\2\u0095\u0096\7c\2\2\u0096\u0097\7m\2\2\u0097")
        buf.write("\16\3\2\2\2\u0098\u0099\7e\2\2\u0099\u009a\7q\2\2\u009a")
        buf.write("\u009b\7p\2\2\u009b\u009c\7v\2\2\u009c\u009d\7k\2\2\u009d")
        buf.write("\u009e\7p\2\2\u009e\u009f\7w\2\2\u009f\u00a0\7g\2\2\u00a0")
        buf.write("\20\3\2\2\2\u00a1\u00a2\7t\2\2\u00a2\u00a3\7g\2\2\u00a3")
        buf.write("\u00a4\7v\2\2\u00a4\u00a5\7w\2\2\u00a5\u00a6\7t\2\2\u00a6")
        buf.write("\u00a7\7p\2\2\u00a7\22\3\2\2\2\u00a8\u00a9\7k\2\2\u00a9")
        buf.write("\u00aa\7p\2\2\u00aa\u00ab\7v\2\2\u00ab\24\3\2\2\2\u00ac")
        buf.write("\u00ad\7x\2\2\u00ad\u00ae\7q\2\2\u00ae\u00af\7k\2\2\u00af")
        buf.write("\u00b0\7f\2\2\u00b0\26\3\2\2\2\u00b1\u00b2\7d\2\2\u00b2")
        buf.write("\u00b3\7q\2\2\u00b3\u00b4\7q\2\2\u00b4\u00b5\7n\2\2\u00b5")
        buf.write("\u00b6\7g\2\2\u00b6\u00b7\7c\2\2\u00b7\u00b8\7p\2\2\u00b8")
        buf.write("\30\3\2\2\2\u00b9\u00ba\7h\2\2\u00ba\u00bb\7n\2\2\u00bb")
        buf.write("\u00bc\7q\2\2\u00bc\u00bd\7c\2\2\u00bd\u00be\7v\2\2\u00be")
        buf.write("\32\3\2\2\2\u00bf\u00c0\7u\2\2\u00c0\u00c1\7v\2\2\u00c1")
        buf.write("\u00c2\7t\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4\7p\2\2\u00c4")
        buf.write("\u00c5\7i\2\2\u00c5\34\3\2\2\2\u00c6\u00c7\7-\2\2\u00c7")
        buf.write("\36\3\2\2\2\u00c8\u00c9\7,\2\2\u00c9 \3\2\2\2\u00ca\u00cb")
        buf.write("\7#\2\2\u00cb\"\3\2\2\2\u00cc\u00cd\7~\2\2\u00cd\u00ce")
        buf.write("\7~\2\2\u00ce$\3\2\2\2\u00cf\u00d0\7#\2\2\u00d0\u00d1")
        buf.write("\7?\2\2\u00d1&\3\2\2\2\u00d2\u00d3\7>\2\2\u00d3(\3\2\2")
        buf.write("\2\u00d4\u00d5\7>\2\2\u00d5\u00d6\7?\2\2\u00d6*\3\2\2")
        buf.write("\2\u00d7\u00d8\7?\2\2\u00d8,\3\2\2\2\u00d9\u00da\7/\2")
        buf.write("\2\u00da.\3\2\2\2\u00db\u00dc\7\61\2\2\u00dc\60\3\2\2")
        buf.write("\2\u00dd\u00de\7\'\2\2\u00de\62\3\2\2\2\u00df\u00e0\7")
        buf.write("(\2\2\u00e0\u00e1\7(\2\2\u00e1\64\3\2\2\2\u00e2\u00e3")
        buf.write("\7?\2\2\u00e3\u00e4\7?\2\2\u00e4\66\3\2\2\2\u00e5\u00e6")
        buf.write("\7@\2\2\u00e68\3\2\2\2\u00e7\u00e8\7@\2\2\u00e8\u00e9")
        buf.write("\7?\2\2\u00e9:\3\2\2\2\u00ea\u00eb\7]\2\2\u00eb<\3\2\2")
        buf.write("\2\u00ec\u00ed\7_\2\2\u00ed>\3\2\2\2\u00ee\u00ef\7}\2")
        buf.write("\2\u00ef@\3\2\2\2\u00f0\u00f1\7\177\2\2\u00f1B\3\2\2\2")
        buf.write("\u00f2\u00f3\7*\2\2\u00f3D\3\2\2\2\u00f4\u00f5\7+\2\2")
        buf.write("\u00f5F\3\2\2\2\u00f6\u00f7\7=\2\2\u00f7H\3\2\2\2\u00f8")
        buf.write("\u00f9\7.\2\2\u00f9J\3\2\2\2\u00fa\u00fb\7v\2\2\u00fb")
        buf.write("\u00fc\7t\2\2\u00fc\u00fd\7w\2\2\u00fd\u0104\7g\2\2\u00fe")
        buf.write("\u00ff\7h\2\2\u00ff\u0100\7c\2\2\u0100\u0101\7n\2\2\u0101")
        buf.write("\u0102\7u\2\2\u0102\u0104\7g\2\2\u0103\u00fa\3\2\2\2\u0103")
        buf.write("\u00fe\3\2\2\2\u0104L\3\2\2\2\u0105\u0106\t\2\2\2\u0106")
        buf.write("N\3\2\2\2\u0107\u0108\7\60\2\2\u0108P\3\2\2\2\u0109\u010f")
        buf.write("\t\3\2\2\u010a\u010b\7g\2\2\u010b\u010f\7/\2\2\u010c\u010d")
        buf.write("\7G\2\2\u010d\u010f\7/\2\2\u010e\u0109\3\2\2\2\u010e\u010a")
        buf.write("\3\2\2\2\u010e\u010c\3\2\2\2\u010fR\3\2\2\2\u0110\u0112")
        buf.write("\5M\'\2\u0111\u0110\3\2\2\2\u0112\u0113\3\2\2\2\u0113")
        buf.write("\u0111\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0115\3\2\2\2")
        buf.write("\u0115\u0119\5O(\2\u0116\u0118\5M\'\2\u0117\u0116\3\2")
        buf.write("\2\2\u0118\u011b\3\2\2\2\u0119\u0117\3\2\2\2\u0119\u011a")
        buf.write("\3\2\2\2\u011a\u0129\3\2\2\2\u011b\u0119\3\2\2\2\u011c")
        buf.write("\u011e\5M\'\2\u011d\u011c\3\2\2\2\u011e\u0121\3\2\2\2")
        buf.write("\u011f\u011d\3\2\2\2\u011f\u0120\3\2\2\2\u0120\u0122\3")
        buf.write("\2\2\2\u0121\u011f\3\2\2\2\u0122\u0124\5O(\2\u0123\u0125")
        buf.write("\5M\'\2\u0124\u0123\3\2\2\2\u0125\u0126\3\2\2\2\u0126")
        buf.write("\u0124\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u0129\3\2\2\2")
        buf.write("\u0128\u0111\3\2\2\2\u0128\u011f\3\2\2\2\u0129T\3\2\2")
        buf.write("\2\u012a\u012c\5M\'\2\u012b\u012a\3\2\2\2\u012c\u012d")
        buf.write("\3\2\2\2\u012d\u012b\3\2\2\2\u012d\u012e\3\2\2\2\u012e")
        buf.write("\u012f\3\2\2\2\u012f\u0131\5Q)\2\u0130\u0132\5M\'\2\u0131")
        buf.write("\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u0131\3\2\2\2")
        buf.write("\u0133\u0134\3\2\2\2\u0134V\3\2\2\2\u0135\u0137\5M\'\2")
        buf.write("\u0136\u0135\3\2\2\2\u0137\u013a\3\2\2\2\u0138\u0136\3")
        buf.write("\2\2\2\u0138\u0139\3\2\2\2\u0139\u013b\3\2\2\2\u013a\u0138")
        buf.write("\3\2\2\2\u013b\u013d\5O(\2\u013c\u013e\5M\'\2\u013d\u013c")
        buf.write("\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u013d\3\2\2\2\u013f")
        buf.write("\u0140\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u0143\5Q)\2\u0142")
        buf.write("\u0144\5M\'\2\u0143\u0142\3\2\2\2\u0144\u0145\3\2\2\2")
        buf.write("\u0145\u0143\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u015a\3")
        buf.write("\2\2\2\u0147\u0149\5M\'\2\u0148\u0147\3\2\2\2\u0149\u014a")
        buf.write("\3\2\2\2\u014a\u0148\3\2\2\2\u014a\u014b\3\2\2\2\u014b")
        buf.write("\u014c\3\2\2\2\u014c\u0150\5O(\2\u014d\u014f\5M\'\2\u014e")
        buf.write("\u014d\3\2\2\2\u014f\u0152\3\2\2\2\u0150\u014e\3\2\2\2")
        buf.write("\u0150\u0151\3\2\2\2\u0151\u0153\3\2\2\2\u0152\u0150\3")
        buf.write("\2\2\2\u0153\u0155\5Q)\2\u0154\u0156\5M\'\2\u0155\u0154")
        buf.write("\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0155\3\2\2\2\u0157")
        buf.write("\u0158\3\2\2\2\u0158\u015a\3\2\2\2\u0159\u0138\3\2\2\2")
        buf.write("\u0159\u0148\3\2\2\2\u015aX\3\2\2\2\u015b\u015f\5S*\2")
        buf.write("\u015c\u015f\5U+\2\u015d\u015f\5W,\2\u015e\u015b\3\2\2")
        buf.write("\2\u015e\u015c\3\2\2\2\u015e\u015d\3\2\2\2\u015fZ\3\2")
        buf.write("\2\2\u0160\u0162\5M\'\2\u0161\u0160\3\2\2\2\u0162\u0163")
        buf.write("\3\2\2\2\u0163\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164")
        buf.write("\\\3\2\2\2\u0165\u0166\7$\2\2\u0166^\3\2\2\2\u0167\u0168")
        buf.write("\7^\2\2\u0168\u0169\t\4\2\2\u0169`\3\2\2\2\u016a\u016b")
        buf.write("\7^\2\2\u016b\u016c\n\5\2\2\u016cb\3\2\2\2\u016d\u016e")
        buf.write("\n\6\2\2\u016ed\3\2\2\2\u016f\u0173\t\7\2\2\u0170\u0172")
        buf.write("\t\b\2\2\u0171\u0170\3\2\2\2\u0172\u0175\3\2\2\2\u0173")
        buf.write("\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174f\3\2\2\2\u0175")
        buf.write("\u0173\3\2\2\2\u0176\u0178\t\t\2\2\u0177\u0176\3\2\2\2")
        buf.write("\u0178\u0179\3\2\2\2\u0179\u0177\3\2\2\2\u0179\u017a\3")
        buf.write("\2\2\2\u017a\u017b\3\2\2\2\u017b\u017c\b\64\2\2\u017c")
        buf.write("h\3\2\2\2\u017d\u017e\7\61\2\2\u017e\u017f\7,\2\2\u017f")
        buf.write("j\3\2\2\2\u0180\u0181\7,\2\2\u0181\u0182\7\61\2\2\u0182")
        buf.write("l\3\2\2\2\u0183\u0184\7\61\2\2\u0184\u0185\7\61\2\2\u0185")
        buf.write("n\3\2\2\2\u0186\u018a\5i\65\2\u0187\u0189\13\2\2\2\u0188")
        buf.write("\u0187\3\2\2\2\u0189\u018c\3\2\2\2\u018a\u018b\3\2\2\2")
        buf.write("\u018a\u0188\3\2\2\2\u018b\u018d\3\2\2\2\u018c\u018a\3")
        buf.write("\2\2\2\u018d\u018e\5k\66\2\u018e\u018f\3\2\2\2\u018f\u0190")
        buf.write("\b8\2\2\u0190p\3\2\2\2\u0191\u0195\5m\67\2\u0192\u0194")
        buf.write("\n\n\2\2\u0193\u0192\3\2\2\2\u0194\u0197\3\2\2\2\u0195")
        buf.write("\u0193\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u0198\3\2\2\2")
        buf.write("\u0197\u0195\3\2\2\2\u0198\u0199\b9\2\2\u0199r\3\2\2\2")
        buf.write("\u019a\u019d\5_\60\2\u019b\u019d\t\13\2\2\u019c\u019a")
        buf.write("\3\2\2\2\u019c\u019b\3\2\2\2\u019dt\3\2\2\2\u019e\u01a2")
        buf.write("\5]/\2\u019f\u01a1\5s:\2\u01a0\u019f\3\2\2\2\u01a1\u01a4")
        buf.write("\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3")
        buf.write("\u01a5\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a5\u01a6\5]/\2\u01a6")
        buf.write("v\3\2\2\2\u01a7\u01ae\5]/\2\u01a8\u01ad\5_\60\2\u01a9")
        buf.write("\u01ad\5s:\2\u01aa\u01ab\7^\2\2\u01ab\u01ad\7\2\2\3\u01ac")
        buf.write("\u01a8\3\2\2\2\u01ac\u01a9\3\2\2\2\u01ac\u01aa\3\2\2\2")
        buf.write("\u01ad\u01b0\3\2\2\2\u01ae\u01ac\3\2\2\2\u01ae\u01af\3")
        buf.write("\2\2\2\u01af\u01b5\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b1\u01b2")
        buf.write("\5]/\2\u01b2\u01b3\7^\2\2\u01b3\u01b5\3\2\2\2\u01b4\u01a7")
        buf.write("\3\2\2\2\u01b4\u01b1\3\2\2\2\u01b5x\3\2\2\2\u01b6\u01ba")
        buf.write("\5]/\2\u01b7\u01b9\5s:\2\u01b8\u01b7\3\2\2\2\u01b9\u01bc")
        buf.write("\3\2\2\2\u01ba\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb")
        buf.write("\u01bd\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bd\u01be\5a\61\2")
        buf.write("\u01bez\3\2\2\2\u01bf\u01c0\13\2\2\2\u01c0|\3\2\2\2\37")
        buf.write("\2\u0103\u010e\u0113\u0119\u011f\u0126\u0128\u012d\u0133")
        buf.write("\u0138\u013f\u0145\u014a\u0150\u0157\u0159\u015e\u0163")
        buf.write("\u0173\u0179\u018a\u0195\u019c\u01a2\u01ac\u01ae\u01b4")
        buf.write("\u01ba\3\b\2\2")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    INTTYPE = 9
    VOIDTYPE = 10
    BOOLTYPE = 11
    FLOATTYPE = 12
    STRINGTYPE = 13
    ADD = 14
    MUL = 15
    NOT = 16
    OR = 17
    NEQ = 18
    LESS = 19
    ELESS = 20
    ASSIGN = 21
    SUB = 22
    DIV = 23
    MOD = 24
    AND = 25
    EQ = 26
    GREAT = 27
    EGREAT = 28
    LS = 29
    RS = 30
    LB = 31
    RB = 32
    LP = 33
    RP = 34
    SEMI = 35
    CM = 36
    BOOLLIT = 37
    FLOATLIT = 38
    INTLIT = 39
    ID = 40
    WS = 41
    BLOCKCOMMENT = 42
    LINECOMMENT = 43
    STRINGLIT = 44
    UNCLOSE_STRING = 45
    ILLEGAL_ESCAPE = 46
    ERROR_CHAR = 47

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'do'", "'while'", "'for'", "'break'", "'continue'", 
            "'return'", "'int'", "'void'", "'boolean'", "'float'", "'string'", 
            "'+'", "'*'", "'!'", "'||'", "'!='", "'<'", "'<='", "'='", "'-'", 
            "'/'", "'%'", "'&&'", "'=='", "'>'", "'>='", "'['", "']'", "'{'", 
            "'}'", "'('", "')'", "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "BOOLTYPE", "FLOATTYPE", "STRINGTYPE", 
            "ADD", "MUL", "NOT", "OR", "NEQ", "LESS", "ELESS", "ASSIGN", 
            "SUB", "DIV", "MOD", "AND", "EQ", "GREAT", "EGREAT", "LS", "RS", 
            "LB", "RB", "LP", "RP", "SEMI", "CM", "BOOLLIT", "FLOATLIT", 
            "INTLIT", "ID", "WS", "BLOCKCOMMENT", "LINECOMMENT", "STRINGLIT", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "INTTYPE", "VOIDTYPE", "BOOLTYPE", "FLOATTYPE", 
                  "STRINGTYPE", "ADD", "MUL", "NOT", "OR", "NEQ", "LESS", 
                  "ELESS", "ASSIGN", "SUB", "DIV", "MOD", "AND", "EQ", "GREAT", 
                  "EGREAT", "LS", "RS", "LB", "RB", "LP", "RP", "SEMI", 
                  "CM", "BOOLLIT", "NUMBER", "POINT", "EXP", "NOEXP", "NOPOINT", 
                  "ALL", "FLOATLIT", "INTLIT", "QUOTE", "ESCAPE_SEQUENCE", 
                  "ESCAPE_ILLEGAL", "NOTQUOTE", "ID", "WS", "LCOMMENT", 
                  "RCOMMENT", "COMMENT", "BLOCKCOMMENT", "LINECOMMENT", 
                  "STRING", "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:
            result = super().emit();
            raise UncloseString(result.text[1:])
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text[1:]);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            if tk == self.STRINGLIT:
                st = self.text[1:-1]
                self.text = st
            return super().emit();


