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
    #     expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main)[VarDecl(Id(a),[5,9,3]),VarDecl(Id(b),[7])],([VarDecl(Id(m),[10,8],ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4))),VarDecl(Id(ngao)),VarDecl(Id(du),IntLiteral(3)),VarDecl(Id(thienha),[5,9,1,2])][]))])"""
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
    #     expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main)[VarDecl(Id(a),[83])],([][If(BinaryOp(==,Id(x),Id(y)),[],[Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1)))])Else([VarDecl(Id(a))],[])]))])"""
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
    #     expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main)[VarDecl(Id(a),[83])],([][If(BinaryOp(==,Id(x),Id(y)),[],[Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1)))])ElseIf(BinaryOp(>,Id(x),Id(y)),[],[Assign(Id(y),BinaryOp(+,Id(y),IntLiteral(1)))])ElseIf(BinaryOp(<,Id(x),Id(y)),[],[Assign(Id(y),BinaryOp(-,Id(y),Id(x)))])]))])"""
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
    #     expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main)[VarDecl(Id(a),[83])],([][If(BinaryOp(==,Id(x),Id(y)),[],[Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1)))])ElseIf(BinaryOp(>,Id(x),Id(y)),[VarDecl(Id(a),IntLiteral(1))],[])ElseIf(BinaryOp(<,Id(x),Id(y)),[VarDecl(Id(b),IntLiteral(2))],[])Else([],[If(BinaryOp(>,Id(y),IntLiteral(10)),[],[Assign(Id(y),BinaryOp(\,Id(y),IntLiteral(2)))])])]))])"""
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
    #     expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main)[VarDecl(Id(a),[83])],([][If(BinaryOp(==,Id(x),Id(y)),[],[Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1)))])ElseIf(BinaryOp(>,Id(x),Id(y)),[VarDecl(Id(a),IntLiteral(1))],[Assign(Id(x),BinaryOp(*,Id(a),FloatLiteral(10.5)))])ElseIf(BinaryOp(<,Id(x),Id(y)),[VarDecl(Id(b),IntLiteral(2))],[Assign(Id(y),BinaryOp(+,Id(b),CallExpr(Id(foo),[])))])Else([],[If(BinaryOp(>,Id(y),IntLiteral(10)),[],[Assign(Id(y),BinaryOp(\,Id(y),IntLiteral(2))),Return(IntLiteral(1))])])]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,310))

    # def test_funcDeclar_2(self):
    #     input = """Function: main
    #     Body:
    #     (a + foo())[1] = 1;
    #     a[1] = a[1] * s;
    #     EndBody.
    #     """
    #     expect = """Program([FuncDecl(Id(main)[],([][Assign(ArrayCell(BinaryOp(+,Id(a),CallExpr(Id(foo),[])),[IntLiteral(1)]),IntLiteral(1)),Assign(ArrayCell(Id(a),[IntLiteral(1)]),BinaryOp(*,ArrayCell(Id(a),[IntLiteral(1)]),Id(s)))]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,311))

    # def test_funcDeclar_3(self):
    #     input = """Function: main
    #     Body:
    #     (a + foo())[1] = {{1,2,3}, {1,2,3}, {1,2,3}};
    #     a[1] = a[1 + foo((a + foo())[1])] * s;
    #     EndBody.
    #     """
    #     expect = """Program([FuncDecl(Id(main)[],([][Assign(ArrayCell(BinaryOp(+,Id(a),CallExpr(Id(foo),[])),[IntLiteral(1)]),ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3)),ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3)),ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3)))),Assign(ArrayCell(Id(a),[IntLiteral(1)]),BinaryOp(*,ArrayCell(Id(a),[BinaryOp(+,IntLiteral(1),CallExpr(Id(foo),[ArrayCell(BinaryOp(+,Id(a),CallExpr(Id(foo),[])),[IntLiteral(1)])]))]),Id(s)))]))])"""
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
    #     expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main)[VarDecl(Id(a),[83])],([][For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),IntLiteral(10)),IntLiteral(2),[],[CallExpr(Id(writeln),[Id(i)])])]))])"""
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
    #     expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main)[VarDecl(Id(a),[83])],([][For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),IntLiteral(10)),BinaryOp(+,Id(i),IntLiteral(2)),[],[Assign(Id(x),BinaryOp(+,Id(x),FloatLiteral(10.0)))])]))])"""
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
    #     expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main)[VarDecl(Id(a),[83])],([VarDecl(Id(qq)),VarDecl(Id(dd)),VarDecl(Id(ee))][For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),IntLiteral(10)),BinaryOp(+,Id(i),IntLiteral(2)),[VarDecl(Id(y),BooleanLiteral(true))],[Assign(Id(x),CallExpr(Id(foo),[Id(i)])),Assign(ArrayCell(Id(x),[Id(i)]),ArrayCell(Id(foo),[BinaryOp(+,Id(x),Id(i))])),For(Id(j),IntLiteral(5),BinaryOp(>=,Id(j),IntLiteral(0)),BinaryOp(-,Id(j),IntLiteral(1)),[],[Break(),Return(IntLiteral(1))])])]))])"""
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
    #     expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main)[VarDecl(Id(a),[83])],([][While(BinaryOp(==,Id(x),BooleanLiteral(true)),[],[])]))])"""
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
    #     expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main)[VarDecl(Id(a),[83])],([][While(BinaryOp(==,Id(x),BooleanLiteral(true)),[],[While(BinaryOp(==,Id(y),IntLiteral(1)),[],[])])]))])"""
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
    #     expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main)[VarDecl(Id(a),[83])],([][While(BinaryOp(==,Id(x),BooleanLiteral(true)),[],[While(BinaryOp(==,Id(y),IntLiteral(1)),[],[Assign(Id(dd),Id(nn))])])]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,318))

    # def test_whileFunc_4(self):
    #     input = """Var: x = 5;
    #     Function: main
    #     Parameter: a[0o123]
    #     Body:
    #         While (x < 10.5) Do
    #             x = x + 1;
    #             While y == 1 Do
    #                 dd = nn;
    #                 y[i] = x[y + i];
    #             EndWhile.
    #         EndWhile.
    #     EndBody.
    #     """
    #     expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main)[VarDecl(Id(a),[83])],([][While(BinaryOp(<,Id(x),FloatLiteral(10.5)),[],[Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1))),While(BinaryOp(==,Id(y),IntLiteral(1)),[],[Assign(Id(dd),Id(nn)),Assign(ArrayCell(Id(y),[Id(i)]),ArrayCell(Id(x),[BinaryOp(+,Id(y),Id(i))]))])])]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,319))

    # def test_whileFunc_5(self):
    #     input = """Var: x = 5;
    #     Function: main
    #     Parameter: a[0o123]
    #     Body:
    #         While (x < 10.5) Do
    #             x = x + 1;
    #             While y == 1 Do
    #                 dd = nn;
    #                 y[i] = x[y + i];
    #                 a[0xDD] = 10.9;
    #             EndWhile.
    #         EndWhile.
    #     EndBody.
    #     """
    #     expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main)[VarDecl(Id(a),[83])],([][While(BinaryOp(<,Id(x),FloatLiteral(10.5)),[],[Assign(Id(x),BinaryOp(+,Id(x),IntLiteral(1))),While(BinaryOp(==,Id(y),IntLiteral(1)),[],[Assign(Id(dd),Id(nn)),Assign(ArrayCell(Id(y),[Id(i)]),ArrayCell(Id(x),[BinaryOp(+,Id(y),Id(i))])),Assign(ArrayCell(Id(a),[IntLiteral(221)]),FloatLiteral(10.9))])])]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,320))

    # def test_DoWhileFunc_1(self):
    #     input = """Var: x = 5;
    #     Function: main
    #     Parameter: a[0o123]
    #     Body:
    #         Do While 1
    #         EndDo.
    #     EndBody.
    #     """
    #     expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main)[VarDecl(Id(a),[83])],([][Dowhile([],[],IntLiteral(1))]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    # def test_DoWhileFunc_2(self):
    #     input = """Var: x = 5;
    #     Function: main
    #     Parameter: a[0o123]
    #     Body:
    #         Do
    #             Do 
    #                 Var: a = 10, c = 100.5;
    #             While (x <= 1) || (x != 10)
    #             EndDo.
    #         While (x <= 1) || (x != 10)
    #         EndDo.
    #     EndBody.
    #     """
    #     expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main)[VarDecl(Id(a),[83])],([][Dowhile([],[Dowhile([VarDecl(Id(a),IntLiteral(10)),VarDecl(Id(c),FloatLiteral(100.5))],[],BinaryOp(||,BinaryOp(<=,Id(x),IntLiteral(1)),BinaryOp(!=,Id(x),IntLiteral(10))))],BinaryOp(||,BinaryOp(<=,Id(x),IntLiteral(1)),BinaryOp(!=,Id(x),IntLiteral(10))))]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 322))
    
    # def test_DoWhileFunc_3(self):
    #     input = """Var: x = 5;
    #     Function: main
    #     Parameter: a[0o123], b, c
    #     Body:
    #         Do 
    #             Var: a = 10, c = 100.5;
    #             x = a[x + 1][foo(a + 1) + 3];
    #         While (x <= 1) || (x != 10)
    #         EndDo.
    #     EndBody.
    #     """
    #     expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main)[VarDecl(Id(a),[83]),VarDecl(Id(b)),VarDecl(Id(c))],([][Dowhile([VarDecl(Id(a),IntLiteral(10)),VarDecl(Id(c),FloatLiteral(100.5))],[Assign(Id(x),ArrayCell(Id(a),[BinaryOp(+,Id(x),IntLiteral(1)),BinaryOp(+,CallExpr(Id(foo),[BinaryOp(+,Id(a),IntLiteral(1))]),IntLiteral(3))]))],BinaryOp(||,BinaryOp(<=,Id(x),IntLiteral(1)),BinaryOp(!=,Id(x),IntLiteral(10))))]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    # def test_all_1(self):
    #     input = """Var: x = 5;
    #     Function: main
    #     Parameter: a[0o123]
    #     Body:
    #         y = x-(!(!True));
    #         Return;
    #     EndBody.
    #     Function: count
    #     Parameter: i
    #     Body:
    #         y = x-(!(!True));
    #         Return;
    #     EndBody.
    #     """
    #     expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main)[VarDecl(Id(a),[83])],([][Assign(Id(y),BinaryOp(-,Id(x),UnaryOp(!,UnaryOp(!,BooleanLiteral(true))))),Return()])),FuncDecl(Id(count)[VarDecl(Id(i))],([][Assign(Id(y),BinaryOp(-,Id(x),UnaryOp(!,UnaryOp(!,BooleanLiteral(true))))),Return()]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    # def test_ifStmtInFunc_5(self):
    #     input = """
    #     Var: i[123][1][2]={1,2,3,4,5};
    #     Function: main
    #     Parameter: a, b
    #     Body:
    #     Var: r = 10., v;
    #     If 5 + 2 == 3 Then 
    #         Var:a;
    #         a = x +3;
    #     ElseIf 5+2 == 3 Then 
    #         Var:a;
    #         a = x +3;
    #     ElseIf 5+2 == 3 Then 
    #         Var:a;
    #         a = x +3;
    #     Else
    #         Var:a;
    #         a = x +3;
    #     EndIf.
    #     EndBody.
    #     """
    #     expect = """Program([VarDecl(Id(i),[123,1,2],ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5))),FuncDecl(Id(main)[VarDecl(Id(a)),VarDecl(Id(b))],([VarDecl(Id(r),FloatLiteral(10.0)),VarDecl(Id(v))][If(BinaryOp(==,BinaryOp(+,IntLiteral(5),IntLiteral(2)),IntLiteral(3)),[VarDecl(Id(a))],[Assign(Id(a),BinaryOp(+,Id(x),IntLiteral(3)))])ElseIf(BinaryOp(==,BinaryOp(+,IntLiteral(5),IntLiteral(2)),IntLiteral(3)),[VarDecl(Id(a))],[Assign(Id(a),BinaryOp(+,Id(x),IntLiteral(3)))])ElseIf(BinaryOp(==,BinaryOp(+,IntLiteral(5),IntLiteral(2)),IntLiteral(3)),[VarDecl(Id(a))],[Assign(Id(a),BinaryOp(+,Id(x),IntLiteral(3)))])Else([VarDecl(Id(a))],[Assign(Id(a),BinaryOp(+,Id(x),IntLiteral(3)))])]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    # def test_ifStmtInFunc_6(self):
    #     input = """
    #     Var: i[123][1][2]={1,2,3,4,5};
    #     Function: main
    #     Parameter: a, b
    #     Body:
    #     Var: r = 10., v;
    #     If 5 + 2 == 3 Then 
    #         Var:a;
    #         a = x +3;
    #     ElseIf 5+2 == 3 Then 
    #         Var:a;
    #         a = x +3;
    #     EndIf.
    #     EndBody.
    #     """
    #     expect = """Program([VarDecl(Id(i),[123,1,2],ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5))),FuncDecl(Id(main)[VarDecl(Id(a)),VarDecl(Id(b))],([VarDecl(Id(r),FloatLiteral(10.0)),VarDecl(Id(v))][If(BinaryOp(==,BinaryOp(+,IntLiteral(5),IntLiteral(2)),IntLiteral(3)),[VarDecl(Id(a))],[Assign(Id(a),BinaryOp(+,Id(x),IntLiteral(3)))])ElseIf(BinaryOp(==,BinaryOp(+,IntLiteral(5),IntLiteral(2)),IntLiteral(3)),[VarDecl(Id(a))],[Assign(Id(a),BinaryOp(+,Id(x),IntLiteral(3)))])]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    # def test_ifStmtInFunc_7(self):
    #     input = """
    #         Var: i;
    #         Function: main
    #         Parameter: a, b
    #         Body:
    #         Var: r = 10., v;
    #         If 5 + 2 == 3 Then 
    #             Var:a;
    #             Var:b;
    #             a = x +3;
    #             a = x +3;
    #         ElseIf 5+2 == 3 Then 
    #             Var:a;
    #             Var:b;
    #             a = x +3;
    #             a = x +3;
    #         ElseIf 5+2 == 3 Then 
    #             Var:a;
    #             Var:b;
    #             a = x +3;
    #             a = x +3;
    #         Else
    #             Var:a;
    #             Var:b;
    #             a = x +3;
    #             a = x +3;
    #         EndIf.
    #         EndBody.
    #         """
    #     expect = """Program([VarDecl(Id(i)),FuncDecl(Id(main)[VarDecl(Id(a)),VarDecl(Id(b))],([VarDecl(Id(r),FloatLiteral(10.0)),VarDecl(Id(v))][If(BinaryOp(==,BinaryOp(+,IntLiteral(5),IntLiteral(2)),IntLiteral(3)),[VarDecl(Id(a)),VarDecl(Id(b))],[Assign(Id(a),BinaryOp(+,Id(x),IntLiteral(3))),Assign(Id(a),BinaryOp(+,Id(x),IntLiteral(3)))])ElseIf(BinaryOp(==,BinaryOp(+,IntLiteral(5),IntLiteral(2)),IntLiteral(3)),[VarDecl(Id(a)),VarDecl(Id(b))],[Assign(Id(a),BinaryOp(+,Id(x),IntLiteral(3))),Assign(Id(a),BinaryOp(+,Id(x),IntLiteral(3)))])ElseIf(BinaryOp(==,BinaryOp(+,IntLiteral(5),IntLiteral(2)),IntLiteral(3)),[VarDecl(Id(a)),VarDecl(Id(b))],[Assign(Id(a),BinaryOp(+,Id(x),IntLiteral(3))),Assign(Id(a),BinaryOp(+,Id(x),IntLiteral(3)))])Else([VarDecl(Id(a)),VarDecl(Id(b))],[Assign(Id(a),BinaryOp(+,Id(x),IntLiteral(3))),Assign(Id(a),BinaryOp(+,Id(x),IntLiteral(3)))])]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    # def test_all_2(self):
    #     input = """Var: x = 5;
    #     Function: main
    #     Body:
    #         x = 10;
    #         printLn(x);
    #         Continue;
    #     EndBody.
    #     """
    #     expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main)[],([][Assign(Id(x),IntLiteral(10)),CallExpr(Id(printLn),[Id(x)]),Continue()]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    # def test_all_3(self):
    #     input = """Var: x = 5;
    #     Function: main
    #     Body:
    #         x = 10;
    #         printLn(x);
    #         Continue;
    #         Break;
    #         Return;
    #         foo();
    #     EndBody.
    #     """
    #     expect = """Program([VarDecl(Id(x),IntLiteral(5)),FuncDecl(Id(main)[],([][Assign(Id(x),IntLiteral(10)),CallExpr(Id(printLn),[Id(x)]),Continue(),Break(),Return(),CallExpr(Id(foo),[])]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    # def test_declare_6(self):
    #     input = """Var: b[2][3] = {{2,3,4},{4,5,6}};"""
    #     expect = """Program([VarDecl(Id(b),[2,3],ArrayLiteral(ArrayLiteral(IntLiteral(2),IntLiteral(3),IntLiteral(4)),ArrayLiteral(IntLiteral(4),IntLiteral(5),IntLiteral(6))))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,330))

    # def test_declare_7(self):
    #     input = """Var: a = 0;
    #     Function: main
    #     Body:
    #         a[3 + foo(2)] = a[b [2][3]] + 4;
    #     EndBody."""
    #     expect = """Program([VarDecl(Id(a),IntLiteral(0)),FuncDecl(Id(main)[],([][Assign(ArrayCell(Id(a),[BinaryOp(+,IntLiteral(3),CallExpr(Id(foo),[IntLiteral(2)]))]),BinaryOp(+,ArrayCell(Id(a),[ArrayCell(Id(b),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(4)))]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,331))

    # def test_declare_8(self):
    #     input = """Var: a = 0;
    #     Function: main
    #     Body:
    #         v = (4. \. 3.) *. 3.14 *. r *. r *. r;
    #     EndBody."""
    #     expect = """Program([VarDecl(Id(a),IntLiteral(0)),FuncDecl(Id(main)[],([][Assign(Id(v),BinaryOp(*.,BinaryOp(*.,BinaryOp(*.,BinaryOp(*.,BinaryOp(\.,FloatLiteral(4.0),FloatLiteral(3.0)),FloatLiteral(3.14)),Id(r)),Id(r)),Id(r)))]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,332))

    # def test_declare_9(self):
    #     input = """Var: a = 0;
    #     Function: main
    #     Body:
    #         foo(a[1][2] + 2, x + 1);
    #     EndBody."""
    #     expect = """Program([VarDecl(Id(a),IntLiteral(0)),FuncDecl(Id(main)[],([][CallExpr(Id(foo),[BinaryOp(+,ArrayCell(Id(a),[IntLiteral(1),IntLiteral(2)]),IntLiteral(2)),BinaryOp(+,Id(x),IntLiteral(1))])]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,333))

    # def test_declare_10(self):
    #     input = """Var: a = 0;
    #     Function: main
    #     Body:
    #         x = foo(a[1][2] + 2, x + 1);
    #     EndBody."""
    #     expect = """Program([VarDecl(Id(a),IntLiteral(0)),FuncDecl(Id(main)[],([][Assign(Id(x),CallExpr(Id(foo),[BinaryOp(+,ArrayCell(Id(a),[IntLiteral(1),IntLiteral(2)]),IntLiteral(2)),BinaryOp(+,Id(x),IntLiteral(1))]))]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,334))

    # def test_whileFunc_6(self):
    #     input = """Function: foo
    #     Parameter: a[5], b
    #     Body:
    #         Var: i = 0;
    #         While (i < 5) Do
    #             a[i] = b +. 1.0;
    #             i = i + 1;
    #         EndWhile.
    #     EndBody."""
    #     expect = """Program([FuncDecl(Id(foo)[VarDecl(Id(a),[5]),VarDecl(Id(b))],([VarDecl(Id(i),IntLiteral(0))][While(BinaryOp(<,Id(i),IntLiteral(5)),[],[Assign(ArrayCell(Id(a),[Id(i)]),BinaryOp(+.,Id(b),FloatLiteral(1.0))),Assign(Id(i),BinaryOp(+,Id(i),IntLiteral(1)))])]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,335))

    # def test_whileFunc_6(self):
    #     input = """Function: foo
    #     Parameter: a[5], b
    #     Body:
    #         Var: i = 0;
    #         While (i < 5) Do
    #             a[i] = b +. 1.0;
    #             i = i + 1;
    #         EndWhile.
    #     EndBody."""
    #     expect = """Program([FuncDecl(Id(foo)[VarDecl(Id(a),[5]),VarDecl(Id(b))],([VarDecl(Id(i),IntLiteral(0))][While(BinaryOp(<,Id(i),IntLiteral(5)),[],[Assign(ArrayCell(Id(a),[Id(i)]),BinaryOp(+.,Id(b),FloatLiteral(1.0))),Assign(Id(i),BinaryOp(+,Id(i),IntLiteral(1)))])]))])"""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,335))

#     def test_all_4(self):
#         input = """Var: a = 0;
# Function: main
# Body:
#     For (i = 0, i < 10, 2) Do
#         writeln(i);
#     EndFor.
# EndBody."""
#         expect = """Program([VarDecl(Id(a),IntLiteral(0)),FuncDecl(Id(main)[],([][For(Id(i),IntLiteral(0),BinaryOp(<,Id(i),IntLiteral(10)),IntLiteral(2),[],[CallExpr(Id(writeln),[Id(i)])])]))])"""
#         self.assertTrue(TestAST.checkASTGen(input,expect,336))

#     def test_all_5(self):
#         input = """Var: a = 5;
# Var: b[2][3] = {{2,3,4},{4,5,6}};
# Var: c, d = 6, e, f;
# Var: m, n[10];"""
#         expect = """Program([VarDecl(Id(a),IntLiteral(5)),VarDecl(Id(b),[2,3],ArrayLiteral(ArrayLiteral(IntLiteral(2),IntLiteral(3),IntLiteral(4)),ArrayLiteral(IntLiteral(4),IntLiteral(5),IntLiteral(6)))),VarDecl(Id(c)),VarDecl(Id(d),IntLiteral(6)),VarDecl(Id(e)),VarDecl(Id(f)),VarDecl(Id(m)),VarDecl(Id(n),[10])])"""
#         self.assertTrue(TestAST.checkASTGen(input,expect,337))

#     def test_all_6(self):
#         input = """Var: x;
# Function: fact
#     Parameter: n
#     Body:
#         If n == 0 Then
#             Return 1;
#         Else
#             Return n * fact (n - 1);
#         EndIf.
#     EndBody.
# Function: main
#     Body:
#         x = 10;
#         fact (x);
#     EndBody."""
#         expect = """Program([VarDecl(Id(x)),FuncDecl(Id(fact)[VarDecl(Id(n))],([][If(BinaryOp(==,Id(n),IntLiteral(0)),[],[Return(IntLiteral(1))])Else([],[Return(BinaryOp(*,Id(n),CallExpr(Id(fact),[BinaryOp(-,Id(n),IntLiteral(1))])))])])),FuncDecl(Id(main)[],([][Assign(Id(x),IntLiteral(10)),CallExpr(Id(fact),[Id(x)])]))])"""
#         self.assertTrue(TestAST.checkASTGen(input,expect,338))

#     def test_all_7(self):
#         input = """Var: a[5] = {1,4,3,2,0};
# Var: b[2][3]={{1,2,3},{4,5,6}};"""
#         expect = """Program([VarDecl(Id(a),[5],ArrayLiteral(IntLiteral(1),IntLiteral(4),IntLiteral(3),IntLiteral(2),IntLiteral(0))),VarDecl(Id(b),[2,3],ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(2),IntLiteral(3)),ArrayLiteral(IntLiteral(4),IntLiteral(5),IntLiteral(6))))])"""
#         self.assertTrue(TestAST.checkASTGen(input,expect,339))

#     def test_all_8(self):
#         input = """Var: x;
# Function: fact
#     Parameter: n
#     Body:
#         If n == 0 Then
#             Return 1;
#         Else
#             Return n * fact (n - 1);
#         EndIf.
#     EndBody.
# Function: main
#     Body:
#         x = 10;
#         fact (x);
#     EndBody."""
#         expect = """Program([VarDecl(Id(x)),FuncDecl(Id(fact)[VarDecl(Id(n))],([][If(BinaryOp(==,Id(n),IntLiteral(0)),[],[Return(IntLiteral(1))])Else([],[Return(BinaryOp(*,Id(n),CallExpr(Id(fact),[BinaryOp(-,Id(n),IntLiteral(1))])))])])),FuncDecl(Id(main)[],([][Assign(Id(x),IntLiteral(10)),CallExpr(Id(fact),[Id(x)])]))])"""
#         self.assertTrue(TestAST.checkASTGen(input,expect,340))

#     def test_all_9(self):
#         input = """Var: a = 0;
# Function: main
# Body:
#     foo(a[1][2] + 2, x + 1);
#     foo (2 + x, 4. \. y);
#     goo ();
# EndBody."""
#         expect = """Program([VarDecl(Id(a),IntLiteral(0)),FuncDecl(Id(main)[],([][CallExpr(Id(foo),[BinaryOp(+,ArrayCell(Id(a),[IntLiteral(1),IntLiteral(2)]),IntLiteral(2)),BinaryOp(+,Id(x),IntLiteral(1))]),CallExpr(Id(foo),[BinaryOp(+,IntLiteral(2),Id(x)),BinaryOp(\.,FloatLiteral(4.0),Id(y))]),CallExpr(Id(goo),[])]))])"""
#         self.assertTrue(TestAST.checkASTGen(input,expect,341))

#     def test_all_10(self):
#         input = """Var: a = 0;
# Function: main
# Body:
#     foo(a[1][2] + 2, x + 1);
#     foo (2 + x, 4. \. y);
#     goo ();
#     If bool_of_string ("True") Then
#         a = int_of_string (read ());
#         b = float_of_int (a) +. 2.0;
#         foo(a[1][2] + 2, x + 1);
#         foo (2 + x, 4. \. y);
#         goo ();
#     EndIf.
# EndBody."""
#         expect = """Program([VarDecl(Id(a),IntLiteral(0)),FuncDecl(Id(main)[],([][CallExpr(Id(foo),[BinaryOp(+,ArrayCell(Id(a),[IntLiteral(1),IntLiteral(2)]),IntLiteral(2)),BinaryOp(+,Id(x),IntLiteral(1))]),CallExpr(Id(foo),[BinaryOp(+,IntLiteral(2),Id(x)),BinaryOp(\.,FloatLiteral(4.0),Id(y))]),CallExpr(Id(goo),[]),If(CallExpr(Id(bool_of_string),[StringLiteral(True)]),[],[Assign(Id(a),CallExpr(Id(int_of_string),[CallExpr(Id(read),[])])),Assign(Id(b),BinaryOp(+.,CallExpr(Id(float_of_int),[Id(a)]),FloatLiteral(2.0))),CallExpr(Id(foo),[BinaryOp(+,ArrayCell(Id(a),[IntLiteral(1),IntLiteral(2)]),IntLiteral(2)),BinaryOp(+,Id(x),IntLiteral(1))]),CallExpr(Id(foo),[BinaryOp(+,IntLiteral(2),Id(x)),BinaryOp(\.,FloatLiteral(4.0),Id(y))]),CallExpr(Id(goo),[])])]))])"""
#         self.assertTrue(TestAST.checkASTGen(input,expect,342))

#     def test_all_11(self):
#         input = """Function: test
# Parameter: n
# Body:
#     If n > 10 Then
#         Return 5;
#     Else
#         Return False;
#     EndIf.
# EndBody."""
#         expect = """Program([FuncDecl(Id(test)[VarDecl(Id(n))],([][If(BinaryOp(>,Id(n),IntLiteral(10)),[],[Return(IntLiteral(5))])Else([],[Return(BooleanLiteral(false))])]))])"""
#         self.assertTrue(TestAST.checkASTGen(input,expect,343))

#     def test_all_12(self):
#         input = """Var: a = 1, b[2][3] = {5}, c[2] = {{1,3},{1,5,7}};
# Function: test
# Parameter: n
# Body:
#     If n > 10 Then
#         Return 5;
#     Else
#         Return False;
#     EndIf.
# EndBody."""
#         expect = """Program([VarDecl(Id(a),IntLiteral(1)),VarDecl(Id(b),[2,3],ArrayLiteral(IntLiteral(5))),VarDecl(Id(c),[2],ArrayLiteral(ArrayLiteral(IntLiteral(1),IntLiteral(3)),ArrayLiteral(IntLiteral(1),IntLiteral(5),IntLiteral(7)))),FuncDecl(Id(test)[VarDecl(Id(n))],([][If(BinaryOp(>,Id(n),IntLiteral(10)),[],[Return(IntLiteral(5))])Else([],[Return(BooleanLiteral(false))])]))])"""
#         self.assertTrue(TestAST.checkASTGen(input,expect,344))

#     def test_all_13(self):
#         input = """Function: test
# Parameter: n
# Body:
#     If n > 10 Then
#         Return 5;
#     Else
#         Return a[4][5 + b[2][3]];
#     EndIf.
# EndBody."""
#         expect = """Program([FuncDecl(Id(test)[VarDecl(Id(n))],([][If(BinaryOp(>,Id(n),IntLiteral(10)),[],[Return(IntLiteral(5))])Else([],[Return(ArrayCell(Id(a),[IntLiteral(4),BinaryOp(+,IntLiteral(5),ArrayCell(Id(b),[IntLiteral(2),IntLiteral(3)]))]))])]))])"""
#         self.assertTrue(TestAST.checkASTGen(input,expect,345))

#     def test_all_14(self):
#         input = """Var: a = "Xin chao moi nguoi!";
# Var: b = 5, c = False;"""
#         expect = """Program([VarDecl(Id(a),StringLiteral(Xin chao moi nguoi!)),VarDecl(Id(b),IntLiteral(5)),VarDecl(Id(c),BooleanLiteral(false))])"""
#         self.assertTrue(TestAST.checkASTGen(input,expect,346))

#     def test_all_15(self):
#         input = """Function: test
# Body:
#     If n > 10 Then
#         Return n;
#     ElseIf n > 8 Then
#         Return n + 1;
#     ElseIf n > 6 Then
#         Return n + 2;
#     ElseIf n > 4 Then
#         Return n + 3;
#     ElseIf n > 2 Then
#         Return n + 4;
#     Else
#         Return False;
#     EndIf.
# EndBody."""
#         expect = """Program([FuncDecl(Id(test)[],([][If(BinaryOp(>,Id(n),IntLiteral(10)),[],[Return(Id(n))])ElseIf(BinaryOp(>,Id(n),IntLiteral(8)),[],[Return(BinaryOp(+,Id(n),IntLiteral(1)))])ElseIf(BinaryOp(>,Id(n),IntLiteral(6)),[],[Return(BinaryOp(+,Id(n),IntLiteral(2)))])ElseIf(BinaryOp(>,Id(n),IntLiteral(4)),[],[Return(BinaryOp(+,Id(n),IntLiteral(3)))])ElseIf(BinaryOp(>,Id(n),IntLiteral(2)),[],[Return(BinaryOp(+,Id(n),IntLiteral(4)))])Else([],[Return(BooleanLiteral(false))])]))])"""
#         self.assertTrue(TestAST.checkASTGen(input,expect,347))

#     def test_all_16(self):
#         input = """Function: test
# Body:
#     If n > 10 Then
#         Return n;
#     ElseIf n > 8 Then
#         Return n + 1;
#     Else
#         Return False;
#     EndIf.
# EndBody."""
#         expect = """Program([FuncDecl(Id(test)[],([][If(BinaryOp(>,Id(n),IntLiteral(10)),[],[Return(Id(n))])ElseIf(BinaryOp(>,Id(n),IntLiteral(8)),[],[Return(BinaryOp(+,Id(n),IntLiteral(1)))])Else([],[Return(BooleanLiteral(false))])]))])"""
#         self.assertTrue(TestAST.checkASTGen(input,expect,348))

#     def test_all_17(self):
#         input = """Function: test
# Body:
#     If n > 10 Then
#         Return n;
#     ElseIf n > 8 Then
#         Return n + 1;
#     ElseIf n > 6 Then
#         Return n + 2;
#     ElseIf n > 4 Then
#         Return n + 3;
#     ElseIf n > 2 Then
#         Return n + 4;
#     EndIf.
# EndBody."""
#         expect = """Program([FuncDecl(Id(test)[],([][If(BinaryOp(>,Id(n),IntLiteral(10)),[],[Return(Id(n))])ElseIf(BinaryOp(>,Id(n),IntLiteral(8)),[],[Return(BinaryOp(+,Id(n),IntLiteral(1)))])ElseIf(BinaryOp(>,Id(n),IntLiteral(6)),[],[Return(BinaryOp(+,Id(n),IntLiteral(2)))])ElseIf(BinaryOp(>,Id(n),IntLiteral(4)),[],[Return(BinaryOp(+,Id(n),IntLiteral(3)))])ElseIf(BinaryOp(>,Id(n),IntLiteral(2)),[],[Return(BinaryOp(+,Id(n),IntLiteral(4)))])]))])"""
#         self.assertTrue(TestAST.checkASTGen(input,expect,349))
        # expect = """"""
        # self.assertTrue(TestAST.checkASTGen(input, expect, 321))