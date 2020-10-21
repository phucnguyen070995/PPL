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
        input = """Var:x[10] = True, a;"""
        expect = str(Program([VarDecl(Id("x"),[10],BooleanLiteral(True)),VarDecl(Id("a"),[],None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_declare_5(self):
        input = """Var:x[10][50] = True, a;"""
        expect = str(Program([VarDecl(Id("x"),[10,50],BooleanLiteral(True)),VarDecl(Id("a"),[],None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_declare_6(self):
        input = """Var:x[10][50] = True, a = 1;"""
        expect = str(Program([VarDecl(Id("x"),[10,50],BooleanLiteral(True)),VarDecl(Id("a"),[],IntLiteral(1))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306)) 

    def test_declare_7(self):
        input = """Var:x[10][50] = True, a = 10, c = 100.5;"""
        expect = str(Program([VarDecl(Id("x"),[10,50],BooleanLiteral(True)),VarDecl(Id("a"),[],IntLiteral(10)),VarDecl(Id("c"),[],FloatLiteral(100.5))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
    
    def test_declare_8(self):
        input = """Var:x[10][50] = True, a = 10, c = 100.5;
        Var: me;
        """
        expect = str(Program([VarDecl(Id("x"),[10,50],BooleanLiteral(True)),VarDecl(Id("a"),[],IntLiteral(10)),VarDecl(Id("c"),[],FloatLiteral(100.5)), VarDecl(Id("me"),[],[])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    
    def test_declare_9(self):
        input = """Var:x[10][50] = True, a = 10, c = 100.5;
        Var: me, you;
        """
        expect = str(Program([VarDecl(Id("x"),[10,50],BooleanLiteral(True)),VarDecl(Id("a"),[],IntLiteral(10)),VarDecl(Id("c"),[],FloatLiteral(100.5)), VarDecl(Id("me"),[],[]), VarDecl(Id("you"),[],[])]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))
     
    def test_declare_10(self):
        input = """Var:x[10][50] = True, a = 10, c = 100.5;
        Var: me, you;
        Var: he[1][2][3][4][5] = 12.5;
        Var: she = False;
        """
        expect = str(Program([VarDecl(Id("x"),[10,50],BooleanLiteral(True)),VarDecl(Id("a"),[],IntLiteral(10)),VarDecl(Id("c"),[],FloatLiteral(100.5)), VarDecl(Id("me"),[],[]), VarDecl(Id("you"),[],[]), VarDecl(Id("he"),[1,2,3,4,5],FloatLiteral(12.5)), VarDecl(Id("she"),[],BooleanLiteral(False))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_funcDeclar1(self):
        input = """Var: x = 5;
        Function: main
        Body:
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),[],([],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_funcDeclar2(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[5], b
        Body:
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),[VarDecl(Id("a"),[5],[]), VarDecl(Id("b"),[],[])],([],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))
    
    def test_funcDeclar3(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[5][9][3], b[7]
        Body:
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),[VarDecl(Id("a"),[5,9,3],[]),VarDecl(Id("b"),[7],[])],([],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_funcDeclar4(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[5][9][3], b[7]
        Body:
        Var: m;
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),[VarDecl(Id("a"),[5,9,3],[]),VarDecl(Id("b"),[7],[])],([VarDecl(Id("m"),[],[])],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_funcDeclar5(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[5][9][3], b[7]
        Body:
        Var: m = 10;
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),[VarDecl(Id("a"),[5,9,3],[]),VarDecl(Id("b"),[7],[])],([VarDecl(Id("m"),[],IntLiteral(10))],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_funcDeclar6(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[5][9][3], b[7]
        Body:
        Var: m[10][8] = 10.0;
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),[VarDecl(Id("a"),[5,9,3],[]),VarDecl(Id("b"),[7],[])],([VarDecl(Id("m"),[10,8],FloatLiteral(10.0))],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_funcDeclar7(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[5][9][3], b[7]
        Body:
        Var: m[10][8] = 10.0;
        Var: a = 1;
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),[VarDecl(Id("a"),[5,9,3],[]),VarDecl(Id("b"),[7],[])],([VarDecl(Id("m"),[10,8],FloatLiteral(10.0)),VarDecl(Id("a"),[],IntLiteral("1")) ],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    
    def test_funcDeclar8(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[5][9][3], b[7]
        Body:
        Var: m[10][8] = 10.0;
        Var: ngao, du = 3, thienha[5][9][1][2];
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),[VarDecl(Id("a"),[5,9,3],[]),VarDecl(Id("b"),[7],[])],
            ([VarDecl(Id("m"),[10,8],FloatLiteral(10.0)),VarDecl(Id("ngao"),[],[]), VarDecl(Id("du"),[],IntLiteral(3)),
             VarDecl(Id("thienha"),[5,9,1,2],[])],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_funcDeclar9(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[5], b
        Body:
        Var: yy;
        yy = 5;
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),[VarDecl(Id("a"),[5],[]), VarDecl(Id("b"),[],[])],([VarDecl(Id("yy"),[],[])],[Assign(Id("yy"),IntLiteral(5))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_asignInFunc_0(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[5], b
        Body:
        Var: yy;
        yy = 5 + 7;
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),[VarDecl(Id("a"),[5],[]), VarDecl(Id("b"),[],[])],([VarDecl(Id("yy"),[],[])],[Assign(Id("yy"),BinaryOp("+",IntLiteral(5),IntLiteral(7)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_asignInFunc_1(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[5], b
        Body:
        Var: yy;
        yy = x + 7;
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),[VarDecl(Id("a"),[5],[]), VarDecl(Id("b"),[],[])],([VarDecl(Id("yy"),[],[])],[Assign(Id("yy"),BinaryOp("+",Id("x"),IntLiteral(7)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_asignInFunc_2(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[5], b
        Body:
        Var: yy;
        yy = x[5] + 7;
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),[VarDecl(Id("a"),[5],[]), VarDecl(Id("b"),[],[])],([VarDecl(Id("yy"),[],[])],[Assign(Id("yy"),BinaryOp("+",ArrayCell(Id("x"),[IntLiteral(5)]) ,IntLiteral(7)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_asignInFunc_3(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[5], b
        Body:
        Var: yy;
        yy = x[5 + b[a + c[9]]] + 7;
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),[VarDecl(Id("a"),[5],[]), VarDecl(Id("b"),[],[])],([VarDecl(Id("yy"),[],[])],
            [Assign(Id("yy"),BinaryOp("+",ArrayCell(Id("x"),[BinaryOp("+",IntLiteral(5),ArrayCell(Id("b"),[BinaryOp("+",Id("a"),ArrayCell(Id("c"),[IntLiteral(9)]))]))]) ,IntLiteral(7)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))


    def test_asignInFunc_4(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[5][9][3], b[7]
        Body:
        Var: m[10][8] = 10.0;
        a = b;
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
            [VarDecl(Id("a"),[5,9,3],[]),VarDecl(Id("b"),[7],[])],
            ([VarDecl(Id("m"),[10,8],FloatLiteral(10.0))],[Assign(Id("a"),Id("b"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_asignInFunc_5(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0xAB]
        Body:
        a = b;
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
            [VarDecl(Id("a"),[171],[])],
            ([],[Assign(Id("a"),Id("b"))]))
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
    
    def test_asignInFunc_6(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
        a = b;
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
            [VarDecl(Id("a"),[83],[])],
            ([],[Assign(Id("a"),Id("b"))]))
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_asignInFunc_7(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
        a = foo();
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
            [VarDecl(Id("a"),[83],[])],
            ([],[Assign(Id("a"), CallExpr(Id("foo"),[]))]))
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_asignInFunc_8(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
        a = foo(b);
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
            [VarDecl(Id("a"),[83],[])],
            ([],[Assign(Id("a"), CallExpr(Id("foo"),[Id("b")]))]))
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_asignInFunc_9(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
        a = foo(b[x]);
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
            [VarDecl(Id("a"),[83],[])],
            ([],[Assign(Id("a"), CallExpr(Id("foo"),[ArrayCell(Id("b"),[Id("x")]) ]))]))
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_asignInFunc_9(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
        a = foo(b[x]);
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
            [VarDecl(Id("a"),[83],[])],
            ([],[Assign(Id("a"), CallExpr(Id("foo"),[ArrayCell(Id("b"),[Id("x")]) ]))]))
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_ifStmtInFunc_0(self):
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
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
            [VarDecl(Id("a"),[83],[])],
            (
                [],
                [If( 
                    [
                        (BinaryOp("==", Id("x"), Id("y")),
                        [],
                        [Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1)))]
                        )
                    ],
                    ([VarDecl(Id('a'), [], None)],[]))
                ]
            ))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))


    def test_ifStmtInFunc_1(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0O123]
        Body:
        If x == y Then x = x + 1; 
        EndIf.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
            [VarDecl(Id("a"),[83],[])],
            (
                [],
                [If( 
                    [
                        (BinaryOp("==", Id("x"), Id("y")),
                        [],
                        [Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1)))]
                        )
                    ],
                    ([],[]))
                ]
            ))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_ifStmtInFunc_2(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0O123]
        Body:
        If x == y Then x = x + 1; 
        ElseIf x > y Then y = y + 1;
        EndIf.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
            [VarDecl(Id("a"),[83],[])],
            (
                [],
                [If( 
                    [
                        (BinaryOp("==", Id("x"), Id("y")),
                        [],
                        [Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1)))]
                        ),
                        (
                            BinaryOp(">", Id("x"), Id("y")),
                            [],
                            [Assign(Id("y"), BinaryOp("+", Id("y"), IntLiteral(1) ))]
                        )
                    ],
                    ([],[]))
                ]
            ))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_ifStmtInFunc_3(self):
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
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
            [VarDecl(Id("a"),[83],[])],
            (
                [],
                [If( 
                    [
                        (BinaryOp("==", Id("x"), Id("y")),
                        [],
                        [Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1)))]
                        ),
                        (
                            BinaryOp(">", Id("x"), Id("y")),
                            [],
                            [Assign(Id("y"), BinaryOp("+", Id("y"), IntLiteral(1) ))]
                        ),
                        (
                            BinaryOp("<", Id("x"), Id("y")),
                            [],
                            [Assign(Id("y"), BinaryOp("-", Id("y"), Id("x")))]
                        )
                    ],
                    ([],[])
                    )
                ]
            ))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_ifStmtInFunc_3(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0O123]
        Body:
        If x == y Then x = x + 1; 
        ElseIf x > y Then 
        ElseIf x < y Then 
        EndIf.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
            [VarDecl(Id("a"),[83],[])],
            (
                [],
                [If( 
                    [
                        (BinaryOp("==", Id("x"), Id("y")),
                        [],
                        [Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1)))]
                        ),
                        (
                            BinaryOp(">", Id("x"), Id("y")),
                            [],
                            []
                        ),
                        (
                            BinaryOp("<", Id("x"), Id("y")),
                            [],
                            []
                        )
                    ],
                    ([],[]))
                ]
            ))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,333)) 

    def test_ifStmtInFunc_4(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0O123]
        Body:
        If x == y Then x = x + 1; 
        ElseIf x > y Then 
        ElseIf x < y Then 
        Else
        EndIf.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
            [VarDecl(Id("a"),[83],[])],
            (
                [],
                [If( 
                    [
                        (BinaryOp("==", Id("x"), Id("y")),
                        [],
                        [Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1)))]
                        ),
                        (
                            BinaryOp(">", Id("x"), Id("y")),
                            [],
                            []
                        ),
                        (
                            BinaryOp("<", Id("x"), Id("y")),
                            [],
                            []
                        )
                    ],
                    ([],[]))
                ]
            ))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,334)) 

    def test_ifStmtInFunc_5(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0O123]
        Body:
        If x == y Then x = x + 1; 
        ElseIf x > y Then 
        ElseIf x < y Then 
        Else
            If y > 10 Then y = y / 2;
            EndIf.
        EndIf.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
            [VarDecl(Id("a"),[83],[])],
            (
                [],
                [If( 
                    [
                        (BinaryOp("==", Id("x"), Id("y")),
                        [],
                        [Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1)))]
                        ),
                        (
                            BinaryOp(">", Id("x"), Id("y")),
                            [],
                            []
                        ),
                        (
                            BinaryOp("<", Id("x"), Id("y")),
                            [],
                            []
                        )
                    ],
                    (
                        [],
                        [
                            If(
                                [
                                    (
                                        BinaryOp(">", Id("y"), IntLiteral(10)),
                                        [],
                                        [Assign(Id("y"), BinaryOp("/", Id("y"), IntLiteral(2)))]
                                    )
                                ],
                                (
                                    [],
                                    []
                                )
                            )
                        ]
                    ))
                ]
            ))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,335)) 

    def test_ifStmtInFunc_6(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0O123]
        Body:
        If x == y Then x = x + 1; 
        ElseIf x > y Then x = voo(1.2);
        ElseIf x < y Then y = b[goo(x)];
        Else foo();
        EndIf.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
            [VarDecl(Id("a"),[83],[])],
            (
                [],
                [If( 
                    [
                        (BinaryOp("==", Id("x"), Id("y")),
                        [],
                        [Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1)))]
                        ),
                        (
                            BinaryOp(">", Id("x"), Id("y")),
                            [],
                            [Assign(Id("x"), CallExpr(Id("voo"), [FloatLiteral(1.2)]))]
                        ),
                        (
                            BinaryOp("<", Id("x"), Id("y")),
                            [],
                            [Assign(Id("y"), ArrayCell(Id("b"), [CallExpr(Id("goo"),[Id("x")])]) )]
                        )
                    ],
                    ([],[CallStmt(Id("foo"),[])])
                    )
                ]
            ))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,336)) 

      
    def test_ifStmtInFunc_7(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0O123]
        Body:
        If x == y Then x = x + 1; 
        ElseIf x > y Then Var: a = 1;
        ElseIf x < y Then Var: b = 2;
        Else
            If y > 10 Then y = y / 2;
            EndIf.
        EndIf.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
            [VarDecl(Id("a"),[83],[])],
            (
                [],
                [If( 
                    [
                        (BinaryOp("==", Id("x"), Id("y")),
                        [],
                        [Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1)))]
                        ),
                        (
                            BinaryOp(">", Id("x"), Id("y")),
                            [VarDecl(Id("a"),[], IntLiteral(1))],
                            []
                        ),
                        (
                            BinaryOp("<", Id("x"), Id("y")),
                            [VarDecl(Id("b"),[], IntLiteral(2))],
                            []
                        )
                    ],
                    (
                        [],
                        [
                            If(
                                [
                                    (
                                        BinaryOp(">", Id("y"), IntLiteral(10)),
                                        [],
                                        [Assign(Id("y"), BinaryOp("/", Id("y"), IntLiteral(2)))]
                                    )
                                ],
                                (
                                    [],
                                    []
                                )
                            )
                        ]
                    ))
                ]
            ))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,337)) 

    def test_ifStmtInFunc_8(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0O123]
        Body:
        If x == y Then x = x + 1; 
        ElseIf x > y Then Var: a = 1; x = a * 10.5;
        ElseIf x < y Then Var: b = 2; y = b + foo();
        Else
            If y > 10 Then y = y / 2; Return 1;
            EndIf.
        EndIf.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
            [VarDecl(Id("a"),[83],[])],
            (
                [],
                [If( 
                    [
                        (BinaryOp("==", Id("x"), Id("y")),
                        [],
                        [Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1)))]
                        ),
                        (
                            BinaryOp(">", Id("x"), Id("y")),
                            [VarDecl(Id("a"),[], IntLiteral(1))],
                            [Assign(Id("x"), BinaryOp("*", Id("a"), FloatLiteral(10.5)))]
                        ),
                        (
                            BinaryOp("<", Id("x"), Id("y")),
                            [VarDecl(Id("b"),[], IntLiteral(2))],
                            [Assign(Id("y"), BinaryOp("+", Id("b"), CallExpr(Id("foo"), [])))]
                        )
                    ],
                    (
                        [],
                        [
                            If(
                                [
                                    (
                                        BinaryOp(">", Id("y"), IntLiteral(10)),
                                        [],
                                        [Assign(Id("y"), BinaryOp("/", Id("y"), IntLiteral(2))), Return(IntLiteral(1))]
                                    )
                                ],
                                (
                                    [],
                                    []
                                )
                            )
                        ]
                    ))
                ]
            ))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,338)) 

    def test_ifStmtInFunc_9(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0O123]
        Body:
        If x == y Then x = x + 1; 
        ElseIf x > y Then Var: a = 1; x = a * 10.5;
        ElseIf x < y Then Var: b = 2; y = b + foo();
        Else
            If y > 10 Then y = y / 2; Return 1;
            Else
            Return foo(x[10]);
            EndIf.
        EndIf.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
            [VarDecl(Id("a"),[83],[])],
            (
                [],
                [If( 
                    [
                        (BinaryOp("==", Id("x"), Id("y")),
                        [],
                        [Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1)))]
                        ),
                        (
                            BinaryOp(">", Id("x"), Id("y")),
                            [VarDecl(Id("a"),[], IntLiteral(1))],
                            [Assign(Id("x"), BinaryOp("*", Id("a"), FloatLiteral(10.5)))]
                        ),
                        (
                            BinaryOp("<", Id("x"), Id("y")),
                            [VarDecl(Id("b"),[], IntLiteral(2))],
                            [Assign(Id("y"), BinaryOp("+", Id("b"), CallExpr(Id("foo"), [])))]
                        )
                    ],
                    (
                        [],
                        [
                            If(
                                [
                                    (
                                        BinaryOp(">", Id("y"), IntLiteral(10)),
                                        [],
                                        [Assign(Id("y"), BinaryOp("/", Id("y"), IntLiteral(2))), Return(IntLiteral(1))]
                                    )
                                ],
                                (
                                    [], 
                                    [Return(CallExpr(Id("foo"), [ArrayCell(Id("x"), [IntLiteral(10)])] ))]
                                ) 
                            )
                        ]
                    ))
                ]
            ))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_forFunc_0(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
        For (i = 0, i < 10, i = i + 2) Do
        writeln(i);
        EndFor.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
                [VarDecl(Id("a"),[83],[])],
                (
                    [],

                    [For(
                        Id("i"),
                        IntLiteral(0),
                        BinaryOp("<",Id("i"),IntLiteral(10)),
                        Id("i"),
                        BinaryOp("+",Id("i"), IntLiteral(2)),
                        (
                            [],
                            [
                                CallStmt(Id("writeln"),[Id("i")])
                            ]
                        )
                    )]
                )
            )]))
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_forFunc_1(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
        For (i = 0, i < 10, i = i + 2) Do
        EndFor.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
                [VarDecl(Id("a"),[83],[])],
                (
                    [],

                    [For(
                        Id("i"),
                        IntLiteral(0),
                        BinaryOp("<",Id("i"),IntLiteral(10)),
                        Id("i"),
                        BinaryOp("+",Id("i"), IntLiteral(2)),
                        (
                            [],
                            []
                        ) 
                    )]
                )
            )]))
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_forFunc_2(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
        For (i = 0, i < 10, i = i + 2) Do
        x = x + 10.0;
        EndFor.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
                [VarDecl(Id("a"),[83],[])],
                (
                    [],

                    [For(
                        Id("i"),
                        IntLiteral(0),
                        BinaryOp("<",Id("i"),IntLiteral(10)),
                        Id("i"),
                        BinaryOp("+",Id("i"), IntLiteral(2)),
                        (
                            [],
                            [
                                Assign(Id("x"), BinaryOp("+", Id("x"), FloatLiteral(10.0)))
                            ]
                        ) 
                    )]
                )
            )]))
        self.assertTrue(TestAST.checkASTGen(input,expect,342))
    
    

    def test_forFunc_3(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
        For (i = 0, i < 10, i = i + 2) Do
        Var: a = 10;
        x = foo(i);
        EndFor.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
                [VarDecl(Id("a"),[83],[])],
                (
                    [],

                    [For(
                        Id("i"),
                        IntLiteral(0),
                        BinaryOp("<",Id("i"),IntLiteral(10)),
                        Id("i"),
                        BinaryOp("+",Id("i"), IntLiteral(2)),
                        (
                            [VarDecl(Id("a"),[],IntLiteral(10))],
                            [
                                Assign(Id("x"), CallExpr(Id("foo"), [Id("i")]))
                            ]
                        ) 
                    )]
                )
            )]))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))
    
    def test_forFunc_4(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
        For (i = 0, i < 10, i = i + 2) Do
        x = foo(i);
        EndFor.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
                [VarDecl(Id("a"),[83],[])],
                (
                    [],

                    [For(
                        Id("i"),
                        IntLiteral(0),
                        BinaryOp("<",Id("i"),IntLiteral(10)),
                        Id("i"),
                        BinaryOp("+",Id("i"), IntLiteral(2)),
                        (
                            [],
                            [
                                Assign(Id("x"), CallExpr(Id("foo"), [Id("i")]))
                            ]
                        ) 
                    )]
                )
            )]))
        self.assertTrue(TestAST.checkASTGen(input,expect,344))
    
    def test_forFunc_5(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
        For (i = 0, i < 10, i = i + 2) Do
            Var: y = True;
            x = foo(i);
            x[i] = foo[x+i];
        EndFor.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
                [VarDecl(Id("a"),[83],[])],
                (
                    [],

                    [For(
                        Id("i"),
                        IntLiteral(0),
                        BinaryOp("<",Id("i"),IntLiteral(10)),
                        Id("i"),
                        BinaryOp("+",Id("i"), IntLiteral(2)),
                        (
                            [VarDecl(Id("y"),[], BooleanLiteral(True))],
                            [
                                Assign(Id("x"), CallExpr(Id("foo"), [Id("i")])),
                                Assign(ArrayCell(Id("x"), [Id("i")]), ArrayCell(Id("foo"), [BinaryOp("+",Id("x"),Id("i"))]) )
                            ]
                        ) 
                    )]
                )
            )]))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))


    def test_forFunc_6(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
        For (i = 0, i < 10, i = i + 2) Do
            Var: y = True;
            x = foo(i);
            x[i] = foo[x+i];
            For (j = 5, j >= 0, j = j -1) Do
            EndFor.
        EndFor.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
                [VarDecl(Id("a"),[83],[])],
                (
                    [],

                    [For(
                        Id("i"),
                        IntLiteral(0),
                        BinaryOp("<",Id("i"),IntLiteral(10)),
                        Id("i"),
                        BinaryOp("+",Id("i"), IntLiteral(2)),
                        (
                            [VarDecl(Id("y"),[], BooleanLiteral(True))],
                            [
                                Assign(Id("x"), CallExpr(Id("foo"), [Id("i")])),
                                Assign(ArrayCell(Id("x"), [Id("i")]), ArrayCell(Id("foo"), [BinaryOp("+",Id("x"),Id("i"))])),
                                For(
                                    Id("j"),
                                    IntLiteral(5),
                                    BinaryOp(">=",Id("j"),IntLiteral(0)),
                                    Id("j"),
                                    BinaryOp("-",Id("j"), IntLiteral(1)),
                                    (
                                        [],
                                        []
                                    )
                                )
                            ]
                        ) 
                    )]
                )
            )]))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))
    
    def test_forFunc_7(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
        Var: qq, dd, ee;
        For (i = 0, i < 10, i = i + 2) Do
            Var: y = True;
            x = foo(i);
            x[i] = foo[x+i];
            For (j = 5, j >= 0, j = j -1) Do
            Return 1;
            EndFor.
        EndFor.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
                [VarDecl(Id("a"),[83],[])],
                (
                    [VarDecl(Id("qq"),[], None), VarDecl(Id("dd"),[], None), VarDecl(Id("ee"),[], None)],

                    [For(
                        Id("i"),
                        IntLiteral(0),
                        BinaryOp("<",Id("i"),IntLiteral(10)),
                        Id("i"),
                        BinaryOp("+",Id("i"), IntLiteral(2)),
                        (
                            [VarDecl(Id("y"),[], BooleanLiteral(True))],
                            [
                                Assign(Id("x"), CallExpr(Id("foo"), [Id("i")])),
                                Assign(ArrayCell(Id("x"), [Id("i")]), ArrayCell(Id("foo"), [BinaryOp("+",Id("x"),Id("i"))])),
                                For(
                                    Id("j"),
                                    IntLiteral(5),
                                    BinaryOp(">=",Id("j"),IntLiteral(0)),
                                    Id("j"),
                                    BinaryOp("-",Id("j"), IntLiteral(1)),
                                    (
                                        [],
                                        [Return(IntLiteral(1))]
                                    )
                                )
                            ]
                        ) 
                    )]
                )
            )]))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_forFunc_8(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
        Var: qq, dd, ee;
        For (i = 0, i < 10, i = i + 2) Do
            Var: y = True;
            x = foo(i);
            x[i] = foo[x+i];
            For (j = 5, j >= 0, j = j -1) Do
            Break;
            Return 1;
            EndFor.
        EndFor.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
                [VarDecl(Id("a"),[83],[])],
                (
                    [VarDecl(Id("qq"),[], None), VarDecl(Id("dd"),[], None), VarDecl(Id("ee"),[], None)],

                    [For(
                        Id("i"),
                        IntLiteral(0),
                        BinaryOp("<",Id("i"),IntLiteral(10)),
                        Id("i"),
                        BinaryOp("+",Id("i"), IntLiteral(2)),
                        (
                            [VarDecl(Id("y"),[], BooleanLiteral(True))],
                            [
                                Assign(Id("x"), CallExpr(Id("foo"), [Id("i")])),
                                Assign(ArrayCell(Id("x"), [Id("i")]), ArrayCell(Id("foo"), [BinaryOp("+",Id("x"),Id("i"))])),
                                For(
                                    Id("j"),
                                    IntLiteral(5),
                                    BinaryOp(">=",Id("j"),IntLiteral(0)),
                                    Id("j"),
                                    BinaryOp("-",Id("j"), IntLiteral(1)),
                                    (
                                        [],
                                        [Break(), Return(IntLiteral(1))]
                                    )
                                )
                            ]
                        ) 
                    )]
                )
            )]))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_forFunc_9(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
        Var: qq, dd, ee;
        For (i = 0, i < 10, i = i + 2) Do
            Var: y = True;
            x = foo(i);
            x[i] = foo[x+i];
            For (j = 5, j >= 0, j = j -1) Do
                For (k = 0, k > 1, k = j - k) Do
                EndFor.
                Break;
                Return 1;
            EndFor.
        EndFor.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
                [VarDecl(Id("a"),[83],[])],
                (
                    [VarDecl(Id("qq"),[], None), VarDecl(Id("dd"),[], None), VarDecl(Id("ee"),[], None)],

                    [For(
                        Id("i"),
                        IntLiteral(0),
                        BinaryOp("<",Id("i"),IntLiteral(10)),
                        Id("i"),
                        BinaryOp("+",Id("i"), IntLiteral(2)),
                        (
                            [VarDecl(Id("y"),[], BooleanLiteral(True))],
                            [
                                Assign(Id("x"), CallExpr(Id("foo"), [Id("i")])),
                                Assign(ArrayCell(Id("x"), [Id("i")]), ArrayCell(Id("foo"), [BinaryOp("+",Id("x"),Id("i"))])),
                                For(
                                    Id("j"),
                                    IntLiteral(5),
                                    BinaryOp(">=",Id("j"),IntLiteral(0)),
                                    Id("j"),
                                    BinaryOp("-",Id("j"), IntLiteral(1)),
                                    (
                                        [],
                                        [
                                            For(
                                                Id("k"),
                                                IntLiteral(0),
                                                BinaryOp(">",Id("k"),IntLiteral(1)),
                                                Id("k"),
                                                BinaryOp("-",Id("j"), Id("k")),
                                                (
                                                    [], []
                                                )),
                                            Break(), 
                                            Return(IntLiteral(1))
                                        ]
                                    )
                                )
                            ]
                        ) 
                    )]
                )
            )]))
        self.assertTrue(TestAST.checkASTGen(input,expect,349))


    
    def test_whileFunc_0(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            While x == True Do 
            EndWhile.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
                [VarDecl(Id("a"),[83],[])],
                (
                        [],
                        [
                            While(BinaryOp("==",Id("x"), BooleanLiteral(True)), ([],[]))
                        ]
                ))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_whileFunc_1(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            While x == True Do 
                While y == 1 Do
                EndWhile.
            EndWhile.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
                [VarDecl(Id("a"),[83],[])],
                (
                        [],
                        [
                            While(BinaryOp("==",Id("x"), BooleanLiteral(True)), 
                            (
                                [],
                                [
                                    While(BinaryOp("==",Id("y"), IntLiteral(1)), ([],[]))
                                ]
                           ))
                        ]
                ))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,351))
    
    def test_whileFunc_2(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            While x == True Do 
                While y == 1 Do
                    dd = nn;
                EndWhile.
            EndWhile.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
                [VarDecl(Id("a"),[83],[])],
                (
                        [],
                        [
                            While(BinaryOp("==",Id("x"), BooleanLiteral(True)), 
                            (
                                [],
                                [
                                    While(BinaryOp("==",Id("y"), IntLiteral(1)), ([],[Assign(Id("dd"), Id("nn"))]))
                                ]
                           ))
                        ]
                ))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_whileFunc_3(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            While (x < 10.5) Do 
                While y == 1 Do
                    dd = nn;
                EndWhile.
            EndWhile.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
                [VarDecl(Id("a"),[83],[])],
                (
                        [],
                        [
                            While(BinaryOp("<",Id("x"), FloatLiteral(10.5)), 
                            (
                                [],
                                [
                                    While(BinaryOp("==",Id("y"), IntLiteral(1)), ([],[Assign(Id("dd"), Id("nn"))]))
                                ]
                           ))
                        ]
                ))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353)) 
  

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
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
                [VarDecl(Id("a"),[83],[])],
                (
                        [],
                        [
                            While(BinaryOp("<",Id("x"), FloatLiteral(10.5)), 
                            (
                                [],
                                [
                                    Assign(Id("x"), BinaryOp("+",Id("x"),IntLiteral(1))),
                                    While(BinaryOp("==",Id("y"), IntLiteral(1)), 
                                    (
                                        [],
                                        [Assign(Id("dd"), Id("nn")),
                                        Assign(ArrayCell(Id("y"), [Id("i")]), ArrayCell(Id("x"),[BinaryOp("+",Id("y"), Id("i"))]))
                                        ]
                                    ))
                                ]
                           ))
                        ]
                ))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354)) 

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
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
                [VarDecl(Id("a"),[83],[])],
                (
                        [],
                        [
                            While(BinaryOp("<",Id("x"), FloatLiteral(10.5)), 
                            (
                                [],
                                [
                                    Assign(Id("x"), BinaryOp("+",Id("x"),IntLiteral(1))),
                                    While(BinaryOp("==",Id("y"), IntLiteral(1)), 
                                    (
                                        [],
                                        [Assign(Id("dd"), Id("nn")),
                                        Assign(ArrayCell(Id("y"), [Id("i")]), ArrayCell(Id("x"),[BinaryOp("+",Id("y"), Id("i"))])),
                                        Assign(ArrayCell(Id("a"), [IntLiteral(221)]), FloatLiteral(10.9))
                                        ]
                                    ))
                                ]
                           ))
                        ]
                ))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,355)) 

    def test_whileFunc_6(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            While (x < 10.5) Do 
                x = x + 1;
                Continue;
                While y == 1 Do
                    dd = nn;
                    y[i] = x[y + i];
                    a[0xDD] = 10.9;
                    Return x + y;
                EndWhile.
            EndWhile.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
                [VarDecl(Id("a"),[83],[])],
                (
                        [],
                        [
                            While(BinaryOp("<",Id("x"), FloatLiteral(10.5)), 
                            (
                                [],
                                [
                                    Assign(Id("x"), BinaryOp("+",Id("x"),IntLiteral(1))),
                                    Continue(),
                                    While(BinaryOp("==",Id("y"), IntLiteral(1)), 
                                    (
                                        [],
                                        [Assign(Id("dd"), Id("nn")),
                                        Assign(ArrayCell(Id("y"), [Id("i")]), ArrayCell(Id("x"),[BinaryOp("+",Id("y"), Id("i"))])),
                                        Assign(ArrayCell(Id("a"), [IntLiteral(221)]), FloatLiteral(10.9)),
                                        Return(BinaryOp("+", Id("x"), Id("y")))
                                        ]
                                    ))
                                ]
                           ))
                        ]
                ))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,356)) 

    def test_whileFunc_7(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            While (x < 10.5) Do 
                x = x + 1;
                Continue;
                While y == 1 Do
                    dd = nn;
                    y[i] = x[y + i];
                    a[0xDD] = 10.9;
                    Return x + y;
                EndWhile.
                Return 10;
            EndWhile.
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
                [VarDecl(Id("a"),[83],[])],
                (
                        [],
                        [
                            While(BinaryOp("<",Id("x"), FloatLiteral(10.5)), 
                            (
                                [],
                                [
                                    Assign(Id("x"), BinaryOp("+",Id("x"),IntLiteral(1))),
                                    Continue(),
                                    While(BinaryOp("==",Id("y"), IntLiteral(1)), 
                                    (
                                        [],
                                        [Assign(Id("dd"), Id("nn")),
                                        Assign(ArrayCell(Id("y"), [Id("i")]), ArrayCell(Id("x"),[BinaryOp("+",Id("y"), Id("i"))])),
                                        Assign(ArrayCell(Id("a"), [IntLiteral(221)]), FloatLiteral(10.9)),
                                        Return(BinaryOp("+", Id("x"), Id("y")))
                                        ]
                                    )),
                                    Return(IntLiteral(10))
                                ]
                           ))
                        ]
                ))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,357)) 

    def test_whileFunc_8(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            While (x < 10.5) Do 
                x = x + 1;
                Continue;
                While y == 1 Do
                    dd = nn;
                    y[i] = x[y + i];
                    a[0xDD] = 10.9;
                    Return x + y;
                EndWhile.
                Return 10;
            EndWhile.
            Return dd;
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
                [VarDecl(Id("a"),[83],[])],
                (
                        [],
                        [
                            While(BinaryOp("<",Id("x"), FloatLiteral(10.5)), 
                            (
                                [],
                                [
                                    Assign(Id("x"), BinaryOp("+",Id("x"),IntLiteral(1))),
                                    Continue(),
                                    While(BinaryOp("==",Id("y"), IntLiteral(1)), 
                                    (
                                        [],
                                        [Assign(Id("dd"), Id("nn")),
                                        Assign(ArrayCell(Id("y"), [Id("i")]), ArrayCell(Id("x"),[BinaryOp("+",Id("y"), Id("i"))])),
                                        Assign(ArrayCell(Id("a"), [IntLiteral(221)]), FloatLiteral(10.9)),
                                        Return(BinaryOp("+", Id("x"), Id("y")))
                                        ]
                                    )),
                                    Return(IntLiteral(10))
                                ]
                           )), Return (Id("dd"))
                        ]
                ))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,358)) 

    def test_whileFunc_9(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            While (x < 10.5) Do 
                Var: mm = 10;
                x = x + 1;
                Continue;
                While y == 1 Do
                    Var: nn, qq;
                    dd = nn;
                    y[i] = x[y + i];
                    a[0xDD] = 10.9;
                    Return x + y;
                EndWhile.
                Return 10;
            EndWhile.
            Return dd;
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
                [VarDecl(Id("a"),[83],[])],
                (
                        [],
                        [
                            While(BinaryOp("<",Id("x"), FloatLiteral(10.5)), 
                            (
                                [VarDecl(Id("mm"),[], IntLiteral(10))],
                                [
                                    Assign(Id("x"), BinaryOp("+",Id("x"),IntLiteral(1))),
                                    Continue(),
                                    While(BinaryOp("==",Id("y"), IntLiteral(1)), 
                                    (
                                        [VarDecl(Id("nn"),[], None), VarDecl(Id("qq"),[], None)],
                                        
                                        [Assign(Id("dd"), Id("nn")),
                                        Assign(ArrayCell(Id("y"), [Id("i")]), ArrayCell(Id("x"),[BinaryOp("+",Id("y"), Id("i"))])),
                                        Assign(ArrayCell(Id("a"), [IntLiteral(221)]), FloatLiteral(10.9)),
                                        Return(BinaryOp("+", Id("x"), Id("y")))
                                        ]
                                    )),
                                    Return(IntLiteral(10))
                                ]
                           )), Return (Id("dd"))
                        ]
                ))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))     
    
    
    def test_DoWhileFunc_0(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            Do While 1;
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
                [VarDecl(Id("a"),[83],[])],
                (
                        [],
                        [
                            Dowhile(([],[]), IntLiteral(1))
                        ]
                )
            )
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_DoWhileFunc_2(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            Do While (x <= 1);
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
                [VarDecl(Id("a"),[83],[])],
                (
                        [],
                        [
                            Dowhile(([],[]), BinaryOp("<=", Id("x"), IntLiteral(1)))
                        ]
                ))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_DoWhileFunc_3(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            Do While (x <= 1 || x != 10);
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
                [VarDecl(Id("a"),[83],None)],
                (
                        [],
                        [
                            Dowhile(([],[]),BinaryOp("!=", BinaryOp("<=", Id("x"), BinaryOp("||",IntLiteral(1), Id("x"))), IntLiteral(10)))
                        ]
                        
                ))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_DoWhileFunc_4(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            Do 
                x = a[x + 1];
            While (x <= 1 || x != 10);
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
                [VarDecl(Id("a"),[83],None)],
                (
                        [],
                        [
                            
                            Dowhile(
                                (
                                    [],
                                    [Assign(Id("x"), ArrayCell(Id("a"), [BinaryOp("+", Id("x"), IntLiteral(1))]))]
                                ),
                                BinaryOp("!=", BinaryOp("<=", Id("x"), BinaryOp("||",IntLiteral(1), Id("x"))), IntLiteral(10)))
                        ]
                        
                ))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_DoWhileFunc_4(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            Do 
                x = a[x + 1];
                foo(); 
            While (x <= 1 || x != 10);
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
                [VarDecl(Id("a"),[83],None)],
                (
                        [],
                        [
                            
                            Dowhile(
                                (
                                    [],
                                    [Assign(Id("x"), ArrayCell(Id("a"), [BinaryOp("+", Id("x"), IntLiteral(1))])),
                                    CallStmt(Id("foo"), [])
                                    ]
                                ),
                                BinaryOp("!=", BinaryOp("<=", Id("x"), BinaryOp("||",IntLiteral(1), Id("x"))), IntLiteral(10)))
                        ]
                        
                ))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_DoWhileFunc_5(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            aa = letgo(dd);
            Do 
                x = a[x + 1];
                foo(); 
            While (x <= 1 || x != 10);
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
                [VarDecl(Id("a"),[83],None)],
                (
                        [],
                        [
                            Assign(Id("aa"), CallExpr(Id("letgo"), [Id("dd")])),
                            Dowhile(
                                (
                                    [],
                                    [Assign(Id("x"), ArrayCell(Id("a"), [BinaryOp("+", Id("x"), IntLiteral(1))])),
                                    CallStmt(Id("foo"), [])
                                    ]
                                ),
                                BinaryOp("!=", BinaryOp("<=", Id("x"), BinaryOp("||",IntLiteral(1), Id("x"))), IntLiteral(10)))
                        ]
                        
                ))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test_all_366(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            y = x-(!(!True));
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
                [VarDecl(Id("a"),[83],None)],
                (
                        [],
                        [
                            Assign(
                                Id('y'),
                                BinaryOp(
                                    '-',
                                    Id('x'),
                                    UnaryOp('!', UnaryOp('!', BooleanLiteral(True)))
                                )
                            )
                        ]
                ))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_all_367(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            y = x-(!(!True));
            Return;
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
                [VarDecl(Id("a"),[83],None)],
                (
                        [],
                        [
                            Assign(
                                Id('y'),
                                BinaryOp(
                                    '-',
                                    Id('x'),
                                    UnaryOp('!', UnaryOp('!', BooleanLiteral(True)))
                                )
                            ),
                            Return(None)
                        ]
                ))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,367))
    
    def test_all_368(self):
        input = """Var: x = 5;
        Function: main
        Parameter: a[0o123]
        Body:
            y = x-(!(!True));
            Return;
        EndBody.
        Function: count
        Parameter: a[0o123]
        Body:
            y = x-(!(!True));
            Return;
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),
                [VarDecl(Id("a"),[83],None)],
                (
                        [],
                        [
                            Assign(
                                Id('y'),
                                BinaryOp(
                                    '-',
                                    Id('x'),
                                    UnaryOp('!', UnaryOp('!', BooleanLiteral(True)))
                                )
                            ),
                            Return(None)
                        ]
                )),
                FuncDecl(Id("count"),
                [VarDecl(Id("a"),[83],None)],
                (
                        [],
                        [
                            Assign(
                                Id('y'),
                                BinaryOp(
                                    '-',
                                    Id('x'),
                                    UnaryOp('!', UnaryOp('!', BooleanLiteral(True)))
                                )
                            ),
                            Return(None)
                        ]
                ))
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_all_369(self):
        input = """
        Var: i[123][1][2]=0;
        Function: main
        Parameter: a, b
        Body:
        Var: r = 10., v;
        If 5 + 2 == 3 Then 
            Var:a;
            a = x +3;
        ElseIf 5+2 == 3 Then 
            Var:a;
            a = x +3;
        ElseIf 5+2 == 3 Then 
            Var:a;
            a = x +3;
        Else
            Var:a;
            a = x +3;
        EndIf.
        EndBody.
        """
        expect = str(Program([
        VarDecl(Id("i"), [123,1,2], IntLiteral(0)),
        FuncDecl(Id("main"), 
                [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None)],
                (
                    [VarDecl(Id("r"), [], FloatLiteral(10.0)), VarDecl(Id('v'), [], None)], 
                    [
                        If
                        ([
                            (
                            BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),
                            [VarDecl(Id('a'), [], None)],
                            [Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))]
                            ),
                            (
                            BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),
                            [VarDecl(Id('a'), [], None)],
                            [Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))]
                            ),
                            (
                            BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),
                            [VarDecl(Id('a'), [], None)],
                            [Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))]
                            )
                        ],
                            (
                                [VarDecl(Id('a'), [], None)],
                                [Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))]
                            )
                        )
                    ]
                ))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_all_370(self):
        input = """
        Var: i[123][1][2]=0;
        Function: main
        Parameter: a, b
        Body:
        Var: r = 10., v;
        If 5 + 2 == 3 Then 
            Var:a;
            a = x +3;
        ElseIf 5+2 == 3 Then 
            Var:a;
            a = x +3;
        EndIf.
        EndBody.
        """
        expect = str(Program([
        VarDecl(Id("i"), [123,1,2], IntLiteral(0)),
        FuncDecl(Id("main"), 
                [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None)],
                (
                    [VarDecl(Id("r"), [], FloatLiteral(10.0)), VarDecl(Id('v'), [], None)], 
                    [
                        If
                        ([
                            (
                            BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),
                            [VarDecl(Id('a'), [], None)],
                            [Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))]
                            ),
                            (
                            BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),
                            [VarDecl(Id('a'), [], None)],
                            [Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))]
                            )
                        ],
                        ([],[])
                        )
                    ]
                ))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_simple_program_71(self):
        input = """
            Var: i[123][1][2]=0;
            Function: main
            Parameter: a, b
            Body:
            Var: r = 10., v;
            If 5 + 2 == 3 Then 
                Var:a;
                Var:b;
                a = x +3;
                a = x +3;
            ElseIf 5+2 == 3 Then 
                Var:a;
                Var:b;
                a = x +3;
                a = x +3;
            ElseIf 5+2 == 3 Then 
                Var:a;
                Var:b;
                a = x +3;
                a = x +3;
            Else
                Var:a;
                Var:b;
                a = x +3;
                a = x +3;
            EndIf.
            EndBody.
            """
        expect = str(Program([
        VarDecl(Id("i"), [123,1,2], IntLiteral(0)),
        FuncDecl(Id("main"), 
                [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None)],
                (
                    [VarDecl(Id("r"), [], FloatLiteral(10.0)), VarDecl(Id('v'), [], None)], 
                    [
                        If
                        ([
                            (
                            BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),
                            [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None)],
                            [Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3))),
                            Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))]
                            ),
                            (
                            BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),
                            [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None)],
                            [Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3))),
                            Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))]
                            ),
                            (
                            BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),
                            [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None)],
                            [Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3))),
                            Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))]
                            )
                        ],
                            (
                                [VarDecl(Id('a'), [], None), VarDecl(Id('b'), [], None)],
                                [Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3))),
                                Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))]
                            )
                        )
                    ]
                ))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,371))
    
    def test_all_372(self):
        input = """Var: x = 5;
        Function: main
        Body:
            x = 10;
            printLn(x);
            Continue;
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),[],([],[
                Assign(Id("x"),IntLiteral(10)),
                CallStmt(Id("printLn"),[Id("x")]),
                Continue()
                ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,372))
    
    def test_all_373(self):
        input = """Var: x = 5;
        Function: main
        Body:
            x = 10;
            printLn(x);
            Continue;
            Break;
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),[],([],[
                Assign(Id("x"),IntLiteral(10)),
                CallStmt(Id("printLn"),[Id("x")]),
                Continue(),
                Break()
                ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_all_374(self):
        input = """Var: x = 5;
        Function: main
        Body:
            x = 10;
            printLn(x);
            Continue;
            Break;
            Return;
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),[],([],[
                Assign(Id("x"),IntLiteral(10)),
                CallStmt(Id("printLn"),[Id("x")]),
                Continue(),
                Break(),
                Return(None)
                ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,374))
    
    def test_all_375(self):
        input = """Var: x = 5;
        Function: main
        Body:
            x = 10;
            printLn(x);
            Continue;
            Break;
            Return;
            foo();
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),[],([],[
                Assign(Id("x"),IntLiteral(10)),
                CallStmt(Id("printLn"),[Id("x")]),
                Continue(),
                Break(),
                Return(None),
                CallStmt(Id("foo"), [])
                ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    def test_all_376(self):
        input = """Var: x = 5;
        Function: main
        Body:
            x = 10;
            printLn(x);
            Continue;
            Break;
            Return;
            foo();
            Return foo(10);
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),[],([],[
                Assign(Id("x"),IntLiteral(10)),
                CallStmt(Id("printLn"),[Id("x")]),
                Continue(),
                Break(),
                Return(None),
                CallStmt(Id("foo"), []),
                Return(CallExpr(Id("foo"), [IntLiteral(10)]))
                ]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_all_377(self):
        input = """Var: x = 5;
        Function: main
        Body:
            x = 10;
            printLn(x);
            Continue;
            Break;
            Return;
            foo();
            Return foo(10);            
        EndBody.
        Function: cont
            Body:
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),[],([],[
                Assign(Id("x"),IntLiteral(10)),
                CallStmt(Id("printLn"),[Id("x")]),
                Continue(),
                Break(),
                Return(None),
                CallStmt(Id("foo"), []),
                Return(CallExpr(Id("foo"), [IntLiteral(10)]))
                ])),
            FuncDecl(Id("cont"),[],([], []))
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test_all_378(self):
        input = """Var: x = 5;
        Function: main
        Body:
            Var: x = 5;
            x = 10;
            printLn(x);
            Continue;
            Break;
            Return;
            foo();
            Return foo(10);            
        EndBody.
        Function: cont
        Body:
            Var: x = 5;
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),[],([VarDecl(Id("x"),[],IntLiteral(5))],[
                Assign(Id("x"),IntLiteral(10)),
                CallStmt(Id("printLn"),[Id("x")]),
                Continue(),
                Break(),
                Return(None),
                CallStmt(Id("foo"), []),
                Return(CallExpr(Id("foo"), [IntLiteral(10)]))
                ])),
            FuncDecl(Id("cont"),[],([VarDecl(Id("x"),[],IntLiteral(5))], []))
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,378))
    
    def test_all_379(self):
        input = """Var: x = 5;
        Function: main
        Body:
            Var: aa[0xDD];
            x = 10;
            printLn(x);
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),[],([VarDecl(Id("aa"),[221],None)],[
                Assign(Id("x"),IntLiteral(10)),
                CallStmt(Id("printLn"),[Id("x")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_all_380(self):
        input = """Var: x = 5;
        Function: main
        Body:
            Var: aa[0xDD] = 0xAA;
            x = 10;
            printLn(x);
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),[],([VarDecl(Id("aa"),[221],IntLiteral(170))],[
                Assign(Id("x"),IntLiteral(10)),
                CallStmt(Id("printLn"),[Id("x")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_all_381(self):
        input = """Var: x = 5;
        Function: main
        Body:
            Var: aa[0XDD];
            x = 10;
            printLn(x);
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),[],([VarDecl(Id("aa"),[221],None)],[
                Assign(Id("x"),IntLiteral(10)),
                CallStmt(Id("printLn"),[Id("x")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test_all_382(self):
        input = """Var: x = 5;
        Function: main
        Body:
            Var: aa[0XDD] = 0xAA;
            x = 10;
            printLn(x);
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),[],([VarDecl(Id("aa"),[221],IntLiteral(170))],[
                Assign(Id("x"),IntLiteral(10)),
                CallStmt(Id("printLn"),[Id("x")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_all_383(self):
        input = """Var: x = 5;
        Function: main
        Body:
            Var: aa[0o77];
            x = 10;
            printLn(x);
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),[],([VarDecl(Id("aa"),[63],None)],[
                Assign(Id("x"),IntLiteral(10)),
                CallStmt(Id("printLn"),[Id("x")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def test_all_384(self):
        input = """Var: x = 5;
        Function: main
        Body:
            Var: aa[0o77] = 0O11;
            x = 10;
            printLn(x);
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),[],([VarDecl(Id("aa"),[63],IntLiteral(9))],[
                Assign(Id("x"),IntLiteral(10)),
                CallStmt(Id("printLn"),[Id("x")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_all_385(self):
        input = """Var: x = 1.;        
        """
        expect = str(Program([
            VarDecl(Id("x"),[],FloatLiteral(1.))
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test_all_386(self):
        input = """Var: x = 1.0;        
        """
        expect = str(Program([
            VarDecl(Id("x"),[],FloatLiteral(1.0))
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_all_387(self):
        input = """Var: x = 1.0e10;        
        """
        expect = str(Program([
            VarDecl(Id("x"),[],FloatLiteral(1.0e10))
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_all_388(self):
        input = """Var: x = 1.0e-10;        
        """
        expect = str(Program([
            VarDecl(Id("x"),[],FloatLiteral(1.0e-10))
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,388))
    
    def test_all_389(self):
        input = """Var: x = 1e-10;        
        """
        expect = str(Program([
            VarDecl(Id("x"),[],FloatLiteral(1e-10))
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,389))
   

    def test_all_390(self):
        input = """Var: x = "This is a string containing tab \t";        
        """
        expect = str(Program([
            VarDecl(Id("x"),[],StringLiteral("""This is a string containing tab \t"""))
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,390))

    def test_all_391(self):
        input = r"""
Var: i[123][1][2]=0;
Function: main
Parameter: a, b
Body:
Var: r = 10., v;
For (i = 0, i < 10, i = i + 10.23) Do
    Var:a;
    If 5 + 2 == 3 Then 
    EndIf.
    a = x +3;
EndFor.
EndBody.
"""
        expect = str(Program([
        VarDecl(Id("i"), [123,1,2], IntLiteral(0)),
        FuncDecl(Id("main"), 
                [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None)],
                (
                    [VarDecl(Id("r"), [], FloatLiteral(10.0)), VarDecl(Id('v'), [], None)], 
                    [
                        For(
                            Id('i'),
                            IntLiteral(0),
                            BinaryOp('<',Id('i'), IntLiteral(10)),
                            Id('i'),
                            BinaryOp('+',Id('i'), FloatLiteral(10.23)),
                            (
                                [VarDecl(Id('a'), [], None)],
                                [
                                    If
                                    ([
                                        (
                                        BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),
                                        [],
                                        []
                                        )
                                    ],
                                        (
                                            [],
                                            []
                                        )
                                    ),
                                    Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))
                                ]
                            )

                        )

                    ]
                ))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_all_392(self):
        input = r"""
Var: i[123][1][2]=0;
Function: main
Parameter: a, b
Body:
Var: r = 10., v;
For (i = 0, i < 10, i = i + 10.23) Do
    Var:a;
    If 5 + 2 == 3 Then 
        For (i = 0, i < 10, i = i + 10.23) Do
        Var:a;
        If 5 + 2 == 3 Then 
        EndIf.
        a = x +3;
        EndFor.
    EndIf.
    a = x +3;
EndFor.
EndBody.
"""
        expect = str(Program([
        VarDecl(Id("i"), [123,1,2], IntLiteral(0)),
        FuncDecl(Id("main"), 
                [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None)],
                (
                    [VarDecl(Id("r"), [], FloatLiteral(10.0)), VarDecl(Id('v'), [], None)], 
                    [
                        For(
                            Id('i'),
                            IntLiteral(0),
                            BinaryOp('<',Id('i'), IntLiteral(10)),
                            Id('i'),
                            BinaryOp('+',Id('i'), FloatLiteral(10.23)),
                            (
                                [VarDecl(Id('a'), [], None)],
                                [
                                    If
                                    ([
                                        (
                                        BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),
                                        [],
                                        [
                                            For(
                                                Id('i'),
                                                IntLiteral(0),
                                                BinaryOp('<',Id('i'), IntLiteral(10)),
                                                Id('i'),
                                                BinaryOp('+',Id('i'), FloatLiteral(10.23)),
                                                (
                                                    [VarDecl(Id('a'), [], None)],
                                                    [
                                                        If
                                                        ([
                                                            (
                                                            BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),
                                                            [

                                                            ],
                                                            []
                                                            )
                                                        ],
                                                            (
                                                                [],
                                                                []
                                                            )
                                                        ),
                                                        Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))
                                                    ]
                                                )
                                            )
                                        ]
                                        )
                                    ],
                                        (
                                            [],
                                            []
                                        )
                                    ),
                                    Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3)))
                                ]
                            )
                        )

                    ]
                ))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_all_393(self):
        input = r"""
Var: i[123][1][2]=0;
Function: main
Parameter: a, b
Body:
Var: r = 10., v;
While 5 + 2 == 3 Do 
    Var:a, x = 3;
    a = x +3;
    x = x +3;
    While 5 + 2 == 3 Do 
        Var:a, x = 3;
        a = x +3;
        x = x +3;
    EndWhile.
EndWhile.
EndBody.
"""
        expect = str(Program([
        VarDecl(Id("i"), [123,1,2], IntLiteral(0)),
        FuncDecl(Id("main"), 
                [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None)],
                (
                    [VarDecl(Id("r"), [], FloatLiteral(10.0)), VarDecl(Id('v'), [], None)], 
                    [
                        While(
                            BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),
                            (
                                [VarDecl(Id('a'), [], None),VarDecl(Id('x'), [], IntLiteral(3))],
                                [
                                    Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3))),
                                    Assign(Id('x'),BinaryOp('+',Id('x'),IntLiteral(3))),
                                    While(
                                        BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),
                                        (
                                            [VarDecl(Id('a'), [], None),VarDecl(Id('x'), [], IntLiteral(3))],
                                            [
                                                Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3))),
                                                Assign(Id('x'),BinaryOp('+',Id('x'),IntLiteral(3)))
                                            ]
                                        )
                                    )
                                ]
                            )
                        )
                    ]
                ))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_all_394(self):
        input = r"""
Var: i[123][1][2]=0;
Function: main
Parameter: a, b
Body:
Var: r = 10., v;
Do
    Var:a, x = 3;
    a = x +3;
    x = x +3;
    Do
        Var:a, x = 3;
        a = x +3;
        x = x +3;
    While 5 + 2 == 3;
While 5 + 2 == 3;
EndBody.
"""
        expect = str(Program([
        VarDecl(Id("i"), [123,1,2], IntLiteral(0)),
        FuncDecl(Id("main"), 
                [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None)],
                (
                    [VarDecl(Id("r"), [], FloatLiteral(10.0)), VarDecl(Id('v'), [], None)], 
                    [
                        Dowhile(
                            (
                                [VarDecl(Id('a'), [], None),VarDecl(Id('x'), [], IntLiteral(3))],
                                [
                                    Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3))),
                                    Assign(Id('x'),BinaryOp('+',Id('x'),IntLiteral(3))),
                                    Dowhile(
                                        (
                                            [VarDecl(Id('a'), [], None),VarDecl(Id('x'), [], IntLiteral(3))],
                                            [
                                                Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3))),
                                                Assign(Id('x'),BinaryOp('+',Id('x'),IntLiteral(3))),
                                            ]
                                        ),
                                        BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3))
                                    )
                                ]
                            ),
                            BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3))
                        )
                    ]
                ))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_all_395(self):
        input = r"""
Var: i[123][1][2]=0;
Function: main
Parameter: a, b
Body:
Var: r = 10., v;
Do
    Var:a, x = 3;
    Break;
    a = x +3;
    x = x +3;
    Do
        Var:a, x = 3;
        a = x +3;
        x = x +3;
        Break;
    While 5 + 2 == 3;
While 5 + 2 == 3;
EndBody.
"""
        expect = str(Program([
        VarDecl(Id("i"), [123,1,2], IntLiteral(0)),
        FuncDecl(Id("main"), 
                [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None)],
                (
                    [VarDecl(Id("r"), [], FloatLiteral(10.0)), VarDecl(Id('v'), [], None)], 
                    [
                        Dowhile(
                            (
                                [VarDecl(Id('a'), [], None),VarDecl(Id('x'), [], IntLiteral(3))],
                                [
                                    Break(),
                                    Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3))),
                                    Assign(Id('x'),BinaryOp('+',Id('x'),IntLiteral(3))),
                                    Dowhile(
                                        (
                                            [VarDecl(Id('a'), [], None),VarDecl(Id('x'), [], IntLiteral(3))],
                                            [
                                                Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3))),
                                                Assign(Id('x'),BinaryOp('+',Id('x'),IntLiteral(3))),
                                                Break()
                                            ]
                                        ),
                                        BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3))
                                    )
                                ]
                            ),
                            BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3))
                        )
                    ]
                ))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_all_396(self):
        input = r"""Var: x = "It\'s me";        
        """
        expect = str(Program([
            VarDecl(Id("x"),[],StringLiteral(r"""It\'s me"""))
            ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_all_397(self):
        input = r"""
Var: i[123][1][2]=0;
Function: main
Parameter: a, b
Body:
Var: r = 10., v;
a[3 + foo(2)] = -a[b[2][3]] + 4;
EndBody.
"""
        expect = str(Program([
        VarDecl(Id("i"), [123,1,2], IntLiteral(0)),
        FuncDecl(Id("main"), 
                [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None)],
                (
                    [VarDecl(Id("r"), [], FloatLiteral(10.0)), VarDecl(Id('v'), [], None)], 
                    [
                        Assign(
                                ArrayCell(
                                    Id('a'),
                                    [BinaryOp(
                                        '+',
                                        IntLiteral(3), 
                                        CallExpr(Id('foo'), [IntLiteral(2)])
                                    )]
                                ), 
                                BinaryOp(
                                    '+',
                                    UnaryOp('-',
                                        ArrayCell(
                                            Id('a'),
                                            [
                                                ArrayCell(
                                                    Id('b'),
                                                    [
                                                        IntLiteral(2),
                                                        IntLiteral(3)
                                                    ]
                                                ), 
                                            ]
                                        )
                                    ), 
                                    IntLiteral(4)
                                )
                              )
                    ]
                ))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_all_398(self):
        input = r"""
Var: i[123][1][2]=0;
Function: main
Parameter: a, b
Body:
Var: r = 10., v;
a[3 + foo(2)] = -.(a[b[2][3]] =/= 4);
EndBody.
"""
        expect = str(Program([
        VarDecl(Id("i"), [123,1,2], IntLiteral(0)),
        FuncDecl(Id("main"), 
                [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None)],
                (
                    [VarDecl(Id("r"), [], FloatLiteral(10.0)), VarDecl(Id('v'), [], None)], 
                    [
                        Assign(
                                ArrayCell(
                                    Id('a'),
                                    [BinaryOp(
                                        '+',
                                        IntLiteral(3), 
                                        CallExpr(Id('foo'), [IntLiteral(2)])
                                    )]
                                ), 
                                UnaryOp('-.',
                                    BinaryOp(
                                        '=/=',
                                            ArrayCell(
                                                Id('a'),
                                                [
                                                    ArrayCell(
                                                        Id('b'),
                                                        [
                                                            IntLiteral(2),
                                                            IntLiteral(3)
                                                        ]
                                                    ), 
                                                ]
                                        ), 
                                        IntLiteral(4)
                                    )
                                )
                          )
                    ]
                ))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_all_399(self):
        input = r"""
Var: i[123][1][2]=0;
Function: main
Parameter: a, b
Body:
Var: r = 10., v;
If (5 + 2 == 3) Then 
Else
    Var:a;
    a = x +3;
    Return;
EndIf.
Return;
EndBody.
"""
        expect = str(Program([
        VarDecl(Id("i"), [123,1,2], IntLiteral(0)),
        FuncDecl(Id("main"), 
                [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None)],
                (
                    [VarDecl(Id("r"), [], FloatLiteral(10.0)), VarDecl(Id('v'), [], None)], 
                    [
                        If
                        ([
                            (
                            BinaryOp('==',BinaryOp('+',IntLiteral(5),IntLiteral(2)),IntLiteral(3)),
                            [],
                            []
                            )
                        ],
                            (
                                [VarDecl(Id('a'), [], None)],
                                [
                                    Assign(Id('a'),BinaryOp('+',Id('x'),IntLiteral(3))),
                                    Return(None)
                                ]
                            )
                        ),
                        Return(None)
                    ]
                ))
        ]))
        self.assertTrue(TestAST.checkASTGen(input,expect,399))

    def test_funcDeclar_all(self):
        input = """Var: x = 5;
        Function: main
        Body:
            x = 10;
            printLn(x);
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),[],([],[
                Assign(Id("x"),IntLiteral(10)),
                CallStmt(Id("printLn"),[Id("x")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))
    

    
       