import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_identifier_1(self):
        """test identifiers"""
        # success
        self.assertTrue(TestLexer.checkLexeme("abcd","abcd,<EOF>",101))
    def test_identifier_2(self):
        """test identifiers"""
        # success
        self.assertTrue(TestLexer.checkLexeme("a1cd","a1cd,<EOF>",102))
    def test_identifier_3(self):
        """test identifiers"""
        # success
        self.assertTrue(TestLexer.checkLexeme("a1Ad","a1Ad,<EOF>",103))
    def test_identifier_4(self):
        """test identifiers"""
        # success
        self.assertTrue(TestLexer.checkLexeme("a","a,<EOF>",104))
    def test_identifier_5(self):
        """test identifiers"""
        # success
        self.assertTrue(TestLexer.checkLexeme("a_a","a_a,<EOF>",105))
    def test_identifier_6(self):
        """test identifiers"""
        # success
        self.assertTrue(TestLexer.checkLexeme("a_a123","a_a123,<EOF>",106))
    def test_identifier_7(self):
        """test identifiers"""
        # success
        self.assertTrue(TestLexer.checkLexeme("a_","a_,<EOF>",107))
    def test_identifier_8(self):
        """test identifiers"""
        # success
        self.assertTrue(TestLexer.checkLexeme("a____","a____,<EOF>",108))
    def test_identifier_9(self):
        """test identifiers"""
        # success
        self.assertTrue(TestLexer.checkLexeme("a1a1a1a1__AAA","a1a1a1a1__AAA,<EOF>",109))
    def test_identifier_10(self):
        """test identifiers"""
        # success
        self.assertTrue(TestLexer.checkLexeme("A_a_1_A","Error Token A",110))
    def test_identifier_11(self):
        """test identifiers"""
        # failure
        self.assertTrue(TestLexer.checkLexeme("Abcd","Error Token A",111))
    def test_identifier_12(self):
        """test identifiers"""
        # failure
        self.assertTrue(TestLexer.checkLexeme("11cd","11,cd,<EOF>",112))
    def test_identifier_13(self):
        """test identifiers"""
        # failure
        self.assertTrue(TestLexer.checkLexeme("11Ad","11,Error Token A",113))
    def test_identifier_14(self):
        """test identifiers"""
        # failure
        self.assertTrue(TestLexer.checkLexeme("_","Error Token _",114))
    def test_identifier_15(self):
        """test identifiers"""
        # failure
        self.assertTrue(TestLexer.checkLexeme("._aA",".,Error Token _",115))
    def test_identifier_16(self):
        """test identifiers"""
        # failure
        self.assertTrue(TestLexer.checkLexeme("*A123","*,Error Token A",116))
    def test_identifier_17(self):
        """test identifiers"""
        # failure
        self.assertTrue(TestLexer.checkLexeme("-Aa_","-,Error Token A",117))
    def test_identifier_18(self):
        """test identifiers"""
        # failure
        self.assertTrue(TestLexer.checkLexeme("+a____","+,a____,<EOF>",118))
    def test_identifier_19(self):
        """test identifiers"""
        # failure
        self.assertTrue(TestLexer.checkLexeme("a+","a,+,<EOF>",119))
    def test_identifier_20(self):
        """test identifiers"""
        # failure
        self.assertTrue(TestLexer.checkLexeme("a_aA.","a_aA,.,<EOF>",120))
    def test_array_1(self):
        """test identifiers"""
        # failure
        self.assertTrue(TestLexer.checkLexeme("{1,2,3}","{1,2,3},<EOF>",121))
    def test_array_2(self):
        """test identifiers"""
        # failure
        self.assertTrue(TestLexer.checkLexeme("{{1,3},{2,1},{1,2}}","{{1,3},{2,1},{1,2}},<EOF>",122))
    def test_array_3(self):
        """test identifiers"""
        # failure
        self.assertTrue(TestLexer.checkLexeme("{{{1}},{{2}},{3}}","{{{1}},{{2}},{3}},<EOF>",123))
    def test_array_4(self):
        """test identifiers"""
        # failure
        self.assertTrue(TestLexer.checkLexeme("{{1,2},{{2}},{3}}","{{1,2},{{2}},{3}},<EOF>",124))
    def test_array_5(self):
        """test identifiers"""
        # failure
        self.assertTrue(TestLexer.checkLexeme("{{1,{2}}}","{,{,1,,,{2},},},<EOF>",125))
    def test_array_6(self):
        """test identifiers"""
        # failure
        self.assertTrue(TestLexer.checkLexeme("{{1,2,1},{1,2},{1}}","{{1,2,1},{1,2},{1}},<EOF>",126))
    def test_array_7(self):
        """test identifiers"""
        # failure
        self.assertTrue(TestLexer.checkLexeme("{{1.2,2.3,1.4},{1.5,2.6},{1.7}}","{{1.2,2.3,1.4},{1.5,2.6},{1.7}},<EOF>",126))
    def test_string_1(self):
        """test string"""
        # failure
        self.assertTrue(TestLexer.checkLexeme('"This is a string containing tab \t" ','"This is a string containing tab 	",<EOF>',127))
    def test_string_2(self):
        """test string"""
        # failure
        self.assertTrue(TestLexer.checkLexeme('"This is a string containing tab\n \t" ','Error Token "',128))
    def test_string_3(self):
        """test string"""
        # failure
        self.assertTrue(TestLexer.checkLexeme('"He asked me: \'"Where is John?\'""','"He asked me: \'"Where is John?\'"",<EOF>',129))
    def test_string_4(self):
        """test string"""
        # failure
        self.assertTrue(TestLexer.checkLexeme('"He asked" me: \'"Where is John?\'""','"He asked",me,:,Error Token \'',130))
    def test_string_5(self):
        """test string"""
        # failure
        self.assertTrue(TestLexer.checkLexeme('""','"",<EOF>',131))
    def test_float_1(self):
        """test string"""
        # failure
        self.assertTrue(TestLexer.checkLexeme('12.0e3','12.0e3,<EOF>',132))
    def test_float_2(self):
        """test string"""
        # failure
        self.assertTrue(TestLexer.checkLexeme('12e3','12e3,<EOF>',133))
    def test_float_3(self):
        """test string"""
        # failure
        self.assertTrue(TestLexer.checkLexeme('12.e5','12.e5,<EOF>',134))
    def test_float_4(self):
        """test string"""
        # failure
        self.assertTrue(TestLexer.checkLexeme('12.0e+3','12.0e+3,<EOF>',135))
    def test_float_5(self):
        """test string"""
        # failure
        self.assertTrue(TestLexer.checkLexeme('12000.','12000.,<EOF>',136))
    def test_float_6(self):
        """test string"""
        # failure
        self.assertTrue(TestLexer.checkLexeme('120000e-1','120000e-1,<EOF>',137))
    def test_aray_boolean_1(self):
        """test string"""
        # failure
        self.assertTrue(TestLexer.checkLexeme('{{True,False},{{True}},{False}}','{{True,False},{{True}},{False}},<EOF>',138))
    def test_aray_boolean_2(self):
        """test string"""
        # failure
        self.assertTrue(TestLexer.checkLexeme('{{12.e5,12.e5},{{12.e5}},{12.e5}}','{{12.e5,12.e5},{{12.e5}},{12.e5}},<EOF>',139))