# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u02ed\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("U\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\5\2\u0118\n\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3")
        buf.write("\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"")
        buf.write("\3#\3#\3#\3#\3$\3$\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3")
        buf.write(")\3)\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\3,\3")
        buf.write(",\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\38\38\3")
        buf.write("8\38\38\38\39\39\39\39\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3")
        buf.write(">\3>\3?\3?\3@\3@\3@\3@\3@\7@\u0203\n@\f@\16@\u0206\13")
        buf.write("@\3A\3A\7A\u020a\nA\fA\16A\u020d\13A\3A\5A\u0210\nA\3")
        buf.write("B\3B\3B\3B\7B\u0216\nB\fB\16B\u0219\13B\3C\3C\3C\5C\u021e")
        buf.write("\nC\3D\3D\3D\5D\u0223\nD\3D\6D\u0226\nD\rD\16D\u0227\3")
        buf.write("E\3E\7E\u022c\nE\fE\16E\u022f\13E\3F\3F\7F\u0233\nF\f")
        buf.write("F\16F\u0236\13F\3F\5F\u0239\nF\3F\3F\3F\3F\3F\3F\5F\u0241")
        buf.write("\nF\3G\3G\3G\3H\3H\7H\u0248\nH\fH\16H\u024b\13H\3H\3H")
        buf.write("\3I\3I\3I\3I\3I\3I\3I\3I\7I\u0257\nI\fI\16I\u025a\13I")
        buf.write("\3I\3I\3I\3I\3I\3I\7I\u0262\nI\fI\16I\u0265\13I\3I\3I")
        buf.write("\3I\3I\3I\3I\7I\u026d\nI\fI\16I\u0270\13I\3I\3I\3I\3I")
        buf.write("\3I\3I\7I\u0278\nI\fI\16I\u027b\13I\3I\3I\3I\3I\3I\3I")
        buf.write("\7I\u0283\nI\fI\16I\u0286\13I\5I\u0288\nI\3I\3I\3I\3J")
        buf.write("\7J\u028e\nJ\fJ\16J\u0291\13J\3K\3K\5K\u0295\nK\3L\3L")
        buf.write("\3L\3L\3L\7L\u029c\nL\fL\16L\u029f\13L\3M\6M\u02a2\nM")
        buf.write("\rM\16M\u02a3\3M\3M\3N\3N\3N\3N\7N\u02ac\nN\fN\16N\u02af")
        buf.write("\13N\3N\3N\3N\3N\3N\3O\3O\3O\3O\5O\u02ba\nO\3P\3P\3P\3")
        buf.write("P\3P\5P\u02c1\nP\3Q\3Q\3Q\3Q\3Q\5Q\u02c8\nQ\3R\3R\3S\3")
        buf.write("S\7S\u02ce\nS\fS\16S\u02d1\13S\3S\5S\u02d4\nS\3S\3S\3")
        buf.write("T\3T\7T\u02da\nT\fT\16T\u02dd\13T\3T\3T\3T\3U\3U\3U\3")
        buf.write("U\7U\u02e6\nU\fU\16U\u02e9\13U\3U\3U\3U\4\u0249\u02ad")
        buf.write("\2V\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\2\27\2")
        buf.write("\31\f\33\r\35\16\37\17!\20#\21%\22\'\23)\24+\25-\26/\27")
        buf.write("\61\30\63\31\65\32\67\339\34;\35=\36?\37A C!E\"G#I$K%")
        buf.write("M&O\'Q(S)U*W+Y,[-]._/a\60c\61e\62g\63i\64k\65m\2o\2q\66")
        buf.write("s\2u\2w\2y\2{\2}\2\177\2\u0081\2\u0083\2\u0085\67\u0087")
        buf.write("\2\u0089\2\u008b8\u008d\2\u008f9\u0091:\u0093\2\u0095")
        buf.write(";\u0097<\u0099=\u009b>\u009d\2\u009f\2\u00a1\2\u00a3?")
        buf.write("\u00a5@\u00a7A\u00a9B\3\2\25\3\2c|\3\2C\\\3\2\62;\4\2")
        buf.write("ZZzz\4\2\63;CH\3\2CH\3\2\63;\4\2QQqq\3\2\639\3\2\629\4")
        buf.write("\2GGgg\t\2))^^ddhhppttvv\3\2\"\"\5\2\13\f\17\17\"\"\6")
        buf.write("\2\f\f$$))^^\3\2))\3\2$$\3\2,,\4\3\f\f\17\17\2\u030b\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2q\3\2\2\2\2\u0085\3\2\2\2\2\u008b\3\2\2\2\2\u008f\3")
        buf.write("\2\2\2\2\u0091\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2")
        buf.write("\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5")
        buf.write("\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\3\u0117\3\2\2")
        buf.write("\2\5\u0119\3\2\2\2\7\u011b\3\2\2\2\t\u011d\3\2\2\2\13")
        buf.write("\u011f\3\2\2\2\r\u0121\3\2\2\2\17\u0123\3\2\2\2\21\u0125")
        buf.write("\3\2\2\2\23\u0127\3\2\2\2\25\u0129\3\2\2\2\27\u012b\3")
        buf.write("\2\2\2\31\u012d\3\2\2\2\33\u012f\3\2\2\2\35\u0132\3\2")
        buf.write("\2\2\37\u0134\3\2\2\2!\u0137\3\2\2\2#\u0139\3\2\2\2%\u013c")
        buf.write("\3\2\2\2\'\u013e\3\2\2\2)\u0141\3\2\2\2+\u0143\3\2\2\2")
        buf.write("-\u0145\3\2\2\2/\u0148\3\2\2\2\61\u014b\3\2\2\2\63\u014e")
        buf.write("\3\2\2\2\65\u0151\3\2\2\2\67\u0153\3\2\2\29\u0155\3\2")
        buf.write("\2\2;\u0158\3\2\2\2=\u015b\3\2\2\2?\u015f\3\2\2\2A\u0162")
        buf.write("\3\2\2\2C\u0165\3\2\2\2E\u0169\3\2\2\2G\u016d\3\2\2\2")
        buf.write("I\u016f\3\2\2\2K\u0174\3\2\2\2M\u017a\3\2\2\2O\u0183\3")
        buf.write("\2\2\2Q\u0186\3\2\2\2S\u018b\3\2\2\2U\u0192\3\2\2\2W\u019a")
        buf.write("\3\2\2\2Y\u01a0\3\2\2\2[\u01a7\3\2\2\2]\u01b0\3\2\2\2")
        buf.write("_\u01b4\3\2\2\2a\u01bd\3\2\2\2c\u01c0\3\2\2\2e\u01ca\3")
        buf.write("\2\2\2g\u01d1\3\2\2\2i\u01d6\3\2\2\2k\u01da\3\2\2\2m\u01e0")
        buf.write("\3\2\2\2o\u01e5\3\2\2\2q\u01eb\3\2\2\2s\u01f1\3\2\2\2")
        buf.write("u\u01f3\3\2\2\2w\u01f5\3\2\2\2y\u01f7\3\2\2\2{\u01f9\3")
        buf.write("\2\2\2}\u01fb\3\2\2\2\177\u01fd\3\2\2\2\u0081\u020f\3")
        buf.write("\2\2\2\u0083\u0211\3\2\2\2\u0085\u021d\3\2\2\2\u0087\u021f")
        buf.write("\3\2\2\2\u0089\u0229\3\2\2\2\u008b\u0238\3\2\2\2\u008d")
        buf.write("\u0242\3\2\2\2\u008f\u0245\3\2\2\2\u0091\u024e\3\2\2\2")
        buf.write("\u0093\u028f\3\2\2\2\u0095\u0294\3\2\2\2\u0097\u0296\3")
        buf.write("\2\2\2\u0099\u02a1\3\2\2\2\u009b\u02a7\3\2\2\2\u009d\u02b9")
        buf.write("\3\2\2\2\u009f\u02c0\3\2\2\2\u00a1\u02c7\3\2\2\2\u00a3")
        buf.write("\u02c9\3\2\2\2\u00a5\u02cb\3\2\2\2\u00a7\u02d7\3\2\2\2")
        buf.write("\u00a9\u02e1\3\2\2\2\u00ab\u00ac\7k\2\2\u00ac\u00ad\7")
        buf.write("p\2\2\u00ad\u00ae\7v\2\2\u00ae\u00af\7a\2\2\u00af\u00b0")
        buf.write("\7q\2\2\u00b0\u00b1\7h\2\2\u00b1\u00b2\7a\2\2\u00b2\u00b3")
        buf.write("\7h\2\2\u00b3\u00b4\7n\2\2\u00b4\u00b5\7q\2\2\u00b5\u00b6")
        buf.write("\7c\2\2\u00b6\u0118\7v\2\2\u00b7\u00b8\7h\2\2\u00b8\u00b9")
        buf.write("\7n\2\2\u00b9\u00ba\7q\2\2\u00ba\u00bb\7c\2\2\u00bb\u00bc")
        buf.write("\7v\2\2\u00bc\u00bd\7a\2\2\u00bd\u00be\7q\2\2\u00be\u00bf")
        buf.write("\7h\2\2\u00bf\u00c0\7a\2\2\u00c0\u00c1\7k\2\2\u00c1\u00c2")
        buf.write("\7p\2\2\u00c2\u0118\7v\2\2\u00c3\u00c4\7k\2\2\u00c4\u00c5")
        buf.write("\7p\2\2\u00c5\u00c6\7v\2\2\u00c6\u00c7\7a\2\2\u00c7\u00c8")
        buf.write("\7q\2\2\u00c8\u00c9\7h\2\2\u00c9\u00ca\7a\2\2\u00ca\u00cb")
        buf.write("\7u\2\2\u00cb\u00cc\7v\2\2\u00cc\u00cd\7t\2\2\u00cd\u00ce")
        buf.write("\7k\2\2\u00ce\u00cf\7p\2\2\u00cf\u0118\7i\2\2\u00d0\u00d1")
        buf.write("\7u\2\2\u00d1\u00d2\7v\2\2\u00d2\u00d3\7t\2\2\u00d3\u00d4")
        buf.write("\7k\2\2\u00d4\u00d5\7p\2\2\u00d5\u00d6\7i\2\2\u00d6\u00d7")
        buf.write("\7a\2\2\u00d7\u00d8\7q\2\2\u00d8\u00d9\7h\2\2\u00d9\u00da")
        buf.write("\7a\2\2\u00da\u00db\7k\2\2\u00db\u00dc\7p\2\2\u00dc\u0118")
        buf.write("\7v\2\2\u00dd\u00de\7h\2\2\u00de\u00df\7n\2\2\u00df\u00e0")
        buf.write("\7q\2\2\u00e0\u00e1\7c\2\2\u00e1\u00e2\7v\2\2\u00e2\u00e3")
        buf.write("\7a\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5\7h\2\2\u00e5\u00e6")
        buf.write("\7a\2\2\u00e6\u00e7\7u\2\2\u00e7\u00e8\7v\2\2\u00e8\u00e9")
        buf.write("\7t\2\2\u00e9\u00ea\7k\2\2\u00ea\u00eb\7p\2\2\u00eb\u0118")
        buf.write("\7i\2\2\u00ec\u00ed\7u\2\2\u00ed\u00ee\7v\2\2\u00ee\u00ef")
        buf.write("\7t\2\2\u00ef\u00f0\7k\2\2\u00f0\u00f1\7p\2\2\u00f1\u00f2")
        buf.write("\7i\2\2\u00f2\u00f3\7a\2\2\u00f3\u00f4\7q\2\2\u00f4\u00f5")
        buf.write("\7h\2\2\u00f5\u00f6\7a\2\2\u00f6\u00f7\7h\2\2\u00f7\u00f8")
        buf.write("\7n\2\2\u00f8\u00f9\7q\2\2\u00f9\u00fa\7c\2\2\u00fa\u0118")
        buf.write("\7v\2\2\u00fb\u00fc\7d\2\2\u00fc\u00fd\7q\2\2\u00fd\u00fe")
        buf.write("\7q\2\2\u00fe\u00ff\7n\2\2\u00ff\u0100\7a\2\2\u0100\u0101")
        buf.write("\7q\2\2\u0101\u0102\7h\2\2\u0102\u0103\7a\2\2\u0103\u0104")
        buf.write("\7u\2\2\u0104\u0105\7v\2\2\u0105\u0106\7t\2\2\u0106\u0107")
        buf.write("\7k\2\2\u0107\u0108\7p\2\2\u0108\u0118\7i\2\2\u0109\u010a")
        buf.write("\7u\2\2\u010a\u010b\7v\2\2\u010b\u010c\7t\2\2\u010c\u010d")
        buf.write("\7k\2\2\u010d\u010e\7p\2\2\u010e\u010f\7i\2\2\u010f\u0110")
        buf.write("\7a\2\2\u0110\u0111\7q\2\2\u0111\u0112\7h\2\2\u0112\u0113")
        buf.write("\7a\2\2\u0113\u0114\7d\2\2\u0114\u0115\7q\2\2\u0115\u0116")
        buf.write("\7q\2\2\u0116\u0118\7n\2\2\u0117\u00ab\3\2\2\2\u0117\u00b7")
        buf.write("\3\2\2\2\u0117\u00c3\3\2\2\2\u0117\u00d0\3\2\2\2\u0117")
        buf.write("\u00dd\3\2\2\2\u0117\u00ec\3\2\2\2\u0117\u00fb\3\2\2\2")
        buf.write("\u0117\u0109\3\2\2\2\u0118\4\3\2\2\2\u0119\u011a\7*\2")
        buf.write("\2\u011a\6\3\2\2\2\u011b\u011c\7+\2\2\u011c\b\3\2\2\2")
        buf.write("\u011d\u011e\7]\2\2\u011e\n\3\2\2\2\u011f\u0120\7_\2\2")
        buf.write("\u0120\f\3\2\2\2\u0121\u0122\7<\2\2\u0122\16\3\2\2\2\u0123")
        buf.write("\u0124\7\60\2\2\u0124\20\3\2\2\2\u0125\u0126\7.\2\2\u0126")
        buf.write("\22\3\2\2\2\u0127\u0128\7=\2\2\u0128\24\3\2\2\2\u0129")
        buf.write("\u012a\7}\2\2\u012a\26\3\2\2\2\u012b\u012c\7\177\2\2\u012c")
        buf.write("\30\3\2\2\2\u012d\u012e\7-\2\2\u012e\32\3\2\2\2\u012f")
        buf.write("\u0130\7-\2\2\u0130\u0131\7\60\2\2\u0131\34\3\2\2\2\u0132")
        buf.write("\u0133\7/\2\2\u0133\36\3\2\2\2\u0134\u0135\7/\2\2\u0135")
        buf.write("\u0136\7\60\2\2\u0136 \3\2\2\2\u0137\u0138\7,\2\2\u0138")
        buf.write("\"\3\2\2\2\u0139\u013a\7,\2\2\u013a\u013b\7\60\2\2\u013b")
        buf.write("$\3\2\2\2\u013c\u013d\7^\2\2\u013d&\3\2\2\2\u013e\u013f")
        buf.write("\7^\2\2\u013f\u0140\7\60\2\2\u0140(\3\2\2\2\u0141\u0142")
        buf.write("\7\'\2\2\u0142*\3\2\2\2\u0143\u0144\7#\2\2\u0144,\3\2")
        buf.write("\2\2\u0145\u0146\7(\2\2\u0146\u0147\7(\2\2\u0147.\3\2")
        buf.write("\2\2\u0148\u0149\7~\2\2\u0149\u014a\7~\2\2\u014a\60\3")
        buf.write("\2\2\2\u014b\u014c\7?\2\2\u014c\u014d\7?\2\2\u014d\62")
        buf.write("\3\2\2\2\u014e\u014f\7#\2\2\u014f\u0150\7?\2\2\u0150\64")
        buf.write("\3\2\2\2\u0151\u0152\7>\2\2\u0152\66\3\2\2\2\u0153\u0154")
        buf.write("\7@\2\2\u01548\3\2\2\2\u0155\u0156\7>\2\2\u0156\u0157")
        buf.write("\7?\2\2\u0157:\3\2\2\2\u0158\u0159\7@\2\2\u0159\u015a")
        buf.write("\7?\2\2\u015a<\3\2\2\2\u015b\u015c\7?\2\2\u015c\u015d")
        buf.write("\7\61\2\2\u015d\u015e\7?\2\2\u015e>\3\2\2\2\u015f\u0160")
        buf.write("\7>\2\2\u0160\u0161\7\60\2\2\u0161@\3\2\2\2\u0162\u0163")
        buf.write("\7@\2\2\u0163\u0164\7\60\2\2\u0164B\3\2\2\2\u0165\u0166")
        buf.write("\7>\2\2\u0166\u0167\7?\2\2\u0167\u0168\7\60\2\2\u0168")
        buf.write("D\3\2\2\2\u0169\u016a\7@\2\2\u016a\u016b\7?\2\2\u016b")
        buf.write("\u016c\7\60\2\2\u016cF\3\2\2\2\u016d\u016e\7?\2\2\u016e")
        buf.write("H\3\2\2\2\u016f\u0170\7D\2\2\u0170\u0171\7q\2\2\u0171")
        buf.write("\u0172\7f\2\2\u0172\u0173\7{\2\2\u0173J\3\2\2\2\u0174")
        buf.write("\u0175\7D\2\2\u0175\u0176\7t\2\2\u0176\u0177\7g\2\2\u0177")
        buf.write("\u0178\7c\2\2\u0178\u0179\7m\2\2\u0179L\3\2\2\2\u017a")
        buf.write("\u017b\7E\2\2\u017b\u017c\7q\2\2\u017c\u017d\7p\2\2\u017d")
        buf.write("\u017e\7v\2\2\u017e\u017f\7k\2\2\u017f\u0180\7p\2\2\u0180")
        buf.write("\u0181\7w\2\2\u0181\u0182\7g\2\2\u0182N\3\2\2\2\u0183")
        buf.write("\u0184\7F\2\2\u0184\u0185\7q\2\2\u0185P\3\2\2\2\u0186")
        buf.write("\u0187\7G\2\2\u0187\u0188\7n\2\2\u0188\u0189\7u\2\2\u0189")
        buf.write("\u018a\7g\2\2\u018aR\3\2\2\2\u018b\u018c\7G\2\2\u018c")
        buf.write("\u018d\7n\2\2\u018d\u018e\7u\2\2\u018e\u018f\7g\2\2\u018f")
        buf.write("\u0190\7K\2\2\u0190\u0191\7h\2\2\u0191T\3\2\2\2\u0192")
        buf.write("\u0193\7G\2\2\u0193\u0194\7p\2\2\u0194\u0195\7f\2\2\u0195")
        buf.write("\u0196\7D\2\2\u0196\u0197\7q\2\2\u0197\u0198\7f\2\2\u0198")
        buf.write("\u0199\7{\2\2\u0199V\3\2\2\2\u019a\u019b\7G\2\2\u019b")
        buf.write("\u019c\7p\2\2\u019c\u019d\7f\2\2\u019d\u019e\7K\2\2\u019e")
        buf.write("\u019f\7h\2\2\u019fX\3\2\2\2\u01a0\u01a1\7G\2\2\u01a1")
        buf.write("\u01a2\7p\2\2\u01a2\u01a3\7f\2\2\u01a3\u01a4\7H\2\2\u01a4")
        buf.write("\u01a5\7q\2\2\u01a5\u01a6\7t\2\2\u01a6Z\3\2\2\2\u01a7")
        buf.write("\u01a8\7G\2\2\u01a8\u01a9\7p\2\2\u01a9\u01aa\7f\2\2\u01aa")
        buf.write("\u01ab\7Y\2\2\u01ab\u01ac\7j\2\2\u01ac\u01ad\7k\2\2\u01ad")
        buf.write("\u01ae\7n\2\2\u01ae\u01af\7g\2\2\u01af\\\3\2\2\2\u01b0")
        buf.write("\u01b1\7H\2\2\u01b1\u01b2\7q\2\2\u01b2\u01b3\7t\2\2\u01b3")
        buf.write("^\3\2\2\2\u01b4\u01b5\7H\2\2\u01b5\u01b6\7w\2\2\u01b6")
        buf.write("\u01b7\7p\2\2\u01b7\u01b8\7e\2\2\u01b8\u01b9\7v\2\2\u01b9")
        buf.write("\u01ba\7k\2\2\u01ba\u01bb\7q\2\2\u01bb\u01bc\7p\2\2\u01bc")
        buf.write("`\3\2\2\2\u01bd\u01be\7K\2\2\u01be\u01bf\7h\2\2\u01bf")
        buf.write("b\3\2\2\2\u01c0\u01c1\7R\2\2\u01c1\u01c2\7c\2\2\u01c2")
        buf.write("\u01c3\7t\2\2\u01c3\u01c4\7c\2\2\u01c4\u01c5\7o\2\2\u01c5")
        buf.write("\u01c6\7g\2\2\u01c6\u01c7\7v\2\2\u01c7\u01c8\7g\2\2\u01c8")
        buf.write("\u01c9\7t\2\2\u01c9d\3\2\2\2\u01ca\u01cb\7T\2\2\u01cb")
        buf.write("\u01cc\7g\2\2\u01cc\u01cd\7v\2\2\u01cd\u01ce\7w\2\2\u01ce")
        buf.write("\u01cf\7t\2\2\u01cf\u01d0\7p\2\2\u01d0f\3\2\2\2\u01d1")
        buf.write("\u01d2\7V\2\2\u01d2\u01d3\7j\2\2\u01d3\u01d4\7g\2\2\u01d4")
        buf.write("\u01d5\7p\2\2\u01d5h\3\2\2\2\u01d6\u01d7\7X\2\2\u01d7")
        buf.write("\u01d8\7c\2\2\u01d8\u01d9\7t\2\2\u01d9j\3\2\2\2\u01da")
        buf.write("\u01db\7Y\2\2\u01db\u01dc\7j\2\2\u01dc\u01dd\7k\2\2\u01dd")
        buf.write("\u01de\7n\2\2\u01de\u01df\7g\2\2\u01dfl\3\2\2\2\u01e0")
        buf.write("\u01e1\7V\2\2\u01e1\u01e2\7t\2\2\u01e2\u01e3\7w\2\2\u01e3")
        buf.write("\u01e4\7g\2\2\u01e4n\3\2\2\2\u01e5\u01e6\7H\2\2\u01e6")
        buf.write("\u01e7\7c\2\2\u01e7\u01e8\7n\2\2\u01e8\u01e9\7u\2\2\u01e9")
        buf.write("\u01ea\7g\2\2\u01eap\3\2\2\2\u01eb\u01ec\7G\2\2\u01ec")
        buf.write("\u01ed\7p\2\2\u01ed\u01ee\7f\2\2\u01ee\u01ef\7F\2\2\u01ef")
        buf.write("\u01f0\7q\2\2\u01f0r\3\2\2\2\u01f1\u01f2\t\2\2\2\u01f2")
        buf.write("t\3\2\2\2\u01f3\u01f4\t\3\2\2\u01f4v\3\2\2\2\u01f5\u01f6")
        buf.write("\t\4\2\2\u01f6x\3\2\2\2\u01f7\u01f8\7a\2\2\u01f8z\3\2")
        buf.write("\2\2\u01f9\u01fa\7)\2\2\u01fa|\3\2\2\2\u01fb\u01fc\7$")
        buf.write("\2\2\u01fc~\3\2\2\2\u01fd\u01fe\7\62\2\2\u01fe\u01ff\t")
        buf.write("\5\2\2\u01ff\u0204\t\6\2\2\u0200\u0203\5w<\2\u0201\u0203")
        buf.write("\t\7\2\2\u0202\u0200\3\2\2\2\u0202\u0201\3\2\2\2\u0203")
        buf.write("\u0206\3\2\2\2\u0204\u0202\3\2\2\2\u0204\u0205\3\2\2\2")
        buf.write("\u0205\u0080\3\2\2\2\u0206\u0204\3\2\2\2\u0207\u020b\t")
        buf.write("\b\2\2\u0208\u020a\5w<\2\u0209\u0208\3\2\2\2\u020a\u020d")
        buf.write("\3\2\2\2\u020b\u0209\3\2\2\2\u020b\u020c\3\2\2\2\u020c")
        buf.write("\u0210\3\2\2\2\u020d\u020b\3\2\2\2\u020e\u0210\7\62\2")
        buf.write("\2\u020f\u0207\3\2\2\2\u020f\u020e\3\2\2\2\u0210\u0082")
        buf.write("\3\2\2\2\u0211\u0212\7\62\2\2\u0212\u0213\t\t\2\2\u0213")
        buf.write("\u0217\t\n\2\2\u0214\u0216\t\13\2\2\u0215\u0214\3\2\2")
        buf.write("\2\u0216\u0219\3\2\2\2\u0217\u0215\3\2\2\2\u0217\u0218")
        buf.write("\3\2\2\2\u0218\u0084\3\2\2\2\u0219\u0217\3\2\2\2\u021a")
        buf.write("\u021e\5\u0081A\2\u021b\u021e\5\177@\2\u021c\u021e\5\u0083")
        buf.write("B\2\u021d\u021a\3\2\2\2\u021d\u021b\3\2\2\2\u021d\u021c")
        buf.write("\3\2\2\2\u021e\u0086\3\2\2\2\u021f\u0222\t\f\2\2\u0220")
        buf.write("\u0223\5\31\r\2\u0221\u0223\5\35\17\2\u0222\u0220\3\2")
        buf.write("\2\2\u0222\u0221\3\2\2\2\u0222\u0223\3\2\2\2\u0223\u0225")
        buf.write("\3\2\2\2\u0224\u0226\5w<\2\u0225\u0224\3\2\2\2\u0226\u0227")
        buf.write("\3\2\2\2\u0227\u0225\3\2\2\2\u0227\u0228\3\2\2\2\u0228")
        buf.write("\u0088\3\2\2\2\u0229\u022d\5\17\b\2\u022a\u022c\5w<\2")
        buf.write("\u022b\u022a\3\2\2\2\u022c\u022f\3\2\2\2\u022d\u022b\3")
        buf.write("\2\2\2\u022d\u022e\3\2\2\2\u022e\u008a\3\2\2\2\u022f\u022d")
        buf.write("\3\2\2\2\u0230\u0234\t\b\2\2\u0231\u0233\5w<\2\u0232\u0231")
        buf.write("\3\2\2\2\u0233\u0236\3\2\2\2\u0234\u0232\3\2\2\2\u0234")
        buf.write("\u0235\3\2\2\2\u0235\u0239\3\2\2\2\u0236\u0234\3\2\2\2")
        buf.write("\u0237\u0239\7\62\2\2\u0238\u0230\3\2\2\2\u0238\u0237")
        buf.write("\3\2\2\2\u0239\u0240\3\2\2\2\u023a\u0241\5\u0089E\2\u023b")
        buf.write("\u0241\5\u0087D\2\u023c\u023d\5\u0089E\2\u023d\u023e\5")
        buf.write("\u0087D\2\u023e\u0241\3\2\2\2\u023f\u0241\5\u0089E\2\u0240")
        buf.write("\u023a\3\2\2\2\u0240\u023b\3\2\2\2\u0240\u023c\3\2\2\2")
        buf.write("\u0240\u023f\3\2\2\2\u0240\u0241\3\2\2\2\u0241\u008c\3")
        buf.write("\2\2\2\u0242\u0243\7^\2\2\u0243\u0244\t\r\2\2\u0244\u008e")
        buf.write("\3\2\2\2\u0245\u0249\5}?\2\u0246\u0248\5\u009dO\2\u0247")
        buf.write("\u0246\3\2\2\2\u0248\u024b\3\2\2\2\u0249\u024a\3\2\2\2")
        buf.write("\u0249\u0247\3\2\2\2\u024a\u024c\3\2\2\2\u024b\u0249\3")
        buf.write("\2\2\2\u024c\u024d\5}?\2\u024d\u0090\3\2\2\2\u024e\u024f")
        buf.write("\5\25\13\2\u024f\u0287\5\u0093J\2\u0250\u0258\5\u0085")
        buf.write("C\2\u0251\u0252\5\u0093J\2\u0252\u0253\5\21\t\2\u0253")
        buf.write("\u0254\5\u0093J\2\u0254\u0255\5\u0085C\2\u0255\u0257\3")
        buf.write("\2\2\2\u0256\u0251\3\2\2\2\u0257\u025a\3\2\2\2\u0258\u0256")
        buf.write("\3\2\2\2\u0258\u0259\3\2\2\2\u0259\u0288\3\2\2\2\u025a")
        buf.write("\u0258\3\2\2\2\u025b\u0263\5\u008bF\2\u025c\u025d\5\u0093")
        buf.write("J\2\u025d\u025e\5\21\t\2\u025e\u025f\5\u0093J\2\u025f")
        buf.write("\u0260\5\u008bF\2\u0260\u0262\3\2\2\2\u0261\u025c\3\2")
        buf.write("\2\2\u0262\u0265\3\2\2\2\u0263\u0261\3\2\2\2\u0263\u0264")
        buf.write("\3\2\2\2\u0264\u0288\3\2\2\2\u0265\u0263\3\2\2\2\u0266")
        buf.write("\u026e\5\u008fH\2\u0267\u0268\5\u0093J\2\u0268\u0269\5")
        buf.write("\21\t\2\u0269\u026a\5\u0093J\2\u026a\u026b\5\u008fH\2")
        buf.write("\u026b\u026d\3\2\2\2\u026c\u0267\3\2\2\2\u026d\u0270\3")
        buf.write("\2\2\2\u026e\u026c\3\2\2\2\u026e\u026f\3\2\2\2\u026f\u0288")
        buf.write("\3\2\2\2\u0270\u026e\3\2\2\2\u0271\u0279\5\u0091I\2\u0272")
        buf.write("\u0273\5\u0093J\2\u0273\u0274\5\21\t\2\u0274\u0275\5\u0093")
        buf.write("J\2\u0275\u0276\5\u0091I\2\u0276\u0278\3\2\2\2\u0277\u0272")
        buf.write("\3\2\2\2\u0278\u027b\3\2\2\2\u0279\u0277\3\2\2\2\u0279")
        buf.write("\u027a\3\2\2\2\u027a\u0288\3\2\2\2\u027b\u0279\3\2\2\2")
        buf.write("\u027c\u0284\5\u0095K\2\u027d\u027e\5\u0093J\2\u027e\u027f")
        buf.write("\5\21\t\2\u027f\u0280\5\u0093J\2\u0280\u0281\5\u0095K")
        buf.write("\2\u0281\u0283\3\2\2\2\u0282\u027d\3\2\2\2\u0283\u0286")
        buf.write("\3\2\2\2\u0284\u0282\3\2\2\2\u0284\u0285\3\2\2\2\u0285")
        buf.write("\u0288\3\2\2\2\u0286\u0284\3\2\2\2\u0287\u0250\3\2\2\2")
        buf.write("\u0287\u025b\3\2\2\2\u0287\u0266\3\2\2\2\u0287\u0271\3")
        buf.write("\2\2\2\u0287\u027c\3\2\2\2\u0288\u0289\3\2\2\2\u0289\u028a")
        buf.write("\5\u0093J\2\u028a\u028b\5\27\f\2\u028b\u0092\3\2\2\2\u028c")
        buf.write("\u028e\t\16\2\2\u028d\u028c\3\2\2\2\u028e\u0291\3\2\2")
        buf.write("\2\u028f\u028d\3\2\2\2\u028f\u0290\3\2\2\2\u0290\u0094")
        buf.write("\3\2\2\2\u0291\u028f\3\2\2\2\u0292\u0295\5m\67\2\u0293")
        buf.write("\u0295\5o8\2\u0294\u0292\3\2\2\2\u0294\u0293\3\2\2\2\u0295")
        buf.write("\u0096\3\2\2\2\u0296\u029d\5s:\2\u0297\u029c\5s:\2\u0298")
        buf.write("\u029c\5u;\2\u0299\u029c\5y=\2\u029a\u029c\5w<\2\u029b")
        buf.write("\u0297\3\2\2\2\u029b\u0298\3\2\2\2\u029b\u0299\3\2\2\2")
        buf.write("\u029b\u029a\3\2\2\2\u029c\u029f\3\2\2\2\u029d\u029b\3")
        buf.write("\2\2\2\u029d\u029e\3\2\2\2\u029e\u0098\3\2\2\2\u029f\u029d")
        buf.write("\3\2\2\2\u02a0\u02a2\t\17\2\2\u02a1\u02a0\3\2\2\2\u02a2")
        buf.write("\u02a3\3\2\2\2\u02a3\u02a1\3\2\2\2\u02a3\u02a4\3\2\2\2")
        buf.write("\u02a4\u02a5\3\2\2\2\u02a5\u02a6\bM\2\2\u02a6\u009a\3")
        buf.write("\2\2\2\u02a7\u02a8\7,\2\2\u02a8\u02a9\7,\2\2\u02a9\u02ad")
        buf.write("\3\2\2\2\u02aa\u02ac\5\u00a1Q\2\u02ab\u02aa\3\2\2\2\u02ac")
        buf.write("\u02af\3\2\2\2\u02ad\u02ae\3\2\2\2\u02ad\u02ab\3\2\2\2")
        buf.write("\u02ae\u02b0\3\2\2\2\u02af\u02ad\3\2\2\2\u02b0\u02b1\7")
        buf.write(",\2\2\u02b1\u02b2\7,\2\2\u02b2\u02b3\3\2\2\2\u02b3\u02b4")
        buf.write("\bN\2\2\u02b4\u009c\3\2\2\2\u02b5\u02ba\n\20\2\2\u02b6")
        buf.write("\u02ba\5\u008dG\2\u02b7\u02b8\7)\2\2\u02b8\u02ba\7$\2")
        buf.write("\2\u02b9\u02b5\3\2\2\2\u02b9\u02b6\3\2\2\2\u02b9\u02b7")
        buf.write("\3\2\2\2\u02ba\u009e\3\2\2\2\u02bb\u02bc\7^\2\2\u02bc")
        buf.write("\u02c1\n\r\2\2\u02bd\u02c1\7^\2\2\u02be\u02bf\t\21\2\2")
        buf.write("\u02bf\u02c1\n\22\2\2\u02c0\u02bb\3\2\2\2\u02c0\u02bd")
        buf.write("\3\2\2\2\u02c0\u02be\3\2\2\2\u02c1\u00a0\3\2\2\2\u02c2")
        buf.write("\u02c3\n\23\2\2\u02c3\u02c8\n\23\2\2\u02c4\u02c5\n\23")
        buf.write("\2\2\u02c5\u02c8\t\23\2\2\u02c6\u02c8\n\23\2\2\u02c7\u02c2")
        buf.write("\3\2\2\2\u02c7\u02c4\3\2\2\2\u02c7\u02c6\3\2\2\2\u02c8")
        buf.write("\u00a2\3\2\2\2\u02c9\u02ca\13\2\2\2\u02ca\u00a4\3\2\2")
        buf.write("\2\u02cb\u02cf\7$\2\2\u02cc\u02ce\5\u009dO\2\u02cd\u02cc")
        buf.write("\3\2\2\2\u02ce\u02d1\3\2\2\2\u02cf\u02cd\3\2\2\2\u02cf")
        buf.write("\u02d0\3\2\2\2\u02d0\u02d3\3\2\2\2\u02d1\u02cf\3\2\2\2")
        buf.write("\u02d2\u02d4\t\24\2\2\u02d3\u02d2\3\2\2\2\u02d4\u02d5")
        buf.write("\3\2\2\2\u02d5\u02d6\bS\3\2\u02d6\u00a6\3\2\2\2\u02d7")
        buf.write("\u02db\7$\2\2\u02d8\u02da\5\u009dO\2\u02d9\u02d8\3\2\2")
        buf.write("\2\u02da\u02dd\3\2\2\2\u02db\u02d9\3\2\2\2\u02db\u02dc")
        buf.write("\3\2\2\2\u02dc\u02de\3\2\2\2\u02dd\u02db\3\2\2\2\u02de")
        buf.write("\u02df\5\u009fP\2\u02df\u02e0\bT\4\2\u02e0\u00a8\3\2\2")
        buf.write("\2\u02e1\u02e2\7,\2\2\u02e2\u02e3\7,\2\2\u02e3\u02e7\3")
        buf.write("\2\2\2\u02e4\u02e6\5\u00a1Q\2\u02e5\u02e4\3\2\2\2\u02e6")
        buf.write("\u02e9\3\2\2\2\u02e7\u02e5\3\2\2\2\u02e7\u02e8\3\2\2\2")
        buf.write("\u02e8\u02ea\3\2\2\2\u02e9\u02e7\3\2\2\2\u02ea\u02eb\7")
        buf.write("\2\2\3\u02eb\u02ec\bU\5\2\u02ec\u00aa\3\2\2\2$\2\u0117")
        buf.write("\u0202\u0204\u020b\u020f\u0217\u021d\u0222\u0227\u022d")
        buf.write("\u0234\u0238\u0240\u0249\u0258\u0263\u026e\u0279\u0284")
        buf.write("\u0287\u028f\u0294\u029b\u029d\u02a3\u02ad\u02b9\u02c0")
        buf.write("\u02c7\u02cf\u02d3\u02db\u02e7\6\b\2\2\3S\2\3T\3\3U\4")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TYPE_COERCIONS = 1
    LP = 2
    RP = 3
    LB = 4
    RB = 5
    COLON = 6
    DOT = 7
    COMMA = 8
    SEMI = 9
    ADDOP = 10
    ADDF = 11
    SUBOP = 12
    SUBF = 13
    MULOP = 14
    MULF = 15
    DIVOP = 16
    DIVF = 17
    MODOP = 18
    NOT = 19
    AND = 20
    OR = 21
    EQ = 22
    NEQ = 23
    LT = 24
    GT = 25
    LTE = 26
    GTE = 27
    NEQF = 28
    LTF = 29
    GTF = 30
    LTEF = 31
    GTEF = 32
    ASSIG = 33
    BODY = 34
    BREAK = 35
    CONTINUE = 36
    DO = 37
    ELSE = 38
    ELSEIF = 39
    ENDBODY = 40
    ENDIF = 41
    ENDFOR = 42
    ENDWHILE = 43
    FOR = 44
    FUNCTION = 45
    IF = 46
    PARAMETER = 47
    RETURN = 48
    THEN = 49
    VAR = 50
    WHILE = 51
    ENDDO = 52
    INTERGER = 53
    FLOAT = 54
    STRING = 55
    ARRAY = 56
    BOOLEAN = 57
    ID = 58
    WS = 59
    COMMENT = 60
    ERROR_CHAR = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63
    UNTERMINATED_COMMENT = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'['", "']'", "':'", "'.'", "','", "';'", "'+'", 
            "'+.'", "'-'", "'-.'", "'*'", "'*.'", "'\\'", "'\\.'", "'%'", 
            "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", 
            "'>='", "'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'", "'='", "'Body'", 
            "'Break'", "'Continue'", "'Do'", "'Else'", "'ElseIf'", "'EndBody'", 
            "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
            "'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
            "'EndDo'" ]

    symbolicNames = [ "<INVALID>",
            "TYPE_COERCIONS", "LP", "RP", "LB", "RB", "COLON", "DOT", "COMMA", 
            "SEMI", "ADDOP", "ADDF", "SUBOP", "SUBF", "MULOP", "MULF", "DIVOP", 
            "DIVF", "MODOP", "NOT", "AND", "OR", "EQ", "NEQ", "LT", "GT", 
            "LTE", "GTE", "NEQF", "LTF", "GTF", "LTEF", "GTEF", "ASSIG", 
            "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", 
            "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
            "RETURN", "THEN", "VAR", "WHILE", "ENDDO", "INTERGER", "FLOAT", 
            "STRING", "ARRAY", "BOOLEAN", "ID", "WS", "COMMENT", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "TYPE_COERCIONS", "LP", "RP", "LB", "RB", "COLON", "DOT", 
                  "COMMA", "SEMI", "LCB", "RCB", "ADDOP", "ADDF", "SUBOP", 
                  "SUBF", "MULOP", "MULF", "DIVOP", "DIVF", "MODOP", "NOT", 
                  "AND", "OR", "EQ", "NEQ", "LT", "GT", "LTE", "GTE", "NEQF", 
                  "LTF", "GTF", "LTEF", "GTEF", "ASSIG", "BODY", "BREAK", 
                  "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", 
                  "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
                  "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", 
                  "LOWCASE", "UPPERCASE", "NUMBER", "UNDERCORE", "SINGLE_QUOTE", 
                  "DOUBLE_QUOTE", "HEXA", "DECIMAL", "OCTAL", "INTERGER", 
                  "EXPONENT", "DECIMAL_PART", "FLOAT", "ESCAPE_SEQUENCE", 
                  "STRING", "ARRAY", "SPACE", "BOOLEAN", "ID", "WS", "COMMENT", 
                  "CHAR", "ESCAPE_ILLEGAL", "COMMENT_BODY", "ERROR_CHAR", 
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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[81] = self.UNCLOSE_STRING_action 
            actions[82] = self.ILLEGAL_ESCAPE_action 
            actions[83] = self.UNTERMINATED_COMMENT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            		y = str(self.text)
            		impossible = ['\n', '\r']
            		if y[-1] in impossible:
            			raise UncloseString(y[1:-1])
            		else:
            			raise UncloseString(y[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                    raise UnterminatedComment() 
                
     


