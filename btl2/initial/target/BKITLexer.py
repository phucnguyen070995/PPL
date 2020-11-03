# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u022c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\3\2\3\2\3\3\3\3")
        buf.write("\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3")
        buf.write("\n\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3$\3$\3$\3")
        buf.write("$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3\'")
        buf.write("\3\'\3\'\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*")
        buf.write("\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3")
        buf.write(",\3-\3-\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3/\3/\3/\3/\3")
        buf.write("/\3/\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\38\38\38\38\38\38\39\39\3:\3")
        buf.write(":\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3?\3?\3?\7?\u018f\n?\f")
        buf.write("?\16?\u0192\13?\3@\3@\7@\u0196\n@\f@\16@\u0199\13@\3@")
        buf.write("\5@\u019c\n@\3A\3A\3A\3A\7A\u01a2\nA\fA\16A\u01a5\13A")
        buf.write("\3B\3B\3B\5B\u01aa\nB\3C\3C\3C\5C\u01af\nC\3C\6C\u01b2")
        buf.write("\nC\rC\16C\u01b3\3D\3D\7D\u01b8\nD\fD\16D\u01bb\13D\3")
        buf.write("E\3E\3E\3E\3E\3E\5E\u01c3\nE\3F\3F\3F\3G\3G\7G\u01ca\n")
        buf.write("G\fG\16G\u01cd\13G\3G\3G\3G\3H\3H\5H\u01d4\nH\3I\3I\3")
        buf.write("I\3I\3I\7I\u01db\nI\fI\16I\u01de\13I\3J\6J\u01e1\nJ\r")
        buf.write("J\16J\u01e2\3J\3J\3K\3K\3K\3K\7K\u01eb\nK\fK\16K\u01ee")
        buf.write("\13K\3K\3K\3K\3K\3K\3L\3L\3L\3L\5L\u01f9\nL\3M\3M\3M\3")
        buf.write("M\3M\5M\u0200\nM\3N\3N\3N\3N\3N\5N\u0207\nN\3O\3O\3P\3")
        buf.write("P\7P\u020d\nP\fP\16P\u0210\13P\3P\5P\u0213\nP\3P\3P\3")
        buf.write("Q\3Q\7Q\u0219\nQ\fQ\16Q\u021c\13Q\3Q\3Q\3Q\3R\3R\3R\3")
        buf.write("R\7R\u0225\nR\fR\16R\u0228\13R\3R\3R\3R\4\u01cb\u01ec")
        buf.write("\2S\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\2m\2o\67")
        buf.write("q\2s\2u\2w\2y\2{\2}\2\177\2\u0081\2\u00838\u0085\2\u0087")
        buf.write("\2\u00899\u008b\2\u008d:\u008f;\u0091<\u0093=\u0095>\u0097")
        buf.write("\2\u0099\2\u009b\2\u009d?\u009f@\u00a1A\u00a3B\3\2\24")
        buf.write("\3\2c|\3\2C\\\3\2\62;\4\2ZZzz\4\2\63;CH\3\2CH\3\2\63;")
        buf.write("\4\2QQqq\3\2\639\3\2\629\4\2GGgg\t\2))^^ddhhppttvv\5\2")
        buf.write("\13\f\17\17\"\"\6\2\f\f$$))^^\3\2))\3\2$$\3\2,,\4\3\f")
        buf.write("\f\17\17\2\u0238\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
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
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2o\3\2\2\2\2\u0083\3")
        buf.write("\2\2\2\2\u0089\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2")
        buf.write("\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u009d")
        buf.write("\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2")
        buf.write("\2\3\u00a5\3\2\2\2\5\u00a7\3\2\2\2\7\u00a9\3\2\2\2\t\u00ab")
        buf.write("\3\2\2\2\13\u00ad\3\2\2\2\r\u00af\3\2\2\2\17\u00b1\3\2")
        buf.write("\2\2\21\u00b3\3\2\2\2\23\u00b5\3\2\2\2\25\u00b7\3\2\2")
        buf.write("\2\27\u00b9\3\2\2\2\31\u00bb\3\2\2\2\33\u00be\3\2\2\2")
        buf.write("\35\u00c0\3\2\2\2\37\u00c3\3\2\2\2!\u00c5\3\2\2\2#\u00c8")
        buf.write("\3\2\2\2%\u00ca\3\2\2\2\'\u00cd\3\2\2\2)\u00cf\3\2\2\2")
        buf.write("+\u00d1\3\2\2\2-\u00d4\3\2\2\2/\u00d7\3\2\2\2\61\u00da")
        buf.write("\3\2\2\2\63\u00dd\3\2\2\2\65\u00df\3\2\2\2\67\u00e1\3")
        buf.write("\2\2\29\u00e4\3\2\2\2;\u00e7\3\2\2\2=\u00eb\3\2\2\2?\u00ee")
        buf.write("\3\2\2\2A\u00f1\3\2\2\2C\u00f5\3\2\2\2E\u00f9\3\2\2\2")
        buf.write("G\u00fb\3\2\2\2I\u0100\3\2\2\2K\u0106\3\2\2\2M\u010f\3")
        buf.write("\2\2\2O\u0112\3\2\2\2Q\u0117\3\2\2\2S\u011e\3\2\2\2U\u0126")
        buf.write("\3\2\2\2W\u012c\3\2\2\2Y\u0133\3\2\2\2[\u013c\3\2\2\2")
        buf.write("]\u0140\3\2\2\2_\u0149\3\2\2\2a\u014c\3\2\2\2c\u0156\3")
        buf.write("\2\2\2e\u015d\3\2\2\2g\u0162\3\2\2\2i\u0166\3\2\2\2k\u016c")
        buf.write("\3\2\2\2m\u0171\3\2\2\2o\u0177\3\2\2\2q\u017d\3\2\2\2")
        buf.write("s\u017f\3\2\2\2u\u0181\3\2\2\2w\u0183\3\2\2\2y\u0185\3")
        buf.write("\2\2\2{\u0187\3\2\2\2}\u0189\3\2\2\2\177\u019b\3\2\2\2")
        buf.write("\u0081\u019d\3\2\2\2\u0083\u01a9\3\2\2\2\u0085\u01ab\3")
        buf.write("\2\2\2\u0087\u01b5\3\2\2\2\u0089\u01bc\3\2\2\2\u008b\u01c4")
        buf.write("\3\2\2\2\u008d\u01c7\3\2\2\2\u008f\u01d3\3\2\2\2\u0091")
        buf.write("\u01d5\3\2\2\2\u0093\u01e0\3\2\2\2\u0095\u01e6\3\2\2\2")
        buf.write("\u0097\u01f8\3\2\2\2\u0099\u01ff\3\2\2\2\u009b\u0206\3")
        buf.write("\2\2\2\u009d\u0208\3\2\2\2\u009f\u020a\3\2\2\2\u00a1\u0216")
        buf.write("\3\2\2\2\u00a3\u0220\3\2\2\2\u00a5\u00a6\7*\2\2\u00a6")
        buf.write("\4\3\2\2\2\u00a7\u00a8\7+\2\2\u00a8\6\3\2\2\2\u00a9\u00aa")
        buf.write("\7]\2\2\u00aa\b\3\2\2\2\u00ab\u00ac\7_\2\2\u00ac\n\3\2")
        buf.write("\2\2\u00ad\u00ae\7<\2\2\u00ae\f\3\2\2\2\u00af\u00b0\7")
        buf.write("\60\2\2\u00b0\16\3\2\2\2\u00b1\u00b2\7.\2\2\u00b2\20\3")
        buf.write("\2\2\2\u00b3\u00b4\7=\2\2\u00b4\22\3\2\2\2\u00b5\u00b6")
        buf.write("\7}\2\2\u00b6\24\3\2\2\2\u00b7\u00b8\7\177\2\2\u00b8\26")
        buf.write("\3\2\2\2\u00b9\u00ba\7-\2\2\u00ba\30\3\2\2\2\u00bb\u00bc")
        buf.write("\7-\2\2\u00bc\u00bd\7\60\2\2\u00bd\32\3\2\2\2\u00be\u00bf")
        buf.write("\7/\2\2\u00bf\34\3\2\2\2\u00c0\u00c1\7/\2\2\u00c1\u00c2")
        buf.write("\7\60\2\2\u00c2\36\3\2\2\2\u00c3\u00c4\7,\2\2\u00c4 \3")
        buf.write("\2\2\2\u00c5\u00c6\7,\2\2\u00c6\u00c7\7\60\2\2\u00c7\"")
        buf.write("\3\2\2\2\u00c8\u00c9\7^\2\2\u00c9$\3\2\2\2\u00ca\u00cb")
        buf.write("\7^\2\2\u00cb\u00cc\7\60\2\2\u00cc&\3\2\2\2\u00cd\u00ce")
        buf.write("\7\'\2\2\u00ce(\3\2\2\2\u00cf\u00d0\7#\2\2\u00d0*\3\2")
        buf.write("\2\2\u00d1\u00d2\7(\2\2\u00d2\u00d3\7(\2\2\u00d3,\3\2")
        buf.write("\2\2\u00d4\u00d5\7~\2\2\u00d5\u00d6\7~\2\2\u00d6.\3\2")
        buf.write("\2\2\u00d7\u00d8\7?\2\2\u00d8\u00d9\7?\2\2\u00d9\60\3")
        buf.write("\2\2\2\u00da\u00db\7#\2\2\u00db\u00dc\7?\2\2\u00dc\62")
        buf.write("\3\2\2\2\u00dd\u00de\7>\2\2\u00de\64\3\2\2\2\u00df\u00e0")
        buf.write("\7@\2\2\u00e0\66\3\2\2\2\u00e1\u00e2\7>\2\2\u00e2\u00e3")
        buf.write("\7?\2\2\u00e38\3\2\2\2\u00e4\u00e5\7@\2\2\u00e5\u00e6")
        buf.write("\7?\2\2\u00e6:\3\2\2\2\u00e7\u00e8\7?\2\2\u00e8\u00e9")
        buf.write("\7\61\2\2\u00e9\u00ea\7?\2\2\u00ea<\3\2\2\2\u00eb\u00ec")
        buf.write("\7>\2\2\u00ec\u00ed\7\60\2\2\u00ed>\3\2\2\2\u00ee\u00ef")
        buf.write("\7@\2\2\u00ef\u00f0\7\60\2\2\u00f0@\3\2\2\2\u00f1\u00f2")
        buf.write("\7>\2\2\u00f2\u00f3\7?\2\2\u00f3\u00f4\7\60\2\2\u00f4")
        buf.write("B\3\2\2\2\u00f5\u00f6\7@\2\2\u00f6\u00f7\7?\2\2\u00f7")
        buf.write("\u00f8\7\60\2\2\u00f8D\3\2\2\2\u00f9\u00fa\7?\2\2\u00fa")
        buf.write("F\3\2\2\2\u00fb\u00fc\7D\2\2\u00fc\u00fd\7q\2\2\u00fd")
        buf.write("\u00fe\7f\2\2\u00fe\u00ff\7{\2\2\u00ffH\3\2\2\2\u0100")
        buf.write("\u0101\7D\2\2\u0101\u0102\7t\2\2\u0102\u0103\7g\2\2\u0103")
        buf.write("\u0104\7c\2\2\u0104\u0105\7m\2\2\u0105J\3\2\2\2\u0106")
        buf.write("\u0107\7E\2\2\u0107\u0108\7q\2\2\u0108\u0109\7p\2\2\u0109")
        buf.write("\u010a\7v\2\2\u010a\u010b\7k\2\2\u010b\u010c\7p\2\2\u010c")
        buf.write("\u010d\7w\2\2\u010d\u010e\7g\2\2\u010eL\3\2\2\2\u010f")
        buf.write("\u0110\7F\2\2\u0110\u0111\7q\2\2\u0111N\3\2\2\2\u0112")
        buf.write("\u0113\7G\2\2\u0113\u0114\7n\2\2\u0114\u0115\7u\2\2\u0115")
        buf.write("\u0116\7g\2\2\u0116P\3\2\2\2\u0117\u0118\7G\2\2\u0118")
        buf.write("\u0119\7n\2\2\u0119\u011a\7u\2\2\u011a\u011b\7g\2\2\u011b")
        buf.write("\u011c\7K\2\2\u011c\u011d\7h\2\2\u011dR\3\2\2\2\u011e")
        buf.write("\u011f\7G\2\2\u011f\u0120\7p\2\2\u0120\u0121\7f\2\2\u0121")
        buf.write("\u0122\7D\2\2\u0122\u0123\7q\2\2\u0123\u0124\7f\2\2\u0124")
        buf.write("\u0125\7{\2\2\u0125T\3\2\2\2\u0126\u0127\7G\2\2\u0127")
        buf.write("\u0128\7p\2\2\u0128\u0129\7f\2\2\u0129\u012a\7K\2\2\u012a")
        buf.write("\u012b\7h\2\2\u012bV\3\2\2\2\u012c\u012d\7G\2\2\u012d")
        buf.write("\u012e\7p\2\2\u012e\u012f\7f\2\2\u012f\u0130\7H\2\2\u0130")
        buf.write("\u0131\7q\2\2\u0131\u0132\7t\2\2\u0132X\3\2\2\2\u0133")
        buf.write("\u0134\7G\2\2\u0134\u0135\7p\2\2\u0135\u0136\7f\2\2\u0136")
        buf.write("\u0137\7Y\2\2\u0137\u0138\7j\2\2\u0138\u0139\7k\2\2\u0139")
        buf.write("\u013a\7n\2\2\u013a\u013b\7g\2\2\u013bZ\3\2\2\2\u013c")
        buf.write("\u013d\7H\2\2\u013d\u013e\7q\2\2\u013e\u013f\7t\2\2\u013f")
        buf.write("\\\3\2\2\2\u0140\u0141\7H\2\2\u0141\u0142\7w\2\2\u0142")
        buf.write("\u0143\7p\2\2\u0143\u0144\7e\2\2\u0144\u0145\7v\2\2\u0145")
        buf.write("\u0146\7k\2\2\u0146\u0147\7q\2\2\u0147\u0148\7p\2\2\u0148")
        buf.write("^\3\2\2\2\u0149\u014a\7K\2\2\u014a\u014b\7h\2\2\u014b")
        buf.write("`\3\2\2\2\u014c\u014d\7R\2\2\u014d\u014e\7c\2\2\u014e")
        buf.write("\u014f\7t\2\2\u014f\u0150\7c\2\2\u0150\u0151\7o\2\2\u0151")
        buf.write("\u0152\7g\2\2\u0152\u0153\7v\2\2\u0153\u0154\7g\2\2\u0154")
        buf.write("\u0155\7t\2\2\u0155b\3\2\2\2\u0156\u0157\7T\2\2\u0157")
        buf.write("\u0158\7g\2\2\u0158\u0159\7v\2\2\u0159\u015a\7w\2\2\u015a")
        buf.write("\u015b\7t\2\2\u015b\u015c\7p\2\2\u015cd\3\2\2\2\u015d")
        buf.write("\u015e\7V\2\2\u015e\u015f\7j\2\2\u015f\u0160\7g\2\2\u0160")
        buf.write("\u0161\7p\2\2\u0161f\3\2\2\2\u0162\u0163\7X\2\2\u0163")
        buf.write("\u0164\7c\2\2\u0164\u0165\7t\2\2\u0165h\3\2\2\2\u0166")
        buf.write("\u0167\7Y\2\2\u0167\u0168\7j\2\2\u0168\u0169\7k\2\2\u0169")
        buf.write("\u016a\7n\2\2\u016a\u016b\7g\2\2\u016bj\3\2\2\2\u016c")
        buf.write("\u016d\7V\2\2\u016d\u016e\7t\2\2\u016e\u016f\7w\2\2\u016f")
        buf.write("\u0170\7g\2\2\u0170l\3\2\2\2\u0171\u0172\7H\2\2\u0172")
        buf.write("\u0173\7c\2\2\u0173\u0174\7n\2\2\u0174\u0175\7u\2\2\u0175")
        buf.write("\u0176\7g\2\2\u0176n\3\2\2\2\u0177\u0178\7G\2\2\u0178")
        buf.write("\u0179\7p\2\2\u0179\u017a\7f\2\2\u017a\u017b\7F\2\2\u017b")
        buf.write("\u017c\7q\2\2\u017cp\3\2\2\2\u017d\u017e\t\2\2\2\u017e")
        buf.write("r\3\2\2\2\u017f\u0180\t\3\2\2\u0180t\3\2\2\2\u0181\u0182")
        buf.write("\t\4\2\2\u0182v\3\2\2\2\u0183\u0184\7a\2\2\u0184x\3\2")
        buf.write("\2\2\u0185\u0186\7)\2\2\u0186z\3\2\2\2\u0187\u0188\7$")
        buf.write("\2\2\u0188|\3\2\2\2\u0189\u018a\7\62\2\2\u018a\u018b\t")
        buf.write("\5\2\2\u018b\u0190\t\6\2\2\u018c\u018f\5u;\2\u018d\u018f")
        buf.write("\t\7\2\2\u018e\u018c\3\2\2\2\u018e\u018d\3\2\2\2\u018f")
        buf.write("\u0192\3\2\2\2\u0190\u018e\3\2\2\2\u0190\u0191\3\2\2\2")
        buf.write("\u0191~\3\2\2\2\u0192\u0190\3\2\2\2\u0193\u0197\t\b\2")
        buf.write("\2\u0194\u0196\5u;\2\u0195\u0194\3\2\2\2\u0196\u0199\3")
        buf.write("\2\2\2\u0197\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u019c")
        buf.write("\3\2\2\2\u0199\u0197\3\2\2\2\u019a\u019c\7\62\2\2\u019b")
        buf.write("\u0193\3\2\2\2\u019b\u019a\3\2\2\2\u019c\u0080\3\2\2\2")
        buf.write("\u019d\u019e\7\62\2\2\u019e\u019f\t\t\2\2\u019f\u01a3")
        buf.write("\t\n\2\2\u01a0\u01a2\t\13\2\2\u01a1\u01a0\3\2\2\2\u01a2")
        buf.write("\u01a5\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a4\3\2\2\2")
        buf.write("\u01a4\u0082\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a6\u01aa\5")
        buf.write("\177@\2\u01a7\u01aa\5}?\2\u01a8\u01aa\5\u0081A\2\u01a9")
        buf.write("\u01a6\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01a8\3\2\2\2")
        buf.write("\u01aa\u0084\3\2\2\2\u01ab\u01ae\t\f\2\2\u01ac\u01af\5")
        buf.write("\27\f\2\u01ad\u01af\5\33\16\2\u01ae\u01ac\3\2\2\2\u01ae")
        buf.write("\u01ad\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b1\3\2\2\2")
        buf.write("\u01b0\u01b2\5u;\2\u01b1\u01b0\3\2\2\2\u01b2\u01b3\3\2")
        buf.write("\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u0086")
        buf.write("\3\2\2\2\u01b5\u01b9\5\r\7\2\u01b6\u01b8\5u;\2\u01b7\u01b6")
        buf.write("\3\2\2\2\u01b8\u01bb\3\2\2\2\u01b9\u01b7\3\2\2\2\u01b9")
        buf.write("\u01ba\3\2\2\2\u01ba\u0088\3\2\2\2\u01bb\u01b9\3\2\2\2")
        buf.write("\u01bc\u01c2\5\177@\2\u01bd\u01c3\5\u0087D\2\u01be\u01c3")
        buf.write("\5\u0085C\2\u01bf\u01c0\5\u0087D\2\u01c0\u01c1\5\u0085")
        buf.write("C\2\u01c1\u01c3\3\2\2\2\u01c2\u01bd\3\2\2\2\u01c2\u01be")
        buf.write("\3\2\2\2\u01c2\u01bf\3\2\2\2\u01c3\u008a\3\2\2\2\u01c4")
        buf.write("\u01c5\7^\2\2\u01c5\u01c6\t\r\2\2\u01c6\u008c\3\2\2\2")
        buf.write("\u01c7\u01cb\5{>\2\u01c8\u01ca\5\u0097L\2\u01c9\u01c8")
        buf.write("\3\2\2\2\u01ca\u01cd\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cb")
        buf.write("\u01c9\3\2\2\2\u01cc\u01ce\3\2\2\2\u01cd\u01cb\3\2\2\2")
        buf.write("\u01ce\u01cf\5{>\2\u01cf\u01d0\bG\2\2\u01d0\u008e\3\2")
        buf.write("\2\2\u01d1\u01d4\5k\66\2\u01d2\u01d4\5m\67\2\u01d3\u01d1")
        buf.write("\3\2\2\2\u01d3\u01d2\3\2\2\2\u01d4\u0090\3\2\2\2\u01d5")
        buf.write("\u01dc\5q9\2\u01d6\u01db\5q9\2\u01d7\u01db\5s:\2\u01d8")
        buf.write("\u01db\5w<\2\u01d9\u01db\5u;\2\u01da\u01d6\3\2\2\2\u01da")
        buf.write("\u01d7\3\2\2\2\u01da\u01d8\3\2\2\2\u01da\u01d9\3\2\2\2")
        buf.write("\u01db\u01de\3\2\2\2\u01dc\u01da\3\2\2\2\u01dc\u01dd\3")
        buf.write("\2\2\2\u01dd\u0092\3\2\2\2\u01de\u01dc\3\2\2\2\u01df\u01e1")
        buf.write("\t\16\2\2\u01e0\u01df\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2")
        buf.write("\u01e0\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3\u01e4\3\2\2\2")
        buf.write("\u01e4\u01e5\bJ\3\2\u01e5\u0094\3\2\2\2\u01e6\u01e7\7")
        buf.write(",\2\2\u01e7\u01e8\7,\2\2\u01e8\u01ec\3\2\2\2\u01e9\u01eb")
        buf.write("\5\u009bN\2\u01ea\u01e9\3\2\2\2\u01eb\u01ee\3\2\2\2\u01ec")
        buf.write("\u01ed\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ed\u01ef\3\2\2\2")
        buf.write("\u01ee\u01ec\3\2\2\2\u01ef\u01f0\7,\2\2\u01f0\u01f1\7")
        buf.write(",\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f3\bK\3\2\u01f3\u0096")
        buf.write("\3\2\2\2\u01f4\u01f9\n\17\2\2\u01f5\u01f9\5\u008bF\2\u01f6")
        buf.write("\u01f7\7)\2\2\u01f7\u01f9\7$\2\2\u01f8\u01f4\3\2\2\2\u01f8")
        buf.write("\u01f5\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f9\u0098\3\2\2\2")
        buf.write("\u01fa\u01fb\7^\2\2\u01fb\u0200\n\r\2\2\u01fc\u0200\7")
        buf.write("^\2\2\u01fd\u01fe\t\20\2\2\u01fe\u0200\n\21\2\2\u01ff")
        buf.write("\u01fa\3\2\2\2\u01ff\u01fc\3\2\2\2\u01ff\u01fd\3\2\2\2")
        buf.write("\u0200\u009a\3\2\2\2\u0201\u0207\n\22\2\2\u0202\u0203")
        buf.write("\t\22\2\2\u0203\u0207\n\22\2\2\u0204\u0205\t\22\2\2\u0205")
        buf.write("\u0207\7\2\2\3\u0206\u0201\3\2\2\2\u0206\u0202\3\2\2\2")
        buf.write("\u0206\u0204\3\2\2\2\u0207\u009c\3\2\2\2\u0208\u0209\13")
        buf.write("\2\2\2\u0209\u009e\3\2\2\2\u020a\u020e\7$\2\2\u020b\u020d")
        buf.write("\5\u0097L\2\u020c\u020b\3\2\2\2\u020d\u0210\3\2\2\2\u020e")
        buf.write("\u020c\3\2\2\2\u020e\u020f\3\2\2\2\u020f\u0212\3\2\2\2")
        buf.write("\u0210\u020e\3\2\2\2\u0211\u0213\t\23\2\2\u0212\u0211")
        buf.write("\3\2\2\2\u0213\u0214\3\2\2\2\u0214\u0215\bP\4\2\u0215")
        buf.write("\u00a0\3\2\2\2\u0216\u021a\7$\2\2\u0217\u0219\5\u0097")
        buf.write("L\2\u0218\u0217\3\2\2\2\u0219\u021c\3\2\2\2\u021a\u0218")
        buf.write("\3\2\2\2\u021a\u021b\3\2\2\2\u021b\u021d\3\2\2\2\u021c")
        buf.write("\u021a\3\2\2\2\u021d\u021e\5\u0099M\2\u021e\u021f\bQ\5")
        buf.write("\2\u021f\u00a2\3\2\2\2\u0220\u0221\7,\2\2\u0221\u0222")
        buf.write("\7,\2\2\u0222\u0226\3\2\2\2\u0223\u0225\5\u009bN\2\u0224")
        buf.write("\u0223\3\2\2\2\u0225\u0228\3\2\2\2\u0226\u0224\3\2\2\2")
        buf.write("\u0226\u0227\3\2\2\2\u0227\u0229\3\2\2\2\u0228\u0226\3")
        buf.write("\2\2\2\u0229\u022a\7\2\2\3\u022a\u022b\bR\6\2\u022b\u00a4")
        buf.write("\3\2\2\2\32\2\u018e\u0190\u0197\u019b\u01a3\u01a9\u01ae")
        buf.write("\u01b3\u01b9\u01c2\u01cb\u01d3\u01da\u01dc\u01e2\u01ec")
        buf.write("\u01f8\u01ff\u0206\u020e\u0212\u021a\u0226\7\3G\2\b\2")
        buf.write("\2\3P\3\3Q\4\3R\5")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LP = 1
    RP = 2
    LB = 3
    RB = 4
    COLON = 5
    DOT = 6
    COMMA = 7
    SEMI = 8
    LCB = 9
    RCB = 10
    ADDOP = 11
    ADDF = 12
    SUBOP = 13
    SUBF = 14
    MULOP = 15
    MULF = 16
    DIVOP = 17
    DIVF = 18
    MODOP = 19
    NOT = 20
    AND = 21
    OR = 22
    EQ = 23
    NEQ = 24
    LT = 25
    GT = 26
    LTE = 27
    GTE = 28
    NEQF = 29
    LTF = 30
    GTF = 31
    LTEF = 32
    GTEF = 33
    ASSIG = 34
    BODY = 35
    BREAK = 36
    CONTINUE = 37
    DO = 38
    ELSE = 39
    ELSEIF = 40
    ENDBODY = 41
    ENDIF = 42
    ENDFOR = 43
    ENDWHILE = 44
    FOR = 45
    FUNCTION = 46
    IF = 47
    PARAMETER = 48
    RETURN = 49
    THEN = 50
    VAR = 51
    WHILE = 52
    ENDDO = 53
    INTERGER = 54
    FLOAT = 55
    STRING = 56
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
            "'('", "')'", "'['", "']'", "':'", "'.'", "','", "';'", "'{'", 
            "'}'", "'+'", "'+.'", "'-'", "'-.'", "'*'", "'*.'", "'\\'", 
            "'\\.'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", 
            "'>'", "'<='", "'>='", "'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'", 
            "'='", "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", 
            "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", 
            "'For'", "'Function'", "'If'", "'Parameter'", "'Return'", "'Then'", 
            "'Var'", "'While'", "'EndDo'" ]

    symbolicNames = [ "<INVALID>",
            "LP", "RP", "LB", "RB", "COLON", "DOT", "COMMA", "SEMI", "LCB", 
            "RCB", "ADDOP", "ADDF", "SUBOP", "SUBF", "MULOP", "MULF", "DIVOP", 
            "DIVF", "MODOP", "NOT", "AND", "OR", "EQ", "NEQ", "LT", "GT", 
            "LTE", "GTE", "NEQF", "LTF", "GTF", "LTEF", "GTEF", "ASSIG", 
            "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", 
            "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
            "RETURN", "THEN", "VAR", "WHILE", "ENDDO", "INTERGER", "FLOAT", 
            "STRING", "BOOLEAN", "ID", "WS", "COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "LP", "RP", "LB", "RB", "COLON", "DOT", "COMMA", "SEMI", 
                  "LCB", "RCB", "ADDOP", "ADDF", "SUBOP", "SUBF", "MULOP", 
                  "MULF", "DIVOP", "DIVF", "MODOP", "NOT", "AND", "OR", 
                  "EQ", "NEQ", "LT", "GT", "LTE", "GTE", "NEQF", "LTF", 
                  "GTF", "LTEF", "GTEF", "ASSIG", "BODY", "BREAK", "CONTINUE", 
                  "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", 
                  "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", 
                  "THEN", "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", "LOWCASE", 
                  "UPPERCASE", "NUMBER", "UNDERCORE", "SINGLE_QUOTE", "DOUBLE_QUOTE", 
                  "HEXA", "DECIMAL", "OCTAL", "INTERGER", "EXPONENT", "DECIMAL_PART", 
                  "FLOAT", "ESCAPE_SEQUENCE", "STRING", "BOOLEAN", "ID", 
                  "WS", "COMMENT", "CHAR", "ESCAPE_ILLEGAL", "COMMENT_BODY", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

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
            actions[69] = self.STRING_action 
            actions[78] = self.UNCLOSE_STRING_action 
            actions[79] = self.ILLEGAL_ESCAPE_action 
            actions[80] = self.UNTERMINATED_COMMENT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                                            self.text = self.text[1:-1]
                                        
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            		y = str(self.text)
            		impossible = ['\n', '\r']
            		if y[-1] in impossible:
            			raise UncloseString(y[1:-1])
            		else:
            			raise UncloseString(y[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                    raise UnterminatedComment() 
                
     


