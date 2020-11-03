import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_declare_0(self):
        input = """Var:x;"""
        expect = str(Program([VarDecl(Id("x"),[],None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_declare_1(self):
        input = """Var:x, a;"""
        expect = str(Program([VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_declare_2(self):
        input = """Var:x = 1, a;"""
        expect = str(Program([VarDecl(Id("x"),[],IntLiteral(1)),VarDecl(Id("a"),[],None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_declare_3(self):
        input = """Var:x = True, a;"""
        expect = str(Program([VarDecl(Id("x"),[],BooleanLiteral(True)),VarDecl(Id("a"),[],None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    
    def test_declare_4(self):
        input = """Var: x[10][50] = {1,2,3,4};
        Var: a = 10, c = 100.5;
        Var: me;
        """
        expect = """Program([VarDecl(Id(x),[10,50],ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4))),VarDecl(Id(a),IntLiteral(10)),VarDecl(Id(c),FloatLiteral(100.5)),VarDecl(Id(me))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_declare_5(self):
        input = """Var: x[10][50] = {{1},{2},{3},{4}};
        Var: a = 10, c = 100.5;
        Var: me;
        """
        expect = """Program([VarDecl(Id(x),[10,50],ArrayLiteral(ArrayLiteral(IntLiteral(1)),ArrayLiteral(IntLiteral(2)),ArrayLiteral(IntLiteral(3)),ArrayLiteral(IntLiteral(4)))),VarDecl(Id(a),IntLiteral(10)),VarDecl(Id(c),FloatLiteral(100.5)),VarDecl(Id(me))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
    
    def test_funcDeclar_1(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[5][9][3], b[7]
        Body:
        Var: m[10][8] = {1,2,3,4};
        Var: ngao, du = 3, thienha[5][9][1][2];
        EndBody.
        """
        expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main),[VarDecl(Id(a),[5,9,3]),VarDecl(Id(b),[7])],([VarDecl(Id(m),[10,8],ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4))),VarDecl(Id(ngao)),VarDecl(Id(du),IntLiteral(3)),VarDecl(Id(thienha),[5,9,1,2])],[]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_ifStmtInFunc_1(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0O123]
        Body:
        If x == y Then x = x + 1; 
        Else
            Var: a; 
        EndIf.
        EndBody.
        """
        expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main),[VarDecl(Id(a),[83])],([],[If(BinaryOp(==,Id(x),Id(y)),[],[Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1)))])Else([VarDecl(Id(a))],[])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_ifStmtInFunc_2(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0O123]
        Body:
        If x == y Then x = x + 1; 
        ElseIf x > y Then y = y + 1;
        ElseIf x < y Then y = y - x;
        EndIf.
        EndBody.
        """
        expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main),[VarDecl(Id(a),[83])],([],[If(BinaryOp(==,Id(x),Id(y)),[],[Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1)))])ElseIf(BinaryOp(>,Id(x),Id(y)),[],[Assign(Id(y),BinaryOp(+,Id(y),IntLiteral(1)))])ElseIf(BinaryOp(<,Id(x),Id(y)),[],[Assign(Id(y),BinaryOp(-,Id(y),Id(x)))])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_ifStmtInFunc_3(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0O123]
        Body:
        If x == y Then x = x + 1; 
        ElseIf x > y Then Var: a = 1;
        ElseIf x < y Then Var: b = 2;
        Else
            If y > 10 Then y = y \ 2;
            EndIf.
        EndIf.
        EndBody.
        """
        expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main),[VarDecl(Id(a),[83])],([],[If(BinaryOp(==,Id(x),Id(y)),[],[Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1)))])ElseIf(BinaryOp(>,Id(x),Id(y)),[VarDecl(Id(a),IntLiteral(1))],[])ElseIf(BinaryOp(<,Id(x),Id(y)),[VarDecl(Id(b),IntLiteral(2))],[])Else([],[If(BinaryOp(>,Id(y),IntLiteral(10)),[],[Assign(Id(y),BinaryOp(\,Id(y),IntLiteral(2)))])])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_ifStmtInFunc_4(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0O123]
        Body:
        If x == y Then x = x + 1; 
        ElseIf x > y Then Var: a = 1; x = a * 10.5;
        ElseIf x < y Then Var: b = 2; y = b + foo();
        Else
            If y > 10 Then y = y \ 2; Return 1;
            EndIf.
        EndIf.
        EndBody.
        """
        expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main),[VarDecl(Id(a),[83])],([],[If(BinaryOp(==,Id(x),Id(y)),[],[Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1)))])ElseIf(BinaryOp(>,Id(x),Id(y)),[VarDecl(Id(a),IntLiteral(1))],[Assign(Id(x),BinaryOp(*,Id(a),FloatLiteral(10.5)))])ElseIf(BinaryOp(<,Id(x),Id(y)),[VarDecl(Id(b),IntLiteral(2))],[Assign(Id(y),BinaryOp(+,Id(b),CallExpr(Id(foo),[])))])Else([],[If(BinaryOp(>,Id(y),IntLiteral(10)),[],[Assign(Id(y),BinaryOp(\,Id(y),IntLiteral(2))),Return(IntLiteral(1))])])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_funcDeclar_2(self):
        input = """Function: main
        Body:
        (a + foo())[1] = 1;
        a[1] = a[1] * s;
        EndBody.
        """
        expect = """Program([FuncDecl(Id(main),[],([],[Assign(ArrayCell(BinaryOp(+,Id(a),CallExpr(Id(foo),[])),[IntLiteral(1)]),IntLiteral(1)),Assign(ArrayCell(Id(a),[IntLiteral(1)]),BinaryOp(*,ArrayCell(Id(a),[IntLiteral(1)]),Id(s)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_funcDeclar_3(self):
        input = """Function: main
        Body:
        (a + foo())[1] = {{1,2,3}, {1,2,3}, {1,2,3}};
        a[1] = a[1 + foo((a + foo())[1])] * s;
        EndBody.
        """
        expect = """Program([FuncDecl(Id(main),[],([],[Assign(ArrayCell(BinaryOp(+,Id(a),CallExpr(Id(foo),[])),[IntLiteral(1)]),ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3)),ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3)),ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3)))),Assign(ArrayCell(Id(a),[IntLiteral(1)]),BinaryOp(*,ArrayCell(Id(a),[BinaryOp(+,IntLiteral(1),CallExpr(Id(foo),[ArrayCell(BinaryOp(+,Id(a),CallExpr(Id(foo),[])),[IntLiteral(1)])]))]),Id(s)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,312))