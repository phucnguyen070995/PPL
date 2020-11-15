import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_ast_0(self):
        input = """Var:x;"""
        expect = Program([VarDecl(Id("x"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 300))
    def test_ast_1(self):
        input = """Var: x = 20, y=50, z;"""
        expect = Program([VarDecl(Id('x'),[],IntLiteral('20')),VarDecl(Id('y'),[],IntLiteral('50')),VarDecl(Id('z'),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    def test_ast_2(self):
        input = """Var: x = "This is string", y = 2.2e-1;  """
        expect = Program([VarDecl(Id('x'),[],StringLiteral("""This is string""")),VarDecl(Id('y'),[],FloatLiteral('0.22'))])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    def test_ast_3(self):
        input = """Var: x[1][2] = {1,2,3}, y[3];"""
        expect = Program([VarDecl(Id('x'),[1,2],ArrayLiteral([IntLiteral('1'),IntLiteral('2'),IntLiteral('3')])),VarDecl(Id('y'),[3],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    def test_ast_4(self):
        input = """Var: x = True;"""
        expect = Program([VarDecl(Id('x'),[],BooleanLiteral('true'))])
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
    def test_ast_5(self):
        input = """Var: x[1] = {20};"""
        expect = Program([VarDecl(Id('x'),[1],ArrayLiteral([IntLiteral('20')]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
    def test_ast_6(self):
        input = """Var: x[1][2] = {20,30};"""
        expect = Program([VarDecl(Id('x'),[1,2],ArrayLiteral([IntLiteral('20'),IntLiteral('30')]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    def test_ast_7(self):
        input = """Var: x[1] = {20,30,40};"""
        expect = Program([VarDecl(Id('x'),[1],ArrayLiteral([IntLiteral('20'),IntLiteral('30'),IntLiteral('40')]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
    def test_ast_8(self):
        input = """Var: x[0o11] = {20};"""
        expect = Program([VarDecl(Id('x'),[9],ArrayLiteral([IntLiteral('20')]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    def test_ast_9(self):
        input = """Var: x = "String include quote \'"text\'" ";"""
        expect = Program([VarDecl(Id('x'),[],StringLiteral("""String include quote '"text'" """))])
        self.assertTrue(TestAST.checkASTGen(input,expect,309))
    # if statement
    def test_ast_10(self):
        input = """Function: foo
                    Parameter: a,b,c
                    Body:
                        Return a+b+c;
                    EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[Return(BinaryOp('+',BinaryOp('+',Id('a'),Id('b')),Id('c')))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,310))
    def test_ast_11(self):
        input = """Var: a = 1, b =2;
            Function: foo
            Parameter: a,b,c
            Body:
                If a < b Then
                    Return a+b+c;
                ElseIf a == b Then
                    Return a+b;
                Else
                    Return a;
                EndIf.
            EndBody."""
        expect = Program([VarDecl(Id('a'),[],IntLiteral('1')),VarDecl(Id('b'),[],IntLiteral('2')),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[If([(BinaryOp('<',Id('a'),Id('b')),[],[Return(BinaryOp('+',BinaryOp('+',Id('a'),Id('b')),Id('c')))]),(BinaryOp('==',Id('a'),Id('b')),[],[Return(BinaryOp('+',Id('a'),Id('b')))])],([],[Return(Id('a'))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,311))
    def test_ast_12(self):
        input = """Var: a = 1, b =2;
            Function: foo
            Parameter: a,b,c
            Body:
                If a <= b Then
                    Return a+b+c;
                Else
                    Return a;
                EndIf.
            EndBody."""
        expect = Program([VarDecl(Id('a'),[],IntLiteral('1')),VarDecl(Id('b'),[],IntLiteral('2')),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[If([(BinaryOp('<=',Id('a'),Id('b')),[],[Return(BinaryOp('+',BinaryOp('+',Id('a'),Id('b')),Id('c')))])],([],[Return(Id('a'))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,312))
    def test_ast_13(self):
        input = """Var: a = 1, b =2;
            Function: foo
            Parameter: a,b,c
            Body:
                If a >=. b Then
                    Return a+b+c;
                EndIf.
            EndBody."""
        expect = Program([VarDecl(Id('a'),[],IntLiteral('1')),VarDecl(Id('b'),[],IntLiteral('2')),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[If([(BinaryOp('>=.',Id('a'),Id('b')),[],[Return(BinaryOp('+',BinaryOp('+',Id('a'),Id('b')),Id('c')))])],[])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,313))
    def test_ast_14(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                If a < b Then
                    While True Do
                        foo(a,b);
                    EndWhile.
                ElseIf a == b Then
                    Return a+b;
                Else
                    Return a;
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[If([(BinaryOp('<',Id('a'),Id('b')),[],[While(BooleanLiteral('true'),([],[CallStmt(Id('foo'),[Id('a'),Id('b')])]))]),(BinaryOp('==',Id('a'),Id('b')),[],[Return(BinaryOp('+',Id('a'),Id('b')))])],([],[Return(Id('a'))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,314))
    def test_ast_15(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                If a < b Then
                    While True Do
                        foo(a,b);
                    EndWhile.
                ElseIf a == b Then
                    Return a+b;
                Else
                    Return a;
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[If([(BinaryOp('<',Id('a'),Id('b')),[],[While(BooleanLiteral('true'),([],[CallStmt(Id('foo'),[Id('a'),Id('b')])]))]),(BinaryOp('==',Id('a'),Id('b')),[],[Return(BinaryOp('+',Id('a'),Id('b')))])],([],[Return(Id('a'))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,315))
    def test_ast_16(self):
        input = """Function: foo
            Parameter: a[2],b,c
            Body:
                If a[1] < b Then
                    While True Do
                        foo(a[0],b);
                    EndWhile.
                ElseIf a[1] == b Then
                    Return a[0]+b;
                Else
                    Return a[0];
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[2],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[If([(BinaryOp('<',ArrayCell(Id('a'),[IntLiteral('1')]),Id('b')),[],[While(BooleanLiteral('true'),([],[CallStmt(Id('foo'),[ArrayCell(Id('a'),[IntLiteral('0')]),Id('b')])]))]),(BinaryOp('==',ArrayCell(Id('a'),[IntLiteral('1')]),Id('b')),[],[Return(BinaryOp('+',ArrayCell(Id('a'),[IntLiteral('0')]),Id('b')))])],([],[Return(ArrayCell(Id('a'),[IntLiteral('0')]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,316))
    def test_ast_17(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                If a =/= b Then
                    While True Do
                        foo(a,b);
                    EndWhile.
                ElseIf a == b Then
                    Return a+b;
                Else
                    Return a;
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[If([(BinaryOp('=/=',Id('a'),Id('b')),[],[While(BooleanLiteral('true'),([],[CallStmt(Id('foo'),[Id('a'),Id('b')])]))]),(BinaryOp('==',Id('a'),Id('b')),[],[Return(BinaryOp('+',Id('a'),Id('b')))])],([],[Return(Id('a'))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,317))
    def test_ast_18(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                If a == b*c[1][2][3] Then
                    While True Do
                        foo(a,b);
                    EndWhile.
                ElseIf a == b Then
                    Return a+b;
                Else
                    Return a;
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[If([(BinaryOp('==',Id('a'),BinaryOp('*',Id('b'),ArrayCell(Id('c'),[IntLiteral('1'),IntLiteral('2'),IntLiteral('3')]))),[],[While(BooleanLiteral('true'),([],[CallStmt(Id('foo'),[Id('a'),Id('b')])]))]),(BinaryOp('==',Id('a'),Id('b')),[],[Return(BinaryOp('+',Id('a'),Id('b')))])],([],[Return(Id('a'))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,318))
    def test_ast_19(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                If a == b Then
                    While True Do
                        foo(a,b);
                    EndWhile.
                ElseIf a == b Then
                    Return a+b;
                Else
                    If !(a % b == 1) Then
                        Return a;
                    EndIf.
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[If([(BinaryOp('==',Id('a'),Id('b')),[],[While(BooleanLiteral('true'),([],[CallStmt(Id('foo'),[Id('a'),Id('b')])]))]),(BinaryOp('==',Id('a'),Id('b')),[],[Return(BinaryOp('+',Id('a'),Id('b')))])],([],[If([(UnaryOp('!',BinaryOp('==',BinaryOp('%',Id('a'),Id('b')),IntLiteral('1'))),[],[Return(Id('a'))])],[])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,319))
    # for statement
    def test_ast_20(self):
        input = """Function: foo_for
            Parameter: a,b,c
            Body:
                For (i = 1, i < 10, 2) Do
                    If a % b == 1 Then
                        Return a;
                    EndIf.
                EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id('foo_for'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[For(Id('i'),IntLiteral('1'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('2'),([],[If([(BinaryOp('==',BinaryOp('%',Id('a'),Id('b')),IntLiteral('1')),[],[Return(Id('a'))])],[])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,320))
    def test_ast_21(self):
        input = """Function: foo_for
            Parameter: a,b,c
            Body:
                For (i = 1, i < 10, 2) Do
                    For (i = 1, i > 10, 3) Do
                        Return a;
                    EndFor.
                EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id('foo_for'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[For(Id('i'),IntLiteral('1'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('2'),([],[For(Id('i'),IntLiteral('1'),BinaryOp('>',Id('i'),IntLiteral('10')),IntLiteral('3'),([],[Return(Id('a'))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,321))
    def test_ast_22(self):
        input = """Function: foo_for
            Parameter: a,b,c
            Body:
                For (i = 1, i < 10, foo(1)) Do
                    For (i = 1, i > 10, i) Do
                        Return a;
                    EndFor.
                EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id('foo_for'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[For(Id('i'),IntLiteral('1'),BinaryOp('<',Id('i'),IntLiteral('10')),CallExpr(Id('foo'),[IntLiteral('1')]),([],[For(Id('i'),IntLiteral('1'),BinaryOp('>',Id('i'),IntLiteral('10')),Id('i'),([],[Return(Id('a'))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,322))
    def test_ast_23(self):
        input = """Function: foo_for
            Parameter: a,b,c
            Body:
                For (i = foo(1), i < foo(10), foo(1)) Do
                    For (j = i, j < i + 10, i) Do
                        Return a;
                    EndFor.
                EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id('foo_for'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[For(Id('i'),CallExpr(Id('foo'),[IntLiteral('1')]),BinaryOp('<',Id('i'),CallExpr(Id('foo'),[IntLiteral('10')])),CallExpr(Id('foo'),[IntLiteral('1')]),([],[For(Id('j'),Id('i'),BinaryOp('<',Id('j'),BinaryOp('+',Id('i'),IntLiteral('10'))),Id('i'),([],[Return(Id('a'))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,323))
    def test_ast_24(self):
        input = """Function: foo_for
            Parameter: a,b,c
            Body:
                For (i = 1, i , i) Do
                    For (j = i, j < i + 10, i) Do
                        
                    EndFor.
                EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id('foo_for'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[For(Id('i'),IntLiteral('1'),Id('i'),Id('i'),([],[For(Id('j'),Id('i'),BinaryOp('<',Id('j'),BinaryOp('+',Id('i'),IntLiteral('10'))),Id('i'),([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
    def test_ast_25(self):
        input = """Function: foo_for
            Parameter: a,b,c
            Body:
                For (i = 1, i , i) Do
                    For (j = i + 1, j < i + 10, i) Do
                        Return a;
                    EndFor.
                EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id('foo_for'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[For(Id('i'),IntLiteral('1'),Id('i'),Id('i'),([],[For(Id('j'),BinaryOp('+',Id('i'),IntLiteral('1')),BinaryOp('<',Id('j'),BinaryOp('+',Id('i'),IntLiteral('10'))),Id('i'),([],[Return(Id('a'))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
    def test_ast_26(self):
        input = """Function: foo_for
            Parameter: a,b,c
            Body:
                For (i = 1, i < 5, i) Do
                    For (j = i, j < i + 10, i) Do
                        Return foo_for()[1];
                    EndFor.
                EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id('foo_for'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[For(Id('i'),IntLiteral('1'),BinaryOp('<',Id('i'),IntLiteral('5')),Id('i'),([],[For(Id('j'),Id('i'),BinaryOp('<',Id('j'),BinaryOp('+',Id('i'),IntLiteral('10'))),Id('i'),([],[Return(ArrayCell(CallExpr(Id('foo_for'),[]),[IntLiteral('1')]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,326))
    def test_ast_27(self):
        input = """Function: foo_for
            Parameter: a,b,c
            Body:
                For (i = i, i, i) Do
                    For (j = i[1], j < i + 10, i) Do
                        Return a;
                    EndFor.
                EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id('foo_for'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[For(Id('i'),Id('i'),Id('i'),Id('i'),([],[For(Id('j'),ArrayCell(Id('i'),[IntLiteral('1')]),BinaryOp('<',Id('j'),BinaryOp('+',Id('i'),IntLiteral('10'))),Id('i'),([],[Return(Id('a'))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
    def test_ast_28(self):
        input = """Function: foo_for
            Parameter: a,b,c
            Body:
                For (i = i, i, i) Do
                    For (j = i, j < i + 10, i) Do
                        Return a * foo(b);
                    EndFor.
                EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id('foo_for'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[For(Id('i'),Id('i'),Id('i'),Id('i'),([],[For(Id('j'),Id('i'),BinaryOp('<',Id('j'),BinaryOp('+',Id('i'),IntLiteral('10'))),Id('i'),([],[Return(BinaryOp('*',Id('a'),CallExpr(Id('foo'),[Id('b')])))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,328))
    def test_ast_29(self):
        input = """Function: foo_for
            Parameter: a,b,c
            Body:
                For (i = i, i, i) Do
                    For (j = i, j < i + 10, 1) Do
                        Return a;
                    EndFor.
                EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id('foo_for'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[For(Id('i'),Id('i'),Id('i'),Id('i'),([],[For(Id('j'),Id('i'),BinaryOp('<',Id('j'),BinaryOp('+',Id('i'),IntLiteral('10'))),IntLiteral('1'),([],[Return(Id('a'))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    # test while statmenet
    def test_ast_30(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                While True Do
                    foo(a,b);
                EndWhile.
            EndBody."""
        expect = Program([FuncDecl(Id('foo_while'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[While(BooleanLiteral('true'),([],[CallStmt(Id('foo'),[Id('a'),Id('b')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,330))
    def test_ast_31(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                While a == b Do
                    foo(a,b);
                EndWhile.
            EndBody."""
        expect = Program([FuncDecl(Id('foo_while'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[While(BinaryOp('==',Id('a'),Id('b')),([],[CallStmt(Id('foo'),[Id('a'),Id('b')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,331))
    def test_ast_32(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                While foo(a,b) == b Do
                    foo(a,b);
                EndWhile.
            EndBody."""
        expect = Program([FuncDecl(Id('foo_while'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[While(BinaryOp('==',CallExpr(Id('foo'),[Id('a'),Id('b')]),Id('b')),([],[CallStmt(Id('foo'),[Id('a'),Id('b')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,332))
    def test_ast_33(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                While i < 10 Do
                    print(a[i]);
                    i = i + 1;
                EndWhile.
            EndBody."""
        expect = Program([FuncDecl(Id('foo_while'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[While(BinaryOp('<',Id('i'),IntLiteral('10')),([],[CallStmt(Id('print'),[ArrayCell(Id('a'),[Id('i')])]),Assign(Id('i'),BinaryOp('+',Id('i'),IntLiteral('1')))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,333))
    def test_ast_34(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                While i < 10 Do
                    print(a[i]);
                    While j < i Do
                        print(a[j]);
                        j = j + 1;
                    EndWhile.
                    i = i + 1;
                EndWhile.
            EndBody."""
        expect = Program([FuncDecl(Id('foo_while'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[While(BinaryOp('<',Id('i'),IntLiteral('10')),([],[CallStmt(Id('print'),[ArrayCell(Id('a'),[Id('i')])]),While(BinaryOp('<',Id('j'),Id('i')),([],[CallStmt(Id('print'),[ArrayCell(Id('a'),[Id('j')])]),Assign(Id('j'),BinaryOp('+',Id('j'),IntLiteral('1')))])),Assign(Id('i'),BinaryOp('+',Id('i'),IntLiteral('1')))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,334))
    def test_ast_35(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                While i < 10 Do
                    print(a[i]);
                    While j < i Do
                        print(a[j]);
                        j = {1,2,3,4,5};
                    EndWhile.
                    i = i + 1;
                EndWhile.
            EndBody."""
        expect = Program([FuncDecl(Id('foo_while'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[While(BinaryOp('<',Id('i'),IntLiteral('10')),([],[CallStmt(Id('print'),[ArrayCell(Id('a'),[Id('i')])]),While(BinaryOp('<',Id('j'),Id('i')),([],[CallStmt(Id('print'),[ArrayCell(Id('a'),[Id('j')])]),Assign(Id('j'),ArrayLiteral([IntLiteral('1'),IntLiteral('2'),IntLiteral('3'),IntLiteral('4'),IntLiteral('5')]))])),Assign(Id('i'),BinaryOp('+',Id('i'),IntLiteral('1')))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,335))
    def test_ast_36(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                While i < 10 Do
                    print(a[i]);
                    While j < i Do
                        print(a[j]);
                        j = j + 1;
                    EndWhile.
                    i = i + 1;
                EndWhile.
            EndBody."""
        expect = Program([FuncDecl(Id('foo_while'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[While(BinaryOp('<',Id('i'),IntLiteral('10')),([],[CallStmt(Id('print'),[ArrayCell(Id('a'),[Id('i')])]),While(BinaryOp('<',Id('j'),Id('i')),([],[CallStmt(Id('print'),[ArrayCell(Id('a'),[Id('j')])]),Assign(Id('j'),BinaryOp('+',Id('j'),IntLiteral('1')))])),Assign(Id('i'),BinaryOp('+',Id('i'),IntLiteral('1')))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,336))
    def test_ast_37(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                While i < 10 Do
                    
                EndWhile.
            EndBody."""
        expect = Program([FuncDecl(Id('foo_while'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[While(BinaryOp('<',Id('i'),IntLiteral('10')),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,337))
    def test_ast_38(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                While i < 10 Do
                    print(a[i]);
                    While j == i Do
                        
                    EndWhile.
                    
                EndWhile.
            EndBody."""
        expect = Program([FuncDecl(Id('foo_while'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[While(BinaryOp('<',Id('i'),IntLiteral('10')),([],[CallStmt(Id('print'),[ArrayCell(Id('a'),[Id('i')])]),While(BinaryOp('==',Id('j'),Id('i')),([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,338))
    def test_ast_39(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                While (((i < 10))) Do
                    print(a[i]);
                    While j == i Do
                        print(a[j]);
                        j = j + 1;
                    EndWhile.
                    
                EndWhile.
            EndBody."""
        expect = Program([FuncDecl(Id('foo_while'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[While(BinaryOp('<',Id('i'),IntLiteral('10')),([],[CallStmt(Id('print'),[ArrayCell(Id('a'),[Id('i')])]),While(BinaryOp('==',Id('j'),Id('i')),([],[CallStmt(Id('print'),[ArrayCell(Id('a'),[Id('j')])]),Assign(Id('j'),BinaryOp('+',Id('j'),IntLiteral('1')))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    # test do while
    def test_ast_40(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                Do
                    print(a[i]);
                    While j == i Do
                        print(a[j]);
                        j = j + 1;
                    EndWhile.
                    i = i + 1;
                While (((i < 10)))
                EndDo.
            EndBody."""
        expect = Program([FuncDecl(Id('foo_while'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[Dowhile(([],[CallStmt(Id('print'),[ArrayCell(Id('a'),[Id('i')])]),While(BinaryOp('==',Id('j'),Id('i')),([],[CallStmt(Id('print'),[ArrayCell(Id('a'),[Id('j')])]),Assign(Id('j'),BinaryOp('+',Id('j'),IntLiteral('1')))])),Assign(Id('i'),BinaryOp('+',Id('i'),IntLiteral('1')))]),BinaryOp('<',Id('i'),IntLiteral('10')))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,340))
    def test_ast_41(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                Do
                    print(a[i]);
                    While j == i Do
                        print(a[j]);
                        j = j + 1;
                    EndWhile.
                    i = i + 1;
                While ( False )
                EndDo.
            EndBody."""
        expect = Program([FuncDecl(Id('foo_while'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[Dowhile(([],[CallStmt(Id('print'),[ArrayCell(Id('a'),[Id('i')])]),While(BinaryOp('==',Id('j'),Id('i')),([],[CallStmt(Id('print'),[ArrayCell(Id('a'),[Id('j')])]),Assign(Id('j'),BinaryOp('+',Id('j'),IntLiteral('1')))])),Assign(Id('i'),BinaryOp('+',Id('i'),IntLiteral('1')))]),BooleanLiteral('false'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,341))
    def test_ast_42(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                Do
                    ** Empty While **
                While ( False )
                EndDo.
            EndBody."""
        expect = Program([FuncDecl(Id('foo_while'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[Dowhile(([],[]),BooleanLiteral('false'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,342))
    def test_ast_43(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                Do
                    Do
                        Return a;
                    While ( False )
                    EndDo.
                While ( False )
                EndDo.
            EndBody."""
        expect = Program([FuncDecl(Id('foo_while'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[Dowhile(([],[Dowhile(([],[Return(Id('a'))]),BooleanLiteral('false'))]),BooleanLiteral('false'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,343))
    def test_ast_44(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                Do
                    Do
                        Return a;
                    While ( 2 + 3 < 4 )
                    EndDo.
                While ( False )
                EndDo.
            EndBody."""
        expect = Program([FuncDecl(Id('foo_while'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[Dowhile(([],[Dowhile(([],[Return(Id('a'))]),BinaryOp('<',BinaryOp('+',IntLiteral('2'),IntLiteral('3')),IntLiteral('4')))]),BooleanLiteral('false'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,344))
    def test_ast_45(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                Do
                    Do
                        Return a;
                    While ( False )
                    EndDo.
                While ( False )
                EndDo.
            EndBody."""
        expect = Program([FuncDecl(Id('foo_while'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[Dowhile(([],[Dowhile(([],[Return(Id('a'))]),BooleanLiteral('false'))]),BooleanLiteral('false'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,345))
    def test_ast_46(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                Do
                    Do
                        Return a;
                    While(True)
                    EndDo.
                While ( False && True )
                EndDo.
            EndBody."""
        expect = Program([FuncDecl(Id('foo_while'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[Dowhile(([],[Dowhile(([],[Return(Id('a'))]),BooleanLiteral('true'))]),BinaryOp('&&',BooleanLiteral('false'),BooleanLiteral('true')))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,346))
    def test_ast_47(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                Do
                    While i < 10 Do
                        print(a[i]);
                        While j < i Do
                            **print(a[j]);**
                            j = j + 1;
                        EndWhile.
                        i = i + 1;
                    EndWhile.
                While ( False )
                EndDo.
            EndBody."""
        expect = Program([FuncDecl(Id('foo_while'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[Dowhile(([],[While(BinaryOp('<',Id('i'),IntLiteral('10')),([],[CallStmt(Id('print'),[ArrayCell(Id('a'),[Id('i')])]),While(BinaryOp('<',Id('j'),Id('i')),([],[Assign(Id('j'),BinaryOp('+',Id('j'),IntLiteral('1')))])),Assign(Id('i'),BinaryOp('+',Id('i'),IntLiteral('1')))]))]),BooleanLiteral('false'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,347))
    def test_ast_48(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                Do
                    While i < 10 Do
                        print(a[i]);
                        While j < i Do
                            **print(a[j]);**
                            For (i = 1, i < 10, foo(1)) Do
                                For (i = 1, i > 10, i) Do
                                    Return a;
                                EndFor.
                            EndFor.
                        EndWhile.
                        i = i + 1;
                    EndWhile.
                While ( False )
                EndDo.
            EndBody."""
        expect = Program([FuncDecl(Id('foo_while'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[Dowhile(([],[While(BinaryOp('<',Id('i'),IntLiteral('10')),([],[CallStmt(Id('print'),[ArrayCell(Id('a'),[Id('i')])]),While(BinaryOp('<',Id('j'),Id('i')),([],[For(Id('i'),IntLiteral('1'),BinaryOp('<',Id('i'),IntLiteral('10')),CallExpr(Id('foo'),[IntLiteral('1')]),([],[For(Id('i'),IntLiteral('1'),BinaryOp('>',Id('i'),IntLiteral('10')),Id('i'),([],[Return(Id('a'))]))]))])),Assign(Id('i'),BinaryOp('+',Id('i'),IntLiteral('1')))]))]),BooleanLiteral('false'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,348))
    def test_ast_49(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                Do
                    Return a;
                While(True)
                EndDo.

            EndBody."""
        expect = Program([FuncDecl(Id('foo_while'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[Dowhile(([],[Return(Id('a'))]),BooleanLiteral('true'))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    # test break statement
    def test_ast_50(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                If a < b Then
                    While True Do
                        Break;
                    EndWhile.
                ElseIf a == b Then
                    For (i = 1, i < 10, 1) Do
                        foo(b,a);
                    EndFor.
                Else
                    Do
                        
                    While (a <=. 10.0)
                    EndDo.
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[If([(BinaryOp('<',Id('a'),Id('b')),[],[While(BooleanLiteral('true'),([],[Break()]))]),(BinaryOp('==',Id('a'),Id('b')),[],[For(Id('i'),IntLiteral('1'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('1'),([],[CallStmt(Id('foo'),[Id('b'),Id('a')])]))])],([],[Dowhile(([],[]),BinaryOp('<=.',Id('a'),FloatLiteral('10.0')))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,350))
    def test_ast_51(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                If a < b Then
                    While True Do
                        Break;
                    EndWhile.
                ElseIf a == b Then
                    For (i = 1, i < 10, 1) Do
                        foo(b,a);
                    EndFor.
                Else
                    Do
                        
                    While (a <=. 10.0)
                    EndDo.
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[If([(BinaryOp('<',Id('a'),Id('b')),[],[While(BooleanLiteral('true'),([],[Break()]))]),(BinaryOp('==',Id('a'),Id('b')),[],[For(Id('i'),IntLiteral('1'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('1'),([],[CallStmt(Id('foo'),[Id('b'),Id('a')])]))])],([],[Dowhile(([],[]),BinaryOp('<=.',Id('a'),FloatLiteral('10.0')))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,351))


    # test continue statement
    def test_ast_52(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                If a < b Then
                    While True Do
                        Continue;
                    EndWhile.
                ElseIf a == b Then
                    For (i = 1, i < 10, 1) Do
                        foo(b,a);
                    EndFor.
                Else
                    Do
                        
                    While (a <=. 10.0)
                    EndDo.
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[If([(BinaryOp('<',Id('a'),Id('b')),[],[While(BooleanLiteral('true'),([],[Continue()]))]),(BinaryOp('==',Id('a'),Id('b')),[],[For(Id('i'),IntLiteral('1'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('1'),([],[CallStmt(Id('foo'),[Id('b'),Id('a')])]))])],([],[Dowhile(([],[]),BinaryOp('<=.',Id('a'),FloatLiteral('10.0')))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,352))
    def test_ast_53(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                If a < b Then
                    While True Do
                        Continue;
                    EndWhile.
                ElseIf a == b Then
                    For (i = 1, i < 10, 1) Do
                        foo(b,a);
                    EndFor.
                Else
                    Do
                        
                    While (a <=. 10.0)
                    EndDo.
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[If([(BinaryOp('<',Id('a'),Id('b')),[],[While(BooleanLiteral('true'),([],[Continue()]))]),(BinaryOp('==',Id('a'),Id('b')),[],[For(Id('i'),IntLiteral('1'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('1'),([],[CallStmt(Id('foo'),[Id('b'),Id('a')])]))])],([],[Dowhile(([],[]),BinaryOp('<=.',Id('a'),FloatLiteral('10.0')))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    # test function call
    def test_ast_54(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                a = boo(1,2.3);
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[Assign(Id('a'),CallExpr(Id('boo'),[IntLiteral('1'),FloatLiteral('2.3')]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,354))
    def test_ast_55(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                a = boo(1, boo(1, foo(1)));
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[Assign(Id('a'),CallExpr(Id('boo'),[IntLiteral('1'),CallExpr(Id('boo'),[IntLiteral('1'),CallExpr(Id('foo'),[IntLiteral('1')])])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,355))
    def test_ast_56(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                Return boo( a[12] );
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[Return(CallExpr(Id('boo'),[ArrayCell(Id('a'),[IntLiteral('12')])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,356))
    def test_ast_57(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                Return boo(  );
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[Return(CallExpr(Id('boo'),[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,357))
    def test_ast_58(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                Return boo(2)[1];
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[Return(ArrayCell(CallExpr(Id('boo'),[IntLiteral('2')]),[IntLiteral('1')]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,358))
    def test_ast_59(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                Return boo( ( (1) ) );
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[Return(CallExpr(Id('boo'),[IntLiteral('1')]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,359))


    # summary test
    def test_ast_60(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                If a < b Then
                    While True Do
                        foo(a,b);
                    EndWhile.
                ElseIf a == b Then
                    For (i = 1, i < 10, 1) Do
                        foo(b,a);
                    EndFor.
                Else
                    Return a;
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[If([(BinaryOp('<',Id('a'),Id('b')),[],[While(BooleanLiteral('true'),([],[CallStmt(Id('foo'),[Id('a'),Id('b')])]))]),(BinaryOp('==',Id('a'),Id('b')),[],[For(Id('i'),IntLiteral('1'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('1'),([],[CallStmt(Id('foo'),[Id('b'),Id('a')])]))])],([],[Return(Id('a'))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,360))
    def test_ast_61(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                If a < b Then
                    While True Do
                        foo(a,b);
                    EndWhile.
                ElseIf a == b Then
                    For (i = 1, i < 10, 1) Do
                        foo(b,a);
                    EndFor.
                Else
                    Return a;
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[If([(BinaryOp('<',Id('a'),Id('b')),[],[While(BooleanLiteral('true'),([],[CallStmt(Id('foo'),[Id('a'),Id('b')])]))]),(BinaryOp('==',Id('a'),Id('b')),[],[For(Id('i'),IntLiteral('1'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('1'),([],[CallStmt(Id('foo'),[Id('b'),Id('a')])]))])],([],[Return(Id('a'))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,361))
    def test_ast_62(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                If a < b Then
                    While True Do
                        foo(a,b);
                    EndWhile.
                ElseIf a == b Then
                    For (i = 1, i < 10, 1) Do
                        foo(b,a);
                    EndFor.
                Else
                    Do
                        foo(boo(10));
                    While (a <=. 10.0)
                    EndDo.
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[If([(BinaryOp('<',Id('a'),Id('b')),[],[While(BooleanLiteral('true'),([],[CallStmt(Id('foo'),[Id('a'),Id('b')])]))]),(BinaryOp('==',Id('a'),Id('b')),[],[For(Id('i'),IntLiteral('1'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('1'),([],[CallStmt(Id('foo'),[Id('b'),Id('a')])]))])],([],[Dowhile(([],[CallStmt(Id('foo'),[CallExpr(Id('boo'),[IntLiteral('10')])])]),BinaryOp('<=.',Id('a'),FloatLiteral('10.0')))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_ast_63(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                If a < b Then
                    While True Do
                        
                    EndWhile.
                ElseIf a == b Then
                    For (i = 1, i < 10, 1) Do
                        foo(b,a);
                    EndFor.
                Else
                    Do

                    While (a <=. 10.0)
                    EndDo.
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[If([(BinaryOp('<',Id('a'),Id('b')),[],[While(BooleanLiteral('true'),([],[]))]),(BinaryOp('==',Id('a'),Id('b')),[],[For(Id('i'),IntLiteral('1'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('1'),([],[CallStmt(Id('foo'),[Id('b'),Id('a')])]))])],([],[Dowhile(([],[]),BinaryOp('<=.',Id('a'),FloatLiteral('10.0')))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,363))
    def test_ast_64(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                If a < b Then
                    While True Do
                        Break;
                    EndWhile.
                ElseIf a == b Then
                    For (i = 1, i < 10, 1) Do
                        foo(foo(foo()));
                    EndFor.
                Else
                    Do
                        Continue;
                    While (a \\. 10.0 =/= 10.5)
                    EndDo.
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[If([(BinaryOp('<',Id('a'),Id('b')),[],[While(BooleanLiteral('true'),([],[Break()]))]),(BinaryOp('==',Id('a'),Id('b')),[],[For(Id('i'),IntLiteral('1'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('1'),([],[CallStmt(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[])])])]))])],([],[Dowhile(([],[Continue()]),BinaryOp('=/=',BinaryOp('\.',Id('a'),FloatLiteral('10.0')),FloatLiteral('10.5')))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,364))
    def test_ast_65(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                a = b;
                b = a;
                a = 1 + b;
                If a < b Then
                    While True Do
                        foo(foo(foo()));
                    EndWhile.
                ElseIf a == b Then
                    For (i = 1, i < 10, 1) Do
                        While True Do
                            foo(foo(foo()));
                        EndWhile.
                    EndFor.
                Else
                    Do
                        Continue;
                    While (a \\. 10.0 =/= 10.5)
                    EndDo.
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[Assign(Id('a'),Id('b')),Assign(Id('b'),Id('a')),Assign(Id('a'),BinaryOp('+',IntLiteral('1'),Id('b'))),If([(BinaryOp('<',Id('a'),Id('b')),[],[While(BooleanLiteral('true'),([],[CallStmt(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[])])])]))]),(BinaryOp('==',Id('a'),Id('b')),[],[For(Id('i'),IntLiteral('1'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('1'),([],[While(BooleanLiteral('true'),([],[CallStmt(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[])])])]))]))])],([],[Dowhile(([],[Continue()]),BinaryOp('=/=',BinaryOp('\.',Id('a'),FloatLiteral('10.0')),FloatLiteral('10.5')))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,365))
    def test_ast_66(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                a = 0x123456;
                If a < b Then
                    While True Do
                        Break;
                    EndWhile.
                ElseIf a == b Then
                    For (i = 1, i < 10, 1) Do
                        foo(foo(foo(5)));
                    EndFor.
                Else
                    Do
                        Do
                            Continue;
                        While (a \\. 10.0 =/= 10.5e-3)
                        EndDo.
                    While (a \\. 10.0 =/= 10.5e-3)
                    EndDo.
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[Assign(Id('a'),IntLiteral('1193046')),If([(BinaryOp('<',Id('a'),Id('b')),[],[While(BooleanLiteral('true'),([],[Break()]))]),(BinaryOp('==',Id('a'),Id('b')),[],[For(Id('i'),IntLiteral('1'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('1'),([],[CallStmt(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[IntLiteral('5')])])])]))])],([],[Dowhile(([],[Dowhile(([],[Continue()]),BinaryOp('=/=',BinaryOp('\.',Id('a'),FloatLiteral('10.0')),FloatLiteral('0.0105')))]),BinaryOp('=/=',BinaryOp('\.',Id('a'),FloatLiteral('10.0')),FloatLiteral('0.0105')))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,366))
    def test_ast_67(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                a = 0x123456;
                If a < b Then
                    While True Do
                        Break;
                    EndWhile.
                ElseIf a == b Then
                    For (i = 1, i < 10, 1) Do
                        foo(foo(foo(5)));
                    EndFor.
                Else
                    Do
                        Do
                            Continue;
                        While (a \\. 10.0 =/= 10.5e-3)
                        EndDo.
                    While (a \\. 10.0 =/= 10.5e-3)
                    EndDo.
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[Assign(Id('a'),IntLiteral('1193046')),If([(BinaryOp('<',Id('a'),Id('b')),[],[While(BooleanLiteral('true'),([],[Break()]))]),(BinaryOp('==',Id('a'),Id('b')),[],[For(Id('i'),IntLiteral('1'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('1'),([],[CallStmt(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[IntLiteral('5')])])])]))])],([],[Dowhile(([],[Dowhile(([],[Continue()]),BinaryOp('=/=',BinaryOp('\.',Id('a'),FloatLiteral('10.0')),FloatLiteral('0.0105')))]),BinaryOp('=/=',BinaryOp('\.',Id('a'),FloatLiteral('10.0')),FloatLiteral('0.0105')))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,367))
    def test_ast_68(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                a = 0x123456;
                If a < b Then
                    While True && False && True Do
                        Break;
                    EndWhile.
                ElseIf a == b Then
                    For (i = 1, i < 10, 1) Do
                        foo(foo(foo(5)));
                    EndFor.
                Else
                    Do
                        Do
                            Continue;
                        While (a \\. 10.0 =/= 10.5e-3)
                        EndDo.
                    While (a \\. 10.0 =/= 10.5e-3)
                    EndDo.
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[Assign(Id('a'),IntLiteral('1193046')),If([(BinaryOp('<',Id('a'),Id('b')),[],[While(BinaryOp('&&',BinaryOp('&&',BooleanLiteral('true'),BooleanLiteral('false')),BooleanLiteral('true')),([],[Break()]))]),(BinaryOp('==',Id('a'),Id('b')),[],[For(Id('i'),IntLiteral('1'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('1'),([],[CallStmt(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[IntLiteral('5')])])])]))])],([],[Dowhile(([],[Dowhile(([],[Continue()]),BinaryOp('=/=',BinaryOp('\.',Id('a'),FloatLiteral('10.0')),FloatLiteral('0.0105')))]),BinaryOp('=/=',BinaryOp('\.',Id('a'),FloatLiteral('10.0')),FloatLiteral('0.0105')))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,368))
    def test_ast_69(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                a = 0x123456;
                If (a < b) && (b < c) Then
                    While True && False && True Do
                        Break;
                    EndWhile.
                ElseIf a == b Then
                    For (i = 1, i < 10, 1) Do
                        foo(foo(foo(5)));
                    EndFor.
                Else
                    Do
                        Do
                            Continue;
                        While (a \\. 10.0 =/= 10.5e-3)
                        EndDo.
                    While (a \\. 10.0 =/= 10.5e-3)
                    EndDo.
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None)],([],[Assign(Id('a'),IntLiteral('1193046')),If([(BinaryOp('&&',BinaryOp('<',Id('a'),Id('b')),BinaryOp('<',Id('b'),Id('c'))),[],[While(BinaryOp('&&',BinaryOp('&&',BooleanLiteral('true'),BooleanLiteral('false')),BooleanLiteral('true')),([],[Break()]))]),(BinaryOp('==',Id('a'),Id('b')),[],[For(Id('i'),IntLiteral('1'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('1'),([],[CallStmt(Id('foo'),[CallExpr(Id('foo'),[CallExpr(Id('foo'),[IntLiteral('5')])])])]))])],([],[Dowhile(([],[Dowhile(([],[Continue()]),BinaryOp('=/=',BinaryOp('\.',Id('a'),FloatLiteral('10.0')),FloatLiteral('0.0105')))]),BinaryOp('=/=',BinaryOp('\.',Id('a'),FloatLiteral('10.0')),FloatLiteral('0.0105')))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,369))
    def test_ast_70(self):
        input = """Function: foo
            Body:
                a = foo() + goo();
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[],([],[Assign(Id('a'),BinaryOp('+',CallExpr(Id('foo'),[]),CallExpr(Id('goo'),[])))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))
    def test_ast_71(self):
        input = """Var: a = 1.2e-3;
            Function: foo
            Parameter: a, b
            Body:
                Var: b[2][3] = {{2,3,4},{4,5,6}};
                b = a[2][1];
                a = b;
            EndBody.
            Function: goo
            Parameter: c, d
            Body:
                c[2] = {3,2};
                d = 2.e+1;
            EndBody."""
        expect = Program([VarDecl(Id('a'),[],FloatLiteral('0.0012')),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([VarDecl(Id('b'),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral('2'),IntLiteral('3'),IntLiteral('4')]),ArrayLiteral([IntLiteral('4'),IntLiteral('5'),IntLiteral('6')])]))],[Assign(Id('b'),ArrayCell(Id('a'),[IntLiteral('2'),IntLiteral('1')])),Assign(Id('a'),Id('b'))])),FuncDecl(Id('goo'),[VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],None)],([],[Assign(ArrayCell(Id('c'),[IntLiteral('2')]),ArrayLiteral([IntLiteral('3'),IntLiteral('2')])),Assign(Id('d'),FloatLiteral('20.0'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))
    def test_ast_72(self):
        input = """Function: foo
            Body:
                a = a && b > c;
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[],([],[Assign(Id('a'),BinaryOp('>',BinaryOp('&&',Id('a'),Id('b')),Id('c')))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))
    def test_ast_73(self):
        input = """Function: foo
            Body:
                a[1.2] = a && b > c;
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[],([],[Assign(ArrayCell(Id('a'),[FloatLiteral('1.2')]),BinaryOp('>',BinaryOp('&&',Id('a'),Id('b')),Id('c')))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))
    def test_ast_74(self):
        input = """Var: a[1] = {1};
            Function: foo
            Body:
                a[1] = a && (b < c);
            EndBody."""
        expect = Program([VarDecl(Id('a'),[1],ArrayLiteral([IntLiteral('1')])),FuncDecl(Id('foo'),[],([],[Assign(ArrayCell(Id('a'),[IntLiteral('1')]),BinaryOp('&&',Id('a'),BinaryOp('<',Id('b'),Id('c'))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_ast_75(self):
        input = """Function: foo
            Body:
                a = !-a && b < c + d*e;
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[],([],[Assign(Id('a'),BinaryOp('<',BinaryOp('&&',UnaryOp('!',UnaryOp('-',Id('a'))),Id('b')),BinaryOp('+',Id('c'),BinaryOp('*',Id('d'),Id('e')))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))
    def test_ast_76(self):
        input = """Function: foo
            Body:
                If a && b Then
                    For (i = 1, i < 20, 2) Do
                        foo(b,a,c);
                    EndFor.
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[],([],[If([(BinaryOp('&&',Id('a'),Id('b')),[],[For(Id('i'),IntLiteral('1'),BinaryOp('<',Id('i'),IntLiteral('20')),IntLiteral('2'),([],[CallStmt(Id('foo'),[Id('b'),Id('a'),Id('c')])]))])],[])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))
    def test_ast_77(self):
        input = """Function: foo
        Body:
            For (i = 5, a*.b\\.c-.d-.e=/=f , goo(g,h)) Do
                For (j = 0, j < 20, 1) Do
                    writeln(i);
                    If a && b Then
                        While True Do
                            foo(a,b,c);
                        EndWhile.
                    Else
                        Return a + b;
                    EndIf.
                EndFor.
            EndFor.
        EndBody."""
        expect = Program([FuncDecl(Id('foo'),[],([],[For(Id('i'),IntLiteral('5'),BinaryOp('=/=',BinaryOp('-.',BinaryOp('-.',BinaryOp('\.',BinaryOp('*.',Id('a'),Id('b')),Id('c')),Id('d')),Id('e')),Id('f')),CallExpr(Id('goo'),[Id('g'),Id('h')]),([],[For(Id('j'),IntLiteral('0'),BinaryOp('<',Id('j'),IntLiteral('20')),IntLiteral('1'),([],[CallStmt(Id('writeln'),[Id('i')]),If([(BinaryOp('&&',Id('a'),Id('b')),[],[While(BooleanLiteral('true'),([],[CallStmt(Id('foo'),[Id('a'),Id('b'),Id('c')])]))])],([],[Return(BinaryOp('+',Id('a'),Id('b')))]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect, 377))
    def test_ast_78(self):
        input = """Function: foo
            Body:
                Do
                    a = c+.d;
                    If (a<=.b) Then
                        Continue;
                    EndIf.
                    doThis();
                While (a<.c)
                EndDo.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[],([],[Dowhile(([],[Assign(Id('a'),BinaryOp('+.',Id('c'),Id('d'))),If([(BinaryOp('<=.',Id('a'),Id('b')),[],[Continue()])],[]),CallStmt(Id('doThis'),[])]),BinaryOp('<.',Id('a'),Id('c')))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect, 378))
    def test_ast_79(self):
        input = """Function: foo
            
            Body:

            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect, 379))
    def test_ast_80(self):
        input = """Var: a;
            Function: foo
            Body:

            EndBody."""
        expect = Program([VarDecl(Id('a'),[],None),FuncDecl(Id('foo'),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect, 380))
    def test_ast_81(self):
        input = """Var: int, float, string, boolean;
            Function: foo
            Body:

            EndBody."""
        expect = Program([VarDecl(Id('int'),[],None),VarDecl(Id('float'),[],None),VarDecl(Id('string'),[],None),VarDecl(Id('boolean'),[],None),FuncDecl(Id('foo'),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect, 381))
    def test_ast_82(self):
        input = """Function: foo
            Parameter: a,b,c, e
            Body:
                a = 0x123456;
                If a < b Then
                    While True Do
                        Break;
                    EndWhile.
                ElseIf a == b Then
                    For (i = 1, i < 10, 1) Do
                        
                        If a < b Then
                            Return a;
                        EndIf.
                    EndFor.
                Else
                    
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('e'),[],None)],([],[Assign(Id('a'),IntLiteral('1193046')),If([(BinaryOp('<',Id('a'),Id('b')),[],[While(BooleanLiteral('true'),([],[Break()]))]),(BinaryOp('==',Id('a'),Id('b')),[],[For(Id('i'),IntLiteral('1'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('1'),([],[If([(BinaryOp('<',Id('a'),Id('b')),[],[Return(Id('a'))])],[])]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,382))
    def test_ast_83(self):
        input = """Function: foo
            Parameter: a,b,c, e
            Body:
                a = 0x123456;
                If a < b Then
                    While True Do
                        Break;
                    EndWhile.
                ElseIf a == b Then
                    For (i = 1, i < 10, 1) Do
                        
                        If a < b Then
                            Return a;
                        EndIf.
                    EndFor.
                Else
                    Do
                        Continue;
                    While (a \\. 10.0 =/= 10.5e-3)
                    EndDo.
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('e'),[],None)],([],[Assign(Id('a'),IntLiteral('1193046')),If([(BinaryOp('<',Id('a'),Id('b')),[],[While(BooleanLiteral('true'),([],[Break()]))]),(BinaryOp('==',Id('a'),Id('b')),[],[For(Id('i'),IntLiteral('1'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('1'),([],[If([(BinaryOp('<',Id('a'),Id('b')),[],[Return(Id('a'))])],[])]))])],([],[Dowhile(([],[Continue()]),BinaryOp('=/=',BinaryOp('\.',Id('a'),FloatLiteral('10.0')),FloatLiteral('0.0105')))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,383))
    def test_ast_84(self):
        input = """Function: foo
            Parameter: n,a[2][3][4],b[4][1],m
            Body:
                a = 0x123456;
                If a < b Then
                    While True Do
                        Break;
                    EndWhile.
                ElseIf a == b Then
                    For (i = 1, i < 10, 1) Do
                        
                        If a < b Then
                            Return a;
                        EndIf.
                    EndFor.
                Else
                    Do
                        Continue;
                    While (a \\. 10.0 =/= 10.5e-3)
                    EndDo.
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('n'),[],None),VarDecl(Id('a'),[2,3,4],None),VarDecl(Id('b'),[4,1],None),VarDecl(Id('m'),[],None)],([],[Assign(Id('a'),IntLiteral('1193046')),If([(BinaryOp('<',Id('a'),Id('b')),[],[While(BooleanLiteral('true'),([],[Break()]))]),(BinaryOp('==',Id('a'),Id('b')),[],[For(Id('i'),IntLiteral('1'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('1'),([],[If([(BinaryOp('<',Id('a'),Id('b')),[],[Return(Id('a'))])],[])]))])],([],[Dowhile(([],[Continue()]),BinaryOp('=/=',BinaryOp('\.',Id('a'),FloatLiteral('10.0')),FloatLiteral('0.0105')))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,384))
    def test_ast_85(self):
        input = """Function: abctest
            Parameter: n,a[2][3][4],b[4][1],m
            Body:
                If n > 20 Then
                    Return 5;
                ElseIf n >5 Then a=a+.1; Return a;
                Else
                    Return False;
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('abctest'),[VarDecl(Id('n'),[],None),VarDecl(Id('a'),[2,3,4],None),VarDecl(Id('b'),[4,1],None),VarDecl(Id('m'),[],None)],([],[If([(BinaryOp('>',Id('n'),IntLiteral('20')),[],[Return(IntLiteral('5'))]),(BinaryOp('>',Id('n'),IntLiteral('5')),[],[Assign(Id('a'),BinaryOp('+.',Id('a'),IntLiteral('1'))),Return(Id('a'))])],([],[Return(BooleanLiteral('false'))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))
    def test_ast_86(self):
        input = """Function: abctest
            Parameter: n,a[2][3][4],b[4][1],m
            Body:
            n = "Lorem Ipsum is simply dummy text of the printing and typesetting";
                If n > 20 Then
                    Return n + n;
                ElseIf n >5 Then a=a+.1; Return a;
                Else
                    Return False;
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('abctest'),[VarDecl(Id('n'),[],None),VarDecl(Id('a'),[2,3,4],None),VarDecl(Id('b'),[4,1],None),VarDecl(Id('m'),[],None)],([],[Assign(Id('n'),StringLiteral("""Lorem Ipsum is simply dummy text of the printing and typesetting""")),If([(BinaryOp('>',Id('n'),IntLiteral('20')),[],[Return(BinaryOp('+',Id('n'),Id('n')))]),(BinaryOp('>',Id('n'),IntLiteral('5')),[],[Assign(Id('a'),BinaryOp('+.',Id('a'),IntLiteral('1'))),Return(Id('a'))])],([],[Return(BooleanLiteral('false'))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))
    def test_ast_87(self):
        input = """Function: main
            Body:
                Var:a[2]={12,3,4},b=2,c=True;
                Var:c=4;
            EndBody.Function: foo
            Body:
                a=b+1;b=a==b;r=a+b+c-e-.d;
                foo((a+b+.12e10));
            EndBody."""
        expect = Program([FuncDecl(Id('main'),[],([VarDecl(Id('a'),[2],ArrayLiteral([IntLiteral('12'),IntLiteral('3'),IntLiteral('4')])),VarDecl(Id('b'),[],IntLiteral('2')),VarDecl(Id('c'),[],BooleanLiteral('true')),VarDecl(Id('c'),[],IntLiteral('4'))],[])),FuncDecl(Id('foo'),[],([],[Assign(Id('a'),BinaryOp('+',Id('b'),IntLiteral('1'))),Assign(Id('b'),BinaryOp('==',Id('a'),Id('b'))),Assign(Id('r'),BinaryOp('-.',BinaryOp('-',BinaryOp('+',BinaryOp('+',Id('a'),Id('b')),Id('c')),Id('e')),Id('d'))),CallStmt(Id('foo'),[BinaryOp('+.',BinaryOp('+',Id('a'),Id('b')),FloatLiteral('120000000000.0'))])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))
    def test_ast_88(self):
        input = """Function: foo
            Body:
                If a && b Then
                    For (i = 1, i < foo(), 2) Do
                        a[foo()] = foo(b,a,c);
                    EndFor.
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[],([],[If([(BinaryOp('&&',Id('a'),Id('b')),[],[For(Id('i'),IntLiteral('1'),BinaryOp('<',Id('i'),CallExpr(Id('foo'),[])),IntLiteral('2'),([],[Assign(ArrayCell(Id('a'),[CallExpr(Id('foo'),[])]),CallExpr(Id('foo'),[Id('b'),Id('a'),Id('c')]))]))])],[])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))
    def test_ast_89(self):
        input = """Function: foo
            Body:
                If a && b Then
                    For (i = 1, i < foo(), 2) Do
                        a[foo()][foo(b,a,c)] = foo(b,a,c);
                    EndFor.
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[],([],[If([(BinaryOp('&&',Id('a'),Id('b')),[],[For(Id('i'),IntLiteral('1'),BinaryOp('<',Id('i'),CallExpr(Id('foo'),[])),IntLiteral('2'),([],[Assign(ArrayCell(Id('a'),[CallExpr(Id('foo'),[]),CallExpr(Id('foo'),[Id('b'),Id('a'),Id('c')])]),CallExpr(Id('foo'),[Id('b'),Id('a'),Id('c')]))]))])],[])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))
    def test_ast_90(self):
        input = """Function: foo
            Body:
                ** Empty body **
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))
    def test_ast_91(self):
        input = """Function: foo
            Parameter: a,b,c,d
            Body:
                If a < b Then
                    While True Do
                        foo(a,b,c);
                    EndWhile.
                ElseIf a == b Then
                    For (i = 1, i < 10, 1) Do
                        foo(b,a);
                    EndFor.
                Else
                    Return a;
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None),VarDecl(Id('c'),[],None),VarDecl(Id('d'),[],None)],([],[If([(BinaryOp('<',Id('a'),Id('b')),[],[While(BooleanLiteral('true'),([],[CallStmt(Id('foo'),[Id('a'),Id('b'),Id('c')])]))]),(BinaryOp('==',Id('a'),Id('b')),[],[For(Id('i'),IntLiteral('1'),BinaryOp('<',Id('i'),IntLiteral('10')),IntLiteral('1'),([],[CallStmt(Id('foo'),[Id('b'),Id('a')])]))])],([],[Return(Id('a'))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))
    def test_ast_92(self):
        input = """Function: main
            Parameter: x
            Body:   
                Do
                    Return True;
                    Break;
                While (True)
                EndDo.
            EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[Dowhile(([],[Return(BooleanLiteral('true')),Break()]),BooleanLiteral('true'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))
    def test_ast_93(self):
        input = """Function: main
            Parameter: x
            Body:   
                While ((b>=a)==(b!=c)+d*a*b*c) Do
                    writeln(i);
                    If (a==2) Then
                        Return True;
                        Break;
                    EndIf.
                    While (False) Do
                        writeln(i);
                    EndWhile.
                    While ((b>=a)==(b!=c)+d*a*b*c) Do
                        writeln(i);
                    EndWhile.
                EndWhile.
            EndBody."""
        expect = Program([FuncDecl(Id('main'),[VarDecl(Id('x'),[],None)],([],[While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[CallStmt(Id('writeln'),[Id('i')]),If([(BinaryOp('==',Id('a'),IntLiteral('2')),[],[Return(BooleanLiteral('true')),Break()])],[]),While(BooleanLiteral('false'),([],[CallStmt(Id('writeln'),[Id('i')])])),While(BinaryOp('==',BinaryOp('>=',Id('b'),Id('a')),BinaryOp('+',BinaryOp('!=',Id('b'),Id('c')),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('d'),Id('a')),Id('b')),Id('c')))),([],[CallStmt(Id('writeln'),[Id('i')])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))
    def test_ast_94(self):
        input = """Function: foo
            Body:
                str = ** "string" * "string" ** "abc";
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[],([],[Assign(Id('str'),StringLiteral("""abc"""))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))
    def test_ast_95(self):
        input = """Function: foo
            Body:
                ** "string" ** ** "string" **
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))
    def test_ast_96(self):
        input = """Var: b[2][3] = {{2,3,4}};
        Function: foo
        Parameter: a, b
        Body:
            **  
            * This is a block comment 
            * This is a block comment
            * This is a block comment 
            **
            b = a[2][1];
            a = b;
        EndBody."""
        expect = Program([VarDecl(Id('b'),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral('2'),IntLiteral('3'),IntLiteral('4')])])),FuncDecl(Id('foo'),[VarDecl(Id('a'),[],None),VarDecl(Id('b'),[],None)],([],[Assign(Id('b'),ArrayCell(Id('a'),[IntLiteral('2'),IntLiteral('1')])),Assign(Id('a'),Id('b'))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))
    def test_ast_97(self):
        input = """Function: foo
            Body:
                If (a < b) && (!b <= c) Then
                    For (i = 1, i < foo(), 2) Do
                        a = foo(b,a,c);
                    EndFor.
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[],([],[If([(BinaryOp('&&',BinaryOp('<',Id('a'),Id('b')),BinaryOp('<=',UnaryOp('!',Id('b')),Id('c'))),[],[For(Id('i'),IntLiteral('1'),BinaryOp('<',Id('i'),CallExpr(Id('foo'),[])),IntLiteral('2'),([],[Assign(Id('a'),CallExpr(Id('foo'),[Id('b'),Id('a'),Id('c')]))]))])],[])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))
    def test_ast_98(self):
        input = """Function: foo
            Body:
                If (a < b) && !b <= c Then
                    For (i = 1, i < foo(), 2) Do
                        a[1] = foo(b,a,c) + foo();
                    EndFor.
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[],([],[If([(BinaryOp('<=',BinaryOp('&&',BinaryOp('<',Id('a'),Id('b')),UnaryOp('!',Id('b'))),Id('c')),[],[For(Id('i'),IntLiteral('1'),BinaryOp('<',Id('i'),CallExpr(Id('foo'),[])),IntLiteral('2'),([],[Assign(ArrayCell(Id('a'),[IntLiteral('1')]),BinaryOp('+',CallExpr(Id('foo'),[Id('b'),Id('a'),Id('c')]),CallExpr(Id('foo'),[])))]))])],[])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))
    def test_ast_99(self):
        input = """Function: foo
            Body:
                If (a < b) && !b <= c Then
                    For (i = 1, i < foo(), 2) Do
                        a[1] = foo(b,a,c) + foo(a[1][2][3]);
                    EndFor.
                EndIf.
            EndBody."""
        expect = Program([FuncDecl(Id('foo'),[],([],[If([(BinaryOp('<=',BinaryOp('&&',BinaryOp('<',Id('a'),Id('b')),UnaryOp('!',Id('b'))),Id('c')),[],[For(Id('i'),IntLiteral('1'),BinaryOp('<',Id('i'),CallExpr(Id('foo'),[])),IntLiteral('2'),([],[Assign(ArrayCell(Id('a'),[IntLiteral('1')]),BinaryOp('+',CallExpr(Id('foo'),[Id('b'),Id('a'),Id('c')]),CallExpr(Id('foo'),[ArrayCell(Id('a'),[IntLiteral('1'),IntLiteral('2'),IntLiteral('3')])])))]))])],[])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))