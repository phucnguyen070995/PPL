import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    #test ID
    def test_ID_101(self):
        self.assertTrue(TestLexer.checkLexeme("aa b cccc 4","aa,b,cccc,4,<EOF>",101))
    def test_ID_102(self):
        self.assertTrue(TestLexer.checkLexeme("abCd","abCd,<EOF>",102))
    def test_ID_103(self):
        self.assertTrue(TestLexer.checkLexeme("xA_B","xA_B,<EOF>",103))
    def test_ID_104(self):
        self.assertTrue(TestLexer.checkLexeme("abc123","abc123,<EOF>",104))
    def test_ID_105(self):
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",105))
    def test_ID_106(self):
        self.assertTrue(TestLexer.checkLexeme("&123\n123","Error Token &",106))
    def test_ID_107(self):
        self.assertTrue(TestLexer.checkLexeme("abc12345?xxs","abc12345,Error Token ?",107))
    def test_ID_108(self):
        self.assertTrue(TestLexer.checkLexeme("abc/n123","abc,/,n123,<EOF>",108))
    def test_ID_109(self):
        self.assertTrue(TestLexer.checkLexeme("abc\n123","abc,123,<EOF>",109))
    def test_ID_110(self):
        self.assertTrue(TestLexer.checkLexeme("abc\t123","abc,123,<EOF>",110))
    def test_ID_111(self):
        self.assertTrue(TestLexer.checkLexeme("abcdefs_\nx_123","abcdefs_,x_123,<EOF>",111))
    def test_ID_112(self):
        self.assertTrue(TestLexer.checkLexeme("_abcdef","Error Token _",112))
    def test_ID_112(self):
        self.assertTrue(TestLexer.checkLexeme("_abcdef","Error Token _",112))   
    def test_lower_upper_id_113(self):
        self.assertTrue(TestLexer.checkLexeme("Var","Var,<EOF>",113))
    def test_wrong_token_114(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",114))
    #test keyword
    def test_keywords_115(self):
        self.assertTrue(TestLexer.checkLexeme("Body Break","Body,Break,<EOF>",115))
    def test_keywords_116(self):
        self.assertTrue(TestLexer.checkLexeme("Continue ElseIf If","Continue,ElseIf,If,<EOF>",116))
    #test operator
    def test_Operators_117(self):
        self.assertTrue(TestLexer.checkLexeme("1 + 6","1,+,6,<EOF>",117))
    def test_Operators_118(self):
        self.assertTrue(TestLexer.checkLexeme("1 +. 6","1,+.,6,<EOF>",118))
    def test_Operators_119(self):
        self.assertTrue(TestLexer.checkLexeme("1 =/= 6","1,=/=,6,<EOF>",119))
    def test_Operators_120(self):
        self.assertTrue(TestLexer.checkLexeme("a && b","a,&&,b,<EOF>",120))
    def test_Operators_121(self):
        self.assertTrue(TestLexer.checkLexeme("a >=. b","a,>=.,b,<EOF>",121))
    # test Separators
    def test_Separators_122(self):
        self.assertTrue(TestLexer.checkLexeme("(a + b)","(,a,+,b,),<EOF>",122))
    def test_Separators_123(self):
        self.assertTrue(TestLexer.checkLexeme("a[b + c[1]]","a,[,b,+,c,[,1,],],<EOF>",123))
    # test Literals
    # Integer
    def test_interger_124(self):
        self.assertTrue(TestLexer.checkLexeme("123456 0 ","123456,0,<EOF>",124))
    def test_interger_125(self):
        self.assertTrue(TestLexer.checkLexeme("0xABC 0XABC","0xABC,0XABC,<EOF>",125))
    def test_interger_126(self):
        self.assertTrue(TestLexer.checkLexeme("0o123 0O123","0o123,0O123,<EOF>",126))
    def test_interger_127(self):
        self.assertTrue(TestLexer.checkLexeme("0o123A 0O123C","0o123,Error Token A",127))
    def test_interger_128(self):
        self.assertTrue(TestLexer.checkLexeme("0x123XY15","0x123,Error Token X",128))
    def test_interger_129(self):
        self.assertTrue(TestLexer.checkLexeme("12345600","12345600,<EOF>",129))
    def test_interger_130(self):
        self.assertTrue(TestLexer.checkLexeme("0xABCDEF","0xABCDEF,<EOF>",130))
    #boolean
    def test_boolean_131(self):
        self.assertTrue(TestLexer.checkLexeme("True False","True,False,<EOF>",131))
    #string
    def test_illegal_escape_132(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",132))
    def test_illegal_escape_133(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\x def"  ""","""Illegal Escape In String: abc\\x""",133))
    def test_illegal_escape_134(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\z def"  ""","""Illegal Escape In String: abc\z""",134))
    def test_illegal_escape_135(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",135))

    def test_unterminated_string_136(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,136))
    def test_unterminated_string_137(self):
        self.assertTrue(TestLexer.checkLexeme(""" abc" def  ""","""abc,Unclosed String:  def  """,137))
    def test_unterminated_string_138(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,138))
    def test_unterminated_string_139(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,139))
    def test_normal_string_with_string_140(self):
        self.assertTrue(TestLexer.checkLexeme(""" This is ""","""Error Token T""",140))
    #comment
    def test_comment_141(self):
        self.assertTrue(TestLexer.checkLexeme("**Nguyet**","<EOF>",141))
    def test_comment_142(self):
        self.assertTrue(TestLexer.checkLexeme("**Nguyet *Doan *Thi **","<EOF>",142))
    def test_comment_143(self):
        self.assertTrue(TestLexer.checkLexeme("**Nguyet.","*,*,Error Token N",143))
    def test_block_comment_144(self):
        self.assertTrue(TestLexer.checkLexeme("** A block comment **","<EOF>",144))
    def test_block_comment_145(self):
        self.assertTrue(TestLexer.checkLexeme("** This is a block comment ** 123abc","123,abc,<EOF>",145))
    def test_block_comment_146(self):
        self.assertTrue(TestLexer.checkLexeme("** Not a block comment.","*,*,Error Token N",146))
    def test_block_comment_147(self):
        self.assertTrue(TestLexer.checkLexeme("** abc // 123 **","<EOF>",147))   
    def test_block_comment_148(self):
        self.assertTrue(TestLexer.checkLexeme("** abc \n 123 **","<EOF>",148))
    def test_block_comment_149(self):
        self.assertTrue(TestLexer.checkLexeme("** abc \b \t \r 123 **","<EOF>",149))

    def test_block_comment_150(self):
        self.assertTrue(TestLexer.checkLexeme("** abc \\ .. // \b \t \r 123 **","<EOF>",150))
     #test variable declaration
    def test_variabledecl_151(self):
        self.assertTrue(TestLexer.checkLexeme("Var x, a[5];","Var,x,,,a,[,5,],;,<EOF>",151))
    def test_variabledecl_152(self):
        self.assertTrue(TestLexer.checkLexeme("Var a, b, c[1], d, e[2];","Var,a,,,b,,,c,[,1,],,,d,,,e,[,2,],;,<EOF>",152))
    def test_variabledecl_153(self):
        self.assertTrue(TestLexer.checkLexeme("Var str='A string!'","Var,str,=,Error Token '",153))
    # def test_variabledecl_154(self):
    #     self.assertTrue(TestLexer.checkLexeme("""a_="this is a string" ""","a_,=,this is a string,<EOF>",154))
    def test_variabledecl_155(self):
        self.assertTrue(TestLexer.checkLexeme("a__var__123 = 456","a__var__123,=,456,<EOF>",156))
    def test_variabledecl_157(self):
        self.assertTrue(TestLexer.checkLexeme("Var x (123, string);","Var,x,(,123,,,string,),;,<EOF>",157))

    #test float
    def test_float_158(self):
        self.assertTrue(TestLexer.checkLexeme("12.0e3 12e3 12.e5 12.0e3 12.0E3 12000. 120000e-1","12.0e3,12e3,12.e5,12.0e3,12.0E3,12000.,120000e-1,<EOF>",158))
    def test_float_159(self):
        self.assertTrue(TestLexer.checkLexeme("0.12e5","0.12e5,<EOF>",159))
    def test_float_160(self):
        self.assertTrue(TestLexer.checkLexeme("12e3458","12e3458,<EOF>",160))
    def test_float_161(self):
        self.assertTrue(TestLexer.checkLexeme("1233.e-3","1233.e-3,<EOF>",161))
    def test_float_162(self):
        self.assertTrue(TestLexer.checkLexeme(".477",".,477,<EOF>",162))
    def test_float_163(self):
        self.assertTrue(TestLexer.checkLexeme("599.","599.,<EOF>",163))
    def test_float_164(self):
        self.assertTrue(TestLexer.checkLexeme("9E-88","9E-88,<EOF>",164))
    def test_float_165(self):
        self.assertTrue(TestLexer.checkLexeme(".776E-6",".,776E-6,<EOF>",165))
    def test_float_166(self):
        self.assertTrue(TestLexer.checkLexeme("11.0","11.0,<EOF>",166))
    def test_float_167(self):
        self.assertTrue(TestLexer.checkLexeme("0.12","0.12,<EOF>",167))
    def test_float_168(self):
        self.assertTrue(TestLexer.checkLexeme("-0.15","-,0.15,<EOF>",168))
    def test_float_169(self):
        self.assertTrue(TestLexer.checkLexeme("-40.0","-,40.0,<EOF>",169))
    def test_float_170(self):
        self.assertTrue(TestLexer.checkLexeme("-zyx123","-,zyx123,<EOF>",170))
    def test_float_171(self):
        self.assertTrue(TestLexer.checkLexeme("-12358.69abc","-,12358.69,abc,<EOF>",171))
    def test_float_172(self):
        self.assertTrue(TestLexer.checkLexeme("-1.2,3.","-,1.2,,,3.,<EOF>",172))
    def test_float_173(self):
        self.assertTrue(TestLexer.checkLexeme("-1.e-29","-,1.e-29,<EOF>",173))
    def test_float_174(self):
        self.assertTrue(TestLexer.checkLexeme("-1.e-2359","-,1.e-2359,<EOF>",174))

    #test illegal escape in string
    def test_IllegalEscapeString_175(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\i123 ""","""Illegal Escape In String: abc\\i""",175))
    def test_IllegalEscapeString_176(self):
        self.assertTrue(TestLexer.checkLexeme(""" abc "xyz\\m123" ""","abc,Illegal Escape In String: xyz\\m""",176))
    def test_IllegalEscapeString_177(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\t" ""","""abc	,<EOF>""",177))
    def test_IllegalEscapeString_178(self):
        self.assertTrue(TestLexer.checkLexeme("\"abc\\n\"","abc\\n,<EOF>",178))
    def test_IllegalEscapeString_179(self):
        self.assertTrue(TestLexer.checkLexeme(".a",".,a,<EOF>",179))
    #test unclosed string
    def test_UnclosedString_180(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\r123""","""Unclosed String: abc\n123""",180))
    def test_UnclosedString_181(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\123""","""Illegal Escape In String: abc\\1""",181))
    #test string
    def test_String_182(self):
        self.assertTrue(TestLexer.checkLexeme("""abc/d\\\\1234""","abc,/,d,\,\,1234,<EOF>",182))
    def test_String_183(self):
        self.assertTrue(TestLexer.checkLexeme("abc = 123xyz / defz","abc,=,123,xyz,/,defz,<EOF>",183))
    def test_String_184(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is \\t\\r a string!" ""","This is \\t\\r a string!,<EOF>",184))
    def test_String_185(self):
        self.assertTrue(TestLexer.checkLexeme(""" "a" ""","""a,<EOF>""",185))
    def test_String_186(self):
        self.assertTrue(TestLexer.checkLexeme(""" "456a789" ""","""456a789,<EOF>""",186))
    def test_String_187(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abcxyz\n123" ""","Unclosed String: abcxyz",187))
    def test_all_188(self):
        self.assertTrue(TestLexer.checkLexeme("Function: Do While!.","Function,:,Do,While,!,.,<EOF>",188))
    def test_String_189(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abcxyz" ""","""abcxyz,<EOF>""",189))
    def test_all_190(self):
        self.assertTrue(TestLexer.checkLexeme("Function: Do While!.","Function,:,Do,While,!,.,<EOF>",190))
    def test_all_191(self):
        self.assertTrue(TestLexer.checkLexeme("foo(a + b - c * d[9])","foo,(,a,+,b,-,c,*,d,[,9,],),<EOF>",191))

    def test_all_192(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\ndef"  ""","""Unclosed String: abc""",192))
    def test_all_193(self):
        self.assertTrue(TestLexer.checkLexeme("\"it is '\"01'\"\"","""it is '"01'",<EOF>""", 193))
    def test_all_194(self):
        self.assertTrue(TestLexer.checkLexeme("\"new line\\n is valid \"", "new line\\n is valid ,<EOF>", 195))
    def test_all_195(self):
        self.assertTrue(TestLexer.checkLexeme("\"tab \\t\"", "tab \\t,<EOF>", 195))
    def test_all_196(self):
        self.assertTrue(TestLexer.checkLexeme("\"vari\\'s name\"", "vari\\'s name,<EOF>", 196))
    def test_all_197(self):
        self.assertTrue(TestLexer.checkLexeme("\"xxx \\\\ ayb\"","xxx \\\\ ayb,<EOF>", 197)) 
    def test_all_198(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string containing tab" ""","""This is a string containing tab,<EOF>""",198))
    def test_all_199(self):
        self.assertTrue(TestLexer.checkLexeme(""" "why"  ""","""why,<EOF>""",199)) 
    def test_all_200(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Doan Thi Nhu Nguyet"  ""","""Doan Thi Nhu Nguyet,<EOF>""",200))
    def test_all_201(self):
        self.assertTrue(TestLexer.checkLexeme("+. -. *. / =/= <. >. <=. >=.","+.,-.,*.,/,=/=,<.,>.,<=.,>=.,<EOF>",201))
    def test_all_202(self):
        self.assertTrue(TestLexer.checkLexeme("+ - * \ % == != < > <= >=","+,-,*,\,%,==,!=,<,>,<=,>=,<EOF>",202))
    def test_all_203(self):
        self.assertTrue(TestLexer.checkLexeme("! && ||","!,&&,||,<EOF>",203))