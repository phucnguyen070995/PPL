import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):

    def test_400(self):
        """Simple program: main"""
        input = """Function: main
                   Body: 
                        foo();
                   EndBody."""
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_401(self):
        """Complex program"""
        input = """Function: main  
                   Body:
                        printStrLn();
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_402(self):
        """More complex program"""
        input = """Function: main 
                    Body:
                        printStrLn(read(4));
                    EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_403(self):
        """Simple program: main """
        input = Program([FuncDecl(Id("main"),[],([],[
            CallExpr(Id("foo"),[])]))])
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_404(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[
                        CallExpr(Id("read"),[IntLiteral(4)])
                        ])]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_405(self):
        """Complex program"""
        input = Program([
                FuncDecl(Id("main"),[],([],[
                    CallStmt(Id("printStrLn"),[])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_406(self):
        """Simple program: main"""
        input = """
                    Var: x, y, z;
                    Function: main
                    Parameter: a,b,c
                    Body:
                        Var: i, j, k;
                        x = 1;
                        If (j == 2) Then
                            Var: f;
                            f = x;
                        Else
                            Var: n;
                            f = 3;
                        EndIf.
                        
                    EndBody.
                """
        expect = str(Undeclared(Identifier(),"f"))
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_407(self):
        """Simple program: main"""
        input = """
                    Var: x, y, z;
                    Function: main
                    Parameter: a,b,c
                    Body:
                        Var: i, j, k;
                        x = 1;
                        y = 2;
                        If (j == 2) Then
                            Var: f;
                            f = x;
                        Else
                            z = 3.0;
                        EndIf.
                    EndBody.
                    Function: foo
                    Body:
                        y = 5.0;
                    EndBody.
                """
        expect = str(TypeMismatchInStatement(Assign(Id('y'),FloatLiteral(5.0))))
        self.assertTrue(TestChecker.test(input,expect,407))

    # def test_408(self):
    #     """Simple program: main"""
    #     input = Program([VarDecl(Id("x"),[10,50],ArrayLiteral([IntLiteral(2)]))])
    #     expect = str('')
    #     self.assertTrue(TestChecker.test(input,expect,408))