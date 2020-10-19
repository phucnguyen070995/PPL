import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):

    # variables declaration
    def test_vardec_1(self):
        input = """Var: a = 5;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_vardec_2(self):
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def test_vardec_3(self):
        input = """Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test_vardec_4(self):
        input = """Var: a,tes=123,  b,c;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def test_vardec_5(self):
        input = """Var: m=12, n[10];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def test_vardec_6(self):
        input = """Var: n[10]={1,2,3}, a,b,c,d;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test_vardec_7(self):
        input = """Var: n[10]={1,2,3}, a2[3],b123[123],c,d;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_vardec_8(self):
        input = """Var: n[10][2]={{1},{2},{3}}, a,b,c,d;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_vardec_9(self):
        input = """Var: a[1],b[1],c[1],d[1];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_vardec_10(self):
        input = """Var: n[10][1][2][3]={1,2,3}, a,b,c,d;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    def test_vardec_11(self):
        input = """Var: a[1],b[1],c[1],d[1];
        Var: a[1],b[1],c[1],d[1];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_vardec_12(self):
        input = """Var: qwe[1][2][3]={1,2,3}, a,b,c,d;
        Var: qwe[1][2][3]={1,2,3}, a,b,c,d;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_vardec_13(self):
        input = """Var: qwe[1][2][3]={1,2,3}, a,b,c,d;
        Var: qwe[1][2][3]={1,2,3}, a,b,c,d;
        Var:a=1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_vardec_14(self):
        input = """Var:a=1;Var:a=1;Var:a=1;Var:a=1;Var:a=1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_vardec_15(self):
        input = """Var: n[10][1][2][3]={{123,2,3,4},{2},3};"""
        expect = "Error on line 1 col 20: {"
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    # function declaration
    def test_funcdec_1(self):
        input = """Function: main
        Body:
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_funcdec_2(self):
        input = """Function: main
        Body:Var:a=1;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test_funcdec_3(self):
        input = """Function: main
        Body:Var:a[2]={12,3,4},b=2,c=True;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test_funcdec_4(self):
        input = """Function: main
        Body:Var:a[2]={12,3,4},b=2,c=True;
        Var:c=4;
        EndIf
        EndBody."""
        expect = "Error on line 4 col 8: EndIf"
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test_funcdec_5(self):
        input = """Function: main
        Body:Var:a[2]={12,3,4},b=2,c=True;
        Var:c=4;
        a=b+1;b=a==b;r=a+b+c-e-.d;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_funcdec_6(self):
        input = """Function: main
        Body:Var:a[2]={12,3,4},b=2,c=True;
        Var:c=4;
        a=b+1;b=a==b;r=a+b+c-e-.d;
        foo(foo((a+b+.12e10))+foo());
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test_funcdec_7(self):
        input = """Function: main
        Body:Var:a[2]={12,3,4},b=2,c=True;
        Var:c=4;
        EndBody.Function: foo
        Body:a=b+1;b=a==b;r=a+b+c-e-.d;
        foo((a+b+.12e10));EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test_funcdec_8(self):
        input = """Function: main
        Body:
        Function:fooBody:EndBody.
        EndBody."""
        expect = "Error on line 3 col 8: Function"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test_funcdec_9(self):
        input = """Function: main
        Body:
        EndBody.Function: main
        Body:
        EndBody.Function: main
        Body:
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test_funcdec_10(self):
        input = """Function: main
        Body:
        EndBody.
        Var: a = 5;Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;Var: m, n[10];
        Function: main
        Body:
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    # STATEMENT

    def test_elseif_1(self):
        input = """Function: test
        Parameter: n
        Body:
            If n > 10 Then
                Return 5;
            ElseIf n >5 Then a=a+1; Return a;
            ElseIf n < 10 Then a=a+1; Return a;
            Else
                Return False;
            EndIf.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test_elseif_2(self):
        input = """Function: test
        Parameter: n
        Body:
            If n > 10 Then
                Return 5;
            ElseIf n >5 then a=a+1; Return a;
            Else
                Return False;
            EndIf.
        EndBody."""
        expect = "Error on line 6 col 24: then"
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def test_param_1(self):
        input = """Function: abctest
        Parameter: n,a[2],b[5][6],m
        Body:
            If n > 10 Then
                Return 5;
            ElseIf n >5 Then a=a+.1; Return a;
            Else
                Return False;
            EndIf.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test_ifelse_1(self):
        input = """Function: abctest
        Parameter: a[2],b[5][6]
        Body:
            Var:b;
            Var:b,c,d;
            If n > 10 Then
                Return 5;
            ElseIf n >5 Then a=a+1; Return a;
            Else
                Return False;
            EndIf.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test_ifelse_2(self):
        input = """Function: abctest
        Parameter: a[2],b[5][6]
        Body:
            Var:b;
            Function: funcinsidefunc
            Body:
            EndBody.
            If n > 10 Then
                Return 5;
            ElseIf n >5 Then a=a+1; Return a;
            Else
                Return False;
            EndIf.
        EndBody."""
        expect = "Error on line 5 col 12: Function"
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test_ifelse_3(self):
        input = """Function: abctest
        Parameter: a[2],b[5][6]
        Body:
            Var:b;
            If n > 10 Then
                Return 5;
            EndIf.
            Var:c=2;
        EndBody."""
        expect = "Error on line 8 col 12: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test_param_2(self):
        input = """Function: abctest
        Parameter: a[2],b[5][6]
        Body:
            If n > 10 Then
                Return 5;
            ElseIf n >5 Then aa+1; Return a;
            Else
                Return False;
            EndIf.
        EndBody."""
        expect = "Error on line 6 col 31: +"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test_for_1(self):
        input = """Function: main
        Parameter: x
        Body:   For (a=5,a<10,aa+1) Do abc(a); EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test_for_2(self):
        input = """Function: main
        Parameter: x
        Body:
            For (a=5,a<10,a+.1) Do 
                abc(a);
                For (a=2,a==0,a*1) Do
                    If ab==cd Then
                    a=a+1;
                    EndIf.
                EndFor.
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test_for_3(self):
        input = """Function: main
        Parameter: x
        Body:
            For (i = 0, i < 10, 2) Do
            writeln(i);
            EndFor.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    # comment
    def test_comment_in_program_1(self):
        input = """**Declare variable**Var: he = "hello";
        Var: b = 5, c = False;
        **Program over "over"**"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 298))

    def test_comment_in_program_2(self):
        input = """**Declare variable**Var: he = "hello";
        Var: b = 5, c = False;
        **Program over "over"** Var: a = {"bk","c","d"};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 299))

    def test_comment_in_program_3(self):
        input = """**Declare variable**Var: he = "hello";
        Var: b = 5, c = False;
        **Program over "over"** Var: a = {"bk","c","d"},ac,ab,ad=8;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 300))


# reference


def test_if_stm_9(self):
    input = """Function: test
Body:
    If n > 10 Then
        If n > 10 Then
            print("Hello World!");
        ElseIf n > 8 Then
            If n > 10 Then
                print("Hello World!");
            ElseIf n > 8 Then
                If n != 10 Then
                    print("Hello World!");
                ElseIf n > 8 Then
                    If n > 10 Then
                        While (i < 5) Do
                            a[i] = b +. 1.0;
                            i = i + 1;
                        EndWhile.
                        print("Hello World!");
                    ElseIf n >=. 8 Then
                        print("Hello World!");
                    print("Hello World!");
                EndIf.
                print("Hello World!");
            EndIf.
            While (i < 5) Do
                a[i] = b +. 1.0;
                i = i + 1;
            EndWhile.
            print("Hello World!");
        EndIf.
        print("Hello World!");
    EndIf.
        print("Hello World!");
    EndIf.
EndBody."""
    expect = "successful"
    self.assertTrue(TestParser.checkParser(input, expect, 279))
