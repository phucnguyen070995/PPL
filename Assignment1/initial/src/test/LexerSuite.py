import unittest
from TestUtils import TestLexer
class LexerSuite(unittest.TestCase):
          
    import unittest
from TestUtils import TestLexer
class LexerSuite(unittest.TestCase):
    def test_id_first(self):
        self.assertTrue(TestLexer.checkLexeme("""456dv""","456,dv,<EOF>",102))
    def test_id_digit(self):
        self.assertTrue(TestLexer.checkLexeme("""linh123""","linh123,<EOF>",103))
    def test_id_underscore(self):
        self.assertTrue(TestLexer.checkLexeme("""_linh_123""","_linh_123,<EOF>",104))
    def test_id_upperCase(self):
        self.assertTrue(TestLexer.checkLexeme("""A_linh_123A""","A_linh_123A,<EOF>",105))
    def test_int(self):
        self.assertTrue(TestLexer.checkLexeme("""0 10""","0,10,<EOF>",106))
    def test_subInt(self):
        self.assertTrue(TestLexer.checkLexeme("""-0 -1123125423543254354510""","-,0,-,1123125423543254354510,<EOF>",107))
    def test_float(self):
        self.assertTrue(TestLexer.checkLexeme("""1.2.3.4.5.""","1.2,.3,.4,.5,Error Token .",108))
    def test_floatNoWhole(self):
        self.assertTrue(TestLexer.checkLexeme(""".1.1.1.1.1""",".1,.1,.1,.1,.1,<EOF>",109))
    def test_floatNoWhole2(self):
        self.assertTrue(TestLexer.checkLexeme(""".11.   """,".11,Error Token .",110))
    def test_floatNoE(self):
        self.assertTrue(TestLexer.checkLexeme(""".1 1. 1.2.  """,".1,1.,1.2,Error Token .",111))
    def test_floatNoPoint(self):
        self.assertTrue(TestLexer.checkLexeme("""1e0 1E0 0e-1 1112E0 e- E""","1e0,1E0,0e-1,1112E0,e,-,E,<EOF>",112))
    def test_floatNoPoint2(self):
        self.assertTrue(TestLexer.checkLexeme("""0e- e0-""","0,e,-,e0,-,<EOF>",113))
    def test_floatEPoint(self):
        self.assertTrue(TestLexer.checkLexeme("""1.2e 12e3. 1.e3 .e-2 .1e-2 ""","1.2,e,12e3,Error Token .",114))
    def test_floatEPoint2(self):
        self.assertTrue(TestLexer.checkLexeme(""".1e-2 .e-2 """,".1e-2,Error Token .",115))
    def test_floatEPoint3(self):
        self.assertTrue(TestLexer.checkLexeme("""1.2 1. .1 1e2 1.2E-2 1.2e-2 .1E2 9.0 12e8 0.33E-3 128e-42""","1.2,1.,.1,1e2,1.2E-2,1.2e-2,.1E2,9.0,12e8,0.33E-3,128e-42,<EOF>",116))
    def test_trueFalse(self):
        self.assertTrue(TestLexer.checkLexeme("""true false true""","true,false,true,<EOF>",117))
    def test_string(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc"abc"  ""","abc,abc,Unclosed String:   ",118))
    def test_string2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\"abc"  ""","abc,abc,Unclosed String:   ",119))
    def test_string3(self):
        self.assertTrue(TestLexer.checkLexeme(r""" "\\c\r\n\t\""  """,r"\\c\r\n\t\",<EOF>",120))
    def test_string4(self):
        self.assertTrue(TestLexer.checkLexeme(r""" "a\\\c\r\n\t\""  """,r"Illegal Escape In String: a\\\c",121))
    def test_string5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\\" ""","""Unclosed String: \\" """,122))
    def test_string6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "\\""",'Unclosed String: \\',123))
    def test_string7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\""",'Unclosed String: abc\\',124))
    def test_string8(self):
        self.assertTrue(TestLexer.checkLexeme("""\"""","Unclosed String: ",125))   
    def test_string9(self):
        self.assertTrue(TestLexer.checkLexeme("""\\""","Error Token \\",126))   
    def test_string10(self):
        INPUT = """
        "Hi, I'm Lin "
        "\t"
        """
        EXPECT = """Hi, I'm Lin ,	,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(INPUT, EXPECT,127))             
    def test_string11(self):
        INPUT = """
        "Hello World"
        "\t\r"
        """
        EXPECT = 'Hello World,Unclosed String: 	'
        self.assertTrue(TestLexer.checkLexeme(INPUT, EXPECT,128))           
    def test_string12(self):
        INPUT = """\"\\"""
        EXPECT = 'Unclosed String: \\'
        self.assertTrue(TestLexer.checkLexeme(INPUT, EXPECT,129))        
    def test_string13(self):
        INPUT = """\"
        \\"""
        EXPECT = 'Unclosed String: '
        self.assertTrue(TestLexer.checkLexeme(INPUT, EXPECT,130))        
    def test_string14(self):
        INPUT = """\"\\\""""
        EXPECT = 'Unclosed String: \\"'
        self.assertTrue(TestLexer.checkLexeme(INPUT, EXPECT,131))        
    def test_string15(self):
        INPUT = """\"\\abc"\""""
        EXPECT = 'Illegal Escape In String: \\a'
        self.assertTrue(TestLexer.checkLexeme(INPUT, EXPECT,132))        
    def test_string16(self):
        INPUT = """\"\rabc"""
        EXPECT = 'Unclosed String: '
        self.assertTrue(TestLexer.checkLexeme(INPUT, EXPECT,133))        
    
    def test_string17(self):
        INPUT = """Nguyen_Van_Hoai_Linh\r\t\t\t\t0_ID= 14"""
        EXPECT = 'Nguyen_Van_Hoai_Linh,0,_ID,=,14,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(INPUT, EXPECT,134))   
    def test_string18(self):
        INPUT = """\"Testing by\HLin Nguyen hcmut"""
        EXPECT = 'Illegal Escape In String: Testing by\H'
        self.assertTrue(TestLexer.checkLexeme(INPUT, EXPECT,135))             
    def test_string19(self):
        INPUT = """\"E.e.-3.e.-O.F\""""
        EXPECT = 'E.e.-3.e.-O.F,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(INPUT, EXPECT,136))        
    def test_string20(self):
        INPUT = """NoMoneyButCrazy\n\""""
        EXPECT = 'NoMoneyButCrazy,Unclosed String: '
        self.assertTrue(TestLexer.checkLexeme(INPUT, EXPECT,137))        
    def test_operator(self):
        INPUT = """{==>=<<==}"""
        EXPECT = '{,==,>=,<,<=,=,},<EOF>'
        self.assertTrue(TestLexer.checkLexeme(INPUT, EXPECT,138))        
    def test_Seperators(self):
        INPUT = """{a+2/2 = {a}(b)}"""
        EXPECT = '{,a,+,2,/,2,=,{,a,},(,b,),},<EOF>'
        self.assertTrue(TestLexer.checkLexeme(INPUT, EXPECT,139))        
    def test_Literals(self):
        INPUT = """-222131231824679+asasf126734"""
        EXPECT = '-,222131231824679,+,asasf126734,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(INPUT, EXPECT,140))        
    def test_key(self):
        INPUT = """Int float boolean string \n"""
        EXPECT = 'Int,float,boolean,string,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(INPUT, EXPECT,141))
    def test_Cmt(self):
        INPUT = """//abcxyz\t\b\nabc"""
        EXPECT = 'abc,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(INPUT, EXPECT,142))        
    def test_Cmt2(self):
        INPUT = """/*abcxyz\t\b\n//abc*/"""
        EXPECT = '<EOF>'
        self.assertTrue(TestLexer.checkLexeme(INPUT, EXPECT,143))        
    def test_cmt3(self):
        INPUT = """/*abcxyz\n//abc//H/*"""
        EXPECT = '/,*,abcxyz,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(INPUT, EXPECT,144))      
    def test_cmt4(self):
        INPUT = """/*abcxasuifhdu1823y      a Here ??? ~~~~~~~ \\
        asf
        yz\n//abc//H//*"""
        EXPECT = '/,*,abcxasuifhdu1823y,a,Here,Error Token ?'
        self.assertTrue(TestLexer.checkLexeme(INPUT, EXPECT,145))        
    def test_cmt5(self):
        INPUT = """int[] foo(int a, float b[]) {int c[3];...; if (a>0) foo(a-1,b); ...; return c; }"""
        EXPECT = 'int,[,],foo,(,int,a,,,float,b,[,],),{,int,c,[,3,],;,Error Token .'
        self.assertTrue(TestLexer.checkLexeme(INPUT, EXPECT,146))        
    def test_cmt6(self):
        INPUT = """
        boolean b;
// a variable of type boolean
int i;
// a variable of type int
float f;
// a variable of type float
boolean ba[5]; // a variable of type array on boolean
int ia[3];
// a variable of type array on int
float fa[100]; // a variable of type array on float"""
        EXPECT = 'boolean,b,;,int,i,;,float,f,;,boolean,ba,[,5,],;,int,ia,[,3,],;,float,fa,[,100,],;,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(INPUT, EXPECT,147))
    def test_cmt7(self):
        INPUT = """
        "abc/""\""""
        EXPECT = 'abc/,,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(INPUT, EXPECT,148))        
    def test_noName(self):
        INPUT = """"abc/"\n"aa\t\\n\n\n\n\n\n"""
        EXPECT = 'abc/,Unclosed String: aa	\\n'
        self.assertTrue(TestLexer.checkLexeme(INPUT, EXPECT,149))        
    def test_special(self):
        INPUT3 = '\n\n\n\n\n\n\n\"\n\n\n\n\n\n\n'
        EXPECT = 'Unclosed String: '
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,150))
    def test_special2(self):
        INPUT3 = '"4;1\];[];r3[];]12;3[];][d;]"'
        EXPECT = 'Illegal Escape In String: 4;1\]'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,151))
    def test_special3(self):
        INPUT3 = '"u`12QD1H`?????"'
        EXPECT = 'u`12QD1H`?????,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,152))
    def test_special4(self):
        INPUT3 = '"b\rb\b\b\b\b\r\r"'
        EXPECT = 'Unclosed String: b'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,153))
    def test_special5(self):
        INPUT3 = '"????What this ? \n\n\n\n\n\n\n\n\n\"'
        EXPECT = 'Unclosed String: ????What this ? '
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,154))
    def test_special6(self):
        INPUT3 = '"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tebc\n\n\n\n\n\n\n\n\n\n"'
        EXPECT = 'Unclosed String: 																													ebc'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,155))
    def test_special7(self):
        INPUT3 = '/*"asfasfasd123\n\n\n\n\n"'
        EXPECT = '/,*,Unclosed String: asfasfasd123'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,156))
    def test_special8(self):
        INPUT3 = '/*"asfasfasd123\n\n\n\n\n"*//'
        EXPECT = '/,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,157))
    def test_special9(self):
        INPUT3 = '/*"asfasfasd123\n\n\n\n\n"*/********/'
        EXPECT = '*,*,*,*,*,*,*,*,/,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,158))
    def test_special10(self):
        INPUT3 = '//\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n//*/********/'
        EXPECT = '<EOF>'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,159))
    def test_Name(self):
        INPUT3 = '\r\r\r\r\r\r\r\r\rabc'
        EXPECT = 'abc,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,160))
    def test_Name2(self):
        INPUT3 = 'test case a[][?]][][]{//}][][][][][][][]'
        EXPECT = 'test,case,a,[,],[,Error Token ?'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,161))
    def test_Name3(self):
        INPUT3 = '\n\n\r\nb"this is the test but no close\nn\n\n\n\n\n'
        EXPECT = 'b,Unclosed String: this is the test but no close'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,162))
    def test_Name4(self):
        INPUT3 = '"a\s???????'
        EXPECT = 'Illegal Escape In String: a\s'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,163))
    def test_Name5(self):
        INPUT3 = '""\"'
        EXPECT = ',Unclosed String: '
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,164))
    def test_Name6(self):
        INPUT3 = '"\\n'
        EXPECT = 'Unclosed String: \\n'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,165))
    def test_Name7(self):
        INPUT3 = '//*//239u929j9032j9r0j'
        EXPECT = '<EOF>'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,166))
    def test_Name8(self):
        INPUT3 = '/~~~~//\n\m\m\m\m\m\m\m\m'
        EXPECT = '/,Error Token ~'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,167))
    def test_Name9(self):
        INPUT3 = """void Func(){
}"""
        EXPECT = 'void,Func,(,),{,},<EOF>'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,168))
    def test_Name10(self):
        INPUT3 = """void Func(){
    a[3] ???
}"""
        EXPECT = 'void,Func,(,),{,a,[,3,],Error Token ?'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,169))
    def test_Name11(self):
        INPUT3 = """void Fu?nc(){
    ???a[3] ???
}"""
        EXPECT = 'void,Fu,Error Token ?'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,170))
    def test_Name12(self):
        INPUT3 = """voaid Fu?nc(){
    ???a[3] ???
}"""
        EXPECT = 'voaid,Fu,Error Token ?'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,170))
    def test_Name13(self):
        INPUT3 = """./hereis comman"""
        EXPECT = 'Error Token .'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,171))
    def test_Name14(self):
        INPUT3 = """/*./hereis comman"""
        EXPECT = '/,*,Error Token .'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,172))
    def test_Name15(self):
        INPUT3 = """return abc zub"""
        EXPECT = 'return,abc,zub,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,173))
    def test_Name16(self):
        INPUT3 = """r\rr\rr\r\r\rr\\rr\\r\rr\r\\r\r\r\r\r\rrr\\r\rr\r\r\\r\r"""
        EXPECT = 'r,r,r,r,Error Token \\'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,174))
    def test_Name17(self):
        INPUT3 = """\n\n\n\n\n\n\n\n\n\n\n\n\n\n
        n\n\n\\n\n\n\n\\n\n\n\n\n
        n\n\\n\n\n\\?"""
        EXPECT = 'n,Error Token \\'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,175))
    def test_Name18(self):
        INPUT3 = """9u3425+ 2349 // /324 /1489u"""
        EXPECT = '9,u3425,+,2349,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,176))
    def test_Name19(self):
        INPUT3 = """9u3425+ 2349 / /324 /1489u"""
        EXPECT = '9,u3425,+,2349,/,/,324,/,1489,u,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,177))
    def test_Name20(self):
        INPUT3 = """9u3425+?/*/ 2349 / /324 /1489u"""
        EXPECT = '9,u3425,+,Error Token ?'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,178))
    def test_Name21(self):
        INPUT3 = """\n\n\n\n9u34n'\n\n\n25+?/*/ 2349 / /324 /1489u"""
        EXPECT = '9,u34n,Error Token \''
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,179))
    def test_Name22(self):
        INPUT3 = """\n\n\n\n9u34n\n\n\n2q14i90135+?/*/ 2349 / /324 /1489u"""
        EXPECT = '9,u34n,2,q14i90135,+,Error Token ?'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,180))
    def test_Name23(self):
        INPUT3 = """\n\n\n\n\n\n\ntttttt\\t\t\t\\n9u34n\n\n\n2q14i90135+?/*/ 2349 / /324 /1489u"""
        EXPECT = 'tttttt,Error Token \\'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,181))
    def test_Name24(self):
        INPUT3 = """\n\n\//90135+?/*/ 2349 / /324 /1489u"""
        EXPECT = 'Error Token \\'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,182))
    def test_Name25(self):
        INPUT3 = """\n\n/*\\//90135+?/*/ 2349 / /324 /1489u"""
        EXPECT = '2349,/,/,324,/,1489,u,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,183))
    def test_Name26(self):
        INPUT3 = """"/////////////////////////////"""
        EXPECT = 'Unclosed String: /////////////////////////////'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,184))
    def test_Name27(self):
        INPUT3 = """"////////////\n\n\n\n\n\n/////////////////"""
        EXPECT = 'Unclosed String: ////////////'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,185))
    def test_Name28(self):
        INPUT3 = """"/////\r\r\r\r///////\n\n\n\n\n\n/////////////////"""
        EXPECT = 'Unclosed String: /////'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,186))
    def test_Name29(self):
        INPUT3 = """"/////"\r\r\r\r///////\n\n\n\n\n\n/////////////////"""
        EXPECT = '/////,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,187))
    def test_Name30(self):
        INPUT3 = """"/\t////"\r\r\r\r/\t//////\n\n\n\n\n\n/////////////////"""
        EXPECT = '/	////,/,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,188))
    def test_Name31(self):
        INPUT3 = """"/\t////"\r\r\r\r/\t//////\n\n\n\n\n\n/\c////////////////"""
        EXPECT = '/	////,/,/,Error Token \\'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,189))
    def test_Name32(self):
        INPUT3 = """"/\t////"\r\r\r\r/\t//////\n\n\n\n\n\n/\c///////MyTestLinHnguye/////////"""
        EXPECT = '/	////,/,/,Error Token \\'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,190))
    def test_Name33(self):
        INPUT3 = """"/\t////"\r\r\r\r/\t//////\n\n\nLinHnguye/////////"""
        EXPECT = '/	////,/,LinHnguye,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,191))
    def test_Name34(self):
        INPUT3 = """"/\t////"\r\r\r\r/\t//////\n\n\nLinH//nguye/////////"""
        EXPECT = '/	////,/,LinH,<EOF>'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,192))
    def test_Name35(self):
        INPUT3 = """"/\t////"\r\r\r\r/\t//////\n\n\nLinH/nguye " """
        EXPECT = '/	////,/,LinH,/,nguye,Unclosed String:  '
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,193))
    def test_Name36(self):
        INPUT3 = """"/\t////\r\r\r\r/\t//////\n\n\nLinH/nguye " """
        EXPECT = 'Unclosed String: /	////'
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,194))
    def test_Name37(self):
        INPUT3 = """"/\t////"\r///\n\n\nLinH/nguye " """
        EXPECT = '/	////,LinH,/,nguye,Unclosed String:  '
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,195))
    def test_Name38(self):
        INPUT3 = """"/\t////"\r/\nLinH/nguye " """
        EXPECT = '/	////,/,LinH,/,nguye,Unclosed String:  '
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,196))
    def test_Name39(self):
        INPUT3 = """"/\t////"\r/\nLinH/nguye " """
        EXPECT = '/	////,/,LinH,/,nguye,Unclosed String:  '
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,197))
    def test_Name40(self):
        INPUT3 = """"/\t////"\r/nguye " """
        EXPECT = '/	////,/,nguye,Unclosed String:  '
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,198))
    def test_Name41(self):
        INPUT3 = """"/\t"\r/nguye " """
        EXPECT = '/	,/,nguye,Unclosed String:  '
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,199))
    def test_Name42(self):
        INPUT3 = """"/\t"guye " """
        EXPECT = '/	,guye,Unclosed String:  '
        self.assertTrue(TestLexer.checkLexeme(INPUT3, EXPECT,200))