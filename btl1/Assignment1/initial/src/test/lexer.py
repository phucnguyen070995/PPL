import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):    
    def test(self):
        input = """int main(int a,b,c,d;){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 200))
    def test_basic(self):
        input = """int main(){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))
    def test_basic2(self):
        input = """int main(){;}"""
        expect = "Error on line 1 col 11: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 202)) 
    def test_basic3(self):
        input = """int main(){
    {
    
    }
    
    {n}
}"""
        expect = "Error on line 6 col 6: }"
        self.assertTrue(TestParser.checkParser(input, expect, 203))  
    def test_basic4(self):
        input = """int main(){
    {
    
    }
    int a = 1; 
}"""
        expect = "Error on line 5 col 10: ="
        self.assertTrue(TestParser.checkParser(input, expect, 204)) 
    def test_basic5(self):
        input = """Void main();"""
        expect = "Error on line 1 col 0: Void"
        self.assertTrue(TestParser.checkParser(input, expect, 205))
    def test_basic6(self):
        input = """void rman(){
//}"""
        expect = "Error on line 2 col 3: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 206))    
    def test_basic7(self):
        input = """void rman(){
//iascbns + ?
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 207)) 
    def test_if(self):
        input = """void rman(){
if (){}
}"""
        expect = "Error on line 2 col 4: )"
        self.assertTrue(TestParser.checkParser(input, expect, 208))
    def test_if2(self):
        input = """void rman(){
if (a){//}
}"""
        expect = "Error on line 3 col 1: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 209))
    def test_if3(self):
        input = """void rman(){
if (a){}
if(a<4<4){}
}"""
        expect = "Error on line 3 col 6: <"
        self.assertTrue(TestParser.checkParser(input, expect, 210))
    def test_if4(self):
        input = """int 1710169(){
}"""
        expect = "Error on line 1 col 4: 1710169"
        self.assertTrue(TestParser.checkParser(input, expect, 211))
    def test_if5(self):
        input = """boolean NguyenVanHoaiLinh (){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 212))
    def test_if6(self):
        input = """boolean NguyenVanHoaiLinh (){
    if (a){}
    else {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 213))
    def test_if7(self):
        input = """boolean NguyenVanHoaiLinh (){
    if (a){ a = 1; b= 2;}
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 214))
    def test_if8(self):
        input = """boolean NguyenVan HoaiLinh (){
    if (a){ a = 1; b= 2;}
    else {ok;}
}"""
        expect = "Error on line 1 col 18: HoaiLinh"
        self.assertTrue(TestParser.checkParser(input, expect, 215))
    def test_if9(self):
        input = """boolean NguyenVanHoaiLinh (){
    if (a){ a = 1; abc b= 2;}
    else {ok;}
}"""
        expect = "Error on line 2 col 23: b"
        self.assertTrue(TestParser.checkParser(input, expect, 216))
    def test_if10(self):
        input = """boolean NguyenVanHoaiLinh (){
    if (a){ a = 1; do{}abc b= 2;}
    else {ok;}
}"""
        expect = "Error on line 2 col 27: b"
        self.assertTrue(TestParser.checkParser(input, expect, 217))
    def test_if11(self):
        input = """int NguyenVanHoaiLinh (){
    if (a){ a = 1; do{}abc b= 2;}
    else {ok;}
}"""
        expect = "Error on line 2 col 27: b"
        self.assertTrue(TestParser.checkParser(input, expect, 218))
    def test_doWhile(self):
        input = """int NguyenVanHoaiLinh (){
    if (a<2)
    { a = 1; do{a=2;}while a=a;
    b= 2;}
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 219))
    def test_doWhile2(self):
        input = """int NguyenVanHoaiLinh (){
    if (a<2)
    { a = 1; do{a=2;}while a=a;
    b= 2;}
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 220))
    def test_doWhile3(self):
        input = """int NguyenVanHoaiLinh (){
    if (a<2)
    { a = 1; do{a2}while a=a;
    b= 2;}
    else {ok;}
}"""
        expect = "Error on line 3 col 18: }"
        self.assertTrue(TestParser.checkParser(input, expect, 221))
    def test_doWhile4(self):
        input = """int NguyenVanHoaiLinh (){
    if (a<2)
    { a = 1; {a2}while a=a;
    b= 2;}
    else {ok;}
}"""
        expect = "Error on line 3 col 16: }"
        self.assertTrue(TestParser.checkParser(input, expect, 222))
    def test_doWhile5(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    /*{ a = 1; {a2}while a=a;
    b= 2;}
    else {ok;}
}"""
        expect = "Error on line 3 col 4: /"
        self.assertTrue(TestParser.checkParser(input, expect, 223))
    def test_doWhile6(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    /*{ a = 1; {a2}while a=a;
    b= 2;}
    else {ok;}*/
}"""
        expect = "Error on line 6 col 0: }"
        self.assertTrue(TestParser.checkParser(input, expect, 224))
    def test_doWhile7(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    { a \n= 1; {a2}while a=a;
    b= 2;}
    else {ok;}*/
}"""
        expect = "Error on line 4 col 8: }"
        self.assertTrue(TestParser.checkParser(input, expect, 225))
    def test_doWhile8(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    { a= 1; {a2}while a=a;
    b= 2;}
    else {ok;}
}"""
        expect = "Error on line 3 col 15: }"
        self.assertTrue(TestParser.checkParser(input, expect, 226))
    def test_doWhile9(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {;}
    else {ok;}
}"""
        expect = "Error on line 3 col 5: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 227))
    def test_doWhile10(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;}
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))
    def test_doWhile11(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;}while a= 4; }
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))
    def test_doWhile12(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;}while a= 4; do {a= 3;}while a; }
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 230))
    def test_doWhile13(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;}while a= 4; do {a= 3=a=b;}while a; }
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 231))
    def test_doWhile14(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;}while a= 4; do {a= 3=<a=b;}while a; }
    else {ok;}
}"""
        expect = "Error on line 3 col 35: <"
        self.assertTrue(TestParser.checkParser(input, expect, 233))
    def test_doWhile14(self):
        input = """string VOID (){
    if (a<2)
    {a;do {a;}while a= 4; do {a= 3=<a=b;}while a; }
    else {ok;}
}"""
        expect = "Error on line 3 col 35: <"
        self.assertTrue(TestParser.checkParser(input, expect, 232))
    
    def test_doWhile15(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;}while a= 4; do {a= 3<=a=b;}while a; }
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 234))
    def test_doWhile16(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;a = 1.1E0;}while 0=3; do {a= 3<=a=b;}while a; }
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 235))
    def test_doWhile17(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;a = 1.1E0.;}while 0=3; do {a= 3<=a=b;}while a; }
    else {ok;}
}"""
        expect = "."
        self.assertTrue(TestParser.checkParser(input, expect, 236))
    def test_doWhile18(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;a = 1.;}while 0=3; do {a= 3<=a=b;}while a; }
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 237))
    def test_doWhile19(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;a = 1.;}while 0=3; do {a= 3<=a=b;}while a; a=a=b=\n;}
    else {ok;}
}"""
        expect = "Error on line 4 col 0: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 238))
    def test_doWhile20(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;a = 1.;}while 3=fianfkansk; do {a= 3<=a=b;}while a; a=a=b=\n;}
    else {ok;}
}"""
        expect = "Error on line 4 col 0: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 239))
    def test_doWhile21(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;a = 1.;}while 3=fianfkansk; u=2;}
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 240))
    def test_doWhile22(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;a = 1.;}while 3=fianfkansk; continue; u=2;}
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 241))
    def test_doWhile23(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;a = 1.;}while 3=fianfkansk; u=2;}
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))
    def test_doWhile24(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;a = 1.;}while 3=fianfkansk; u=2;}
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 243))
    def test_doWhile24(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;a = 1.;}while 3=fianfkansk; u=2;}
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 244))
    def test_doWhile25(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;a = 1.;}while 3=fianfkansk; u=2;}
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 245))
    def test_doWhile26(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;a = 1.;} while 3=fianfkansk; break ;u=2;}
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 246))
    def test_doWhile27(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;a = 1.;}while 2=2; int a,b,c,d; cbcd= fbasjdn;}
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 247))
    def test_doWhile28(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;a = 1.;}while a; int a,b,c,d; cbcd= fbasjdn;}
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 248))
    def test_doWhile29(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;if (a==4){a;}int a,b,c,d; cbcd= fbasjdn;}
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 249))
    def test_doWhile30(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;if (a==4){a;}int a,b,c,d; cbcd= adv<3;}
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 250))
    def test_new(self):
        input = """int main(){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))
    def test_new2(self):
        input = """int main(){;}"""
        expect = "Error on line 1 col 11: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 252)) 
    def test_new3(self):
        input = """int main(){
    {
    
    }
    
    {n}
}"""
        expect = "Error on line 6 col 6: }"
        self.assertTrue(TestParser.checkParser(input, expect, 253))  
    def test_new4(self):
        input = """int main(){
    {
    
    }
    int a = 1; 
}"""
        expect = "Error on line 5 col 10: ="
        self.assertTrue(TestParser.checkParser(input, expect, 254)) 
    def test_new5(self):
        input = """Void main();"""
        expect = "Error on line 1 col 0: Void"
        self.assertTrue(TestParser.checkParser(input, expect, 255))
    def test_new6(self):
        input = """void rman(){
//}"""
        expect = "Error on line 2 col 3: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 256))    
    def test_new7(self):
        input = """void rman(){
//iascbns + ?
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 257)) 
    def test_ifnew(self):
        input = """void rman(){
if (){}
}"""
        expect = "Error on line 2 col 4: )"
        self.assertTrue(TestParser.checkParser(input, expect, 258))
    def test_ifnew2(self):
        input = """void rman(){
if (a){//}
}"""
        expect = "Error on line 3 col 1: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 259))
    def test_ifnew3(self):
        input = """void rman(){
if (a){}
if(a<4<4){}
}"""
        expect = "Error on line 3 col 6: <"
        self.assertTrue(TestParser.checkParser(input, expect, 260))
    def test_ifnew4(self):
        input = """int 1710169(){
}"""
        expect = "Error on line 1 col 4: 1710169"
        self.assertTrue(TestParser.checkParser(input, expect, 261))
    def test_ifnew5(self):
        input = """boolean NguyenVanHoaiLinh (){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 262))
    def test_ifnew6(self):
        input = """boolean NguyenVanHoaiLinh (){
    if (a){}
    else {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 263))
    def test_ifnew7(self):
        input = """boolean NguyenVanHoaiLinh (){
    if (a){ a = 1; b= 2;}
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 264))
    def test_ifnew8(self):
        input = """boolean NguyenVan HoaiLinh (){
    if (a){ a = 1; b= 2;}
    else {ok;}
}"""
        expect = "Error on line 1 col 18: HoaiLinh"
        self.assertTrue(TestParser.checkParser(input, expect, 265))
    def test_ifnew9(self):
        input = """boolean NguyenVanHoaiLinh (){
    if (a){ a = 1; abc b= 2;}
    else {ok;}
}"""
        expect = "Error on line 2 col 23: b"
        self.assertTrue(TestParser.checkParser(input, expect, 266))
    def test_ifnew10(self):
        input = """boolean NguyenVanHoaiLinh (){
    if (a){ a = 1; do{}abc b= 2;}
    else {ok;}
}"""
        expect = "Error on line 2 col 27: b"
        self.assertTrue(TestParser.checkParser(input, expect, 267))
    def test_ifnew11(self):
        input = """int NguyenVanHoaiLinh (){
    if (a){ a = 1; do{}abc b= 2;}
    else {ok;}
}"""
        expect = "Error on line 2 col 27: b"
        self.assertTrue(TestParser.checkParser(input, expect, 268))
    def test_doWhilenew(self):
        input = """int NguyenVanHoaiLinh (){
    if (a<2)
    { a = 1; do{a=2;}while a=a;
    b= 2;}
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 269))
    def test_doWhile2new(self):
        input = """int NguyenVanHoaiLinh (){
    if (a<2)
    { a = 1; do{a=2;}while a=a;
    b= 2;}
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 270))
    def test_doWhile3new(self):
        input = """int NguyenVanHoaiLinh (){
    if (a<2)
    { a = 1; do{a2}while a=a;
    b= 2;}
    else {ok;}
}"""
        expect = "Error on line 3 col 18: }"
        self.assertTrue(TestParser.checkParser(input, expect, 271))
    def test_doWhile4new(self):
        input = """int NguyenVanHoaiLinh (){
    if (a<2)
    { a = 1; {a2}while a=a;
    b= 2;}
    else {ok;}
}"""
        expect = "Error on line 3 col 16: }"
        self.assertTrue(TestParser.checkParser(input, expect, 272))
    def test_doWhile5new(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    /*{ a = 1; {a2}while a=a;
    b= 2;}
    else {ok;}
}"""
        expect = "Error on line 3 col 4: /"
        self.assertTrue(TestParser.checkParser(input, expect, 273))
    def test_doWhile6new(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    /*{ a = 1; {a2}while a=a;
    b= 2;}
    else {ok;}*/
}"""
        expect = "Error on line 6 col 0: }"
        self.assertTrue(TestParser.checkParser(input, expect, 274))
    def test_doWhile7new(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    { a \n= 1; {a2}while a=a;
    b= 2;}
    else {ok;}*/
}"""
        expect = "Error on line 4 col 8: }"
        self.assertTrue(TestParser.checkParser(input, expect, 275))
    def test_doWhile8new(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    { a= 1; {a2}while a=a;
    b= 2;}
    else {ok;}
}"""
        expect = "Error on line 3 col 15: }"
        self.assertTrue(TestParser.checkParser(input, expect, 276))
    def test_doWhile9new(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {;}
    else {ok;}
}"""
        expect = "Error on line 3 col 5: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 277))
    def test_doWhile10new(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;}
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 278))
    def test_doWhile11new(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;}while a= 4; }
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 279))
    def test_doWhile12new(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;}while a= 4; do {a= 3;}while a; }
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 280))
    def test_doWhile13new(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;}while a= 4; do {a= 3=a=b;}while a; }
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 281))
    def test_doWhile14new(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;}while a= 4; do {a= 3=<a=b;}while a; }
    else {ok;}
}"""
        expect = "Error on line 3 col 35: <"
        self.assertTrue(TestParser.checkParser(input, expect, 282))
    def test_doWhile15new(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;}while a= 4; do {a= 3<=a=b;}while a; }
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 283))
    def test_doWhile16new(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;a = 1.1E0;}while 0=3; do {a= 3<=a=b;}while a; }
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 284))
    def test_doWhile17new(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;a = 1.1E0.;}while 0=3; do {a= 3<=a=b;}while a; }
    else {ok;}
}"""
        expect = "."
        self.assertTrue(TestParser.checkParser(input, expect, 285))
    def test_doWhile18new(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;a = 1.;}while 0=3; do {a= 3<=a=b;}while a; }
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 286))
    def test_doWhile19new(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;a = 1.;}while 0=3; do {a= 3<=a=b;}while a; a=a=b=\n;}
    else {ok;}
}"""
        expect = "Error on line 4 col 0: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 287))
    def test_doWhile20new(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;a = 1.;}while 3=fianfkansk; do {a= 3<=a=b;}while a; a=a=b=\n;}
    else {ok;}
}"""
        expect = "Error on line 4 col 0: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 288))
    def test_doWhile21new(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;a = 1.;}while 3=fianfkansk; u=2;}
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 289))
    def test_doWhile22new(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;a = 1.;}while 3=fianfkansk; continue; u=2;}
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 290))
    def test_doWhile23new(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;a = 1.;}while 3=fianfkansk; u=2;}
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 291))
    def test_doWhile24new(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;a = 1.;}while 3=fianfkansk; u=2;}
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 292))
    def test_doWhile24new(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;a = 1.;}while 3=fianfkansk; u=2;}
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 293))
    def test_doWhile25new(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;a = 1.;}while 3=fianfkansk; u=2;}
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 294))
    def test_doWhile26new(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;a = 1.;} while 3=fianfkansk; break ;u=2;}
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 295))
    def test_doWhile27new(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;a = 1.;}while 2=2; int a,b,c,d; cbcd= fbasjdn;}
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 296))
    def test_doWhile28new(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;do {a;a = 1.;}while a; int a,b,c,d; cbcd= fbasjdn;}
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 297))
    def test_doWhile29new(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;if (a==4){a;}int a,b,c,d; cbcd= fbasjdn;}
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 298))
    def test_doWhile30new(self):
        input = """string NguyenVanHoaiLinh (){
    if (a<2)
    {a;if (a==4){a;}int a,b,c,d; cbcd= adv<3;}
    else {ok;}
}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 299))
    
    
    