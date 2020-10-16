# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2L")
        buf.write("\u02cc\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3")
        buf.write("\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22")
        buf.write("\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&")
        buf.write("\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3*\3*\3*\3")
        buf.write("*\3+\3+\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\61\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\38\38\38\39\39\39\39\39\39\3")
        buf.write("9\39\39\39\3:\3:\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\3<\3<\3")
        buf.write("<\3<\3=\3=\3=\3=\3=\3=\3>\3>\3>\3>\3>\3?\3?\3?\3?\3?\3")
        buf.write("?\3@\3@\3@\3@\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3E\3")
        buf.write("F\3F\3F\3G\3G\3G\3H\3H\3H\3I\3I\3I\3J\3J\3K\3K\3L\3L\3")
        buf.write("L\3M\3M\3M\3M\3M\7M\u022b\nM\fM\16M\u022e\13M\3N\3N\7")
        buf.write("N\u0232\nN\fN\16N\u0235\13N\3N\5N\u0238\nN\3O\3O\3O\3")
        buf.write("O\7O\u023e\nO\fO\16O\u0241\13O\3P\3P\3P\5P\u0246\nP\3")
        buf.write("Q\3Q\3Q\5Q\u024b\nQ\3Q\6Q\u024e\nQ\rQ\16Q\u024f\3R\3R")
        buf.write("\7R\u0254\nR\fR\16R\u0257\13R\3S\3S\7S\u025b\nS\fS\16")
        buf.write("S\u025e\13S\3S\3S\3S\3S\3S\3S\5S\u0266\nS\3T\3T\3T\3T")
        buf.write("\3T\3T\3T\5T\u026f\nT\3U\3U\3U\3U\3U\3U\7U\u0277\nU\f")
        buf.write("U\16U\u027a\13U\3U\3U\3V\3V\3V\3V\3V\7V\u0283\nV\fV\16")
        buf.write("V\u0286\13V\3V\3V\3V\3V\7V\u028c\nV\fV\16V\u028f\13V\3")
        buf.write("V\3V\3V\3V\7V\u0295\nV\fV\16V\u0298\13V\3V\3V\3V\3V\7")
        buf.write("V\u029e\nV\fV\16V\u02a1\13V\3V\3V\3V\3V\7V\u02a7\nV\f")
        buf.write("V\16V\u02aa\13V\5V\u02ac\nV\3V\3V\3W\3W\5W\u02b2\nW\3")
        buf.write("X\3X\3X\3X\3X\7X\u02b9\nX\fX\16X\u02bc\13X\3Y\6Y\u02bf")
        buf.write("\nY\rY\16Y\u02c0\3Y\3Y\3Z\3Z\3[\3[\3\\\3\\\3]\3]\2\2^")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O")
        buf.write(")Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;")
        buf.write("u<w=y>{?}@\177A\u0081\2\u0083\2\u0085\2\u0087\2\u0089")
        buf.write("\2\u008b\2\u008d\2\u008f\2\u0091\2\u0093\2\u0095\2\u0097")
        buf.write("\2\u0099\2\u009b\2\u009d\2\u009fB\u00a1\2\u00a3\2\u00a5")
        buf.write("C\u00a7\2\u00a9D\u00abE\u00adF\u00afG\u00b1H\u00b3I\u00b5")
        buf.write("J\u00b7K\u00b9L\3\2\17\3\2c|\3\2C\\\3\2\62;\4\2ZZzz\4")
        buf.write("\2\63;CH\3\2CH\3\2\63;\4\2QQqq\3\2\639\3\2\629\4\2GGg")
        buf.write("g\6\2\f\f$$GHQQ\5\2\13\f\17\17\"\"\2\u02e1\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s")
        buf.write("\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2")
        buf.write("}\3\2\2\2\2\177\3\2\2\2\2\u009f\3\2\2\2\2\u00a5\3\2\2")
        buf.write("\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af")
        buf.write("\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2")
        buf.write("\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2\2\3\u00bb\3\2\2\2\5\u00c8")
        buf.write("\3\2\2\2\7\u00d5\3\2\2\2\t\u00e3\3\2\2\2\13\u00f1\3\2")
        buf.write("\2\2\r\u0101\3\2\2\2\17\u0111\3\2\2\2\21\u0120\3\2\2\2")
        buf.write("\23\u012f\3\2\2\2\25\u0131\3\2\2\2\27\u0133\3\2\2\2\31")
        buf.write("\u0135\3\2\2\2\33\u0137\3\2\2\2\35\u0139\3\2\2\2\37\u013b")
        buf.write("\3\2\2\2!\u013d\3\2\2\2#\u013f\3\2\2\2%\u0141\3\2\2\2")
        buf.write("\'\u0143\3\2\2\2)\u0145\3\2\2\2+\u0148\3\2\2\2-\u014a")
        buf.write("\3\2\2\2/\u014d\3\2\2\2\61\u014f\3\2\2\2\63\u0152\3\2")
        buf.write("\2\2\65\u0154\3\2\2\2\67\u0157\3\2\2\29\u0159\3\2\2\2")
        buf.write(";\u015b\3\2\2\2=\u015e\3\2\2\2?\u0161\3\2\2\2A\u0164\3")
        buf.write("\2\2\2C\u0167\3\2\2\2E\u0169\3\2\2\2G\u016b\3\2\2\2I\u016e")
        buf.write("\3\2\2\2K\u0171\3\2\2\2M\u0175\3\2\2\2O\u0178\3\2\2\2")
        buf.write("Q\u017b\3\2\2\2S\u017f\3\2\2\2U\u0183\3\2\2\2W\u0185\3")
        buf.write("\2\2\2Y\u018a\3\2\2\2[\u0190\3\2\2\2]\u0199\3\2\2\2_\u019c")
        buf.write("\3\2\2\2a\u01a1\3\2\2\2c\u01a8\3\2\2\2e\u01b0\3\2\2\2")
        buf.write("g\u01b6\3\2\2\2i\u01bd\3\2\2\2k\u01c6\3\2\2\2m\u01ca\3")
        buf.write("\2\2\2o\u01d3\3\2\2\2q\u01d6\3\2\2\2s\u01e0\3\2\2\2u\u01e7")
        buf.write("\3\2\2\2w\u01ec\3\2\2\2y\u01f0\3\2\2\2{\u01f6\3\2\2\2")
        buf.write("}\u01fb\3\2\2\2\177\u0201\3\2\2\2\u0081\u0207\3\2\2\2")
        buf.write("\u0083\u0209\3\2\2\2\u0085\u020b\3\2\2\2\u0087\u020d\3")
        buf.write("\2\2\2\u0089\u020f\3\2\2\2\u008b\u0212\3\2\2\2\u008d\u0215")
        buf.write("\3\2\2\2\u008f\u0218\3\2\2\2\u0091\u021b\3\2\2\2\u0093")
        buf.write("\u021e\3\2\2\2\u0095\u0220\3\2\2\2\u0097\u0222\3\2\2\2")
        buf.write("\u0099\u0225\3\2\2\2\u009b\u0237\3\2\2\2\u009d\u0239\3")
        buf.write("\2\2\2\u009f\u0245\3\2\2\2\u00a1\u0247\3\2\2\2\u00a3\u0251")
        buf.write("\3\2\2\2\u00a5\u0258\3\2\2\2\u00a7\u026e\3\2\2\2\u00a9")
        buf.write("\u0270\3\2\2\2\u00ab\u027d\3\2\2\2\u00ad\u02b1\3\2\2\2")
        buf.write("\u00af\u02b3\3\2\2\2\u00b1\u02be\3\2\2\2\u00b3\u02c4\3")
        buf.write("\2\2\2\u00b5\u02c6\3\2\2\2\u00b7\u02c8\3\2\2\2\u00b9\u02ca")
        buf.write("\3\2\2\2\u00bb\u00bc\7k\2\2\u00bc\u00bd\7p\2\2\u00bd\u00be")
        buf.write("\7v\2\2\u00be\u00bf\7a\2\2\u00bf\u00c0\7q\2\2\u00c0\u00c1")
        buf.write("\7h\2\2\u00c1\u00c2\7a\2\2\u00c2\u00c3\7h\2\2\u00c3\u00c4")
        buf.write("\7n\2\2\u00c4\u00c5\7q\2\2\u00c5\u00c6\7c\2\2\u00c6\u00c7")
        buf.write("\7v\2\2\u00c7\4\3\2\2\2\u00c8\u00c9\7h\2\2\u00c9\u00ca")
        buf.write("\7n\2\2\u00ca\u00cb\7q\2\2\u00cb\u00cc\7c\2\2\u00cc\u00cd")
        buf.write("\7v\2\2\u00cd\u00ce\7a\2\2\u00ce\u00cf\7q\2\2\u00cf\u00d0")
        buf.write("\7h\2\2\u00d0\u00d1\7a\2\2\u00d1\u00d2\7k\2\2\u00d2\u00d3")
        buf.write("\7p\2\2\u00d3\u00d4\7v\2\2\u00d4\6\3\2\2\2\u00d5\u00d6")
        buf.write("\7k\2\2\u00d6\u00d7\7p\2\2\u00d7\u00d8\7v\2\2\u00d8\u00d9")
        buf.write("\7a\2\2\u00d9\u00da\7q\2\2\u00da\u00db\7h\2\2\u00db\u00dc")
        buf.write("\7a\2\2\u00dc\u00dd\7u\2\2\u00dd\u00de\7v\2\2\u00de\u00df")
        buf.write("\7t\2\2\u00df\u00e0\7k\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2")
        buf.write("\7i\2\2\u00e2\b\3\2\2\2\u00e3\u00e4\7u\2\2\u00e4\u00e5")
        buf.write("\7v\2\2\u00e5\u00e6\7t\2\2\u00e6\u00e7\7k\2\2\u00e7\u00e8")
        buf.write("\7p\2\2\u00e8\u00e9\7i\2\2\u00e9\u00ea\7a\2\2\u00ea\u00eb")
        buf.write("\7q\2\2\u00eb\u00ec\7h\2\2\u00ec\u00ed\7a\2\2\u00ed\u00ee")
        buf.write("\7k\2\2\u00ee\u00ef\7p\2\2\u00ef\u00f0\7v\2\2\u00f0\n")
        buf.write("\3\2\2\2\u00f1\u00f2\7h\2\2\u00f2\u00f3\7n\2\2\u00f3\u00f4")
        buf.write("\7q\2\2\u00f4\u00f5\7c\2\2\u00f5\u00f6\7v\2\2\u00f6\u00f7")
        buf.write("\7a\2\2\u00f7\u00f8\7q\2\2\u00f8\u00f9\7h\2\2\u00f9\u00fa")
        buf.write("\7a\2\2\u00fa\u00fb\7u\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd")
        buf.write("\7t\2\2\u00fd\u00fe\7k\2\2\u00fe\u00ff\7p\2\2\u00ff\u0100")
        buf.write("\7i\2\2\u0100\f\3\2\2\2\u0101\u0102\7u\2\2\u0102\u0103")
        buf.write("\7v\2\2\u0103\u0104\7t\2\2\u0104\u0105\7k\2\2\u0105\u0106")
        buf.write("\7p\2\2\u0106\u0107\7i\2\2\u0107\u0108\7a\2\2\u0108\u0109")
        buf.write("\7q\2\2\u0109\u010a\7h\2\2\u010a\u010b\7a\2\2\u010b\u010c")
        buf.write("\7h\2\2\u010c\u010d\7n\2\2\u010d\u010e\7q\2\2\u010e\u010f")
        buf.write("\7c\2\2\u010f\u0110\7v\2\2\u0110\16\3\2\2\2\u0111\u0112")
        buf.write("\7d\2\2\u0112\u0113\7q\2\2\u0113\u0114\7q\2\2\u0114\u0115")
        buf.write("\7n\2\2\u0115\u0116\7a\2\2\u0116\u0117\7q\2\2\u0117\u0118")
        buf.write("\7h\2\2\u0118\u0119\7a\2\2\u0119\u011a\7u\2\2\u011a\u011b")
        buf.write("\7v\2\2\u011b\u011c\7t\2\2\u011c\u011d\7k\2\2\u011d\u011e")
        buf.write("\7p\2\2\u011e\u011f\7i\2\2\u011f\20\3\2\2\2\u0120\u0121")
        buf.write("\7u\2\2\u0121\u0122\7v\2\2\u0122\u0123\7t\2\2\u0123\u0124")
        buf.write("\7k\2\2\u0124\u0125\7p\2\2\u0125\u0126\7i\2\2\u0126\u0127")
        buf.write("\7a\2\2\u0127\u0128\7q\2\2\u0128\u0129\7h\2\2\u0129\u012a")
        buf.write("\7a\2\2\u012a\u012b\7d\2\2\u012b\u012c\7q\2\2\u012c\u012d")
        buf.write("\7q\2\2\u012d\u012e\7n\2\2\u012e\22\3\2\2\2\u012f\u0130")
        buf.write("\7*\2\2\u0130\24\3\2\2\2\u0131\u0132\7+\2\2\u0132\26\3")
        buf.write("\2\2\2\u0133\u0134\7]\2\2\u0134\30\3\2\2\2\u0135\u0136")
        buf.write("\7_\2\2\u0136\32\3\2\2\2\u0137\u0138\7<\2\2\u0138\34\3")
        buf.write("\2\2\2\u0139\u013a\7\60\2\2\u013a\36\3\2\2\2\u013b\u013c")
        buf.write("\7.\2\2\u013c \3\2\2\2\u013d\u013e\7=\2\2\u013e\"\3\2")
        buf.write("\2\2\u013f\u0140\7}\2\2\u0140$\3\2\2\2\u0141\u0142\7\177")
        buf.write("\2\2\u0142&\3\2\2\2\u0143\u0144\7-\2\2\u0144(\3\2\2\2")
        buf.write("\u0145\u0146\7-\2\2\u0146\u0147\7\60\2\2\u0147*\3\2\2")
        buf.write("\2\u0148\u0149\7/\2\2\u0149,\3\2\2\2\u014a\u014b\7/\2")
        buf.write("\2\u014b\u014c\7\60\2\2\u014c.\3\2\2\2\u014d\u014e\7,")
        buf.write("\2\2\u014e\60\3\2\2\2\u014f\u0150\7,\2\2\u0150\u0151\7")
        buf.write("\60\2\2\u0151\62\3\2\2\2\u0152\u0153\7^\2\2\u0153\64\3")
        buf.write("\2\2\2\u0154\u0155\7^\2\2\u0155\u0156\7\60\2\2\u0156\66")
        buf.write("\3\2\2\2\u0157\u0158\7\'\2\2\u01588\3\2\2\2\u0159\u015a")
        buf.write("\7#\2\2\u015a:\3\2\2\2\u015b\u015c\7(\2\2\u015c\u015d")
        buf.write("\7(\2\2\u015d<\3\2\2\2\u015e\u015f\7~\2\2\u015f\u0160")
        buf.write("\7~\2\2\u0160>\3\2\2\2\u0161\u0162\7?\2\2\u0162\u0163")
        buf.write("\7?\2\2\u0163@\3\2\2\2\u0164\u0165\7#\2\2\u0165\u0166")
        buf.write("\7?\2\2\u0166B\3\2\2\2\u0167\u0168\7>\2\2\u0168D\3\2\2")
        buf.write("\2\u0169\u016a\7@\2\2\u016aF\3\2\2\2\u016b\u016c\7>\2")
        buf.write("\2\u016c\u016d\7?\2\2\u016dH\3\2\2\2\u016e\u016f\7@\2")
        buf.write("\2\u016f\u0170\7?\2\2\u0170J\3\2\2\2\u0171\u0172\7?\2")
        buf.write("\2\u0172\u0173\7\61\2\2\u0173\u0174\7?\2\2\u0174L\3\2")
        buf.write("\2\2\u0175\u0176\7>\2\2\u0176\u0177\7\60\2\2\u0177N\3")
        buf.write("\2\2\2\u0178\u0179\7@\2\2\u0179\u017a\7\60\2\2\u017aP")
        buf.write("\3\2\2\2\u017b\u017c\7>\2\2\u017c\u017d\7?\2\2\u017d\u017e")
        buf.write("\7\60\2\2\u017eR\3\2\2\2\u017f\u0180\7@\2\2\u0180\u0181")
        buf.write("\7?\2\2\u0181\u0182\7\60\2\2\u0182T\3\2\2\2\u0183\u0184")
        buf.write("\7?\2\2\u0184V\3\2\2\2\u0185\u0186\7D\2\2\u0186\u0187")
        buf.write("\7q\2\2\u0187\u0188\7f\2\2\u0188\u0189\7{\2\2\u0189X\3")
        buf.write("\2\2\2\u018a\u018b\7D\2\2\u018b\u018c\7t\2\2\u018c\u018d")
        buf.write("\7g\2\2\u018d\u018e\7c\2\2\u018e\u018f\7m\2\2\u018fZ\3")
        buf.write("\2\2\2\u0190\u0191\7E\2\2\u0191\u0192\7q\2\2\u0192\u0193")
        buf.write("\7p\2\2\u0193\u0194\7v\2\2\u0194\u0195\7k\2\2\u0195\u0196")
        buf.write("\7p\2\2\u0196\u0197\7w\2\2\u0197\u0198\7g\2\2\u0198\\")
        buf.write("\3\2\2\2\u0199\u019a\7F\2\2\u019a\u019b\7q\2\2\u019b^")
        buf.write("\3\2\2\2\u019c\u019d\7G\2\2\u019d\u019e\7n\2\2\u019e\u019f")
        buf.write("\7u\2\2\u019f\u01a0\7g\2\2\u01a0`\3\2\2\2\u01a1\u01a2")
        buf.write("\7G\2\2\u01a2\u01a3\7n\2\2\u01a3\u01a4\7u\2\2\u01a4\u01a5")
        buf.write("\7g\2\2\u01a5\u01a6\7K\2\2\u01a6\u01a7\7h\2\2\u01a7b\3")
        buf.write("\2\2\2\u01a8\u01a9\7G\2\2\u01a9\u01aa\7p\2\2\u01aa\u01ab")
        buf.write("\7f\2\2\u01ab\u01ac\7D\2\2\u01ac\u01ad\7q\2\2\u01ad\u01ae")
        buf.write("\7f\2\2\u01ae\u01af\7{\2\2\u01afd\3\2\2\2\u01b0\u01b1")
        buf.write("\7G\2\2\u01b1\u01b2\7p\2\2\u01b2\u01b3\7f\2\2\u01b3\u01b4")
        buf.write("\7K\2\2\u01b4\u01b5\7h\2\2\u01b5f\3\2\2\2\u01b6\u01b7")
        buf.write("\7G\2\2\u01b7\u01b8\7p\2\2\u01b8\u01b9\7f\2\2\u01b9\u01ba")
        buf.write("\7H\2\2\u01ba\u01bb\7q\2\2\u01bb\u01bc\7t\2\2\u01bch\3")
        buf.write("\2\2\2\u01bd\u01be\7G\2\2\u01be\u01bf\7p\2\2\u01bf\u01c0")
        buf.write("\7f\2\2\u01c0\u01c1\7Y\2\2\u01c1\u01c2\7j\2\2\u01c2\u01c3")
        buf.write("\7k\2\2\u01c3\u01c4\7n\2\2\u01c4\u01c5\7g\2\2\u01c5j\3")
        buf.write("\2\2\2\u01c6\u01c7\7H\2\2\u01c7\u01c8\7q\2\2\u01c8\u01c9")
        buf.write("\7t\2\2\u01c9l\3\2\2\2\u01ca\u01cb\7H\2\2\u01cb\u01cc")
        buf.write("\7w\2\2\u01cc\u01cd\7p\2\2\u01cd\u01ce\7e\2\2\u01ce\u01cf")
        buf.write("\7v\2\2\u01cf\u01d0\7k\2\2\u01d0\u01d1\7q\2\2\u01d1\u01d2")
        buf.write("\7p\2\2\u01d2n\3\2\2\2\u01d3\u01d4\7K\2\2\u01d4\u01d5")
        buf.write("\7h\2\2\u01d5p\3\2\2\2\u01d6\u01d7\7R\2\2\u01d7\u01d8")
        buf.write("\7c\2\2\u01d8\u01d9\7t\2\2\u01d9\u01da\7c\2\2\u01da\u01db")
        buf.write("\7o\2\2\u01db\u01dc\7g\2\2\u01dc\u01dd\7v\2\2\u01dd\u01de")
        buf.write("\7g\2\2\u01de\u01df\7t\2\2\u01dfr\3\2\2\2\u01e0\u01e1")
        buf.write("\7T\2\2\u01e1\u01e2\7g\2\2\u01e2\u01e3\7v\2\2\u01e3\u01e4")
        buf.write("\7w\2\2\u01e4\u01e5\7t\2\2\u01e5\u01e6\7p\2\2\u01e6t\3")
        buf.write("\2\2\2\u01e7\u01e8\7V\2\2\u01e8\u01e9\7j\2\2\u01e9\u01ea")
        buf.write("\7g\2\2\u01ea\u01eb\7p\2\2\u01ebv\3\2\2\2\u01ec\u01ed")
        buf.write("\7X\2\2\u01ed\u01ee\7c\2\2\u01ee\u01ef\7t\2\2\u01efx\3")
        buf.write("\2\2\2\u01f0\u01f1\7Y\2\2\u01f1\u01f2\7j\2\2\u01f2\u01f3")
        buf.write("\7k\2\2\u01f3\u01f4\7n\2\2\u01f4\u01f5\7g\2\2\u01f5z\3")
        buf.write("\2\2\2\u01f6\u01f7\7V\2\2\u01f7\u01f8\7t\2\2\u01f8\u01f9")
        buf.write("\7w\2\2\u01f9\u01fa\7g\2\2\u01fa|\3\2\2\2\u01fb\u01fc")
        buf.write("\7H\2\2\u01fc\u01fd\7c\2\2\u01fd\u01fe\7n\2\2\u01fe\u01ff")
        buf.write("\7u\2\2\u01ff\u0200\7g\2\2\u0200~\3\2\2\2\u0201\u0202")
        buf.write("\7G\2\2\u0202\u0203\7p\2\2\u0203\u0204\7f\2\2\u0204\u0205")
        buf.write("\7F\2\2\u0205\u0206\7q\2\2\u0206\u0080\3\2\2\2\u0207\u0208")
        buf.write("\t\2\2\2\u0208\u0082\3\2\2\2\u0209\u020a\t\3\2\2\u020a")
        buf.write("\u0084\3\2\2\2\u020b\u020c\t\4\2\2\u020c\u0086\3\2\2\2")
        buf.write("\u020d\u020e\7a\2\2\u020e\u0088\3\2\2\2\u020f\u0210\7")
        buf.write("^\2\2\u0210\u0211\7d\2\2\u0211\u008a\3\2\2\2\u0212\u0213")
        buf.write("\7^\2\2\u0213\u0214\7h\2\2\u0214\u008c\3\2\2\2\u0215\u0216")
        buf.write("\7^\2\2\u0216\u0217\7t\2\2\u0217\u008e\3\2\2\2\u0218\u0219")
        buf.write("\7^\2\2\u0219\u021a\7p\2\2\u021a\u0090\3\2\2\2\u021b\u021c")
        buf.write("\7^\2\2\u021c\u021d\7v\2\2\u021d\u0092\3\2\2\2\u021e\u021f")
        buf.write("\7)\2\2\u021f\u0094\3\2\2\2\u0220\u0221\7$\2\2\u0221\u0096")
        buf.write("\3\2\2\2\u0222\u0223\7^\2\2\u0223\u0224\7^\2\2\u0224\u0098")
        buf.write("\3\2\2\2\u0225\u0226\7\62\2\2\u0226\u0227\t\5\2\2\u0227")
        buf.write("\u022c\t\6\2\2\u0228\u022b\5\u0085C\2\u0229\u022b\t\7")
        buf.write("\2\2\u022a\u0228\3\2\2\2\u022a\u0229\3\2\2\2\u022b\u022e")
        buf.write("\3\2\2\2\u022c\u022a\3\2\2\2\u022c\u022d\3\2\2\2\u022d")
        buf.write("\u009a\3\2\2\2\u022e\u022c\3\2\2\2\u022f\u0233\t\b\2\2")
        buf.write("\u0230\u0232\5\u0085C\2\u0231\u0230\3\2\2\2\u0232\u0235")
        buf.write("\3\2\2\2\u0233\u0231\3\2\2\2\u0233\u0234\3\2\2\2\u0234")
        buf.write("\u0238\3\2\2\2\u0235\u0233\3\2\2\2\u0236\u0238\7\62\2")
        buf.write("\2\u0237\u022f\3\2\2\2\u0237\u0236\3\2\2\2\u0238\u009c")
        buf.write("\3\2\2\2\u0239\u023a\7\62\2\2\u023a\u023b\t\t\2\2\u023b")
        buf.write("\u023f\t\n\2\2\u023c\u023e\t\13\2\2\u023d\u023c\3\2\2")
        buf.write("\2\u023e\u0241\3\2\2\2\u023f\u023d\3\2\2\2\u023f\u0240")
        buf.write("\3\2\2\2\u0240\u009e\3\2\2\2\u0241\u023f\3\2\2\2\u0242")
        buf.write("\u0246\5\u009bN\2\u0243\u0246\5\u0099M\2\u0244\u0246\5")
        buf.write("\u009dO\2\u0245\u0242\3\2\2\2\u0245\u0243\3\2\2\2\u0245")
        buf.write("\u0244\3\2\2\2\u0246\u00a0\3\2\2\2\u0247\u024a\t\f\2\2")
        buf.write("\u0248\u024b\5\'\24\2\u0249\u024b\5+\26\2\u024a\u0248")
        buf.write("\3\2\2\2\u024a\u0249\3\2\2\2\u024a\u024b\3\2\2\2\u024b")
        buf.write("\u024d\3\2\2\2\u024c\u024e\5\u0085C\2\u024d\u024c\3\2")
        buf.write("\2\2\u024e\u024f\3\2\2\2\u024f\u024d\3\2\2\2\u024f\u0250")
        buf.write("\3\2\2\2\u0250\u00a2\3\2\2\2\u0251\u0255\5\35\17\2\u0252")
        buf.write("\u0254\5\u0085C\2\u0253\u0252\3\2\2\2\u0254\u0257\3\2")
        buf.write("\2\2\u0255\u0253\3\2\2\2\u0255\u0256\3\2\2\2\u0256\u00a4")
        buf.write("\3\2\2\2\u0257\u0255\3\2\2\2\u0258\u025c\t\b\2\2\u0259")
        buf.write("\u025b\5\u0085C\2\u025a\u0259\3\2\2\2\u025b\u025e\3\2")
        buf.write("\2\2\u025c\u025a\3\2\2\2\u025c\u025d\3\2\2\2\u025d\u0265")
        buf.write("\3\2\2\2\u025e\u025c\3\2\2\2\u025f\u0266\5\u00a3R\2\u0260")
        buf.write("\u0266\5\u00a1Q\2\u0261\u0262\5\u00a3R\2\u0262\u0263\5")
        buf.write("\u00a1Q\2\u0263\u0266\3\2\2\2\u0264\u0266\5\u00a3R\2\u0265")
        buf.write("\u025f\3\2\2\2\u0265\u0260\3\2\2\2\u0265\u0261\3\2\2\2")
        buf.write("\u0265\u0264\3\2\2\2\u0265\u0266\3\2\2\2\u0266\u00a6\3")
        buf.write("\2\2\2\u0267\u026f\5\u0089E\2\u0268\u026f\5\u008bF\2\u0269")
        buf.write("\u026f\5\u008dG\2\u026a\u026f\5\u008fH\2\u026b\u026f\5")
        buf.write("\u0091I\2\u026c\u026f\5\u0093J\2\u026d\u026f\5\u0097L")
        buf.write("\2\u026e\u0267\3\2\2\2\u026e\u0268\3\2\2\2\u026e\u0269")
        buf.write("\3\2\2\2\u026e\u026a\3\2\2\2\u026e\u026b\3\2\2\2\u026e")
        buf.write("\u026c\3\2\2\2\u026e\u026d\3\2\2\2\u026f\u00a8\3\2\2\2")
        buf.write("\u0270\u0278\5\u0095K\2\u0271\u0272\5\u0093J\2\u0272\u0273")
        buf.write("\5\u0095K\2\u0273\u0277\3\2\2\2\u0274\u0277\5\u00a7T\2")
        buf.write("\u0275\u0277\n\r\2\2\u0276\u0271\3\2\2\2\u0276\u0274\3")
        buf.write("\2\2\2\u0276\u0275\3\2\2\2\u0277\u027a\3\2\2\2\u0278\u0276")
        buf.write("\3\2\2\2\u0278\u0279\3\2\2\2\u0279\u027b\3\2\2\2\u027a")
        buf.write("\u0278\3\2\2\2\u027b\u027c\5\u0095K\2\u027c\u00aa\3\2")
        buf.write("\2\2\u027d\u02ab\5#\22\2\u027e\u0284\5\u009fP\2\u027f")
        buf.write("\u0280\5\37\20\2\u0280\u0281\5\u009fP\2\u0281\u0283\3")
        buf.write("\2\2\2\u0282\u027f\3\2\2\2\u0283\u0286\3\2\2\2\u0284\u0282")
        buf.write("\3\2\2\2\u0284\u0285\3\2\2\2\u0285\u02ac\3\2\2\2\u0286")
        buf.write("\u0284\3\2\2\2\u0287\u028d\5\u00a5S\2\u0288\u0289\5\37")
        buf.write("\20\2\u0289\u028a\5\u00a5S\2\u028a\u028c\3\2\2\2\u028b")
        buf.write("\u0288\3\2\2\2\u028c\u028f\3\2\2\2\u028d\u028b\3\2\2\2")
        buf.write("\u028d\u028e\3\2\2\2\u028e\u02ac\3\2\2\2\u028f\u028d\3")
        buf.write("\2\2\2\u0290\u0296\5\u00a9U\2\u0291\u0292\5\37\20\2\u0292")
        buf.write("\u0293\5\u00a9U\2\u0293\u0295\3\2\2\2\u0294\u0291\3\2")
        buf.write("\2\2\u0295\u0298\3\2\2\2\u0296\u0294\3\2\2\2\u0296\u0297")
        buf.write("\3\2\2\2\u0297\u02ac\3\2\2\2\u0298\u0296\3\2\2\2\u0299")
        buf.write("\u029f\5\u00abV\2\u029a\u029b\5\37\20\2\u029b\u029c\5")
        buf.write("\u00abV\2\u029c\u029e\3\2\2\2\u029d\u029a\3\2\2\2\u029e")
        buf.write("\u02a1\3\2\2\2\u029f\u029d\3\2\2\2\u029f\u02a0\3\2\2\2")
        buf.write("\u02a0\u02ac\3\2\2\2\u02a1\u029f\3\2\2\2\u02a2\u02a8\5")
        buf.write("\u00adW\2\u02a3\u02a4\5\37\20\2\u02a4\u02a5\5\u00adW\2")
        buf.write("\u02a5\u02a7\3\2\2\2\u02a6\u02a3\3\2\2\2\u02a7\u02aa\3")
        buf.write("\2\2\2\u02a8\u02a6\3\2\2\2\u02a8\u02a9\3\2\2\2\u02a9\u02ac")
        buf.write("\3\2\2\2\u02aa\u02a8\3\2\2\2\u02ab\u027e\3\2\2\2\u02ab")
        buf.write("\u0287\3\2\2\2\u02ab\u0290\3\2\2\2\u02ab\u0299\3\2\2\2")
        buf.write("\u02ab\u02a2\3\2\2\2\u02ac\u02ad\3\2\2\2\u02ad\u02ae\5")
        buf.write("%\23\2\u02ae\u00ac\3\2\2\2\u02af\u02b2\5{>\2\u02b0\u02b2")
        buf.write("\5}?\2\u02b1\u02af\3\2\2\2\u02b1\u02b0\3\2\2\2\u02b2\u00ae")
        buf.write("\3\2\2\2\u02b3\u02ba\5\u0081A\2\u02b4\u02b9\5\u0081A\2")
        buf.write("\u02b5\u02b9\5\u0083B\2\u02b6\u02b9\5\u0087D\2\u02b7\u02b9")
        buf.write("\5\u0085C\2\u02b8\u02b4\3\2\2\2\u02b8\u02b5\3\2\2\2\u02b8")
        buf.write("\u02b6\3\2\2\2\u02b8\u02b7\3\2\2\2\u02b9\u02bc\3\2\2\2")
        buf.write("\u02ba\u02b8\3\2\2\2\u02ba\u02bb\3\2\2\2\u02bb\u00b0\3")
        buf.write("\2\2\2\u02bc\u02ba\3\2\2\2\u02bd\u02bf\t\16\2\2\u02be")
        buf.write("\u02bd\3\2\2\2\u02bf\u02c0\3\2\2\2\u02c0\u02be\3\2\2\2")
        buf.write("\u02c0\u02c1\3\2\2\2\u02c1\u02c2\3\2\2\2\u02c2\u02c3\b")
        buf.write("Y\2\2\u02c3\u00b2\3\2\2\2\u02c4\u02c5\13\2\2\2\u02c5\u00b4")
        buf.write("\3\2\2\2\u02c6\u02c7\13\2\2\2\u02c7\u00b6\3\2\2\2\u02c8")
        buf.write("\u02c9\13\2\2\2\u02c9\u00b8\3\2\2\2\u02ca\u02cb\13\2\2")
        buf.write("\2\u02cb\u00ba\3\2\2\2\33\2\u022a\u022c\u0233\u0237\u023f")
        buf.write("\u0245\u024a\u024f\u0255\u025c\u0265\u026e\u0276\u0278")
        buf.write("\u0284\u028d\u0296\u029f\u02a8\u02ab\u02b1\u02b8\u02ba")
        buf.write("\u02c0\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

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
    LP = 9
    RP = 10
    LB = 11
    RB = 12
    COLON = 13
    DOT = 14
    COMMA = 15
    SEMI = 16
    LCB = 17
    RCB = 18
    ADDOP = 19
    ADDF = 20
    SUBOP = 21
    SUBF = 22
    MULOP = 23
    MULF = 24
    DIVOP = 25
    DIVF = 26
    MODOP = 27
    NOT = 28
    AND = 29
    OR = 30
    EQ = 31
    NEQ = 32
    LT = 33
    GT = 34
    LTE = 35
    GTE = 36
    NEQF = 37
    LTF = 38
    GTF = 39
    LTEF = 40
    GTEF = 41
    ASSIG = 42
    BODY = 43
    BREAK = 44
    CONTINUE = 45
    DO = 46
    ELSE = 47
    ELSEIF = 48
    ENDBODY = 49
    ENDIF = 50
    ENDFOR = 51
    ENDWHILE = 52
    FOR = 53
    FUNCTION = 54
    IF = 55
    PARAMETER = 56
    RETURN = 57
    THEN = 58
    VAR = 59
    WHILE = 60
    TRUE = 61
    FALSE = 62
    ENDDO = 63
    INTERGER = 64
    FLOAT = 65
    STRING = 66
    ARRAY = 67
    BOOLEAN = 68
    ID = 69
    WS = 70
    ERROR_CHAR = 71
    UNCLOSE_STRING = 72
    ILLEGAL_ESCAPE = 73
    UNTERMINATED_COMMENT = 74

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int_of_float'", "'float_of_int'", "'int_of_string'", "'string_of_int'", 
            "'float_of_string'", "'string_of_float'", "'bool_of_string'", 
            "'string_of_bool'", "'('", "')'", "'['", "']'", "':'", "'.'", 
            "','", "';'", "'{'", "'}'", "'+'", "'+.'", "'-'", "'-.'", "'*'", 
            "'*.'", "'\\'", "'\\.'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
            "'!='", "'<'", "'>'", "'<='", "'>='", "'=/='", "'<.'", "'>.'", 
            "'<=.'", "'>=.'", "'='", "'Body'", "'Break'", "'Continue'", 
            "'Do'", "'Else'", "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", 
            "'EndWhile'", "'For'", "'Function'", "'If'", "'Parameter'", 
            "'Return'", "'Then'", "'Var'", "'While'", "'True'", "'False'", 
            "'EndDo'" ]

    symbolicNames = [ "<INVALID>",
            "LP", "RP", "LB", "RB", "COLON", "DOT", "COMMA", "SEMI", "LCB", 
            "RCB", "ADDOP", "ADDF", "SUBOP", "SUBF", "MULOP", "MULF", "DIVOP", 
            "DIVF", "MODOP", "NOT", "AND", "OR", "EQ", "NEQ", "LT", "GT", 
            "LTE", "GTE", "NEQF", "LTF", "GTF", "LTEF", "GTEF", "ASSIG", 
            "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", 
            "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
            "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", 
            "INTERGER", "FLOAT", "STRING", "ARRAY", "BOOLEAN", "ID", "WS", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "LP", "RP", "LB", "RB", "COLON", "DOT", "COMMA", 
                  "SEMI", "LCB", "RCB", "ADDOP", "ADDF", "SUBOP", "SUBF", 
                  "MULOP", "MULF", "DIVOP", "DIVF", "MODOP", "NOT", "AND", 
                  "OR", "EQ", "NEQ", "LT", "GT", "LTE", "GTE", "NEQF", "LTF", 
                  "GTF", "LTEF", "GTEF", "ASSIG", "BODY", "BREAK", "CONTINUE", 
                  "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", 
                  "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", 
                  "THEN", "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", "LOWCASE", 
                  "UPPERCASE", "NUMBER", "UNDERCORE", "BACKSPACE", "FORMFEED", 
                  "CARRIAGE_RETURN", "NEWLINE", "HORIZONTAL_TAB", "SINGLE_QUOTE", 
                  "DOUBLE_QUOTE", "BACK_SLASH", "HEXA", "DECIMAL", "OCTAL", 
                  "INTERGER", "EXPONENT", "DECIMAL_PART", "FLOAT", "ESCAPE_SEQUENCE", 
                  "STRING", "ARRAY", "BOOLEAN", "ID", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

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


