import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))

    def test_wrong_lower_identifier(self):
        """test wrong identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc.","abc,Error Token .",102))

    def test_real(self):
        self.assertTrue(TestLexer.checkLexeme("1.234","1.234,<EOF>",103))

    def test_wrong_real1(self):
        self.assertTrue(TestLexer.checkLexeme("1.234e-10","1.234e-10,<EOF>",104))

    def test_wrong_real2(self):
        self.assertTrue(TestLexer.checkLexeme(".234e-10","Error Token .",105))

    def test_wrong_real3(self):
        self.assertTrue(TestLexer.checkLexeme("12.e-10","Error Token 1",106))

    def test_string_1(self):
        self.assertTrue(TestLexer.checkLexeme("''", "'',<EOF>", 108))

    def test_string_1(self):
        self.assertTrue(TestLexer.checkLexeme("'Hoang Phuc'", "'Hoang Phuc',<EOF>", 108))

    def test_string_2(self):
        self.assertTrue(TestLexer.checkLexeme("'hello''eab'", "'hello''eab',<EOF>", 109))

    def test_string_3(self):
        self.assertTrue(TestLexer.checkLexeme("'L02_10''a", "'L02_10',Error Token '", 110))