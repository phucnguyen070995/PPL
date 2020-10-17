# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2J")
        buf.write("\u02eb\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20")
        buf.write("\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3")
        buf.write("$\3$\3$\3%\3%\3%\3&\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3")
        buf.write(")\3)\3)\3*\3*\3*\3*\3+\3+\3,\3,\3,\3,\3,\3-\3-\3-\3-\3")
        buf.write("-\3-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\38\38\38\39\3")
        buf.write("9\39\39\39\39\39\39\39\39\3:\3:\3:\3:\3:\3:\3:\3;\3;\3")
        buf.write(";\3;\3;\3<\3<\3<\3<\3=\3=\3=\3=\3=\3=\3>\3>\3>\3>\3>\3")
        buf.write("?\3?\3?\3?\3?\3?\3@\3@\3@\3@\3@\3@\3A\3A\3B\3B\3C\3C\3")
        buf.write("D\3D\3E\3E\3E\3F\3F\3F\3G\3G\3G\3H\3H\3H\3I\3I\3I\3J\3")
        buf.write("J\3K\3K\3L\3L\3L\3M\3M\3M\3M\3M\7M\u0231\nM\fM\16M\u0234")
        buf.write("\13M\3N\3N\7N\u0238\nN\fN\16N\u023b\13N\3N\5N\u023e\n")
        buf.write("N\3O\3O\3O\3O\7O\u0244\nO\fO\16O\u0247\13O\3P\3P\3P\5")
        buf.write("P\u024c\nP\3Q\3Q\3Q\5Q\u0251\nQ\3Q\6Q\u0254\nQ\rQ\16Q")
        buf.write("\u0255\3R\3R\7R\u025a\nR\fR\16R\u025d\13R\3S\3S\7S\u0261")
        buf.write("\nS\fS\16S\u0264\13S\3S\3S\3S\3S\3S\3S\5S\u026c\nS\3T")
        buf.write("\3T\3T\3T\3T\3T\3T\5T\u0275\nT\3U\3U\3U\3U\3U\5U\u027c")
        buf.write("\nU\3V\3V\3W\3W\3W\3W\7W\u0284\nW\fW\16W\u0287\13W\3W")
        buf.write("\3W\3X\3X\3X\3X\3X\3X\3X\3X\7X\u0293\nX\fX\16X\u0296\13")
        buf.write("X\3X\3X\3X\3X\3X\3X\7X\u029e\nX\fX\16X\u02a1\13X\3X\3")
        buf.write("X\3X\3X\3X\3X\7X\u02a9\nX\fX\16X\u02ac\13X\3X\3X\3X\3")
        buf.write("X\3X\3X\7X\u02b4\nX\fX\16X\u02b7\13X\3X\3X\3X\3X\3X\3")
        buf.write("X\7X\u02bf\nX\fX\16X\u02c2\13X\5X\u02c4\nX\3X\3X\3X\3")
        buf.write("Y\7Y\u02ca\nY\fY\16Y\u02cd\13Y\3Z\3Z\5Z\u02d1\nZ\3[\3")
        buf.write("[\3[\3[\3[\7[\u02d8\n[\f[\16[\u02db\13[\3\\\6\\\u02de")
        buf.write("\n\\\r\\\16\\\u02df\3\\\3\\\3]\3]\3^\3^\3_\3_\3`\3`\2")
        buf.write("\2a\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q")
        buf.write(":s;u<w=y>{\2}\2\177?\u0081\2\u0083\2\u0085\2\u0087\2\u0089")
        buf.write("\2\u008b\2\u008d\2\u008f\2\u0091\2\u0093\2\u0095\2\u0097")
        buf.write("\2\u0099\2\u009b\2\u009d\2\u009f@\u00a1\2\u00a3\2\u00a5")
        buf.write("A\u00a7\2\u00a9\2\u00ab\2\u00adB\u00afC\u00b1\2\u00b3")
        buf.write("D\u00b5E\u00b7F\u00b9G\u00bbH\u00bdI\u00bfJ\3\2\20\3\2")
        buf.write("c|\3\2C\\\3\2\62;\4\2ZZzz\4\2\63;CH\3\2CH\3\2\63;\4\2")
        buf.write("QQqq\3\2\639\3\2\629\4\2GGgg\3\2$$\3\2\"\"\5\2\13\f\17")
        buf.write("\17\"\"\2\u02fd\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2")
        buf.write("\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2")
        buf.write("\2\2\2y\3\2\2\2\2\177\3\2\2\2\2\u009f\3\2\2\2\2\u00a5")
        buf.write("\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b3\3\2\2")
        buf.write("\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb")
        buf.write("\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf\3\2\2\2\3\u00c1\3\2\2")
        buf.write("\2\5\u00ce\3\2\2\2\7\u00db\3\2\2\2\t\u00e9\3\2\2\2\13")
        buf.write("\u00f7\3\2\2\2\r\u0107\3\2\2\2\17\u0117\3\2\2\2\21\u0126")
        buf.write("\3\2\2\2\23\u0135\3\2\2\2\25\u0137\3\2\2\2\27\u0139\3")
        buf.write("\2\2\2\31\u013b\3\2\2\2\33\u013d\3\2\2\2\35\u013f\3\2")
        buf.write("\2\2\37\u0141\3\2\2\2!\u0143\3\2\2\2#\u0145\3\2\2\2%\u0147")
        buf.write("\3\2\2\2\'\u0149\3\2\2\2)\u014b\3\2\2\2+\u014e\3\2\2\2")
        buf.write("-\u0150\3\2\2\2/\u0153\3\2\2\2\61\u0155\3\2\2\2\63\u0158")
        buf.write("\3\2\2\2\65\u015a\3\2\2\2\67\u015d\3\2\2\29\u015f\3\2")
        buf.write("\2\2;\u0161\3\2\2\2=\u0164\3\2\2\2?\u0167\3\2\2\2A\u016a")
        buf.write("\3\2\2\2C\u016d\3\2\2\2E\u016f\3\2\2\2G\u0171\3\2\2\2")
        buf.write("I\u0174\3\2\2\2K\u0177\3\2\2\2M\u017b\3\2\2\2O\u017e\3")
        buf.write("\2\2\2Q\u0181\3\2\2\2S\u0185\3\2\2\2U\u0189\3\2\2\2W\u018b")
        buf.write("\3\2\2\2Y\u0190\3\2\2\2[\u0196\3\2\2\2]\u019f\3\2\2\2")
        buf.write("_\u01a2\3\2\2\2a\u01a7\3\2\2\2c\u01ae\3\2\2\2e\u01b6\3")
        buf.write("\2\2\2g\u01bc\3\2\2\2i\u01c3\3\2\2\2k\u01cc\3\2\2\2m\u01d0")
        buf.write("\3\2\2\2o\u01d9\3\2\2\2q\u01dc\3\2\2\2s\u01e6\3\2\2\2")
        buf.write("u\u01ed\3\2\2\2w\u01f2\3\2\2\2y\u01f6\3\2\2\2{\u01fc\3")
        buf.write("\2\2\2}\u0201\3\2\2\2\177\u0207\3\2\2\2\u0081\u020d\3")
        buf.write("\2\2\2\u0083\u020f\3\2\2\2\u0085\u0211\3\2\2\2\u0087\u0213")
        buf.write("\3\2\2\2\u0089\u0215\3\2\2\2\u008b\u0218\3\2\2\2\u008d")
        buf.write("\u021b\3\2\2\2\u008f\u021e\3\2\2\2\u0091\u0221\3\2\2\2")
        buf.write("\u0093\u0224\3\2\2\2\u0095\u0226\3\2\2\2\u0097\u0228\3")
        buf.write("\2\2\2\u0099\u022b\3\2\2\2\u009b\u023d\3\2\2\2\u009d\u023f")
        buf.write("\3\2\2\2\u009f\u024b\3\2\2\2\u00a1\u024d\3\2\2\2\u00a3")
        buf.write("\u0257\3\2\2\2\u00a5\u025e\3\2\2\2\u00a7\u0274\3\2\2\2")
        buf.write("\u00a9\u027b\3\2\2\2\u00ab\u027d\3\2\2\2\u00ad\u027f\3")
        buf.write("\2\2\2\u00af\u028a\3\2\2\2\u00b1\u02cb\3\2\2\2\u00b3\u02d0")
        buf.write("\3\2\2\2\u00b5\u02d2\3\2\2\2\u00b7\u02dd\3\2\2\2\u00b9")
        buf.write("\u02e3\3\2\2\2\u00bb\u02e5\3\2\2\2\u00bd\u02e7\3\2\2\2")
        buf.write("\u00bf\u02e9\3\2\2\2\u00c1\u00c2\7k\2\2\u00c2\u00c3\7")
        buf.write("p\2\2\u00c3\u00c4\7v\2\2\u00c4\u00c5\7a\2\2\u00c5\u00c6")
        buf.write("\7q\2\2\u00c6\u00c7\7h\2\2\u00c7\u00c8\7a\2\2\u00c8\u00c9")
        buf.write("\7h\2\2\u00c9\u00ca\7n\2\2\u00ca\u00cb\7q\2\2\u00cb\u00cc")
        buf.write("\7c\2\2\u00cc\u00cd\7v\2\2\u00cd\4\3\2\2\2\u00ce\u00cf")
        buf.write("\7h\2\2\u00cf\u00d0\7n\2\2\u00d0\u00d1\7q\2\2\u00d1\u00d2")
        buf.write("\7c\2\2\u00d2\u00d3\7v\2\2\u00d3\u00d4\7a\2\2\u00d4\u00d5")
        buf.write("\7q\2\2\u00d5\u00d6\7h\2\2\u00d6\u00d7\7a\2\2\u00d7\u00d8")
        buf.write("\7k\2\2\u00d8\u00d9\7p\2\2\u00d9\u00da\7v\2\2\u00da\6")
        buf.write("\3\2\2\2\u00db\u00dc\7k\2\2\u00dc\u00dd\7p\2\2\u00dd\u00de")
        buf.write("\7v\2\2\u00de\u00df\7a\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1")
        buf.write("\7h\2\2\u00e1\u00e2\7a\2\2\u00e2\u00e3\7u\2\2\u00e3\u00e4")
        buf.write("\7v\2\2\u00e4\u00e5\7t\2\2\u00e5\u00e6\7k\2\2\u00e6\u00e7")
        buf.write("\7p\2\2\u00e7\u00e8\7i\2\2\u00e8\b\3\2\2\2\u00e9\u00ea")
        buf.write("\7u\2\2\u00ea\u00eb\7v\2\2\u00eb\u00ec\7t\2\2\u00ec\u00ed")
        buf.write("\7k\2\2\u00ed\u00ee\7p\2\2\u00ee\u00ef\7i\2\2\u00ef\u00f0")
        buf.write("\7a\2\2\u00f0\u00f1\7q\2\2\u00f1\u00f2\7h\2\2\u00f2\u00f3")
        buf.write("\7a\2\2\u00f3\u00f4\7k\2\2\u00f4\u00f5\7p\2\2\u00f5\u00f6")
        buf.write("\7v\2\2\u00f6\n\3\2\2\2\u00f7\u00f8\7h\2\2\u00f8\u00f9")
        buf.write("\7n\2\2\u00f9\u00fa\7q\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc")
        buf.write("\7v\2\2\u00fc\u00fd\7a\2\2\u00fd\u00fe\7q\2\2\u00fe\u00ff")
        buf.write("\7h\2\2\u00ff\u0100\7a\2\2\u0100\u0101\7u\2\2\u0101\u0102")
        buf.write("\7v\2\2\u0102\u0103\7t\2\2\u0103\u0104\7k\2\2\u0104\u0105")
        buf.write("\7p\2\2\u0105\u0106\7i\2\2\u0106\f\3\2\2\2\u0107\u0108")
        buf.write("\7u\2\2\u0108\u0109\7v\2\2\u0109\u010a\7t\2\2\u010a\u010b")
        buf.write("\7k\2\2\u010b\u010c\7p\2\2\u010c\u010d\7i\2\2\u010d\u010e")
        buf.write("\7a\2\2\u010e\u010f\7q\2\2\u010f\u0110\7h\2\2\u0110\u0111")
        buf.write("\7a\2\2\u0111\u0112\7h\2\2\u0112\u0113\7n\2\2\u0113\u0114")
        buf.write("\7q\2\2\u0114\u0115\7c\2\2\u0115\u0116\7v\2\2\u0116\16")
        buf.write("\3\2\2\2\u0117\u0118\7d\2\2\u0118\u0119\7q\2\2\u0119\u011a")
        buf.write("\7q\2\2\u011a\u011b\7n\2\2\u011b\u011c\7a\2\2\u011c\u011d")
        buf.write("\7q\2\2\u011d\u011e\7h\2\2\u011e\u011f\7a\2\2\u011f\u0120")
        buf.write("\7u\2\2\u0120\u0121\7v\2\2\u0121\u0122\7t\2\2\u0122\u0123")
        buf.write("\7k\2\2\u0123\u0124\7p\2\2\u0124\u0125\7i\2\2\u0125\20")
        buf.write("\3\2\2\2\u0126\u0127\7u\2\2\u0127\u0128\7v\2\2\u0128\u0129")
        buf.write("\7t\2\2\u0129\u012a\7k\2\2\u012a\u012b\7p\2\2\u012b\u012c")
        buf.write("\7i\2\2\u012c\u012d\7a\2\2\u012d\u012e\7q\2\2\u012e\u012f")
        buf.write("\7h\2\2\u012f\u0130\7a\2\2\u0130\u0131\7d\2\2\u0131\u0132")
        buf.write("\7q\2\2\u0132\u0133\7q\2\2\u0133\u0134\7n\2\2\u0134\22")
        buf.write("\3\2\2\2\u0135\u0136\7*\2\2\u0136\24\3\2\2\2\u0137\u0138")
        buf.write("\7+\2\2\u0138\26\3\2\2\2\u0139\u013a\7]\2\2\u013a\30\3")
        buf.write("\2\2\2\u013b\u013c\7_\2\2\u013c\32\3\2\2\2\u013d\u013e")
        buf.write("\7<\2\2\u013e\34\3\2\2\2\u013f\u0140\7\60\2\2\u0140\36")
        buf.write("\3\2\2\2\u0141\u0142\7.\2\2\u0142 \3\2\2\2\u0143\u0144")
        buf.write("\7=\2\2\u0144\"\3\2\2\2\u0145\u0146\7}\2\2\u0146$\3\2")
        buf.write("\2\2\u0147\u0148\7\177\2\2\u0148&\3\2\2\2\u0149\u014a")
        buf.write("\7-\2\2\u014a(\3\2\2\2\u014b\u014c\7-\2\2\u014c\u014d")
        buf.write("\7\60\2\2\u014d*\3\2\2\2\u014e\u014f\7/\2\2\u014f,\3\2")
        buf.write("\2\2\u0150\u0151\7/\2\2\u0151\u0152\7\60\2\2\u0152.\3")
        buf.write("\2\2\2\u0153\u0154\7,\2\2\u0154\60\3\2\2\2\u0155\u0156")
        buf.write("\7,\2\2\u0156\u0157\7\60\2\2\u0157\62\3\2\2\2\u0158\u0159")
        buf.write("\7^\2\2\u0159\64\3\2\2\2\u015a\u015b\7^\2\2\u015b\u015c")
        buf.write("\7\60\2\2\u015c\66\3\2\2\2\u015d\u015e\7\'\2\2\u015e8")
        buf.write("\3\2\2\2\u015f\u0160\7#\2\2\u0160:\3\2\2\2\u0161\u0162")
        buf.write("\7(\2\2\u0162\u0163\7(\2\2\u0163<\3\2\2\2\u0164\u0165")
        buf.write("\7~\2\2\u0165\u0166\7~\2\2\u0166>\3\2\2\2\u0167\u0168")
        buf.write("\7?\2\2\u0168\u0169\7?\2\2\u0169@\3\2\2\2\u016a\u016b")
        buf.write("\7#\2\2\u016b\u016c\7?\2\2\u016cB\3\2\2\2\u016d\u016e")
        buf.write("\7>\2\2\u016eD\3\2\2\2\u016f\u0170\7@\2\2\u0170F\3\2\2")
        buf.write("\2\u0171\u0172\7>\2\2\u0172\u0173\7?\2\2\u0173H\3\2\2")
        buf.write("\2\u0174\u0175\7@\2\2\u0175\u0176\7?\2\2\u0176J\3\2\2")
        buf.write("\2\u0177\u0178\7?\2\2\u0178\u0179\7\61\2\2\u0179\u017a")
        buf.write("\7?\2\2\u017aL\3\2\2\2\u017b\u017c\7>\2\2\u017c\u017d")
        buf.write("\7\60\2\2\u017dN\3\2\2\2\u017e\u017f\7@\2\2\u017f\u0180")
        buf.write("\7\60\2\2\u0180P\3\2\2\2\u0181\u0182\7>\2\2\u0182\u0183")
        buf.write("\7?\2\2\u0183\u0184\7\60\2\2\u0184R\3\2\2\2\u0185\u0186")
        buf.write("\7@\2\2\u0186\u0187\7?\2\2\u0187\u0188\7\60\2\2\u0188")
        buf.write("T\3\2\2\2\u0189\u018a\7?\2\2\u018aV\3\2\2\2\u018b\u018c")
        buf.write("\7D\2\2\u018c\u018d\7q\2\2\u018d\u018e\7f\2\2\u018e\u018f")
        buf.write("\7{\2\2\u018fX\3\2\2\2\u0190\u0191\7D\2\2\u0191\u0192")
        buf.write("\7t\2\2\u0192\u0193\7g\2\2\u0193\u0194\7c\2\2\u0194\u0195")
        buf.write("\7m\2\2\u0195Z\3\2\2\2\u0196\u0197\7E\2\2\u0197\u0198")
        buf.write("\7q\2\2\u0198\u0199\7p\2\2\u0199\u019a\7v\2\2\u019a\u019b")
        buf.write("\7k\2\2\u019b\u019c\7p\2\2\u019c\u019d\7w\2\2\u019d\u019e")
        buf.write("\7g\2\2\u019e\\\3\2\2\2\u019f\u01a0\7F\2\2\u01a0\u01a1")
        buf.write("\7q\2\2\u01a1^\3\2\2\2\u01a2\u01a3\7G\2\2\u01a3\u01a4")
        buf.write("\7n\2\2\u01a4\u01a5\7u\2\2\u01a5\u01a6\7g\2\2\u01a6`\3")
        buf.write("\2\2\2\u01a7\u01a8\7G\2\2\u01a8\u01a9\7n\2\2\u01a9\u01aa")
        buf.write("\7u\2\2\u01aa\u01ab\7g\2\2\u01ab\u01ac\7K\2\2\u01ac\u01ad")
        buf.write("\7h\2\2\u01adb\3\2\2\2\u01ae\u01af\7G\2\2\u01af\u01b0")
        buf.write("\7p\2\2\u01b0\u01b1\7f\2\2\u01b1\u01b2\7D\2\2\u01b2\u01b3")
        buf.write("\7q\2\2\u01b3\u01b4\7f\2\2\u01b4\u01b5\7{\2\2\u01b5d\3")
        buf.write("\2\2\2\u01b6\u01b7\7G\2\2\u01b7\u01b8\7p\2\2\u01b8\u01b9")
        buf.write("\7f\2\2\u01b9\u01ba\7K\2\2\u01ba\u01bb\7h\2\2\u01bbf\3")
        buf.write("\2\2\2\u01bc\u01bd\7G\2\2\u01bd\u01be\7p\2\2\u01be\u01bf")
        buf.write("\7f\2\2\u01bf\u01c0\7H\2\2\u01c0\u01c1\7q\2\2\u01c1\u01c2")
        buf.write("\7t\2\2\u01c2h\3\2\2\2\u01c3\u01c4\7G\2\2\u01c4\u01c5")
        buf.write("\7p\2\2\u01c5\u01c6\7f\2\2\u01c6\u01c7\7Y\2\2\u01c7\u01c8")
        buf.write("\7j\2\2\u01c8\u01c9\7k\2\2\u01c9\u01ca\7n\2\2\u01ca\u01cb")
        buf.write("\7g\2\2\u01cbj\3\2\2\2\u01cc\u01cd\7H\2\2\u01cd\u01ce")
        buf.write("\7q\2\2\u01ce\u01cf\7t\2\2\u01cfl\3\2\2\2\u01d0\u01d1")
        buf.write("\7H\2\2\u01d1\u01d2\7w\2\2\u01d2\u01d3\7p\2\2\u01d3\u01d4")
        buf.write("\7e\2\2\u01d4\u01d5\7v\2\2\u01d5\u01d6\7k\2\2\u01d6\u01d7")
        buf.write("\7q\2\2\u01d7\u01d8\7p\2\2\u01d8n\3\2\2\2\u01d9\u01da")
        buf.write("\7K\2\2\u01da\u01db\7h\2\2\u01dbp\3\2\2\2\u01dc\u01dd")
        buf.write("\7R\2\2\u01dd\u01de\7c\2\2\u01de\u01df\7t\2\2\u01df\u01e0")
        buf.write("\7c\2\2\u01e0\u01e1\7o\2\2\u01e1\u01e2\7g\2\2\u01e2\u01e3")
        buf.write("\7v\2\2\u01e3\u01e4\7g\2\2\u01e4\u01e5\7t\2\2\u01e5r\3")
        buf.write("\2\2\2\u01e6\u01e7\7T\2\2\u01e7\u01e8\7g\2\2\u01e8\u01e9")
        buf.write("\7v\2\2\u01e9\u01ea\7w\2\2\u01ea\u01eb\7t\2\2\u01eb\u01ec")
        buf.write("\7p\2\2\u01ect\3\2\2\2\u01ed\u01ee\7V\2\2\u01ee\u01ef")
        buf.write("\7j\2\2\u01ef\u01f0\7g\2\2\u01f0\u01f1\7p\2\2\u01f1v\3")
        buf.write("\2\2\2\u01f2\u01f3\7X\2\2\u01f3\u01f4\7c\2\2\u01f4\u01f5")
        buf.write("\7t\2\2\u01f5x\3\2\2\2\u01f6\u01f7\7Y\2\2\u01f7\u01f8")
        buf.write("\7j\2\2\u01f8\u01f9\7k\2\2\u01f9\u01fa\7n\2\2\u01fa\u01fb")
        buf.write("\7g\2\2\u01fbz\3\2\2\2\u01fc\u01fd\7V\2\2\u01fd\u01fe")
        buf.write("\7t\2\2\u01fe\u01ff\7w\2\2\u01ff\u0200\7g\2\2\u0200|\3")
        buf.write("\2\2\2\u0201\u0202\7H\2\2\u0202\u0203\7c\2\2\u0203\u0204")
        buf.write("\7n\2\2\u0204\u0205\7u\2\2\u0205\u0206\7g\2\2\u0206~\3")
        buf.write("\2\2\2\u0207\u0208\7G\2\2\u0208\u0209\7p\2\2\u0209\u020a")
        buf.write("\7f\2\2\u020a\u020b\7F\2\2\u020b\u020c\7q\2\2\u020c\u0080")
        buf.write("\3\2\2\2\u020d\u020e\t\2\2\2\u020e\u0082\3\2\2\2\u020f")
        buf.write("\u0210\t\3\2\2\u0210\u0084\3\2\2\2\u0211\u0212\t\4\2\2")
        buf.write("\u0212\u0086\3\2\2\2\u0213\u0214\7a\2\2\u0214\u0088\3")
        buf.write("\2\2\2\u0215\u0216\7^\2\2\u0216\u0217\7d\2\2\u0217\u008a")
        buf.write("\3\2\2\2\u0218\u0219\7^\2\2\u0219\u021a\7h\2\2\u021a\u008c")
        buf.write("\3\2\2\2\u021b\u021c\7^\2\2\u021c\u021d\7t\2\2\u021d\u008e")
        buf.write("\3\2\2\2\u021e\u021f\7^\2\2\u021f\u0220\7p\2\2\u0220\u0090")
        buf.write("\3\2\2\2\u0221\u0222\7^\2\2\u0222\u0223\7v\2\2\u0223\u0092")
        buf.write("\3\2\2\2\u0224\u0225\7)\2\2\u0225\u0094\3\2\2\2\u0226")
        buf.write("\u0227\7$\2\2\u0227\u0096\3\2\2\2\u0228\u0229\7^\2\2\u0229")
        buf.write("\u022a\7^\2\2\u022a\u0098\3\2\2\2\u022b\u022c\7\62\2\2")
        buf.write("\u022c\u022d\t\5\2\2\u022d\u0232\t\6\2\2\u022e\u0231\5")
        buf.write("\u0085C\2\u022f\u0231\t\7\2\2\u0230\u022e\3\2\2\2\u0230")
        buf.write("\u022f\3\2\2\2\u0231\u0234\3\2\2\2\u0232\u0230\3\2\2\2")
        buf.write("\u0232\u0233\3\2\2\2\u0233\u009a\3\2\2\2\u0234\u0232\3")
        buf.write("\2\2\2\u0235\u0239\t\b\2\2\u0236\u0238\5\u0085C\2\u0237")
        buf.write("\u0236\3\2\2\2\u0238\u023b\3\2\2\2\u0239\u0237\3\2\2\2")
        buf.write("\u0239\u023a\3\2\2\2\u023a\u023e\3\2\2\2\u023b\u0239\3")
        buf.write("\2\2\2\u023c\u023e\7\62\2\2\u023d\u0235\3\2\2\2\u023d")
        buf.write("\u023c\3\2\2\2\u023e\u009c\3\2\2\2\u023f\u0240\7\62\2")
        buf.write("\2\u0240\u0241\t\t\2\2\u0241\u0245\t\n\2\2\u0242\u0244")
        buf.write("\t\13\2\2\u0243\u0242\3\2\2\2\u0244\u0247\3\2\2\2\u0245")
        buf.write("\u0243\3\2\2\2\u0245\u0246\3\2\2\2\u0246\u009e\3\2\2\2")
        buf.write("\u0247\u0245\3\2\2\2\u0248\u024c\5\u009bN\2\u0249\u024c")
        buf.write("\5\u0099M\2\u024a\u024c\5\u009dO\2\u024b\u0248\3\2\2\2")
        buf.write("\u024b\u0249\3\2\2\2\u024b\u024a\3\2\2\2\u024c\u00a0\3")
        buf.write("\2\2\2\u024d\u0250\t\f\2\2\u024e\u0251\5\'\24\2\u024f")
        buf.write("\u0251\5+\26\2\u0250\u024e\3\2\2\2\u0250\u024f\3\2\2\2")
        buf.write("\u0250\u0251\3\2\2\2\u0251\u0253\3\2\2\2\u0252\u0254\5")
        buf.write("\u0085C\2\u0253\u0252\3\2\2\2\u0254\u0255\3\2\2\2\u0255")
        buf.write("\u0253\3\2\2\2\u0255\u0256\3\2\2\2\u0256\u00a2\3\2\2\2")
        buf.write("\u0257\u025b\5\35\17\2\u0258\u025a\5\u0085C\2\u0259\u0258")
        buf.write("\3\2\2\2\u025a\u025d\3\2\2\2\u025b\u0259\3\2\2\2\u025b")
        buf.write("\u025c\3\2\2\2\u025c\u00a4\3\2\2\2\u025d\u025b\3\2\2\2")
        buf.write("\u025e\u0262\t\b\2\2\u025f\u0261\5\u0085C\2\u0260\u025f")
        buf.write("\3\2\2\2\u0261\u0264\3\2\2\2\u0262\u0260\3\2\2\2\u0262")
        buf.write("\u0263\3\2\2\2\u0263\u026b\3\2\2\2\u0264\u0262\3\2\2\2")
        buf.write("\u0265\u026c\5\u00a3R\2\u0266\u026c\5\u00a1Q\2\u0267\u0268")
        buf.write("\5\u00a3R\2\u0268\u0269\5\u00a1Q\2\u0269\u026c\3\2\2\2")
        buf.write("\u026a\u026c\5\u00a3R\2\u026b\u0265\3\2\2\2\u026b\u0266")
        buf.write("\3\2\2\2\u026b\u0267\3\2\2\2\u026b\u026a\3\2\2\2\u026b")
        buf.write("\u026c\3\2\2\2\u026c\u00a6\3\2\2\2\u026d\u0275\5\u0089")
        buf.write("E\2\u026e\u0275\5\u008bF\2\u026f\u0275\5\u008dG\2\u0270")
        buf.write("\u0275\5\u008fH\2\u0271\u0275\5\u0091I\2\u0272\u0275\5")
        buf.write("\u0093J\2\u0273\u0275\5\u0097L\2\u0274\u026d\3\2\2\2\u0274")
        buf.write("\u026e\3\2\2\2\u0274\u026f\3\2\2\2\u0274\u0270\3\2\2\2")
        buf.write("\u0274\u0271\3\2\2\2\u0274\u0272\3\2\2\2\u0274\u0273\3")
        buf.write("\2\2\2\u0275\u00a8\3\2\2\2\u0276\u0277\5\u0093J\2\u0277")
        buf.write("\u0278\5\u0095K\2\u0278\u027c\3\2\2\2\u0279\u027a\7^\2")
        buf.write("\2\u027a\u027c\7)\2\2\u027b\u0276\3\2\2\2\u027b\u0279")
        buf.write("\3\2\2\2\u027c\u00aa\3\2\2\2\u027d\u027e\5\u0093J\2\u027e")
        buf.write("\u00ac\3\2\2\2\u027f\u0285\5\u0095K\2\u0280\u0284\5\u00a9")
        buf.write("U\2\u0281\u0284\5\u00a7T\2\u0282\u0284\n\r\2\2\u0283\u0280")
        buf.write("\3\2\2\2\u0283\u0281\3\2\2\2\u0283\u0282\3\2\2\2\u0284")
        buf.write("\u0287\3\2\2\2\u0285\u0283\3\2\2\2\u0285\u0286\3\2\2\2")
        buf.write("\u0286\u0288\3\2\2\2\u0287\u0285\3\2\2\2\u0288\u0289\5")
        buf.write("\u0095K\2\u0289\u00ae\3\2\2\2\u028a\u028b\5#\22\2\u028b")
        buf.write("\u02c3\5\u00b1Y\2\u028c\u0294\5\u009fP\2\u028d\u028e\5")
        buf.write("\u00b1Y\2\u028e\u028f\5\37\20\2\u028f\u0290\5\u00b1Y\2")
        buf.write("\u0290\u0291\5\u009fP\2\u0291\u0293\3\2\2\2\u0292\u028d")
        buf.write("\3\2\2\2\u0293\u0296\3\2\2\2\u0294\u0292\3\2\2\2\u0294")
        buf.write("\u0295\3\2\2\2\u0295\u02c4\3\2\2\2\u0296\u0294\3\2\2\2")
        buf.write("\u0297\u029f\5\u00a5S\2\u0298\u0299\5\u00b1Y\2\u0299\u029a")
        buf.write("\5\37\20\2\u029a\u029b\5\u00b1Y\2\u029b\u029c\5\u00a5")
        buf.write("S\2\u029c\u029e\3\2\2\2\u029d\u0298\3\2\2\2\u029e\u02a1")
        buf.write("\3\2\2\2\u029f\u029d\3\2\2\2\u029f\u02a0\3\2\2\2\u02a0")
        buf.write("\u02c4\3\2\2\2\u02a1\u029f\3\2\2\2\u02a2\u02aa\5\u00ad")
        buf.write("W\2\u02a3\u02a4\5\u00b1Y\2\u02a4\u02a5\5\37\20\2\u02a5")
        buf.write("\u02a6\5\u00b1Y\2\u02a6\u02a7\5\u00adW\2\u02a7\u02a9\3")
        buf.write("\2\2\2\u02a8\u02a3\3\2\2\2\u02a9\u02ac\3\2\2\2\u02aa\u02a8")
        buf.write("\3\2\2\2\u02aa\u02ab\3\2\2\2\u02ab\u02c4\3\2\2\2\u02ac")
        buf.write("\u02aa\3\2\2\2\u02ad\u02b5\5\u00afX\2\u02ae\u02af\5\u00b1")
        buf.write("Y\2\u02af\u02b0\5\37\20\2\u02b0\u02b1\5\u00b1Y\2\u02b1")
        buf.write("\u02b2\5\u00afX\2\u02b2\u02b4\3\2\2\2\u02b3\u02ae\3\2")
        buf.write("\2\2\u02b4\u02b7\3\2\2\2\u02b5\u02b3\3\2\2\2\u02b5\u02b6")
        buf.write("\3\2\2\2\u02b6\u02c4\3\2\2\2\u02b7\u02b5\3\2\2\2\u02b8")
        buf.write("\u02c0\5\u00b3Z\2\u02b9\u02ba\5\u00b1Y\2\u02ba\u02bb\5")
        buf.write("\37\20\2\u02bb\u02bc\5\u00b1Y\2\u02bc\u02bd\5\u00b3Z\2")
        buf.write("\u02bd\u02bf\3\2\2\2\u02be\u02b9\3\2\2\2\u02bf\u02c2\3")
        buf.write("\2\2\2\u02c0\u02be\3\2\2\2\u02c0\u02c1\3\2\2\2\u02c1\u02c4")
        buf.write("\3\2\2\2\u02c2\u02c0\3\2\2\2\u02c3\u028c\3\2\2\2\u02c3")
        buf.write("\u0297\3\2\2\2\u02c3\u02a2\3\2\2\2\u02c3\u02ad\3\2\2\2")
        buf.write("\u02c3\u02b8\3\2\2\2\u02c4\u02c5\3\2\2\2\u02c5\u02c6\5")
        buf.write("\u00b1Y\2\u02c6\u02c7\5%\23\2\u02c7\u00b0\3\2\2\2\u02c8")
        buf.write("\u02ca\t\16\2\2\u02c9\u02c8\3\2\2\2\u02ca\u02cd\3\2\2")
        buf.write("\2\u02cb\u02c9\3\2\2\2\u02cb\u02cc\3\2\2\2\u02cc\u00b2")
        buf.write("\3\2\2\2\u02cd\u02cb\3\2\2\2\u02ce\u02d1\5{>\2\u02cf\u02d1")
        buf.write("\5}?\2\u02d0\u02ce\3\2\2\2\u02d0\u02cf\3\2\2\2\u02d1\u00b4")
        buf.write("\3\2\2\2\u02d2\u02d9\5\u0081A\2\u02d3\u02d8\5\u0081A\2")
        buf.write("\u02d4\u02d8\5\u0083B\2\u02d5\u02d8\5\u0087D\2\u02d6\u02d8")
        buf.write("\5\u0085C\2\u02d7\u02d3\3\2\2\2\u02d7\u02d4\3\2\2\2\u02d7")
        buf.write("\u02d5\3\2\2\2\u02d7\u02d6\3\2\2\2\u02d8\u02db\3\2\2\2")
        buf.write("\u02d9\u02d7\3\2\2\2\u02d9\u02da\3\2\2\2\u02da\u00b6\3")
        buf.write("\2\2\2\u02db\u02d9\3\2\2\2\u02dc\u02de\t\17\2\2\u02dd")
        buf.write("\u02dc\3\2\2\2\u02de\u02df\3\2\2\2\u02df\u02dd\3\2\2\2")
        buf.write("\u02df\u02e0\3\2\2\2\u02e0\u02e1\3\2\2\2\u02e1\u02e2\b")
        buf.write("\\\2\2\u02e2\u00b8\3\2\2\2\u02e3\u02e4\13\2\2\2\u02e4")
        buf.write("\u00ba\3\2\2\2\u02e5\u02e6\13\2\2\2\u02e6\u00bc\3\2\2")
        buf.write("\2\u02e7\u02e8\13\2\2\2\u02e8\u00be\3\2\2\2\u02e9\u02ea")
        buf.write("\13\2\2\2\u02ea\u00c0\3\2\2\2\35\2\u0230\u0232\u0239\u023d")
        buf.write("\u0245\u024b\u0250\u0255\u025b\u0262\u026b\u0274\u027b")
        buf.write("\u0283\u0285\u0294\u029f\u02aa\u02b5\u02c0\u02c3\u02cb")
        buf.write("\u02d0\u02d7\u02d9\u02df\3\b\2\2")
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
    ENDDO = 61
    INTERGER = 62
    FLOAT = 63
    STRING = 64
    ARRAY = 65
    BOOLEAN = 66
    ID = 67
    WS = 68
    ERROR_CHAR = 69
    UNCLOSE_STRING = 70
    ILLEGAL_ESCAPE = 71
    UNTERMINATED_COMMENT = 72

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
            "'Return'", "'Then'", "'Var'", "'While'", "'EndDo'" ]

    symbolicNames = [ "<INVALID>",
            "LP", "RP", "LB", "RB", "COLON", "DOT", "COMMA", "SEMI", "LCB", 
            "RCB", "ADDOP", "ADDF", "SUBOP", "SUBF", "MULOP", "MULF", "DIVOP", 
            "DIVF", "MODOP", "NOT", "AND", "OR", "EQ", "NEQ", "LT", "GT", 
            "LTE", "GTE", "NEQF", "LTF", "GTF", "LTEF", "GTEF", "ASSIG", 
            "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", 
            "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
            "RETURN", "THEN", "VAR", "WHILE", "ENDDO", "INTERGER", "FLOAT", 
            "STRING", "ARRAY", "BOOLEAN", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

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
                  "EXCEPT_QUOTE", "DENY_QUOTE", "STRING", "ARRAY", "SPACE", 
                  "BOOLEAN", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
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


