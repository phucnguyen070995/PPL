import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """Var:x;
                Function: x 
                Body: 

                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_wrong_miss_close(self):
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))
     
    def test_variable_203(self):
        input = """Var:x"""
        expect = "Error on line 1 col 5: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_all_204(self):
        input = """Var: x = 5, y ;
                    Function: x 
                    Body: 
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    
    def test_all_205(self):
        input = """Var: x = 5, y = 6., z = 0X456ABEF ; 
                    Function: x 
                    Body: 
                    
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test_all_206(self):
        input = """Var: x[1] = 5, y[5] = 6., z[1][2] = 0O56 ; 
                    Function: x 
                    Body: 
                    
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test_all_207(self):
        input = """Var: x, y = 2, u; 
                    Function: x 
                    Body: 
                    
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test_all_208(self):
        input = """Var: x = 5, y = 6., z = 0o123 ; 
                    Function: x 
                    Body: 
                    Var: x, y; 
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test_all_209(self):
        input = """Var: x = 5, y = 6., z = 0x1A ; 
                    Function: x 
                    Body: 
                    Var: x, y = 8; 
                    a = b; 
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test_all_210(self):
        input = """Var: x = 5, y = 6., z = "m" ; 
                    Function: x 
                    Body: Var: x, y = 7; 
                    a = b; 
                    fact(); 
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    def test_all_211(self):
        input = """Var: arr[5][7] = "aa" ; 
                   Function: x 
                   Parameter: y 
                   Body:  
                   EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    
    def test_all_212(self):
        input = """Var: arr[5][7] = 1 ; 
                    Function: x 
                    Parameter: y 
                    Body:  
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))
    def test_all_213(self):
        input = """ Function: x 
                    Parameter: y 
                    Body:  
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))
       
    def test_forStm_214(self):
        input = """ Var: x;
                    Function: fact
                    Parameter: n
                    Body:
                    For(i = 1, i < 3, i = i+2)
                    Do
                        i = i + 3;
                    EndFor.
                    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test_forStm_215(self):
        input = """ Var: x;
                    Function: fact
                    Parameter: n
                    Body:
                    For(i = 1, i < 3, i = i+2)
                    Do
                        i = i + 3;
                    EndBody."""
        expect = "Error on line 8 col 20: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_forStm_216(self):
        input = """ Var: x;
                Function: fact
                Parameter: n
                Body:
                For(i = 1, i < 3, i = i+5)
                Do
                    x = i +7;
                    Break;
                EndFor.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))


    def test_forStm_217(self):
        input = """ Var: x;
            Function: fact
            Parameter: n
            Body:
            For (i = 0, i < 10, i = i + 2) Do
            EndFor.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test_forStm_218(self):
        input = """ Var: x;
            Function: fact
            Parameter: n
            Body:
            For (i = 0, i < 10, i = i + 2) Do
            Return 1;
            Break;
            Continue;
            foo();
            goo(a+1);
            EndFor.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test_forStm_219(self):
        input = """Function: fact
            Body:
            For (i = 0, i < 10, i = i + 2) Do
            a = b + i;
            foo();
            goo(a+1);
            EndFor.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))

    def test_forStm_220(self):
        input = """ Var: x;
            Function: fact
            Parameter: n
            Body:
            For (i = 0, i < 10, i = i) Do
            goo();
            Break;
            EndFor.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))

    def test_ifStm_221(self):
        input = """ Var: x;
                Function: fact
                Parameter: n, y
                Body:
                If n == 0 Then
                Return 1;
                Else
                Return n * fact (n - 1);
                EndIf.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def test_ifStm_222(self):
        input = """ Var: x;
                Function: fact
                Parameter: n, y
                Body:
                If n == 0 Then
                Return 1;
                ElseIf x == 3 Then m = 1 +b[1];
                Else
                Return n * fact (n - 1);
                EndIf.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    
    def test_ifStm_223(self):
        input = """ Var: x;
                Function: fact
                Parameter: n, y
                Body:
                If n == 0 Then
                arr[3][2] = 1;
                EndIf.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test_ifStm_224(self):
        input = """ Var: x;
                Function: fact
                Parameter: n, y
                Body:
                If n == 0 Then
                arr[3][2] = 1;
                Else
                For (i = 0, i < 10, i = i) Do
                goo();
                Break;
                EndFor.
                EndIf.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))

    def test_ifStm_225(self):
        input = """ Var: x;
                Function: fact
                Parameter: n, y
                Body:
                If: n == 0 Then
                arr[3][2] = 1;
                EndIf.
                EndBody."""
        expect = "Error on line 5 col 18: :"
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test_ifStm_226(self):
        input = """ Var: x;
                Function: fact
                Parameter: n, y
                Body:
                If n == 0 Then:
                arr[3][2] = 1;
                EndIf.
                EndBody."""
        expect = "Error on line 5 col 30: :"
        self.assertTrue(TestParser.checkParser(input,expect,226))

    def test_ifStm_227(self):
        input = """ Var: x;
                Function: fact
                Parameter: n, y
                Body:
                If n == 0 Then
                arr[3][2] = 1;
                EndBody."""
        expect = "Error on line 7 col 16: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,227))

    def test_ifStm_228(self):
        input = """ Var: x;
                Function: fact
                Parameter: n, y
                Body:
                If.
                EndBody."""
        expect = "Error on line 5 col 18: ."
        self.assertTrue(TestParser.checkParser(input,expect,228))

    def test_ifStm_229(self):
        input = """ Var: x;
                Function: fact
                Parameter: n, y
                Body:
                If n == 0 Then
                arr[3][2] = 1;
                else;
                EndIf.
                EndBody."""
        expect = "Error on line 7 col 20: ;"
        self.assertTrue(TestParser.checkParser(input,expect,229))

    def test_ifStm_230(self):
        input = """ Var: x;
                Function: fact
                Parameter: n, y
                Body:
                if n == 0 Then
                arr[3][2] = 1;
                else;
                EndIf.
                EndBody."""
        expect = "Error on line 5 col 19: n"
        self.assertTrue(TestParser.checkParser(input,expect,230))

    def test_whileStm_231(self):
        input = """ Var: x;
                Function: fact
                Parameter: n, y
                Body:
                While n[1] == a[2] Do
                **Check**
                Break;
                EndWhile.
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))

    def test_whileStm_232(self):
        input = """ Var: x;
                Function: fact
                Parameter: n, y
                Body:
                while n[1] == a[2] Do
                **Check**
                Break;
                EndWhile.   
                EndBody."""
        expect = "Error on line 5 col 22: n"
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test_whileStm_233(self):
        input = """ Var: x;
                Function: fact
                Parameter: n, y
                Body:
                While: n[1] == a[2] Do
                **Check**
                Break;
                EndWhile.   
                EndBody."""
        expect = "Error on line 5 col 21: :"
        self.assertTrue(TestParser.checkParser(input,expect,233))

    def test_whileStm_234(self):
        input = """ Var: x;
                Function: fact
                Parameter: n, y
                Body:
                While n[1] == a[2] Do
                **Check**
                a
                EndWhile.   
                EndBody."""
        expect = "Error on line 8 col 16: EndWhile"
        self.assertTrue(TestParser.checkParser(input,expect,234))

    def test_whileStm_235(self):
        input = """ Var: x;
                Function: fact
                Parameter: n, y
                Body:
                While n[1] == a[2] Do
                **Check**
                a + b
                EndWhile.   
                EndBody."""
        expect = "Error on line 7 col 18: +"
        self.assertTrue(TestParser.checkParser(input,expect,235))

    def test_whileStm_236(self):
        input = """ Var: x;
                Function: fact
                Parameter: n, y
                Body:
                While n[1] == a[2]; Do
                **Check**
                Break;
                EndWhile.   
                EndBody."""
        expect = "Error on line 5 col 34: ;"
        self.assertTrue(TestParser.checkParser(input,expect,236))

    def test_whileStm_237(self):
        input = """ Var: x;
                Function: fact
                Parameter: n, y
                Body:
                While n[1] == a[2]
                **Check**
                Break;
                EndWhile.   
                EndBody."""
        expect = "Error on line 7 col 16: Break"
        self.assertTrue(TestParser.checkParser(input,expect,237))

    def test_whileStm_238(self):
        input = """ Var: x;
                Function: fact
                Parameter: n, y
                Body:
                While n[1] == a[2] Do
                **Check**
                Break;
                EndWhile
                EndBody."""
        expect = "Error on line 9 col 16: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,238))

    def test_whileStm_239(self):
        input = """ Var: x;
                Function: fact
                Parameter: n, y
                Body:
                While n[1] == a[2]
                EndBody."""
        expect = "Error on line 6 col 16: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,239))

    def test_whileStm_240(self):
        input = """ Var: x;
                Function: fact
                Parameter: n, y
                Body:
                While Do
                EndWhile.   
                EndBody."""
        expect = "Error on line 5 col 22: Do"
        self.assertTrue(TestParser.checkParser(input,expect,240))

    def test_doWhileStm_241(self):
        input = """ Var: x;
                Function: fact
                Parameter: n, y
                Body:
                Do x = y;
                While a > b;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test_doWhileStm_242(self):
        input = """ Var: x;
                Function: fact
                Parameter: n, y
                Body:
                Do x = y;
                While a > b && u < m;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test_doWhileStm_243(self):
        input = """ Var: x;
                Function: fact
                Parameter: n, y
                Body:
                Do x = y;
                While a > b;
                EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    
    def test_varible_244(self):
        input = """ Var: x, y;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    def test_varible_245(self):
        input = """ Var: x, y = 1, a;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test_varible_246(self):
        input = """ Var: x = "aa", y = 2;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))

    def test_varible_247(self):
        input = """ Var: x = True, y="Hi im here";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test_parameter_248(self):
        input = """ Var: x = True;
                    Function: foo
                    Parameter: a, b, x[2], y[2][3]
                    Body:

                    EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))
    
    def test_parameter_249(self):
        input = """ Var: x = 1;
                    Function: foo
                    Parameter: a, b, x[2], y[2][3]
                    Body:
                        a[2] = (a + b) + x;
                    EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))
    def test_parameter_250(self):
        input = """ Var: x = 1;
                    Function: foo
                    Parameter: a, b, x[2], y[2][3];
                    Body:
                        a[2] = (a + b) + x;
                    EndBody.
                    """
        expect = "Error on line 3 col 50: ;"
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def test_function_250(self):
        input = """ Var: x;
                    Function: fact
                    Parameter: n
                    Body:
                    If n == 0 Then
                    Return 1;
                    Else
                    Return n * fact (n - 1);
                    EndIf.
                    EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def test_function_251(self):
        input = """ Function: main
                    Body:
                    x = 10;
                    fact (x);
                    EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def test_function_252(self):
        input = """ Function: main
                    Body:
                    EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))
    
    def test_function_253(self):
        input = """ Function:
                    Body:
                    EndBody.
                    """
        expect = "Error on line 2 col 20: Body"
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def test_function_254(self):
        input = """ Function: main
                    """
        expect = "Error on line 2 col 20: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,254))

    def test_function_255(self):
        input = """
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))
    
    def test_function_256(self):
        input = """Function: main
                    Body:
                    Var: r = 10., v;
                    v = (4. / 3.) *. 3.14 *. r *. r *. r;
                    EndBody.

                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))
   

    def test_expression_257(self):
        input = """Function: main
                    Body:
                    x = y + (z -q) *. 10;
                    x = n >=. z;
                    EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))

   
    def test_expression_258(self):
        input = """ Var: a = 5;
                    Var: b[5];
                    Var: c, d = 6, e;
                    Function: main
                    Body:
                    x = y + (z -q) *. 10;
                    x = n >=. z;
                    EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))

    def test_all_259(self):
        input = """ Var: a = "Its string";
                    Var: b[5];
                    Var: c, d = 6, e;
                    Function: main
                    Body:
                    x = y + (z -q) *. 10;
                    x = n >=. z;
                    EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))

    def test_all_260(self):
        input = """ Var: a = "Its string";
                    Var: b[5];
                    Var: c, d = 6, e;
                    Function: main
                    Body:
                    x = y + (z -q) *. 10;
                    x = n >=. z;
                    ng = (arr[b[x[a+1*5 - (a - 9)]]] + 3) * y;
                    EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def test_all_261(self):
        input = """ Var: a = "Its string";
                    Var: b[5] = 1, p, y = 5;
                    Var: c, d = 6, e;
                    Function: main
                    Body:
                    If n =/= m Then
                        Return n[m] - 5;
                    Else
                        Return m + fact(n-1);
                    EndIf.
                    EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))

    def test_all_262(self):
        input = """ Var a = "Its string"
                    Var: b[5] = 1, p, y = 5;
                    Var: c, d = 6, e;
                    Function: main
                    Body:
                    If n =/= m Then
                        Return n[m] - 5;
                    Else
                        Return m + fact(n-1);
                    EndIf.
                    EndBody.
                    """
        expect = "Error on line 1 col 5: a"
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_all_263(self):
        input = """ Var: a = "Its string";
                    Var: b[5] = 1, p, y = 5;
                    Var: c, d = 6, e;
                    Function: cHECK
                    Body
                    a[3 + foo(2)] = a[b[2][3]] + 4;
                    If n =/= m Then
                        Return n[m] - 5;
                    Else
                        Return m + fact(n-1);
                    EndIf.
                    EndBody.
                    """
        expect = "Error on line 6 col 20: a"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test_all_264(self):
        input = """ **This is program
                * Here is declare
                * Here for function
                **
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))

    def test_all_265(self):
        input = """ Var: x[4][0][10];
                    Function: foo
                    Parameter: x[3]
                    Body:
                    While(True) Do
                        i = i + 1;
                    EndWhile.
                    EndBody.
        
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))
    
    def test_all_266(self):
        input = """ Var: x[4][0][10];
                    Function: goo
                    Parameter: x[1][2]
                    Body:
                    While(True) Do
                        If (x == True) Then x = a - 1;
                        EndIf.
                    EndWhile.
                    EndBody.            
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def test_all_267(self):
        input = """ Var: x[4][0][10];
                    Function: you
                    Parameter: x[3][4][6]
                    Body:
                    While(True)                            
                    EndWhile.
                    EndBody.
        
         """
        expect = "Error on line 6 col 20: EndWhile"
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def test_all_268(self):
        input = """ Var: x[4][0][10];
                    Function: me
                    Parameter: x[3][4][6]
                    Body:
                    If
                    EndIf.
                    EndBody.
        
         """
        expect = "Error on line 6 col 20: EndIf"
        self.assertTrue(TestParser.checkParser(input,expect,268))
    
    def test_all_269(self):
        input = """ Var: x[4][0][10];
                    Function: you
                    Parameter: x[3][4][6]
                    Body:
                    While                            
                    EndWhile.
                    EndBody.
        
         """
        expect = "Error on line 6 col 20: EndWhile"
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def test_all_270(self):
        input = """ Var: x[4][0][10];
                    Function: you
                    Parameter: x[3][4][6]
                    Body:
                    While                            
                    EndWhile.
                    EndBody.
        
         """
        expect = "Error on line 6 col 20: EndWhile"
        self.assertTrue(TestParser.checkParser(input,expect,270))

    def test_all_271(self):
        input = """ Var: x[4][0][10];
                    Function: you
                    Parameter: x[3][4][6]
                    Var: y;
                    Body:
                    While                            
                    EndWhile.
                    EndBody.            
         """
        expect = "Error on line 4 col 20: Var"
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def test_all_272(self):
        input = """ Var: x[4][0][10];
                    Function: you
                    Parameter: x[3][4][6]
                    Body:
                    Var: a;
                    If (z == True) Then
                        Return 1;
                    EndIf.
                    While (True)  Do                          
                    EndWhile.
                    EndBody.            
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test_all_273(self):
        input = """ Var: x[4][0][10];
                    Function: you
                    Parameter: x[3][4][6]
                    Body:
                    Var: a;
                    If (z == True) Then
                        Return 1;
                    
                    While (True)  Do                          
                    EndWhile.
                    EndBody.            
         """
        expect = "Error on line 11 col 20: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def test_all_274(self):
        input = """ Var: x = 1, y = 2., z = 3.5;
                    Function: you
                    Parameter: x , y[5]
                    Body:
                    Var: a, b, c = 10e5;
                    If (z == True) Then
                        Return 1;
                    EndIf.
                    While (True)  Do                          
                    EndWhile.
                    EndBody.            
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))
    
    def test_all_275(self):
        input = """ Var: x = 1, y = 2., z = 3.5;
                    Function: you
                    Parameter: x , y[5]
                    Body:
                    Var: a, b, c = 10e5, 5.e-1, 1.e-3;
                    Var a = y;
                    If (z == True) Then
                        Return 1;
                    EndIf.
                    While (True)  Do                          
                    EndWhile.
                    EndBody.            
         """
        expect = "Error on line 5 col 41: 5.e-1"
        self.assertTrue(TestParser.checkParser(input,expect,275))

    def test_all_276(self):
        input = """ Var: x, y = 2., z = 3.5;
                    Function: you
                    Parameter: x , y[5]
                    Body:
                    Var: a, b, c = "string";
                    Var: a = False;
                    If (z == True) Then
                        Return 1;
                    EndIf.
                    While (True)  Do    
                        foo();
                        goo(a);
                        Break;                      
                    EndWhile.
                    EndBody.            
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def test_all_277(self):
        input = """ Var: x, y = 1, z = 3.5;
                    Var: t;
                    Var: sp, yz;
                    Function: you
                    Parameter: q , d[5]
                    Body:
                    Var: a = "string", b;
                    Var: c = False;
                    foo(a + c);
                    If (z == True) Then
                        x = d[y *. z +. t -. c \ 10];
                        Return 1;
                    ElseIf x != 4.e5 Then
                        x = (a + b) * y - z + (sp *. yz);
                    Else
                        Continue;
                    EndIf.
                    While (True)  Do    
                        foo();
                        goo(a);
                        Break;                      
                    EndWhile.
                    For (i = 0, i < 10, i = i +2) Do
                        x = i;
                    EndFor.
                    EndBody.            
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))
    def test_all_278(self):
        input = """ Var: x, y = 1, z = 3.5;
                    Var: t;
                    Var: sp, yz;
                    Function: you
                 
                    Body:
                    Var: a = "string", b;
                    Var: c = False;
                    foo(a + c);
                    If (z == True) Then
                        x = d[y *. z +. t -. c \ 10];
                        Return 1;
                    ElseIf x != 4.e5 Then
                        x = (a + b) * y - z + (sp *. yz);
                    Else
                        Continue;
                    EndIf.
                    While (True)  Do    
                        foo();
                        goo(a);
                        Break;                      
                    EndWhile.
                    For (i = 0, i < 10, i = i +2) Do
                        x = i;
                    EndFor.
                    EndBody.            
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def test_all_279(self):
        input = """ Var: x, y = 1, 2., z = 3.5;
                    Var: t;
                    Var: sp, yz;
                    Function you
                    Parameter: q , d[5]
                    Body:
                    Var: a = "string", b;
                    Var: c = False;
                    foo(a + c);
                    If (z == True) Then
                        x = d[y *. z +. t -. c \ 10];
                        Return 1;
                    ElseIf x != 4.e5 Then
                        x = (a + b) * y - z + (sp *. yz);
                    Else
                        Continue;
                    EndIf.
                    While (True)  Do    
                        foo();
                        goo(a);
                        Break;                      
                    EndWhile.
                    For (i = 0, i < 10, i = i +2) Do
                        x = i;
                    EndFor.
                    EndBody.            
         """
        expect = "Error on line 1 col 16: 2."
        self.assertTrue(TestParser.checkParser(input,expect,279))
    
    def test_all_280(self):
        input = """ Var: x, y = 1, 2., z = 3.5;
                    Var: t;
                    Var: sp, yz;
                    Function: you
                    Parameter: q , d[5]
                    Body:
                    Var: a = "string", b;
                    Var: c = False;
                    foo(a + c);
                    If (z == True) Then
                        x = d[y *. z +. t -. c \ 10];
                        Return 1;
                    ElseIf x != 4.e5 Then
                        x = (a + b) * y - z + (sp *. yz);
                    Else
                        Continue;
                    EndIf.
                    While (True)  Do    
                        foo();
                        goo(a);
                        Break;                      
                    EndWhile.
                    For (i = 0, i < 10, i = i +2) 
                    EndFor.
                    EndBody.            
         """
        expect = "Error on line 1 col 16: 2."
        self.assertTrue(TestParser.checkParser(input,expect,280))

    def test_all_281(self):
        input = """ Var: x, y = 1, 2., z = 3.5;
                    Var: t;
                    Var: sp, yz;
                    Function: you
                    Parameter: q , d[5]
                    Body:
                    Var: a = "string", b;
                    Var: c = False;
                    foo(a + c);
                    If (z == True) Then
                        x = d[y *. z +. t -. c \ 10];
                        Return 1;
                    ElseIf x != 4.e5 Then
                        x = (a + b) * y - z + (sp *. yz);
                    Else
                        Continue;
                    EndIf.
                    While (True)  Do    
                        foo();
                        goo(a);
                        Break;                      
                    EndWhile.
                    For i = 0, i < 10, i = i +2 Do
                        x = i;
                    EndFor.
                    EndBody.            
         """
        expect = "Error on line 23 col 28: i"
        self.assertTrue(TestParser.checkParser(input,expect,281))

    
    def test_all_281(self):
        input = """ 
                    Function: you
                    Parameter: q , d[5]
                    Body:                        
                    For (, , ) Do
                        x = i;
                    EndFor.
                    EndBody.            
         """
        expect = "Error on line 5 col 25: ,"
        self.assertTrue(TestParser.checkParser(input,expect,281))
    
    def test_all_282(self):
        input = """ 
                    Function: you
                    Parameter: q , d[5]
                    Body:                        
                    For (x = 1, , ) Do
                        x = i;
                    EndFor.
                    EndBody.            
         """
        expect ="Error on line 5 col 32: ,"
        self.assertTrue(TestParser.checkParser(input,expect,282))

    def test_all_283(self):
        input = """ 
                    Function: you
                    Parameter: q , d[5]
                    Body:                        
                    For (i = 1, i < 10 , ) Do
                        x = i;
                    EndFor.
                    EndBody.            
         """
        expect = "Error on line 5 col 41: )"
        self.assertTrue(TestParser.checkParser(input,expect,283))

    def test_all_284(self):
        input = """ 
                    Function: you
                    Parameter: q , d[5]
                    Body:                        
                    For (i = a,i < 10, i = i + 1) Do
                        x = i;
                    EndFor.
                    EndBody.            
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))

    def test_all_285(self):
        input = """ 
                    Function: you
                    Parameter: q , d[5]
                    Body:                        
                    For (i = 1,i < 10, i = i + 1) Do
                    EndFor.
                    EndBody.            
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def test_all_286(self):
        input = """ 
                    Function: you
                    Parameter: q , d[5]
                    Body:                        
                    For (i = 1,i < 10, i = i + 1)
                      
                    EndBody.            
         """
        expect = "Error on line 7 col 20: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def test_all_287(self):
        input = """ 
                    Function: you
                    Parameter: q , d[5]
                    Body:                        
                    x = foo() + goo(x);
                    y = foo(x + goo(x));
                    EndBody.            
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,287))

    def test_all_288(self):
        input = """ 
                    Function: you
                    Parameter: q , d[5]
                    Body:                        
                    x = foo(x + y -z ) + goo(x[a - b]);
                    y = foo(2 * (x + goo(x)));
                    EndBody.            
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,288))

    def test_all_289(self):
        input = """ Var: uh;
                    Function: you
                    Parameter: q , d[5]
                    Body:  
                    x = -x;
                    y = -y;                        
                    EndBody.            
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,289))

    def test_all_290(self):
        input = """ Var: uh;
                    Function: you
                    Parameter: q , d[5]
                    Body:  
                    x = -x;
                    y = -y;
                    z = !z;                                            
                    x = foo() + goo(x);
                    y = foo(x + goo(x));
                    EndBody.            
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,290))

    def test_all_291(self):
        input = """ Var: uh;
                    Function: you
                    Parameter: q , d[5]
                    Body:                          
                    If(a != b) Then
                        Break;
                    EndIf.                                    
                    x = foo() + goo(x);
                    y = foo(x + goo(x));
                    EndBody.            
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))

    def test_all_292(self):
        input = """ Var: uh;
                    Function: you                        
                    Body:  
                    x = x == a;                        
                    If(z > 5) Then
                        Break;
                    EndIf.
                    x = foo() + goo(x);
                    y = foo(x + goo(x));
                    EndBody.            
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))
    
    def test_all_293(self):
        input = """ Var: uh;
                    Function: you
                    Parameter: q , d[5]
                    Body:                          
                    If(q <= q *2) Then
                        Break;
                    EndIf.                    
                    x = foo() + goo(x);
                    y = foo(x + goo(x));
                    EndBody.            
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))

    def test_all_294(self):
        input = """ Var: uh;
                    Function: you
                    Parameter: q , d[5]
                    Body: 
                    If(q <=. q *2) Then
                        Break;
                    EndIf.                    
                    x = foo() + goo(x);
                    y = foo(x + goo(x));
                    EndBody.            
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,294))

    def test_all_295(self):
        input = """ Var: uh;
                    Function: you
                    Parameter: q , d[5]
                    Body:
                    If(m >= m *. 3.) Then
                        Break;
                    EndIf.                            
                    x = foo() + goo(x);
                    y = foo(x + goo(x));
                    EndBody.            
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,295))

    def test_all_296(self):
        input = """ Var: uh;
                    Function: you
                    Parameter: q , d[5]
                    Body:  
                    If(ok =/= 5) Then
                        Break;
                    EndIf.                                  
                    x = foo() + goo(x);
                    y = foo(x + goo(x));
                    EndBody.            
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))

    def test_all_297(self):
        input = """ Var: uh;
                    Function: you
                    Parameter: q , d[5]
                    Body: 
                    If((a > b) && (c < d)) Then
                        Break;
                    EndIf.                              
                    x = foo() + goo(x);
                    y = foo(x + goo(x));
                    EndBody.            
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))

    def test_all_298(self):
        input = """ Var: uh;
                    Function: you
                    Parameter: q , d[5]
                    Body:                          
                    
                    x = foo("str") + goo(x);
                    y = foo(x + goo(x));
                    EndBody.            
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))

    def test_all_299(self):
        input = """           """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))

    def test_all_300(self):
        input = """ Var: uh;
                    Function: you
                    Parameter: q , d[5]
                    Body:                                       
                    x = foo(0XAB) + goo(0o12);
                    y = foo(x + goo(True));
                    EndBody.            
         """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,300))



     


        


