# Generated from /home/lin/0-PPL/Assignment/initial/src/main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\61")
        buf.write("\u01ba\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("&\u0104\n&\3\'\3\'\3(\3(\3)\3)\3*\3*\3*\3*\3*\5*\u0111")
        buf.write("\n*\3+\6+\u0114\n+\r+\16+\u0115\3+\3+\7+\u011a\n+\f+\16")
        buf.write("+\u011d\13+\3+\7+\u0120\n+\f+\16+\u0123\13+\3+\3+\6+\u0127")
        buf.write("\n+\r+\16+\u0128\5+\u012b\n+\3,\6,\u012e\n,\r,\16,\u012f")
        buf.write("\3,\3,\6,\u0134\n,\r,\16,\u0135\3-\7-\u0139\n-\f-\16-")
        buf.write("\u013c\13-\3-\3-\6-\u0140\n-\r-\16-\u0141\3-\3-\6-\u0146")
        buf.write("\n-\r-\16-\u0147\3-\6-\u014b\n-\r-\16-\u014c\3-\3-\7-")
        buf.write("\u0151\n-\f-\16-\u0154\13-\3-\3-\6-\u0158\n-\r-\16-\u0159")
        buf.write("\5-\u015c\n-\3.\3.\3.\5.\u0161\n.\3/\6/\u0164\n/\r/\16")
        buf.write("/\u0165\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\63\3")
        buf.write("\63\3\64\3\64\7\64\u0174\n\64\f\64\16\64\u0177\13\64\3")
        buf.write("\65\6\65\u017a\n\65\r\65\16\65\u017b\3\65\3\65\3\66\3")
        buf.write("\66\3\66\3\67\3\67\3\67\38\38\38\39\39\79\u018b\n9\f9")
        buf.write("\169\u018e\139\39\39\39\39\3:\3:\7:\u0196\n:\f:\16:\u0199")
        buf.write("\13:\3:\3:\3;\3;\3;\7;\u01a0\n;\f;\16;\u01a3\13;\3;\3")
        buf.write(";\3<\3<\3=\3=\3=\7=\u01ac\n=\f=\16=\u01af\13=\3>\3>\3")
        buf.write(">\7>\u01b4\n>\f>\16>\u01b7\13>\3>\3>\4\u018c\u01b5\2?")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M\2")
        buf.write("O\2Q\2S\2U\2W\2Y\2[(])_\2a\2c\2e\2g*i+k\2m\2o\2q,s-u.")
        buf.write("w/y\60{\61\3\2\f\3\2\62;\4\2GGgg\t\2$$^^ddhhppttvv\3\2")
        buf.write("$$\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\4\2\f")
        buf.write("\f\17\17\b\2\f\f\17\17$$GHQQ^^\4\2$$^^\2\u01c9\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2[\3\2\2\2\2]\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2q\3")
        buf.write("\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{")
        buf.write("\3\2\2\2\3}\3\2\2\2\5\u0080\3\2\2\2\7\u0085\3\2\2\2\t")
        buf.write("\u0088\3\2\2\2\13\u008e\3\2\2\2\r\u0092\3\2\2\2\17\u0098")
        buf.write("\3\2\2\2\21\u00a1\3\2\2\2\23\u00a8\3\2\2\2\25\u00ac\3")
        buf.write("\2\2\2\27\u00b1\3\2\2\2\31\u00b9\3\2\2\2\33\u00bf\3\2")
        buf.write("\2\2\35\u00c6\3\2\2\2\37\u00c8\3\2\2\2!\u00ca\3\2\2\2")
        buf.write("#\u00cc\3\2\2\2%\u00cf\3\2\2\2\'\u00d2\3\2\2\2)\u00d4")
        buf.write("\3\2\2\2+\u00d7\3\2\2\2-\u00d9\3\2\2\2/\u00db\3\2\2\2")
        buf.write("\61\u00dd\3\2\2\2\63\u00df\3\2\2\2\65\u00e2\3\2\2\2\67")
        buf.write("\u00e5\3\2\2\29\u00e7\3\2\2\2;\u00ea\3\2\2\2=\u00ec\3")
        buf.write("\2\2\2?\u00ee\3\2\2\2A\u00f0\3\2\2\2C\u00f2\3\2\2\2E\u00f4")
        buf.write("\3\2\2\2G\u00f6\3\2\2\2I\u00f8\3\2\2\2K\u0103\3\2\2\2")
        buf.write("M\u0105\3\2\2\2O\u0107\3\2\2\2Q\u0109\3\2\2\2S\u0110\3")
        buf.write("\2\2\2U\u012a\3\2\2\2W\u012d\3\2\2\2Y\u015b\3\2\2\2[\u0160")
        buf.write("\3\2\2\2]\u0163\3\2\2\2_\u0167\3\2\2\2a\u0169\3\2\2\2")
        buf.write("c\u016c\3\2\2\2e\u016f\3\2\2\2g\u0171\3\2\2\2i\u0179\3")
        buf.write("\2\2\2k\u017f\3\2\2\2m\u0182\3\2\2\2o\u0185\3\2\2\2q\u0188")
        buf.write("\3\2\2\2s\u0193\3\2\2\2u\u019c\3\2\2\2w\u01a6\3\2\2\2")
        buf.write("y\u01a8\3\2\2\2{\u01b0\3\2\2\2}~\7k\2\2~\177\7h\2\2\177")
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
        buf.write("N\3\2\2\2\u0107\u0108\7\60\2\2\u0108P\3\2\2\2\u0109\u010a")
        buf.write("\3\2\2\2\u010aR\3\2\2\2\u010b\u0111\t\3\2\2\u010c\u010d")
        buf.write("\7g\2\2\u010d\u0111\7/\2\2\u010e\u010f\7G\2\2\u010f\u0111")
        buf.write("\7/\2\2\u0110\u010b\3\2\2\2\u0110\u010c\3\2\2\2\u0110")
        buf.write("\u010e\3\2\2\2\u0111T\3\2\2\2\u0112\u0114\5M\'\2\u0113")
        buf.write("\u0112\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0113\3\2\2\2")
        buf.write("\u0115\u0116\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u011b\5")
        buf.write("O(\2\u0118\u011a\5M\'\2\u0119\u0118\3\2\2\2\u011a\u011d")
        buf.write("\3\2\2\2\u011b\u0119\3\2\2\2\u011b\u011c\3\2\2\2\u011c")
        buf.write("\u012b\3\2\2\2\u011d\u011b\3\2\2\2\u011e\u0120\5M\'\2")
        buf.write("\u011f\u011e\3\2\2\2\u0120\u0123\3\2\2\2\u0121\u011f\3")
        buf.write("\2\2\2\u0121\u0122\3\2\2\2\u0122\u0124\3\2\2\2\u0123\u0121")
        buf.write("\3\2\2\2\u0124\u0126\5O(\2\u0125\u0127\5M\'\2\u0126\u0125")
        buf.write("\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u0126\3\2\2\2\u0128")
        buf.write("\u0129\3\2\2\2\u0129\u012b\3\2\2\2\u012a\u0113\3\2\2\2")
        buf.write("\u012a\u0121\3\2\2\2\u012bV\3\2\2\2\u012c\u012e\5M\'\2")
        buf.write("\u012d\u012c\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u012d\3")
        buf.write("\2\2\2\u012f\u0130\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u0133")
        buf.write("\5S*\2\u0132\u0134\5M\'\2\u0133\u0132\3\2\2\2\u0134\u0135")
        buf.write("\3\2\2\2\u0135\u0133\3\2\2\2\u0135\u0136\3\2\2\2\u0136")
        buf.write("X\3\2\2\2\u0137\u0139\5M\'\2\u0138\u0137\3\2\2\2\u0139")
        buf.write("\u013c\3\2\2\2\u013a\u0138\3\2\2\2\u013a\u013b\3\2\2\2")
        buf.write("\u013b\u013d\3\2\2\2\u013c\u013a\3\2\2\2\u013d\u013f\5")
        buf.write("O(\2\u013e\u0140\5M\'\2\u013f\u013e\3\2\2\2\u0140\u0141")
        buf.write("\3\2\2\2\u0141\u013f\3\2\2\2\u0141\u0142\3\2\2\2\u0142")
        buf.write("\u0143\3\2\2\2\u0143\u0145\5S*\2\u0144\u0146\5M\'\2\u0145")
        buf.write("\u0144\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u0145\3\2\2\2")
        buf.write("\u0147\u0148\3\2\2\2\u0148\u015c\3\2\2\2\u0149\u014b\5")
        buf.write("M\'\2\u014a\u0149\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014a")
        buf.write("\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u014e\3\2\2\2\u014e")
        buf.write("\u0152\5O(\2\u014f\u0151\5M\'\2\u0150\u014f\3\2\2\2\u0151")
        buf.write("\u0154\3\2\2\2\u0152\u0150\3\2\2\2\u0152\u0153\3\2\2\2")
        buf.write("\u0153\u0155\3\2\2\2\u0154\u0152\3\2\2\2\u0155\u0157\5")
        buf.write("S*\2\u0156\u0158\5M\'\2\u0157\u0156\3\2\2\2\u0158\u0159")
        buf.write("\3\2\2\2\u0159\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015a")
        buf.write("\u015c\3\2\2\2\u015b\u013a\3\2\2\2\u015b\u014a\3\2\2\2")
        buf.write("\u015cZ\3\2\2\2\u015d\u0161\5U+\2\u015e\u0161\5W,\2\u015f")
        buf.write("\u0161\5Y-\2\u0160\u015d\3\2\2\2\u0160\u015e\3\2\2\2\u0160")
        buf.write("\u015f\3\2\2\2\u0161\\\3\2\2\2\u0162\u0164\5M\'\2\u0163")
        buf.write("\u0162\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0163\3\2\2\2")
        buf.write("\u0165\u0166\3\2\2\2\u0166^\3\2\2\2\u0167\u0168\7$\2\2")
        buf.write("\u0168`\3\2\2\2\u0169\u016a\7^\2\2\u016a\u016b\t\4\2\2")
        buf.write("\u016bb\3\2\2\2\u016c\u016d\7^\2\2\u016d\u016e\n\4\2\2")
        buf.write("\u016ed\3\2\2\2\u016f\u0170\n\5\2\2\u0170f\3\2\2\2\u0171")
        buf.write("\u0175\t\6\2\2\u0172\u0174\t\7\2\2\u0173\u0172\3\2\2\2")
        buf.write("\u0174\u0177\3\2\2\2\u0175\u0173\3\2\2\2\u0175\u0176\3")
        buf.write("\2\2\2\u0176h\3\2\2\2\u0177\u0175\3\2\2\2\u0178\u017a")
        buf.write("\t\b\2\2\u0179\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017b")
        buf.write("\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017d\3\2\2\2")
        buf.write("\u017d\u017e\b\65\2\2\u017ej\3\2\2\2\u017f\u0180\7\61")
        buf.write("\2\2\u0180\u0181\7,\2\2\u0181l\3\2\2\2\u0182\u0183\7,")
        buf.write("\2\2\u0183\u0184\7\61\2\2\u0184n\3\2\2\2\u0185\u0186\7")
        buf.write("\61\2\2\u0186\u0187\7\61\2\2\u0187p\3\2\2\2\u0188\u018c")
        buf.write("\5k\66\2\u0189\u018b\13\2\2\2\u018a\u0189\3\2\2\2\u018b")
        buf.write("\u018e\3\2\2\2\u018c\u018d\3\2\2\2\u018c\u018a\3\2\2\2")
        buf.write("\u018d\u018f\3\2\2\2\u018e\u018c\3\2\2\2\u018f\u0190\5")
        buf.write("m\67\2\u0190\u0191\3\2\2\2\u0191\u0192\b9\2\2\u0192r\3")
        buf.write("\2\2\2\u0193\u0197\5o8\2\u0194\u0196\n\t\2\2\u0195\u0194")
        buf.write("\3\2\2\2\u0196\u0199\3\2\2\2\u0197\u0195\3\2\2\2\u0197")
        buf.write("\u0198\3\2\2\2\u0198\u019a\3\2\2\2\u0199\u0197\3\2\2\2")
        buf.write("\u019a\u019b\b:\2\2\u019bt\3\2\2\2\u019c\u01a1\5_\60\2")
        buf.write("\u019d\u01a0\5a\61\2\u019e\u01a0\n\n\2\2\u019f\u019d\3")
        buf.write("\2\2\2\u019f\u019e\3\2\2\2\u01a0\u01a3\3\2\2\2\u01a1\u019f")
        buf.write("\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a4\3\2\2\2\u01a3")
        buf.write("\u01a1\3\2\2\2\u01a4\u01a5\5_\60\2\u01a5v\3\2\2\2\u01a6")
        buf.write("\u01a7\13\2\2\2\u01a7x\3\2\2\2\u01a8\u01ad\5_\60\2\u01a9")
        buf.write("\u01ac\5a\61\2\u01aa\u01ac\n\n\2\2\u01ab\u01a9\3\2\2\2")
        buf.write("\u01ab\u01aa\3\2\2\2\u01ac\u01af\3\2\2\2\u01ad\u01ab\3")
        buf.write("\2\2\2\u01ad\u01ae\3\2\2\2\u01aez\3\2\2\2\u01af\u01ad")
        buf.write("\3\2\2\2\u01b0\u01b5\5_\60\2\u01b1\u01b4\5a\61\2\u01b2")
        buf.write("\u01b4\n\13\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b2\3\2\2")
        buf.write("\2\u01b4\u01b7\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b5\u01b3")
        buf.write("\3\2\2\2\u01b6\u01b8\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b8")
        buf.write("\u01b9\5c\62\2\u01b9|\3\2\2\2\37\2\u0103\u0110\u0115\u011b")
        buf.write("\u0121\u0128\u012a\u012f\u0135\u013a\u0141\u0147\u014c")
        buf.write("\u0152\u0159\u015b\u0160\u0165\u0175\u017b\u018c\u0197")
        buf.write("\u019f\u01a1\u01ab\u01ad\u01b3\u01b5\3\b\2\2")
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
    ERROR_CHAR = 45
    UNCLOSE_STRING = 46
    ILLEGAL_ESCAPE = 47

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
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "INTTYPE", "VOIDTYPE", "BOOLTYPE", "FLOATTYPE", 
                  "STRINGTYPE", "ADD", "MUL", "NOT", "OR", "NEQ", "LESS", 
                  "ELESS", "ASSIGN", "SUB", "DIV", "MOD", "AND", "EQ", "GREAT", 
                  "EGREAT", "LS", "RS", "LB", "RB", "LP", "RP", "SEMI", 
                  "CM", "BOOLLIT", "NUMBER", "POINT", "FRAG", "EXP", "NOEXP", 
                  "NOPOINT", "ALL", "FLOATLIT", "INTLIT", "QUOTE", "ESCAPE_SEQUENCE", 
                  "ESCAPE_ILLEGAL", "NOTQUOTE", "ID", "WS", "LCOMMENT", 
                  "RCOMMENT", "COMMENT", "BLOCKCOMMENT", "LINECOMMENT", 
                  "STRINGLIT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            raise UncloseString(result.text[1:]);
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


