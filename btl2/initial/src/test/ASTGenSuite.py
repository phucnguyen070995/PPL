import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    # def test_declare_0(self):
    #     input = """Var:x;"""
    #     expect = str(Program([VarDecl(Id("x"),[],None)]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,300))

    # def test_declare_1(self):
    #     input = """Var:x, a;"""
    #     expect = str(Program([VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],None)]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,301))

    # def test_declare_2(self):
    #     input = """Var:x = 1, a;"""
    #     expect = str(Program([VarDecl(Id("x"),[],IntLiteral(1)),VarDecl(Id("a"),[],None)]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,302))

    # def test_declare_3(self):
    #     input = """Var:x = True, a;"""
    #     expect = str(Program([VarDecl(Id("x"),[],BooleanLiteral(True)),VarDecl(Id("a"),[],None)]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,303))
    
    # def test_declare_4(self):
    #     input = """Var: x[10][50] = {1,2,3,4};
    #     Var: a = 10, c = 100.5;
    #     Var: me;
    #     """
    #     expect = """Program([VarDecl(Id(x),[10,50],ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4))),VarDecl(Id(a),IntLiteral(10)),VarDecl(Id(c),FloatLiteral(100.5)),VarDecl(Id(me))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,304))

    # def test_declare_5(self):
    #     input = """Var: x[10][50] = {{1},{2},{3},{4}};
    #     Var: a = 10, c = 100.5;
    #     Var: me;
    #     """
    #     expect = """Program([VarDecl(Id(x),[10,50],ArrayLiteral(ArrayLiteral(IntLiteral(1)),ArrayLiteral(IntLiteral(2)),ArrayLiteral(IntLiteral(3)),ArrayLiteral(IntLiteral(4)))),VarDecl(Id(a),IntLiteral(10)),VarDecl(Id(c),FloatLiteral(100.5)),VarDecl(Id(me))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,305))
    
    # def test_funcDeclar_1(self):
    #     input = """Var: x = 5;
    #     Function: main
    #     Parameter: a[5][9][3], b[7]
    #     Body:
    #     Var: m[10][8] = {1,2,3,4};
    #     Var: ngao, du = 3, thienha[5][9][1][2];
    #     EndBody.
    #     """
    #     expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main),[VarDecl(Id(a),[5,9,3]),VarDecl(Id(b),[7])],([VarDecl(Id(m),[10,8],ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4))),VarDecl(Id(ngao)),VarDecl(Id(du),IntLiteral(3)),VarDecl(Id(thienha),[5,9,1,2])],[]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,306))

    # def test_ifStmtInFunc_1(self):
    #     input = """Var: x = 5;
    #     Function: main
    #     Parameter: a[0O123]
    #     Body:
    #     If x == y Then x = x + 1; 
    #     Else
    #         Var: a; 
    #     EndIf.
    #     EndBody.
    #     """
    #     expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main),[VarDecl(Id(a),[83])],([],[If(BinaryOp(==,Id(x),Id(y)),[],[Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1)))])Else([VarDecl(Id(a))],[])]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,307))

    # def test_ifStmtInFunc_2(self):
    #     input = """Var: x = 5;
    #     Function: main
    #     Parameter: a[0O123]
    #     Body:
    #     If x == y Then x = x + 1; 
    #     ElseIf x > y Then y = y + 1;
    #     ElseIf x < y Then y = y - x;
    #     EndIf.
    #     EndBody.
    #     """
    #     expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main),[VarDecl(Id(a),[83])],([],[If(BinaryOp(==,Id(x),Id(y)),[],[Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1)))])ElseIf(BinaryOp(>,Id(x),Id(y)),[],[Assign(Id(y),BinaryOp(+,Id(y),IntLiteral(1)))])ElseIf(BinaryOp(<,Id(x),Id(y)),[],[Assign(Id(y),BinaryOp(-,Id(y),Id(x)))])]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,308))

    # def test_ifStmtInFunc_3(self):
    #     input = """Var: x = 5;
    #     Function: main
    #     Parameter: a[0O123]
    #     Body:
    #     If x == y Then x = x + 1; 
    #     ElseIf x > y Then Var: a = 1;
    #     ElseIf x < y Then Var: b = 2;
    #     Else
    #         If y > 10 Then y = y \ 2;
    #         EndIf.
    #     EndIf.
    #     EndBody.
    #     """
    #     expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main),[VarDecl(Id(a),[83])],([],[If(BinaryOp(==,Id(x),Id(y)),[],[Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1)))])ElseIf(BinaryOp(>,Id(x),Id(y)),[VarDecl(Id(a),IntLiteral(1))],[])ElseIf(BinaryOp(<,Id(x),Id(y)),[VarDecl(Id(b),IntLiteral(2))],[])Else([],[If(BinaryOp(>,Id(y),IntLiteral(10)),[],[Assign(Id(y),BinaryOp(\,Id(y),IntLiteral(2)))])])]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,309))

    # def test_ifStmtInFunc_4(self):
    #     input = """Var: x = 5;
    #     Function: main
    #     Parameter: a[0O123]
    #     Body:
    #     If x == y Then x = x + 1; 
    #     ElseIf x > y Then Var: a = 1; x = a * 10.5;
    #     ElseIf x < y Then Var: b = 2; y = b + foo();
    #     Else
    #         If y > 10 Then y = y \ 2; Return 1;
    #         EndIf.
    #     EndIf.
    #     EndBody.
    #     """
    #     expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main),[VarDecl(Id(a),[83])],([],[If(BinaryOp(==,Id(x),Id(y)),[],[Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1)))])ElseIf(BinaryOp(>,Id(x),Id(y)),[VarDecl(Id(a),IntLiteral(1))],[Assign(Id(x),BinaryOp(*,Id(a),FloatLiteral(10.5)))])ElseIf(BinaryOp(<,Id(x),Id(y)),[VarDecl(Id(b),IntLiteral(2))],[Assign(Id(y),BinaryOp(+,Id(b),CallExpr(Id(foo),[])))])Else([],[If(BinaryOp(>,Id(y),IntLiteral(10)),[],[Assign(Id(y),BinaryOp(\,Id(y),IntLiteral(2))),Return(IntLiteral(1))])])]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,310))

    # def test_funcDeclar_2(self):
    #     input = """Function: main
    #     Body:
    #     (a + foo())[1] = 1;
    #     a[1] = a[1] * s;
    #     EndBody.
    #     """
    #     expect = """Program([FuncDecl(Id(main),[],([],[Assign(ArrayCell(BinaryOp(+,Id(a),CallExpr(Id(foo),[])),[IntLiteral(1)]),IntLiteral(1)),Assign(ArrayCell(Id(a),[IntLiteral(1)]),BinaryOp(*,ArrayCell(Id(a),[IntLiteral(1)]),Id(s)))]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,311))

    # def test_funcDeclar_3(self):
    #     input = """Function: main
    #     Body:
    #     (a + foo())[1] = {{1,2,3}, {1,2,3}, {1,2,3}};
    #     a[1] = a[1 + foo((a + foo())[1])] * s;
    #     EndBody.
    #     """
    #     expect = """Program([FuncDecl(Id(main),[],([],[Assign(ArrayCell(BinaryOp(+,Id(a),CallExpr(Id(foo),[])),[IntLiteral(1)]),ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3)),ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3)),ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3)))),Assign(ArrayCell(Id(a),[IntLiteral(1)]),BinaryOp(*,ArrayCell(Id(a),[BinaryOp(+,IntLiteral(1),CallExpr(Id(foo),[ArrayCell(BinaryOp(+,Id(a),CallExpr(Id(foo),[])),[IntLiteral(1)])]))]),Id(s)))]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,312))

    # def test_forFunc_1(self):
    #     input = """Var: x = 5;
    #     Function: main
    #     Parameter: a[0o123]
    #     Body:
    #     For (i = 0, i < 10, 2) Do
    #     writeln(i);
    #     EndFor.
    #     EndBody.
    #     """
    #     expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main),[VarDecl(Id(a),[83])],([],[For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),IntLiteral(10)),IntLiteral(2),[],[CallExpr(Id(writeln),[Id(i)])])]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,313))

    # def test_forFunc_2(self):
    #     input = """Var: x = 5;
    #     Function: main
    #     Parameter: a[0o123]
    #     Body:
    #     For (i = 0, i < 10, i + 2) Do
    #     x = x + 10.0;
    #     EndFor.
    #     EndBody.
    #     """
    #     expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main),[VarDecl(Id(a),[83])],([],[For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),IntLiteral(10)),BinaryOp(+,Id(i),IntLiteral(2)),[],[Assign(Id(x),BinaryOp(+,Id(x),FloatLiteral(10.0)))])]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,314))

    # def test_forFunc_3(self):
    #     input = """Var: x = 5;
    #     Function: main
    #     Parameter: a[0o123]
    #     Body:
    #     Var: qq, dd, ee;
    #     For (i = 0, i < 10, i + 2) Do
    #         Var: y = True;
    #         x = foo(i);
    #         x[i] = foo[x+i];
    #         For (j = 5, j >= 0, j -1) Do
    #         Break;
    #         Return 1;
    #         EndFor.
    #     EndFor.
    #     EndBody.
    #     """
    #     expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main),[VarDecl(Id(a),[83])],([VarDecl(Id(qq)),VarDecl(Id(dd)),VarDecl(Id(ee))],[For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),IntLiteral(10)),BinaryOp(+,Id(i),IntLiteral(2)),[VarDecl(Id(y),BooleanLiteral(true))],[Assign(Id(x),CallExpr(Id(foo),[Id(i)])),Assign(ArrayCell(Id(x),[Id(i)]),ArrayCell(Id(foo),[BinaryOp(+,Id(x),Id(i))])),For(Id(j),IntLiteral(5),BinaryOp(>=,Id(j),IntLiteral(0)),BinaryOp(-,Id(j),IntLiteral(1)),[],[Break(),Return(IntLiteral(1))])])]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,315))

    # def test_whileFunc_1(self):
    #     input = """Var: x = 5;
    #     Function: main
    #     Parameter: a[0o123]
    #     Body:
    #         While x == True Do 
    #         EndWhile.
    #     EndBody.
    #     """
    #     expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main),[VarDecl(Id(a),[83])],([],[While(BinaryOp(==,Id(x),BooleanLiteral(true)),[],[])]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,316))

    # def test_whileFunc_2(self):
    #     input = """Var: x = 5;
    #     Function: main
    #     Parameter: a[0o123]
    #     Body:
    #         While x == True Do 
    #             While y == 1 Do
    #             EndWhile.
    #         EndWhile.
    #     EndBody.
    #     """
    #     expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main),[VarDecl(Id(a),[83])],([],[While(BinaryOp(==,Id(x),BooleanLiteral(true)),[],[While(BinaryOp(==,Id(y),IntLiteral(1)),[],[])])]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,317))

    # def test_whileFunc_3(self):
    #     input = """Var: x = 5;
    #     Function: main
    #     Parameter: a[0o123]
    #     Body:
    #         While x == True Do 
    #             While y == 1 Do
    #                 dd = nn;
    #             EndWhile.
    #         EndWhile.
    #     EndBody.
    #     """
    #     expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main),[VarDecl(Id(a),[83])],([],[While(BinaryOp(==,Id(x),BooleanLiteral(true)),[],[While(BinaryOp(==,Id(y),IntLiteral(1)),[],[Assign(Id(dd),Id(nn))])])]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_whileFunc_4(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            While (x < 10.5) Do 
                x = x + 1;
                While y == 1 Do
                    dd = nn;
                    y[i] = x[y + i];
                EndWhile.
            EndWhile.
        EndBody.
        """
        expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main),[VarDecl(Id(a),[83])],([],[While(BinaryOp(<,Id(x),FloatLiteral(10.5)),[],[Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1))),While(BinaryOp(==,Id(y),IntLiteral(1)),[],[Assign(Id(dd),Id(nn)),Assign(ArrayCell(Id(y),[Id(i)]),ArrayCell(Id(x),[BinaryOp(+,Id(y),Id(i))]))])])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_whileFunc_5(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            While (x < 10.5) Do 
                x = x + 1;
                While y == 1 Do
                    dd = nn;
                    y[i] = x[y + i];
                    a[0xDD] = 10.9;
                EndWhile.
            EndWhile.
        EndBody.
        """
        expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main),[VarDecl(Id(a),[83])],([],[While(BinaryOp(<,Id(x),FloatLiteral(10.5)),[],[Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1))),While(BinaryOp(==,Id(y),IntLiteral(1)),[],[Assign(Id(dd),Id(nn)),Assign(ArrayCell(Id(y),[Id(i)]),ArrayCell(Id(x),[BinaryOp(+,Id(y),Id(i))])),Assign(ArrayCell(Id(a),[IntLiteral(221)]),FloatLiteral(10.9))])])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,320))