import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    # test variable declaration
    def test_var_dec_1(self):
        input = """Var: x = 20;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    def test_var_dec_2(self):
        input = """Var: x = 20, y=50, z;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    def test_var_dec_3(self):
        input = """Var: x = "This is string", y = 2.2e-1;  """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test_var_dec_4(self):
        input = """Var: x[1][2] = {1,2,3}, y[3];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_var_dec_5(self):
        input = """Var: x = True;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test_var_dec_6(self):
        input = """Var: x[1] = 20;"""
        expect = "Error on line 1 col 12: 20"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test_var_dec_7(self):
        input = """Var: x = {20};"""
        expect = "Error on line 1 col 9: {20}"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test_var_dec_8(self):
        input = """Var: x[a] = {20};"""
        expect = "Error on line 1 col 7: a"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    def test_var_dec_9(self):
        input = """Var: x[1+1] = {20};"""
        expect = "Error on line 1 col 8: +"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test_var_dec_10(self):
        input = """Var: x = "String include quote \'"text\'" ";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))


    # test variable declaration
        # if statement
    def test_if_stmt_1(self):
        input = """Function: foo
                    Parameter: a,b,c
                    Body:
                        Return a+b+c;
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    def test_if_stmt_2(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))
    def test_if_stmt_3(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))
    def test_if_stmt_4(self):
        input = """Var: a = 1, b =2;
            Function: foo
            Parameter: a,b,c
            Body:
                If a >=. b Then
                    Return a+b+c;
                EndIf.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))
    def test_if_stmt_5(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                If a < b Then
                    While True Do
                        foo(a,b);
                    EndWhile.
                ElseIf a == b
                    Return a+b;
                Else
                    Return a;
                EndIf.
            EndBody."""
        expect = "Error on line 9 col 20: Return"
        self.assertTrue(TestParser.checkParser(input,expect,215))
    def test_if_stmt_6(self):
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
                EndIf
            EndBody."""
        expect = "Error on line 13 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,216))
    def test_if_stmt_7(self):
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
                
            EndBody."""
        expect = "Error on line 13 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    def test_if_stmt_8(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                If a =/= b Then
                    While True Do
                        foo(a,b);
                    EndWhile.
                ElseIf a == b Then
                    Return a+b;
                Else.
                    Return a;
                EndIf.
            EndBody."""
        expect = "Error on line 10 col 20: ."
        self.assertTrue(TestParser.checkParser(input,expect,218))
    def test_if_stmt_9(self):
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
                    Return a;
                EndIf;
            EndBody."""
        expect = "Error on line 12 col 21: ;"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    def test_if_stmt_10(self):
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
                    If a % b = 1 Then
                        Return a;
                EndIf.
            EndBody."""
        expect = "Error on line 11 col 29: ="
        self.assertTrue(TestParser.checkParser(input,expect,220))

        # for statement
    def test_for_stmt_1(self):
        input = """Function: foo_for
            Parameter: a,b,c
            Body:
                For (i = 1, i < 10, 2) Do
                    If a % b == 1 Then
                        Return a;
                    EndIf.
                EndFor.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    def test_for_stmt_2(self):
        input = """Function: foo_for
            Parameter: a,b,c
            Body:
                For (i = 1, i < 10, 2) Do
                    For (i = 1, i > 10, 3) Do
                        Return a;
                    EndFor.
                EndFor.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    def test_for_stmt_3(self):
        input = """Function: foo_for
            Parameter: a,b,c
            Body:
                For (i = 1, i < 10, foo(1)) Do
                    For (i = 1, i > 10, i) Do
                        Return a;
                    EndFor.
                EndFor.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))
    def test_for_stmt_4(self):
        input = """Function: foo_for
            Parameter: a,b,c
            Body:
                For (i = foo(1), i < foo(10), foo(1)) Do
                    For (j = i, j < i + 10, i) Do
                        Return a;
                    EndFor.
                EndFor.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))
    def test_for_stmt_5(self):
        input = """Function: foo_for
            Parameter: a,b,c
            Body:
                For (i = 1, i , i) Do
                    For (j = i, j < i + 10, i) Do
                        Return a;
                    EndFor.
                EndFor.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))
    def test_for_stmt_6(self):
        input = """Function: foo_for
            Parameter: a,b,c
            Body:
                For (i = 1, i , i) Do
                    For (j == i, j < i + 10, i) Do
                        Return a;
                    EndFor.
                EndFor.
            EndBody."""
        expect = "Error on line 5 col 27: =="
        self.assertTrue(TestParser.checkParser(input,expect,226))
    def test_for_stmt_7(self):
        input = """Function: foo_for
            Parameter: a,b,c
            Body:
                For (i, i, i) Do
                    For (j = i, j < i + 10, i) Do
                        Return a;
                    EndFor.
                EndFor.
            EndBody."""
        expect = "Error on line 4 col 22: ,"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    def test_for_stmt_8(self):
        input = """Function: foo_for
            Parameter: a,b,c
            Body:
                For (i = i, i, i)
                    For (j = i, j < i + 10, i) Do
                        Return a;
                    EndFor.
                EndFor.
            EndBody."""
        expect = "Error on line 5 col 20: For"
        self.assertTrue(TestParser.checkParser(input,expect,228))
    def test_for_stmt_9(self):
        input = """Function: foo_for
            Parameter: a,b,c
            Body:
                For (i = i, i, i) Do
                    For (j = i, j < i + 10, i) Do
                        Return a;
                    EndFor
                EndFor.
            EndBody."""
        expect = "Error on line 8 col 16: EndFor"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    def test_for_stmt_10(self):
        input = """Function: foo_for
            Parameter: a,b,c
            Body:
                For (i = i, i, i) Do
                    For (j = i, j < i + 10, i = i + 1) Do
                        Return a;
                    EndFor.
                EndFor.
            EndBody."""
        expect = "Error on line 5 col 46: ="
        self.assertTrue(TestParser.checkParser(input,expect,230))

        # test while statmenet
    def test_while_stmt_1(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                While True Do
                    foo(a,b);
                EndWhile.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))
    def test_while_stmt_2(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                While a == b Do
                    foo(a,b);
                EndWhile.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))
    def test_while_stmt_3(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                While foo(a,b) == b Do
                    foo(a,b);
                EndWhile.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    def test_while_stmt_4(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                While i < 10 Do
                    print(a[i]);
                    i = i + 1;
                EndWhile.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))
    def test_while_stmt_5(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))
    def test_while_stmt_6(self):
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
                EndWhile
            EndBody."""
        expect = "Error on line 12 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,236))
    def test_while_stmt_7(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                While i < 10 Do
                    print(a[i]);
                    While j < i
                        print(a[j]);
                        j = j + 1;
                    EndWhile.
                    i = i + 1;
                EndWhile.
            EndBody."""
        expect = "Error on line 7 col 24: print"
        self.assertTrue(TestParser.checkParser(input,expect,237))
    def test_while_stmt_8(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                While i < 10 Do
                    print(a[i]);
                    While j == i Do
                        print(a[j]);
                        j = j + 1;
                    EndWhile.
                    i = i + 1;
                EndWhile.
                EndWhile.
                EndWhile.
                EndWhile.
            EndBody."""
        expect = "Error on line 12 col 16: EndWhile"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    def test_while_stmt_9(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                While i < 10 Do
                    print(a[i]);
                    While j == i Do
                        print(a[j]);
                        j = j + 1;
                    EndWhile.
                    i = i + 1;



                EndWhile;
            EndBody."""
        expect = "Error on line 14 col 24: ;"
        self.assertTrue(TestParser.checkParser(input,expect,239))
    def test_while_stmt_10(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                While (((i < 10))) Do
                    print(a[i]);
                    While j == i Do
                        print(a[j]);
                        j = j + 1;
                    EndWhile
                    i = i + 1;
                EndWhile.
            EndBody."""
        expect = "Error on line 10 col 20: i"
        self.assertTrue(TestParser.checkParser(input,expect,240))

        # test do while
    def test_do_while_stmt_241(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))
    def test_do_while_stmt_242(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))
    def test_do_while_stmt_243(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                Do
                    ** Empty While **
                While ( False )
                EndDo.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))
    def test_do_while_stmt_244(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))
    def test_do_while_stmt_245(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))
    def test_do_while_stmt_246(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                Do
                    Do
                        Return a;
                    
                    EndDo.
                While ( False )
                EndDo.
            EndBody."""
        expect = "Error on line 8 col 20: EndDo"
        self.assertTrue(TestParser.checkParser(input,expect,246))
    def test_do_while_stmt_247(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                Do
                    Do
                        Return a;
                    While(True)
                    EndDo
                While ( False )
                EndDo.
            EndBody."""
        expect = "Error on line 9 col 16: While"
        self.assertTrue(TestParser.checkParser(input,expect,247))
    def test_do_while_stmt_248(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                Do
                    Do.
                        Return a;
                    While(True)
                    EndDo.
                While ( False )
                EndDo.
            EndBody."""
        expect = "Error on line 5 col 22: ."
        self.assertTrue(TestParser.checkParser(input,expect,248))
    def test_do_while_stmt_249(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                Do
                    Do
                        Return a;
                    While(True)
                    EndDo.
                While ( False  = 1)
                EndDo.
            EndBody."""
        expect = "Error on line 9 col 31: ="
        self.assertTrue(TestParser.checkParser(input,expect,249))
    def test_do_while_stmt_250(self):
        input = """Function: foo_while
            Parameter: a,b,c
            Body:
                Do
                    
                        Return a;
                    While(True)
                    EndDo.
                While ( False  == 1)
                EndDo.
            EndBody."""
        expect = "Error on line 10 col 16: EndDo"
        self.assertTrue(TestParser.checkParser(input,expect,250))

        # test break statement
    def test_break_stmt_1(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))
    def test_break_stmt_2(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                If a < b Then
                    While True Do
                        Break
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
        expect = "Error on line 7 col 20: EndWhile"
        self.assertTrue(TestParser.checkParser(input,expect,252))


        # test continue statement
    def test_continue_stmt_1(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))
    def test_continue_stmt_2(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                If a < b Then
                    While True Do
                        Continue
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
        expect = "Error on line 7 col 20: EndWhile"
        self.assertTrue(TestParser.checkParser(input,expect,254))

        # test function call
    def test_func_call_1(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                a = boo(1,2.3);
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))
    def test_func_call_2(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                a = boo(1, boo(1, foo(1)));
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))
    def test_func_call_3(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                Return boo( a[12] );
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))
    def test_func_call_4(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                Return boo(  );
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))
    def test_func_call_5(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                Return boo( ( () ) );
            EndBody."""
        expect = "Error on line 4 col 31: )"
        self.assertTrue(TestParser.checkParser(input,expect,259))
    def test_func_call_6(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                Return boo( ( (1) ) );
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))


        # sunmary test
    def test_sunmary_dec_1(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))
    def test_sunmary_dec_2(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))
    def test_sunmary_dec_3(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test_sunmary_dec_4(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))
    def test_sunmary_dec_5(self):
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
                    While (a \. 10.0 =/= 10.5)
                    EndDo.
                EndIf.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))
    def test_sunmary_dec_6(self):
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
                    While (a \. 10.0 =/= 10.5)
                    EndDo.
                EndIf.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))
    def test_sunmary_dec_7(self):
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
                        While (a \. 10.0 =/= 10.5e-3)
                        EndDo.
                    While (a \. 10.0 =/= 10.5e-3)
                    EndDo.
                EndIf.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))
    def test_sunmary_dec_8(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                a = 0x123456;
                If a < b Then
                    While True Do
                        Break;
                    EndWhile.
                ElseIf a == b Then
                    For (i = 1; i < 10; 1) Do
                        foo(foo(foo(5)));
                    EndFor.
                Else
                    Do
                        Do
                            Continue;
                        While (a \. 10.0 =/= 10.5e-3)
                        EndDo.
                    While (a \. 10.0 =/= 10.5e-3)
                    EndDo.
                EndIf.
            EndBody."""
        expect = "Error on line 10 col 30: ;"
        self.assertTrue(TestParser.checkParser(input,expect,268))
    def test_sunmary_dec_9(self):
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
                        While (a \. 10.0 =/= 10.5e-3)
                        EndDo.
                    While (a \. 10.0 =/= 10.5e-3)
                    EndDo.
                EndIf.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))
    def test_sunmary_dec_10(self):
        input = """Function: foo
            Parameter: a,b,c
            Body:
                a = 0x123456;
                If a < b < c Then
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
                        While (a \. 10.0 =/= 10.5e-3)
                        EndDo.
                    While (a \. 10.0 =/= 10.5e-3)
                    EndDo.
                EndIf.
            EndBody."""
        expect = "Error on line 5 col 25: <"
        self.assertTrue(TestParser.checkParser(input,expect,270))



#     def test_var_dec_2(self):
#         input = """Var: ;"""
#         expect = "Error on line 1 col 5: ;"
#         self.assertTrue(TestParser.checkParser(input,expect,202))
#     def test_var_dec_3(self):
#         input = """Var: b[2][3] = {{2,3,4},{4,5,6}};"""
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,203))
#     def test_var_dec_4(self):
#         input = """Var: c, d = 6, e, f;"""
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,204))
#     def test_var_dec_5(self):
#         input = """Var: m, n[10];"""
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,205))
#     def test_var_dec_6(self):
#         input = """Var: n[10], m;"""
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,206))
#     def test_assignment_stm_1(self):
#         input = """a[3 + foo(2)] = a[b[2][3]] + 4;"""
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,207))
#     def test_assignment_stm_2(self):
#         input = """v = (4. \. 3.) *. 3.14 *. r *. r *. r;"""
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,208))
#     def test_callee_stm_1(self):
#         input = """foo(a[1][2] + 2, x + 1);"""
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,209))
#     def test_callee_stm_2(self):
#         input = """x = foo(a[1][2] + 2, x + 1);"""
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,210))
#     def test_function_1(self):
#         input = """Function: foo
# Parameter: a[5], b
# Body:
#     Var: i = 0;
#     While (i < 5) Do
#         a[i] = b +. 1.0;
#         i = i + 1;
#     EndWhile.
# EndBody."""
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,211))
#     def test_for_1(self):
#         input = """For (i = 0, i < 10, 2) Do
#     writeln(i);
# EndFor."""
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,212))
#     def test_var_dec_7(self):
#         input = """Var: a = 5;
# Var: b[2][3] = {{2,3,4},{4,5,6}};
# Var: c, d = 6, e, f;
# Var: m, n[10];"""
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,213))
#     def test_var_dec_func_dec_1(self):
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
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,214))
#     def test_var_dec_8(self):
#         input = """Var: a[5] = {1,4,3,2,0};
# Var: b[2][3]={{1,2,3},{4,5,6}};"""
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,215))
#     def test_var_dec_func_dec_2(self):
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
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,216))
#     def test_callee_stm_3(self):
#         input = """foo (2 + x, 4. \. y);
# goo ();"""
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,217))
#     def test_type_coercions_1(self):
#         input = """If bool_of_string ("True") Then
# a = int_of_string (read ());
# b = float_of_int (a) +. 2.0;
# EndIf."""
#         expect = "successful"
#         self.assertTrue(TestParser.checkParser(input,expect,218))
    