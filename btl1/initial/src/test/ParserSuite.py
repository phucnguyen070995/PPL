import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_var_dec_1(self):
        """Simple program: int main() {} """
        input = """Var: a = 5;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_var_dec_2(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    def test_var_dec_3(self):
        """Miss variable"""
        input = """Var: b[2][3] = {{2,3,4},{4,5,6}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test_var_dec_4(self):
        """Miss variable"""
        input = """Var: c, d = 6, e, f;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_var_dec_5(self):
        """Miss variable"""
        input = """Var: m, n[10];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test_var_dec_6(self):
        """Miss variable"""
        input = """Var: n[10], m;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test_assignment_stm_1(self):
        """Miss variable"""
        input = """a[3 + foo(2)] = a[b[2][3]] + 4;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test_assignment_stm_2(self):
        """Miss variable"""
        input = """v = (4. \. 3.) *. 3.14 *. r *. r *. r;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))