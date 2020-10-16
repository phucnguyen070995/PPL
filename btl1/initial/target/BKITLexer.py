# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2J")
        buf.write("\u02e0\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("^\t^\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\13\3\13")
        buf.write("\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3")
        buf.write("\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3")
        buf.write("%\3%\3%\3&\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3")
        buf.write("*\3*\3*\3*\3+\3+\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3.\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\60\3")
        buf.write("\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\3\67\38\38\38\39\39\39")
        buf.write("\39\39\39\39\39\39\39\3:\3:\3:\3:\3:\3:\3:\3;\3;\3;\3")
        buf.write(";\3;\3<\3<\3<\3<\3=\3=\3=\3=\3=\3=\3>\3>\3>\3>\3>\3?\3")
        buf.write("?\3?\3?\3?\3?\3@\3@\3@\3@\3@\3@\3A\3A\3B\3B\3C\3C\3D\3")
        buf.write("D\3E\3E\3E\3F\3F\3F\3G\3G\3G\3H\3H\3H\3I\3I\3I\3J\3J\3")
        buf.write("K\3K\3L\3L\3L\3M\3M\3M\3M\3M\7M\u022d\nM\fM\16M\u0230")
        buf.write("\13M\3N\3N\7N\u0234\nN\fN\16N\u0237\13N\3N\5N\u023a\n")
        buf.write("N\3O\3O\3O\3O\7O\u0240\nO\fO\16O\u0243\13O\3P\3P\3P\5")
        buf.write("P\u0248\nP\3Q\3Q\3Q\5Q\u024d\nQ\3Q\6Q\u0250\nQ\rQ\16Q")
        buf.write("\u0251\3R\3R\7R\u0256\nR\fR\16R\u0259\13R\3S\3S\7S\u025d")
        buf.write("\nS\fS\16S\u0260\13S\3S\3S\3S\3S\3S\3S\5S\u0268\nS\3T")
        buf.write("\3T\3T\3T\3T\3T\3T\5T\u0271\nT\3U\3U\3U\3U\3U\3U\7U\u0279")
        buf.write("\nU\fU\16U\u027c\13U\3U\3U\3V\3V\3V\3V\3V\3V\3V\3V\7V")
        buf.write("\u0288\nV\fV\16V\u028b\13V\3V\3V\3V\3V\3V\3V\7V\u0293")
        buf.write("\nV\fV\16V\u0296\13V\3V\3V\3V\3V\3V\3V\7V\u029e\nV\fV")
        buf.write("\16V\u02a1\13V\3V\3V\3V\3V\3V\3V\7V\u02a9\nV\fV\16V\u02ac")
        buf.write("\13V\3V\3V\3V\3V\3V\3V\7V\u02b4\nV\fV\16V\u02b7\13V\5")
        buf.write("V\u02b9\nV\3V\3V\3V\3W\7W\u02bf\nW\fW\16W\u02c2\13W\3")
        buf.write("X\3X\5X\u02c6\nX\3Y\3Y\3Y\3Y\3Y\7Y\u02cd\nY\fY\16Y\u02d0")
        buf.write("\13Y\3Z\6Z\u02d3\nZ\rZ\16Z\u02d4\3Z\3Z\3[\3[\3\\\3\\\3")
        buf.write("]\3]\3^\3^\2\2_\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write("\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65")
        buf.write("i\66k\67m8o9q:s;u<w=y>{\2}\2\177?\u0081\2\u0083\2\u0085")
        buf.write("\2\u0087\2\u0089\2\u008b\2\u008d\2\u008f\2\u0091\2\u0093")
        buf.write("\2\u0095\2\u0097\2\u0099\2\u009b\2\u009d\2\u009f@\u00a1")
        buf.write("\2\u00a3\2\u00a5A\u00a7\2\u00a9B\u00abC\u00ad\2\u00af")
        buf.write("D\u00b1E\u00b3F\u00b5G\u00b7H\u00b9I\u00bbJ\3\2\20\3\2")
        buf.write("c|\3\2C\\\3\2\62;\4\2ZZzz\4\2\63;CH\3\2CH\3\2\63;\4\2")
        buf.write("QQqq\3\2\639\3\2\629\4\2GGgg\7\2\f\f$$))GHQQ\3\2\"\"\5")
        buf.write("\2\13\f\17\17\"\"\2\u02f3\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\2w\3\2\2\2\2y\3\2\2\2\2\177\3\2\2\2\2\u009f\3\2\2\2")
        buf.write("\2\u00a5\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00af")
        buf.write("\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2")
        buf.write("\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb\3\2\2\2\3\u00bd")
        buf.write("\3\2\2\2\5\u00ca\3\2\2\2\7\u00d7\3\2\2\2\t\u00e5\3\2\2")
        buf.write("\2\13\u00f3\3\2\2\2\r\u0103\3\2\2\2\17\u0113\3\2\2\2\21")
        buf.write("\u0122\3\2\2\2\23\u0131\3\2\2\2\25\u0133\3\2\2\2\27\u0135")
        buf.write("\3\2\2\2\31\u0137\3\2\2\2\33\u0139\3\2\2\2\35\u013b\3")
        buf.write("\2\2\2\37\u013d\3\2\2\2!\u013f\3\2\2\2#\u0141\3\2\2\2")
        buf.write("%\u0143\3\2\2\2\'\u0145\3\2\2\2)\u0147\3\2\2\2+\u014a")
        buf.write("\3\2\2\2-\u014c\3\2\2\2/\u014f\3\2\2\2\61\u0151\3\2\2")
        buf.write("\2\63\u0154\3\2\2\2\65\u0156\3\2\2\2\67\u0159\3\2\2\2")
        buf.write("9\u015b\3\2\2\2;\u015d\3\2\2\2=\u0160\3\2\2\2?\u0163\3")
        buf.write("\2\2\2A\u0166\3\2\2\2C\u0169\3\2\2\2E\u016b\3\2\2\2G\u016d")
        buf.write("\3\2\2\2I\u0170\3\2\2\2K\u0173\3\2\2\2M\u0177\3\2\2\2")
        buf.write("O\u017a\3\2\2\2Q\u017d\3\2\2\2S\u0181\3\2\2\2U\u0185\3")
        buf.write("\2\2\2W\u0187\3\2\2\2Y\u018c\3\2\2\2[\u0192\3\2\2\2]\u019b")
        buf.write("\3\2\2\2_\u019e\3\2\2\2a\u01a3\3\2\2\2c\u01aa\3\2\2\2")
        buf.write("e\u01b2\3\2\2\2g\u01b8\3\2\2\2i\u01bf\3\2\2\2k\u01c8\3")
        buf.write("\2\2\2m\u01cc\3\2\2\2o\u01d5\3\2\2\2q\u01d8\3\2\2\2s\u01e2")
        buf.write("\3\2\2\2u\u01e9\3\2\2\2w\u01ee\3\2\2\2y\u01f2\3\2\2\2")
        buf.write("{\u01f8\3\2\2\2}\u01fd\3\2\2\2\177\u0203\3\2\2\2\u0081")
        buf.write("\u0209\3\2\2\2\u0083\u020b\3\2\2\2\u0085\u020d\3\2\2\2")
        buf.write("\u0087\u020f\3\2\2\2\u0089\u0211\3\2\2\2\u008b\u0214\3")
        buf.write("\2\2\2\u008d\u0217\3\2\2\2\u008f\u021a\3\2\2\2\u0091\u021d")
        buf.write("\3\2\2\2\u0093\u0220\3\2\2\2\u0095\u0222\3\2\2\2\u0097")
        buf.write("\u0224\3\2\2\2\u0099\u0227\3\2\2\2\u009b\u0239\3\2\2\2")
        buf.write("\u009d\u023b\3\2\2\2\u009f\u0247\3\2\2\2\u00a1\u0249\3")
        buf.write("\2\2\2\u00a3\u0253\3\2\2\2\u00a5\u025a\3\2\2\2\u00a7\u0270")
        buf.write("\3\2\2\2\u00a9\u0272\3\2\2\2\u00ab\u027f\3\2\2\2\u00ad")
        buf.write("\u02c0\3\2\2\2\u00af\u02c5\3\2\2\2\u00b1\u02c7\3\2\2\2")
        buf.write("\u00b3\u02d2\3\2\2\2\u00b5\u02d8\3\2\2\2\u00b7\u02da\3")
        buf.write("\2\2\2\u00b9\u02dc\3\2\2\2\u00bb\u02de\3\2\2\2\u00bd\u00be")
        buf.write("\7k\2\2\u00be\u00bf\7p\2\2\u00bf\u00c0\7v\2\2\u00c0\u00c1")
        buf.write("\7a\2\2\u00c1\u00c2\7q\2\2\u00c2\u00c3\7h\2\2\u00c3\u00c4")
        buf.write("\7a\2\2\u00c4\u00c5\7h\2\2\u00c5\u00c6\7n\2\2\u00c6\u00c7")
        buf.write("\7q\2\2\u00c7\u00c8\7c\2\2\u00c8\u00c9\7v\2\2\u00c9\4")
        buf.write("\3\2\2\2\u00ca\u00cb\7h\2\2\u00cb\u00cc\7n\2\2\u00cc\u00cd")
        buf.write("\7q\2\2\u00cd\u00ce\7c\2\2\u00ce\u00cf\7v\2\2\u00cf\u00d0")
        buf.write("\7a\2\2\u00d0\u00d1\7q\2\2\u00d1\u00d2\7h\2\2\u00d2\u00d3")
        buf.write("\7a\2\2\u00d3\u00d4\7k\2\2\u00d4\u00d5\7p\2\2\u00d5\u00d6")
        buf.write("\7v\2\2\u00d6\6\3\2\2\2\u00d7\u00d8\7k\2\2\u00d8\u00d9")
        buf.write("\7p\2\2\u00d9\u00da\7v\2\2\u00da\u00db\7a\2\2\u00db\u00dc")
        buf.write("\7q\2\2\u00dc\u00dd\7h\2\2\u00dd\u00de\7a\2\2\u00de\u00df")
        buf.write("\7u\2\2\u00df\u00e0\7v\2\2\u00e0\u00e1\7t\2\2\u00e1\u00e2")
        buf.write("\7k\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4\7i\2\2\u00e4\b")
        buf.write("\3\2\2\2\u00e5\u00e6\7u\2\2\u00e6\u00e7\7v\2\2\u00e7\u00e8")
        buf.write("\7t\2\2\u00e8\u00e9\7k\2\2\u00e9\u00ea\7p\2\2\u00ea\u00eb")
        buf.write("\7i\2\2\u00eb\u00ec\7a\2\2\u00ec\u00ed\7q\2\2\u00ed\u00ee")
        buf.write("\7h\2\2\u00ee\u00ef\7a\2\2\u00ef\u00f0\7k\2\2\u00f0\u00f1")
        buf.write("\7p\2\2\u00f1\u00f2\7v\2\2\u00f2\n\3\2\2\2\u00f3\u00f4")
        buf.write("\7h\2\2\u00f4\u00f5\7n\2\2\u00f5\u00f6\7q\2\2\u00f6\u00f7")
        buf.write("\7c\2\2\u00f7\u00f8\7v\2\2\u00f8\u00f9\7a\2\2\u00f9\u00fa")
        buf.write("\7q\2\2\u00fa\u00fb\7h\2\2\u00fb\u00fc\7a\2\2\u00fc\u00fd")
        buf.write("\7u\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100")
        buf.write("\7k\2\2\u0100\u0101\7p\2\2\u0101\u0102\7i\2\2\u0102\f")
        buf.write("\3\2\2\2\u0103\u0104\7u\2\2\u0104\u0105\7v\2\2\u0105\u0106")
        buf.write("\7t\2\2\u0106\u0107\7k\2\2\u0107\u0108\7p\2\2\u0108\u0109")
        buf.write("\7i\2\2\u0109\u010a\7a\2\2\u010a\u010b\7q\2\2\u010b\u010c")
        buf.write("\7h\2\2\u010c\u010d\7a\2\2\u010d\u010e\7h\2\2\u010e\u010f")
        buf.write("\7n\2\2\u010f\u0110\7q\2\2\u0110\u0111\7c\2\2\u0111\u0112")
        buf.write("\7v\2\2\u0112\16\3\2\2\2\u0113\u0114\7d\2\2\u0114\u0115")
        buf.write("\7q\2\2\u0115\u0116\7q\2\2\u0116\u0117\7n\2\2\u0117\u0118")
        buf.write("\7a\2\2\u0118\u0119\7q\2\2\u0119\u011a\7h\2\2\u011a\u011b")
        buf.write("\7a\2\2\u011b\u011c\7u\2\2\u011c\u011d\7v\2\2\u011d\u011e")
        buf.write("\7t\2\2\u011e\u011f\7k\2\2\u011f\u0120\7p\2\2\u0120\u0121")
        buf.write("\7i\2\2\u0121\20\3\2\2\2\u0122\u0123\7u\2\2\u0123\u0124")
        buf.write("\7v\2\2\u0124\u0125\7t\2\2\u0125\u0126\7k\2\2\u0126\u0127")
        buf.write("\7p\2\2\u0127\u0128\7i\2\2\u0128\u0129\7a\2\2\u0129\u012a")
        buf.write("\7q\2\2\u012a\u012b\7h\2\2\u012b\u012c\7a\2\2\u012c\u012d")
        buf.write("\7d\2\2\u012d\u012e\7q\2\2\u012e\u012f\7q\2\2\u012f\u0130")
        buf.write("\7n\2\2\u0130\22\3\2\2\2\u0131\u0132\7*\2\2\u0132\24\3")
        buf.write("\2\2\2\u0133\u0134\7+\2\2\u0134\26\3\2\2\2\u0135\u0136")
        buf.write("\7]\2\2\u0136\30\3\2\2\2\u0137\u0138\7_\2\2\u0138\32\3")
        buf.write("\2\2\2\u0139\u013a\7<\2\2\u013a\34\3\2\2\2\u013b\u013c")
        buf.write("\7\60\2\2\u013c\36\3\2\2\2\u013d\u013e\7.\2\2\u013e \3")
        buf.write("\2\2\2\u013f\u0140\7=\2\2\u0140\"\3\2\2\2\u0141\u0142")
        buf.write("\7}\2\2\u0142$\3\2\2\2\u0143\u0144\7\177\2\2\u0144&\3")
        buf.write("\2\2\2\u0145\u0146\7-\2\2\u0146(\3\2\2\2\u0147\u0148\7")
        buf.write("-\2\2\u0148\u0149\7\60\2\2\u0149*\3\2\2\2\u014a\u014b")
        buf.write("\7/\2\2\u014b,\3\2\2\2\u014c\u014d\7/\2\2\u014d\u014e")
        buf.write("\7\60\2\2\u014e.\3\2\2\2\u014f\u0150\7,\2\2\u0150\60\3")
        buf.write("\2\2\2\u0151\u0152\7,\2\2\u0152\u0153\7\60\2\2\u0153\62")
        buf.write("\3\2\2\2\u0154\u0155\7^\2\2\u0155\64\3\2\2\2\u0156\u0157")
        buf.write("\7^\2\2\u0157\u0158\7\60\2\2\u0158\66\3\2\2\2\u0159\u015a")
        buf.write("\7\'\2\2\u015a8\3\2\2\2\u015b\u015c\7#\2\2\u015c:\3\2")
        buf.write("\2\2\u015d\u015e\7(\2\2\u015e\u015f\7(\2\2\u015f<\3\2")
        buf.write("\2\2\u0160\u0161\7~\2\2\u0161\u0162\7~\2\2\u0162>\3\2")
        buf.write("\2\2\u0163\u0164\7?\2\2\u0164\u0165\7?\2\2\u0165@\3\2")
        buf.write("\2\2\u0166\u0167\7#\2\2\u0167\u0168\7?\2\2\u0168B\3\2")
        buf.write("\2\2\u0169\u016a\7>\2\2\u016aD\3\2\2\2\u016b\u016c\7@")
        buf.write("\2\2\u016cF\3\2\2\2\u016d\u016e\7>\2\2\u016e\u016f\7?")
        buf.write("\2\2\u016fH\3\2\2\2\u0170\u0171\7@\2\2\u0171\u0172\7?")
        buf.write("\2\2\u0172J\3\2\2\2\u0173\u0174\7?\2\2\u0174\u0175\7\61")
        buf.write("\2\2\u0175\u0176\7?\2\2\u0176L\3\2\2\2\u0177\u0178\7>")
        buf.write("\2\2\u0178\u0179\7\60\2\2\u0179N\3\2\2\2\u017a\u017b\7")
        buf.write("@\2\2\u017b\u017c\7\60\2\2\u017cP\3\2\2\2\u017d\u017e")
        buf.write("\7>\2\2\u017e\u017f\7?\2\2\u017f\u0180\7\60\2\2\u0180")
        buf.write("R\3\2\2\2\u0181\u0182\7@\2\2\u0182\u0183\7?\2\2\u0183")
        buf.write("\u0184\7\60\2\2\u0184T\3\2\2\2\u0185\u0186\7?\2\2\u0186")
        buf.write("V\3\2\2\2\u0187\u0188\7D\2\2\u0188\u0189\7q\2\2\u0189")
        buf.write("\u018a\7f\2\2\u018a\u018b\7{\2\2\u018bX\3\2\2\2\u018c")
        buf.write("\u018d\7D\2\2\u018d\u018e\7t\2\2\u018e\u018f\7g\2\2\u018f")
        buf.write("\u0190\7c\2\2\u0190\u0191\7m\2\2\u0191Z\3\2\2\2\u0192")
        buf.write("\u0193\7E\2\2\u0193\u0194\7q\2\2\u0194\u0195\7p\2\2\u0195")
        buf.write("\u0196\7v\2\2\u0196\u0197\7k\2\2\u0197\u0198\7p\2\2\u0198")
        buf.write("\u0199\7w\2\2\u0199\u019a\7g\2\2\u019a\\\3\2\2\2\u019b")
        buf.write("\u019c\7F\2\2\u019c\u019d\7q\2\2\u019d^\3\2\2\2\u019e")
        buf.write("\u019f\7G\2\2\u019f\u01a0\7n\2\2\u01a0\u01a1\7u\2\2\u01a1")
        buf.write("\u01a2\7g\2\2\u01a2`\3\2\2\2\u01a3\u01a4\7G\2\2\u01a4")
        buf.write("\u01a5\7n\2\2\u01a5\u01a6\7u\2\2\u01a6\u01a7\7g\2\2\u01a7")
        buf.write("\u01a8\7K\2\2\u01a8\u01a9\7h\2\2\u01a9b\3\2\2\2\u01aa")
        buf.write("\u01ab\7G\2\2\u01ab\u01ac\7p\2\2\u01ac\u01ad\7f\2\2\u01ad")
        buf.write("\u01ae\7D\2\2\u01ae\u01af\7q\2\2\u01af\u01b0\7f\2\2\u01b0")
        buf.write("\u01b1\7{\2\2\u01b1d\3\2\2\2\u01b2\u01b3\7G\2\2\u01b3")
        buf.write("\u01b4\7p\2\2\u01b4\u01b5\7f\2\2\u01b5\u01b6\7K\2\2\u01b6")
        buf.write("\u01b7\7h\2\2\u01b7f\3\2\2\2\u01b8\u01b9\7G\2\2\u01b9")
        buf.write("\u01ba\7p\2\2\u01ba\u01bb\7f\2\2\u01bb\u01bc\7H\2\2\u01bc")
        buf.write("\u01bd\7q\2\2\u01bd\u01be\7t\2\2\u01beh\3\2\2\2\u01bf")
        buf.write("\u01c0\7G\2\2\u01c0\u01c1\7p\2\2\u01c1\u01c2\7f\2\2\u01c2")
        buf.write("\u01c3\7Y\2\2\u01c3\u01c4\7j\2\2\u01c4\u01c5\7k\2\2\u01c5")
        buf.write("\u01c6\7n\2\2\u01c6\u01c7\7g\2\2\u01c7j\3\2\2\2\u01c8")
        buf.write("\u01c9\7H\2\2\u01c9\u01ca\7q\2\2\u01ca\u01cb\7t\2\2\u01cb")
        buf.write("l\3\2\2\2\u01cc\u01cd\7H\2\2\u01cd\u01ce\7w\2\2\u01ce")
        buf.write("\u01cf\7p\2\2\u01cf\u01d0\7e\2\2\u01d0\u01d1\7v\2\2\u01d1")
        buf.write("\u01d2\7k\2\2\u01d2\u01d3\7q\2\2\u01d3\u01d4\7p\2\2\u01d4")
        buf.write("n\3\2\2\2\u01d5\u01d6\7K\2\2\u01d6\u01d7\7h\2\2\u01d7")
        buf.write("p\3\2\2\2\u01d8\u01d9\7R\2\2\u01d9\u01da\7c\2\2\u01da")
        buf.write("\u01db\7t\2\2\u01db\u01dc\7c\2\2\u01dc\u01dd\7o\2\2\u01dd")
        buf.write("\u01de\7g\2\2\u01de\u01df\7v\2\2\u01df\u01e0\7g\2\2\u01e0")
        buf.write("\u01e1\7t\2\2\u01e1r\3\2\2\2\u01e2\u01e3\7T\2\2\u01e3")
        buf.write("\u01e4\7g\2\2\u01e4\u01e5\7v\2\2\u01e5\u01e6\7w\2\2\u01e6")
        buf.write("\u01e7\7t\2\2\u01e7\u01e8\7p\2\2\u01e8t\3\2\2\2\u01e9")
        buf.write("\u01ea\7V\2\2\u01ea\u01eb\7j\2\2\u01eb\u01ec\7g\2\2\u01ec")
        buf.write("\u01ed\7p\2\2\u01edv\3\2\2\2\u01ee\u01ef\7X\2\2\u01ef")
        buf.write("\u01f0\7c\2\2\u01f0\u01f1\7t\2\2\u01f1x\3\2\2\2\u01f2")
        buf.write("\u01f3\7Y\2\2\u01f3\u01f4\7j\2\2\u01f4\u01f5\7k\2\2\u01f5")
        buf.write("\u01f6\7n\2\2\u01f6\u01f7\7g\2\2\u01f7z\3\2\2\2\u01f8")
        buf.write("\u01f9\7V\2\2\u01f9\u01fa\7t\2\2\u01fa\u01fb\7w\2\2\u01fb")
        buf.write("\u01fc\7g\2\2\u01fc|\3\2\2\2\u01fd\u01fe\7H\2\2\u01fe")
        buf.write("\u01ff\7c\2\2\u01ff\u0200\7n\2\2\u0200\u0201\7u\2\2\u0201")
        buf.write("\u0202\7g\2\2\u0202~\3\2\2\2\u0203\u0204\7G\2\2\u0204")
        buf.write("\u0205\7p\2\2\u0205\u0206\7f\2\2\u0206\u0207\7F\2\2\u0207")
        buf.write("\u0208\7q\2\2\u0208\u0080\3\2\2\2\u0209\u020a\t\2\2\2")
        buf.write("\u020a\u0082\3\2\2\2\u020b\u020c\t\3\2\2\u020c\u0084\3")
        buf.write("\2\2\2\u020d\u020e\t\4\2\2\u020e\u0086\3\2\2\2\u020f\u0210")
        buf.write("\7a\2\2\u0210\u0088\3\2\2\2\u0211\u0212\7^\2\2\u0212\u0213")
        buf.write("\7d\2\2\u0213\u008a\3\2\2\2\u0214\u0215\7^\2\2\u0215\u0216")
        buf.write("\7h\2\2\u0216\u008c\3\2\2\2\u0217\u0218\7^\2\2\u0218\u0219")
        buf.write("\7t\2\2\u0219\u008e\3\2\2\2\u021a\u021b\7^\2\2\u021b\u021c")
        buf.write("\7p\2\2\u021c\u0090\3\2\2\2\u021d\u021e\7^\2\2\u021e\u021f")
        buf.write("\7v\2\2\u021f\u0092\3\2\2\2\u0220\u0221\7)\2\2\u0221\u0094")
        buf.write("\3\2\2\2\u0222\u0223\7$\2\2\u0223\u0096\3\2\2\2\u0224")
        buf.write("\u0225\7^\2\2\u0225\u0226\7^\2\2\u0226\u0098\3\2\2\2\u0227")
        buf.write("\u0228\7\62\2\2\u0228\u0229\t\5\2\2\u0229\u022e\t\6\2")
        buf.write("\2\u022a\u022d\5\u0085C\2\u022b\u022d\t\7\2\2\u022c\u022a")
        buf.write("\3\2\2\2\u022c\u022b\3\2\2\2\u022d\u0230\3\2\2\2\u022e")
        buf.write("\u022c\3\2\2\2\u022e\u022f\3\2\2\2\u022f\u009a\3\2\2\2")
        buf.write("\u0230\u022e\3\2\2\2\u0231\u0235\t\b\2\2\u0232\u0234\5")
        buf.write("\u0085C\2\u0233\u0232\3\2\2\2\u0234\u0237\3\2\2\2\u0235")
        buf.write("\u0233\3\2\2\2\u0235\u0236\3\2\2\2\u0236\u023a\3\2\2\2")
        buf.write("\u0237\u0235\3\2\2\2\u0238\u023a\7\62\2\2\u0239\u0231")
        buf.write("\3\2\2\2\u0239\u0238\3\2\2\2\u023a\u009c\3\2\2\2\u023b")
        buf.write("\u023c\7\62\2\2\u023c\u023d\t\t\2\2\u023d\u0241\t\n\2")
        buf.write("\2\u023e\u0240\t\13\2\2\u023f\u023e\3\2\2\2\u0240\u0243")
        buf.write("\3\2\2\2\u0241\u023f\3\2\2\2\u0241\u0242\3\2\2\2\u0242")
        buf.write("\u009e\3\2\2\2\u0243\u0241\3\2\2\2\u0244\u0248\5\u009b")
        buf.write("N\2\u0245\u0248\5\u0099M\2\u0246\u0248\5\u009dO\2\u0247")
        buf.write("\u0244\3\2\2\2\u0247\u0245\3\2\2\2\u0247\u0246\3\2\2\2")
        buf.write("\u0248\u00a0\3\2\2\2\u0249\u024c\t\f\2\2\u024a\u024d\5")
        buf.write("\'\24\2\u024b\u024d\5+\26\2\u024c\u024a\3\2\2\2\u024c")
        buf.write("\u024b\3\2\2\2\u024c\u024d\3\2\2\2\u024d\u024f\3\2\2\2")
        buf.write("\u024e\u0250\5\u0085C\2\u024f\u024e\3\2\2\2\u0250\u0251")
        buf.write("\3\2\2\2\u0251\u024f\3\2\2\2\u0251\u0252\3\2\2\2\u0252")
        buf.write("\u00a2\3\2\2\2\u0253\u0257\5\35\17\2\u0254\u0256\5\u0085")
        buf.write("C\2\u0255\u0254\3\2\2\2\u0256\u0259\3\2\2\2\u0257\u0255")
        buf.write("\3\2\2\2\u0257\u0258\3\2\2\2\u0258\u00a4\3\2\2\2\u0259")
        buf.write("\u0257\3\2\2\2\u025a\u025e\t\b\2\2\u025b\u025d\5\u0085")
        buf.write("C\2\u025c\u025b\3\2\2\2\u025d\u0260\3\2\2\2\u025e\u025c")
        buf.write("\3\2\2\2\u025e\u025f\3\2\2\2\u025f\u0267\3\2\2\2\u0260")
        buf.write("\u025e\3\2\2\2\u0261\u0268\5\u00a3R\2\u0262\u0268\5\u00a1")
        buf.write("Q\2\u0263\u0264\5\u00a3R\2\u0264\u0265\5\u00a1Q\2\u0265")
        buf.write("\u0268\3\2\2\2\u0266\u0268\5\u00a3R\2\u0267\u0261\3\2")
        buf.write("\2\2\u0267\u0262\3\2\2\2\u0267\u0263\3\2\2\2\u0267\u0266")
        buf.write("\3\2\2\2\u0267\u0268\3\2\2\2\u0268\u00a6\3\2\2\2\u0269")
        buf.write("\u0271\5\u0089E\2\u026a\u0271\5\u008bF\2\u026b\u0271\5")
        buf.write("\u008dG\2\u026c\u0271\5\u008fH\2\u026d\u0271\5\u0091I")
        buf.write("\2\u026e\u0271\5\u0093J\2\u026f\u0271\5\u0097L\2\u0270")
        buf.write("\u0269\3\2\2\2\u0270\u026a\3\2\2\2\u0270\u026b\3\2\2\2")
        buf.write("\u0270\u026c\3\2\2\2\u0270\u026d\3\2\2\2\u0270\u026e\3")
        buf.write("\2\2\2\u0270\u026f\3\2\2\2\u0271\u00a8\3\2\2\2\u0272\u027a")
        buf.write("\5\u0095K\2\u0273\u0274\5\u0093J\2\u0274\u0275\5\u0095")
        buf.write("K\2\u0275\u0279\3\2\2\2\u0276\u0279\5\u00a7T\2\u0277\u0279")
        buf.write("\n\r\2\2\u0278\u0273\3\2\2\2\u0278\u0276\3\2\2\2\u0278")
        buf.write("\u0277\3\2\2\2\u0279\u027c\3\2\2\2\u027a\u0278\3\2\2\2")
        buf.write("\u027a\u027b\3\2\2\2\u027b\u027d\3\2\2\2\u027c\u027a\3")
        buf.write("\2\2\2\u027d\u027e\5\u0095K\2\u027e\u00aa\3\2\2\2\u027f")
        buf.write("\u0280\5#\22\2\u0280\u02b8\5\u00adW\2\u0281\u0289\5\u009f")
        buf.write("P\2\u0282\u0283\5\u00adW\2\u0283\u0284\5\37\20\2\u0284")
        buf.write("\u0285\5\u00adW\2\u0285\u0286\5\u009fP\2\u0286\u0288\3")
        buf.write("\2\2\2\u0287\u0282\3\2\2\2\u0288\u028b\3\2\2\2\u0289\u0287")
        buf.write("\3\2\2\2\u0289\u028a\3\2\2\2\u028a\u02b9\3\2\2\2\u028b")
        buf.write("\u0289\3\2\2\2\u028c\u0294\5\u00a5S\2\u028d\u028e\5\u00ad")
        buf.write("W\2\u028e\u028f\5\37\20\2\u028f\u0290\5\u00adW\2\u0290")
        buf.write("\u0291\5\u00a5S\2\u0291\u0293\3\2\2\2\u0292\u028d\3\2")
        buf.write("\2\2\u0293\u0296\3\2\2\2\u0294\u0292\3\2\2\2\u0294\u0295")
        buf.write("\3\2\2\2\u0295\u02b9\3\2\2\2\u0296\u0294\3\2\2\2\u0297")
        buf.write("\u029f\5\u00a9U\2\u0298\u0299\5\u00adW\2\u0299\u029a\5")
        buf.write("\37\20\2\u029a\u029b\5\u00adW\2\u029b\u029c\5\u00a9U\2")
        buf.write("\u029c\u029e\3\2\2\2\u029d\u0298\3\2\2\2\u029e\u02a1\3")
        buf.write("\2\2\2\u029f\u029d\3\2\2\2\u029f\u02a0\3\2\2\2\u02a0\u02b9")
        buf.write("\3\2\2\2\u02a1\u029f\3\2\2\2\u02a2\u02aa\5\u00abV\2\u02a3")
        buf.write("\u02a4\5\u00adW\2\u02a4\u02a5\5\37\20\2\u02a5\u02a6\5")
        buf.write("\u00adW\2\u02a6\u02a7\5\u00abV\2\u02a7\u02a9\3\2\2\2\u02a8")
        buf.write("\u02a3\3\2\2\2\u02a9\u02ac\3\2\2\2\u02aa\u02a8\3\2\2\2")
        buf.write("\u02aa\u02ab\3\2\2\2\u02ab\u02b9\3\2\2\2\u02ac\u02aa\3")
        buf.write("\2\2\2\u02ad\u02b5\5\u00afX\2\u02ae\u02af\5\u00adW\2\u02af")
        buf.write("\u02b0\5\37\20\2\u02b0\u02b1\5\u00adW\2\u02b1\u02b2\5")
        buf.write("\u00afX\2\u02b2\u02b4\3\2\2\2\u02b3\u02ae\3\2\2\2\u02b4")
        buf.write("\u02b7\3\2\2\2\u02b5\u02b3\3\2\2\2\u02b5\u02b6\3\2\2\2")
        buf.write("\u02b6\u02b9\3\2\2\2\u02b7\u02b5\3\2\2\2\u02b8\u0281\3")
        buf.write("\2\2\2\u02b8\u028c\3\2\2\2\u02b8\u0297\3\2\2\2\u02b8\u02a2")
        buf.write("\3\2\2\2\u02b8\u02ad\3\2\2\2\u02b9\u02ba\3\2\2\2\u02ba")
        buf.write("\u02bb\5\u00adW\2\u02bb\u02bc\5%\23\2\u02bc\u00ac\3\2")
        buf.write("\2\2\u02bd\u02bf\t\16\2\2\u02be\u02bd\3\2\2\2\u02bf\u02c2")
        buf.write("\3\2\2\2\u02c0\u02be\3\2\2\2\u02c0\u02c1\3\2\2\2\u02c1")
        buf.write("\u00ae\3\2\2\2\u02c2\u02c0\3\2\2\2\u02c3\u02c6\5{>\2\u02c4")
        buf.write("\u02c6\5}?\2\u02c5\u02c3\3\2\2\2\u02c5\u02c4\3\2\2\2\u02c6")
        buf.write("\u00b0\3\2\2\2\u02c7\u02ce\5\u0081A\2\u02c8\u02cd\5\u0081")
        buf.write("A\2\u02c9\u02cd\5\u0083B\2\u02ca\u02cd\5\u0087D\2\u02cb")
        buf.write("\u02cd\5\u0085C\2\u02cc\u02c8\3\2\2\2\u02cc\u02c9\3\2")
        buf.write("\2\2\u02cc\u02ca\3\2\2\2\u02cc\u02cb\3\2\2\2\u02cd\u02d0")
        buf.write("\3\2\2\2\u02ce\u02cc\3\2\2\2\u02ce\u02cf\3\2\2\2\u02cf")
        buf.write("\u00b2\3\2\2\2\u02d0\u02ce\3\2\2\2\u02d1\u02d3\t\17\2")
        buf.write("\2\u02d2\u02d1\3\2\2\2\u02d3\u02d4\3\2\2\2\u02d4\u02d2")
        buf.write("\3\2\2\2\u02d4\u02d5\3\2\2\2\u02d5\u02d6\3\2\2\2\u02d6")
        buf.write("\u02d7\bZ\2\2\u02d7\u00b4\3\2\2\2\u02d8\u02d9\13\2\2\2")
        buf.write("\u02d9\u00b6\3\2\2\2\u02da\u02db\13\2\2\2\u02db\u00b8")
        buf.write("\3\2\2\2\u02dc\u02dd\13\2\2\2\u02dd\u00ba\3\2\2\2\u02de")
        buf.write("\u02df\13\2\2\2\u02df\u00bc\3\2\2\2\34\2\u022c\u022e\u0235")
        buf.write("\u0239\u0241\u0247\u024c\u0251\u0257\u025e\u0267\u0270")
        buf.write("\u0278\u027a\u0289\u0294\u029f\u02aa\u02b5\u02b8\u02c0")
        buf.write("\u02c5\u02cc\u02ce\u02d4\3\b\2\2")
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
                  "STRING", "ARRAY", "SPACE", "BOOLEAN", "ID", "WS", "ERROR_CHAR", 
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


