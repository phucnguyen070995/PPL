import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
	def test_0(self):
		"""AST_TEST_0"""
		input=""" int a[1];"""
		expect = str(Program([VarDecl("a",ArrayType(1,IntType()))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,300))
	def test_1(self):
		"""AST_TEST_1"""
		input=""" void main(int d){a;}"""
		expect = str(Program([FuncDecl(Id("main"),[VarDecl("d",IntType())],VoidType(),Block([Id("a")]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,301))
	def test_10(self):
		"""AST_TEST_10"""
		input="""
    int am(){
        a = b + c*d;
    }
    """
		expect = str(Program([FuncDecl(Id("am"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("+",Id("b"),BinaryOp("*",Id("c"),Id("d"))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,310))
	def test_11(self):
		"""AST_TEST_11"""
		input=""" 
    void linh(){
        if(a<b) a=b;
    }
    """
		expect = str(Program([FuncDecl(Id("linh"),[],VoidType(),Block([If(BinaryOp("<",Id("a"),Id("b")),BinaryOp("=",Id("a"),Id("b")))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,311))
	def test_12(self):
		"""AST_TEST_12"""
		input="""
    void maxlist(int lst){
        for (i; i<1;i=i+1){
            for (a;a;a){}
        }
    }
    """
		expect = str(Program([FuncDecl(Id("maxlist"),[VarDecl("lst",IntType())],VoidType(),Block([For(Id("i"),BinaryOp("<",Id("i"),IntLiteral(1)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([For(Id("a"),Id("a"),Id("a"),Block([]))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,312))
	def test_13(self):
		"""AST_TEST_13"""
		input="""
    void linh(){
        if(a<b) a=b;
    }
    """
		expect = str(Program([FuncDecl(Id("linh"),[],VoidType(),Block([If(BinaryOp("<",Id("a"),Id("b")),BinaryOp("=",Id("a"),Id("b")))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,313))
	def test_14(self):
		"""AST_TEST_14"""
		input="""
    void l(){ 
        a=(a*b)-c+c/e%q||a;
    }
    """
		expect = str(Program([FuncDecl(Id("l"),[],VoidType(),Block([BinaryOp("=",Id("a"),BinaryOp("||",BinaryOp("+",BinaryOp("-",BinaryOp("*",Id("a"),Id("b")),Id("c")),BinaryOp("%",BinaryOp("/",Id("c"),Id("e")),Id("q"))),Id("a")))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,314))
	def test_15(self):
		"""AST_TEST_15"""
		input="""
    int a,b;
    void main(){

    }
    int a[2];
    """
		expect = str(Program([VarDecl("a",IntType()),VarDecl("b",IntType()),FuncDecl(Id("main"),[],VoidType(),Block([])),VarDecl("a",ArrayType(2,IntType()))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,315))
	def test_16(self):
		"""AST_TEST_16"""
		input="""
    /*bascnsdvnnio2io3n1io2ks*//*assnajnjnfjasndasnj*/
    void main(){}
    """
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,316))
	def test_17(self):
		"""AST_TEST_17"""
		input="""
    void main(){
        break;
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Break()]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,317))
	def test_18(self):
		"""AST_TEST_18"""
		input="""
    void main(){
        break;
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Break()]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,318))
	def test_19(self):
		"""AST_TEST_19"""
		input="""
    int main(){
        Break;
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Id("Break")]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,319))
	def test_2(self):
		"""AST_TEST_2"""
		input=""" int a,b,c,list[3]; """
		expect = str(Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("list",ArrayType(3,IntType()))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,302))
	def test_20(self):
		"""AST_TEST_20"""
		input="""
    int main(){
        countinue;
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Id("countinue")]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,320))
	def test_21(self):
		"""AST_TEST_21"""
		input="""
    int main(){
        continue;
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Continue()]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,321))
	def test_22(self):
		"""AST_TEST_22"""
		input="""
    int main(){
       {{{ continue;}}{a;}}
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Block([Block([Block([Continue()])]),Block([Id("a")])])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,322))
	def test_23(self):
		"""AST_TEST_23"""
		input="""
    int main(){
        if ((a<1))  {c=a+1;}
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("<",Id("a"),IntLiteral(1)),Block([BinaryOp("=",Id("c"),BinaryOp("+",Id("a"),IntLiteral(1)))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,323))
	def test_24(self):
		"""AST_TEST_24"""
		input="""
    int main(){
        if ((a<1))  {c=a+1;}
        else {{{{{{{}}}}}}}
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("<",Id("a"),IntLiteral(1)),Block([BinaryOp("=",Id("c"),BinaryOp("+",Id("a"),IntLiteral(1)))]),Block([Block([Block([Block([Block([Block([Block([])])])])])])]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,324))
	def test_25(self):
		"""AST_TEST_25"""
		input="""
    int main(){
        if ((a<1))  {c=a+1;}
        else 
        if (a) {}
        else {}
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("<",Id("a"),IntLiteral(1)),Block([BinaryOp("=",Id("c"),BinaryOp("+",Id("a"),IntLiteral(1)))]),If(Id("a"),Block([]),Block([])))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,325))
	def test_26(self):
		"""AST_TEST_26"""
		input="""
    int main(){
        if ((a<1))  {c=a+1;}
        else 
        if (a) {}
        else {a+1;}
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("<",Id("a"),IntLiteral(1)),Block([BinaryOp("=",Id("c"),BinaryOp("+",Id("a"),IntLiteral(1)))]),If(Id("a"),Block([]),Block([BinaryOp("+",Id("a"),IntLiteral(1))])))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,326))
	def test_27(self):
		"""AST_TEST_27"""
		input="""
    int man(){
        a = a+1 = b+1;
    }
    """
		expect = str(Program([FuncDecl(Id("man"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("=",BinaryOp("+",Id("a"),IntLiteral(1)),BinaryOp("+",Id("b"),IntLiteral(1))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,327))
	def test_28(self):
		"""AST_TEST_28"""
		input="""
    int man(){
        a|| a && a+1 = b+1;
    }
    """
		expect = str(Program([FuncDecl(Id("man"),[],IntType(),Block([BinaryOp("=",BinaryOp("||",Id("a"),BinaryOp("&&",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))),BinaryOp("+",Id("b"),IntLiteral(1)))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,328))
	def test_29(self):
		"""AST_TEST_29"""
		input="""
    int man(){
        a ---------b;
    }
    """
		expect = str(Program([FuncDecl(Id("man"),[],IntType(),Block([BinaryOp("-",Id("a"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",Id("b"))))))))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,329))
	def test_3(self):
		"""AST_TEST_3"""
		input="""int b[1], c;
        float c; 
        string k; 
        boolean n;
    """
		expect = str(Program([VarDecl("b",ArrayType(1,IntType())),VarDecl("c",IntType()),VarDecl("c",FloatType()),VarDecl("k",StringType()),VarDecl("n",BoolType())]))
		self.assertTrue(TestAST.checkASTGen(input,expect,303))
	def test_30(self):
		"""AST_TEST_30"""
		input="""
    int man(){
        a[1] -b[n];
    }
    """
		expect = str(Program([FuncDecl(Id("man"),[],IntType(),Block([BinaryOp("-",ArrayCell(Id("a"),IntLiteral(1)),ArrayCell(Id("b"),Id("n")))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,330))
	def test_31(self):
		"""AST_TEST_31"""
		input="""
    int man(){
        a[1] -b[n];
        call();
        pull();
    }
    """
		expect = str(Program([FuncDecl(Id("man"),[],IntType(),Block([BinaryOp("-",ArrayCell(Id("a"),IntLiteral(1)),ArrayCell(Id("b"),Id("n"))),CallExpr(Id("call"),[]),CallExpr(Id("pull"),[])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,331))
	def test_32(self):
		"""AST_TEST_32"""
		input="""
    int man(){
        call();
        pull();
    }
    """
		expect = str(Program([FuncDecl(Id("man"),[],IntType(),Block([CallExpr(Id("call"),[]),CallExpr(Id("pull"),[])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,332))
	def test_33(self):
		"""AST_TEST_33"""
		input="""
    int man(){
        do a;
        b;
        c;
        d;
        while(cc);
    }
    """
		expect = str(Program([FuncDecl(Id("man"),[],IntType(),Block([Dowhile([Id("a"),Id("b"),Id("c"),Id("d")],Id("cc"))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,333))
	def test_34(self):
		"""AST_TEST_34"""
		input="""
    int man(){
        {}{}{}{a;}
    }
    """
		expect = str(Program([FuncDecl(Id("man"),[],IntType(),Block([Block([]),Block([]),Block([]),Block([Id("a")])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,334))
	def test_35(self):
		"""AST_TEST_35"""
		input="""
    int man(){
        return ;
    }
    """
		expect = str(Program([FuncDecl(Id("man"),[],IntType(),Block([Return()]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,335))
	def test_36(self):
		"""AST_TEST_36"""
		input="""
    int man(){
        return a= 1 ;
    }
    """
		expect = str(Program([FuncDecl(Id("man"),[],IntType(),Block([Return(BinaryOp("=",Id("a"),IntLiteral(1)))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,336))
	def test_37(self):
		"""AST_TEST_37"""
		input="""
    int man(){
        return "a" ;
    }
    """
		expect = str(Program([FuncDecl(Id("man"),[],IntType(),Block([Return(StringLiteral("a"))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,337))
	def test_38(self):
		"""AST_TEST_38"""
		input="""
    int A1man(){
        return "a" ;
    }
    """
		expect = str(Program([FuncDecl(Id("A1man"),[],IntType(),Block([Return(StringLiteral("a"))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,338))
	def test_39(self):
		"""AST_TEST_39"""
		input="""
    int A1man(){
        return "a" ;
        {
            a;b;v;
        }
    }
    """
		expect = str(Program([FuncDecl(Id("A1man"),[],IntType(),Block([Return(StringLiteral("a")),Block([Id("a"),Id("b"),Id("v")])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,339))
	def test_4(self):
		"""AST_TEST_4"""
		input="""
    int m,n;
    void a(int b, string c){}
    """
		expect = str(Program([VarDecl("m",IntType()),VarDecl("n",IntType()),FuncDecl(Id("a"),[VarDecl("b",IntType()),VarDecl("c",StringType())],VoidType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,304))
	def test_40(self):
		"""AST_TEST_40"""
		input="""
    int A1man(int b,string cc){
        return "a" ;
    }
    """
		expect = str(Program([FuncDecl(Id("A1man"),[VarDecl("b",IntType()),VarDecl("cc",StringType())],IntType(),Block([Return(StringLiteral("a"))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,340))
	def test_41(self):
		"""AST_TEST_41"""
		input="""
    int main(int b,string cc){
        return true ;
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[VarDecl("b",IntType()),VarDecl("cc",StringType())],IntType(),Block([Return(BooleanLiteral(True))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,341))
	def test_42(self):
		"""AST_TEST_42"""
		input="""
    int main(int b,string cc){
        return false ;
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[VarDecl("b",IntType()),VarDecl("cc",StringType())],IntType(),Block([Return(BooleanLiteral(False))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,342))
	def test_43(self):
		"""AST_TEST_43"""
		input="""
    int main(int b,string cc){
        return false ;
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[VarDecl("b",IntType()),VarDecl("cc",StringType())],IntType(),Block([Return(BooleanLiteral(False))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,343))
	def test_44(self):
		"""AST_TEST_44"""
		input="""
    int main(int b,string cc[]){
        return false ;
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[VarDecl("b",IntType()),VarDecl("cc",ArrayPointerType(StringType()))],IntType(),Block([Return(BooleanLiteral(False))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,344))
	def test_45(self):
		"""AST_TEST_45"""
		input="""
    int main(int b,string cc[]){
        int  a [1];
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[VarDecl("b",IntType()),VarDecl("cc",ArrayPointerType(StringType()))],IntType(),Block([VarDecl("a",ArrayType(1,IntType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,345))
	def test_46(self):
		"""AST_TEST_46"""
		input="""
    int main(){
        d+e;
        a+c;
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("+",Id("d"),Id("e")),BinaryOp("+",Id("a"),Id("c"))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,346))
	def test_47(self):
		"""AST_TEST_47"""
		input="""
    int main(){
        d+e;a+c;
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("+",Id("d"),Id("e")),BinaryOp("+",Id("a"),Id("c"))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,347))
	def test_48(self):
		"""AST_TEST_48"""
		input="""
    int man(){
        do a;
        b;
        c;
        d;
        while(cc);
    }
    """
		expect = str(Program([FuncDecl(Id("man"),[],IntType(),Block([Dowhile([Id("a"),Id("b"),Id("c"),Id("d")],Id("cc"))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,348))
	def test_49(self):
		"""AST_TEST_49"""
		input="""
    int man(){
        do a;
        b;
        c;
        d;
        while(cc); 
        do a;
        do a; b; c;d;while a;while a;
    }
    """
		expect = str(Program([FuncDecl(Id("man"),[],IntType(),Block([Dowhile([Id("a"),Id("b"),Id("c"),Id("d")],Id("cc")),Dowhile([Id("a"),Dowhile([Id("a"),Id("b"),Id("c"),Id("d")],Id("a"))],Id("a"))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,349))
	def test_5(self):
		"""AST_TEST_5"""
		input="""
    void call(){ print("a"); }
    void main(){
        call();  // this is call functions
    }
    """
		expect = str(Program([FuncDecl(Id("call"),[],VoidType(),Block([CallExpr(Id("print"),[StringLiteral("a")])])),FuncDecl(Id("main"),[],VoidType(),Block([CallExpr(Id("call"),[])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,305))
	def test_50(self):
		"""AST_TEST_50"""
		input="""
    void  main(){
    if (a<c||a =c) {}
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("=",BinaryOp("||",BinaryOp("<",Id("a"),Id("c")),Id("a")),Id("c")),Block([]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,350))
	def test_51(self):
		"""AST_TEST_51"""
		input="""
    void main(){
        break; break; continue;
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Break(),Break(),Continue()]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,351))
	def test_52(self):
		"""AST_TEST_52"""
		input="""
    void main(){
        for(a;b;c){}
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(Id("a"),Id("b"),Id("c"),Block([]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,352))
	def test_53(self):
		"""AST_TEST_53"""
		input="""
    void main(){
        if(a<a=b<c){

        }
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("=",BinaryOp("<",Id("a"),Id("a")),BinaryOp("<",Id("b"),Id("c"))),Block([]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,353))
	def test_54(self):
		"""AST_TEST_54"""
		input="""
    void main(){
        if(!a=a=bc){

        }
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("=",UnaryOp("!",Id("a")),BinaryOp("=",Id("a"),Id("bc"))),Block([]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,354))
	def test_55(self):
		"""AST_TEST_55"""
		input="""
    void main(){
        if(true = false){

        }
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("=",BooleanLiteral(True),BooleanLiteral(False)),Block([]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,355))
	def test_56(self):
		"""AST_TEST_56"""
		input="""
    void main(){
        if(true = false){
            true + False;
        }
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("=",BooleanLiteral(True),BooleanLiteral(False)),Block([BinaryOp("+",BooleanLiteral(True),Id("False"))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,356))
	def test_57(self):
		"""AST_TEST_57"""
		input="""
    void main(){
        if(true = false){
			true + False;
        }
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("=",BooleanLiteral(True),BooleanLiteral(False)),Block([BinaryOp("+",BooleanLiteral(True),Id("False"))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,357))
	def test_58(self):
		"""AST_TEST_58"""
		input="""
    void main(){
        if(true = false){
        !a + b-    iCallYou(calyou(a));
        }
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("=",BooleanLiteral(True),BooleanLiteral(False)),Block([BinaryOp("-",BinaryOp("+",UnaryOp("!",Id("a")),Id("b")),CallExpr(Id("iCallYou"),[CallExpr(Id("calyou"),[Id("a")])]))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,358))
	def test_59(self):
		"""AST_TEST_59"""
		input="""
    void main(){
        if(true = false){
            if(a){}else{a;}
        }
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("=",BooleanLiteral(True),BooleanLiteral(False)),Block([If(Id("a"),Block([]),Block([Id("a")]))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,359))
	def test_6(self):
		"""AST_TEST_6"""
		input="""
    // 1710169 
    /*my assignment 2*/
    void main(int a, string b){
        do {}{}{}
        while (1);
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[VarDecl("a",IntType()),VarDecl("b",StringType())],VoidType(),Block([Dowhile([Block([]),Block([]),Block([])],IntLiteral(1))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,306))
	def test_60(self):
		"""AST_TEST_60"""
		input="""
    void main(){
        a = true;
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("a"),BooleanLiteral(True))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,360))
	def test_61(self):
		"""AST_TEST_61"""
		input="""
    void main(){
        b= e= true = fals;
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([BinaryOp("=",Id("b"),BinaryOp("=",Id("e"),BinaryOp("=",BooleanLiteral(True),Id("fals"))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,361))
	def test_62(self):
		"""AST_TEST_62"""
		input="""
    void maxlist(int lst){
        for (i; i<1;i=i+1){
            for (a;a;a){}
        }
    }
    """
		expect = str(Program([FuncDecl(Id("maxlist"),[VarDecl("lst",IntType())],VoidType(),Block([For(Id("i"),BinaryOp("<",Id("i"),IntLiteral(1)),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([For(Id("a"),Id("a"),Id("a"),Block([]))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,362))
	def test_63(self):
		"""AST_TEST_63"""
		input="""
    void linh(){
        if(a<b) a=b;
    }
    """
		expect = str(Program([FuncDecl(Id("linh"),[],VoidType(),Block([If(BinaryOp("<",Id("a"),Id("b")),BinaryOp("=",Id("a"),Id("b")))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,363))
	def test_64(self):
		"""AST_TEST_64"""
		input="""
    void l(){ 
        a=(a*b)-c+c/e%q||a;
    }
    """
		expect = str(Program([FuncDecl(Id("l"),[],VoidType(),Block([BinaryOp("=",Id("a"),BinaryOp("||",BinaryOp("+",BinaryOp("-",BinaryOp("*",Id("a"),Id("b")),Id("c")),BinaryOp("%",BinaryOp("/",Id("c"),Id("e")),Id("q"))),Id("a")))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,364))
	def test_65(self):
		"""AST_TEST_65"""
		input="""
    int a,b;
    void main(){

    }
    int a[2];
    """
		expect = str(Program([VarDecl("a",IntType()),VarDecl("b",IntType()),FuncDecl(Id("main"),[],VoidType(),Block([])),VarDecl("a",ArrayType(2,IntType()))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,365))
	def test_66(self):
		"""AST_TEST_66"""
		input="""
    /*bascnsdvnnio2io3n1io2ks*//*assnajnjnfjasndasnj*/
    void main(){}
    """
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,366))
	def test_67(self):
		"""AST_TEST_67"""
		input="""
    void main(){
        break;
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Break()]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,367))
	def test_68(self):
		"""AST_TEST_68"""
		input="""
    void main(){
        break;
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([Break()]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,368))
	def test_69(self):
		"""AST_TEST_69"""
		input="""
    int main(){
        Break;
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Id("Break")]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,369))
	def test_7(self):
		"""AST_TEST_7"""
		input="""
    void a(){}
    int b(){}
    string c(){}
    float d(){//
    }
    """
		expect = str(Program([FuncDecl(Id("a"),[],VoidType(),Block([])),FuncDecl(Id("b"),[],IntType(),Block([])),FuncDecl(Id("c"),[],StringType(),Block([])),FuncDecl(Id("d"),[],FloatType(),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,307))
	def test_70(self):
		"""AST_TEST_70"""
		input="""
    int main(){
        countinue;
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Id("countinue")]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,370))
	def test_71(self):
		"""AST_TEST_71"""
		input="""
    int main(){
        continue;
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Continue()]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,371))
	def test_72(self):
		"""AST_TEST_72"""
		input="""
    int main(){
       {{{ continue;}}{a;}}
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Block([Block([Block([Continue()])]),Block([Id("a")])])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,372))
	def test_73(self):
		"""AST_TEST_73"""
		input="""
    int main(){
        if ((a<1))  {c=a+1;}
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("<",Id("a"),IntLiteral(1)),Block([BinaryOp("=",Id("c"),BinaryOp("+",Id("a"),IntLiteral(1)))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,373))
	def test_74(self):
		"""AST_TEST_74"""
		input="""
    int main(){
        if ((a<1))  {c=a+1;}
        else {{{{{{{}}}}}}}
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("<",Id("a"),IntLiteral(1)),Block([BinaryOp("=",Id("c"),BinaryOp("+",Id("a"),IntLiteral(1)))]),Block([Block([Block([Block([Block([Block([Block([])])])])])])]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,374))
	def test_75(self):
		"""AST_TEST_75"""
		input="""
    int main(){
        if ((a<1))  {c=a+1;}
        else 
        if (a) {}
        else {}
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("<",Id("a"),IntLiteral(1)),Block([BinaryOp("=",Id("c"),BinaryOp("+",Id("a"),IntLiteral(1)))]),If(Id("a"),Block([]),Block([])))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,375))
	def test_76(self):
		"""AST_TEST_76"""
		input="""
    int main(){
        if ((a<1))  {c=a+1;}
        else 
        if (a) {}
        else {a+1;}
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("<",Id("a"),IntLiteral(1)),Block([BinaryOp("=",Id("c"),BinaryOp("+",Id("a"),IntLiteral(1)))]),If(Id("a"),Block([]),Block([BinaryOp("+",Id("a"),IntLiteral(1))])))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,376))
	def test_77(self):
		"""AST_TEST_77"""
		input="""
    int man(){
        a = a+1 = b+1;
    }
    """
		expect = str(Program([FuncDecl(Id("man"),[],IntType(),Block([BinaryOp("=",Id("a"),BinaryOp("=",BinaryOp("+",Id("a"),IntLiteral(1)),BinaryOp("+",Id("b"),IntLiteral(1))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,377))
	def test_78(self):
		"""AST_TEST_78"""
		input="""
    int man(){
        a|| a && a+1 = b+1;
    }
    """
		expect = str(Program([FuncDecl(Id("man"),[],IntType(),Block([BinaryOp("=",BinaryOp("||",Id("a"),BinaryOp("&&",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))),BinaryOp("+",Id("b"),IntLiteral(1)))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,378))
	def test_79(self):
		"""AST_TEST_79"""
		input="""
    int man(){
        a ---------b;
    }
    """
		expect = str(Program([FuncDecl(Id("man"),[],IntType(),Block([BinaryOp("-",Id("a"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("-",Id("b"))))))))))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,379))
	def test_8(self):
		"""AST_TEST_8"""
		input="""
    int a; int[] main(int a[], boolean b){}
    """
		expect = str(Program([VarDecl("a",IntType()),FuncDecl(Id("main"),[VarDecl("a",ArrayPointerType(IntType())),VarDecl("b",BoolType())],ArrayPointerType(IntType()),Block([]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,308))
	def test_80(self):
		"""AST_TEST_80"""
		input="""
    int man(){
        a[1] -b[n];
    }
    """
		expect = str(Program([FuncDecl(Id("man"),[],IntType(),Block([BinaryOp("-",ArrayCell(Id("a"),IntLiteral(1)),ArrayCell(Id("b"),Id("n")))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,380))
	def test_81(self):
		"""AST_TEST_81"""
		input="""
    int man(){
        a[1] -b[n];
        call();
        pull();
    }
    """
		expect = str(Program([FuncDecl(Id("man"),[],IntType(),Block([BinaryOp("-",ArrayCell(Id("a"),IntLiteral(1)),ArrayCell(Id("b"),Id("n"))),CallExpr(Id("call"),[]),CallExpr(Id("pull"),[])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,381))
	def test_82(self):
		"""AST_TEST_82"""
		input="""
    int man(){
        call();
        pull();
    }
    """
		expect = str(Program([FuncDecl(Id("man"),[],IntType(),Block([CallExpr(Id("call"),[]),CallExpr(Id("pull"),[])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,382))
	def test_83(self):
		"""AST_TEST_83"""
		input="""
    int man(){
        do a;
        b;
        c;
        d;
        while(cc);
    }
    """
		expect = str(Program([FuncDecl(Id("man"),[],IntType(),Block([Dowhile([Id("a"),Id("b"),Id("c"),Id("d")],Id("cc"))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,383))
	def test_84(self):
		"""AST_TEST_84"""
		input="""
    int man(){
        {}{}{}{a;}
    }
    """
		expect = str(Program([FuncDecl(Id("man"),[],IntType(),Block([Block([]),Block([]),Block([]),Block([Id("a")])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,384))
	def test_85(self):
		"""AST_TEST_85"""
		input="""
    int man(){
        return ;
    }
    """
		expect = str(Program([FuncDecl(Id("man"),[],IntType(),Block([Return()]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,385))
	def test_86(self):
		"""AST_TEST_86"""
		input="""
    int man(){
        return a= 1 ;
    }
    """
		expect = str(Program([FuncDecl(Id("man"),[],IntType(),Block([Return(BinaryOp("=",Id("a"),IntLiteral(1)))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,386))
	def test_87(self):
		"""AST_TEST_87"""
		input="""
    int man(){
        return "a" ;
    }
    """
		expect = str(Program([FuncDecl(Id("man"),[],IntType(),Block([Return(StringLiteral("a"))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,387))
	def test_88(self):
		"""AST_TEST_88"""
		input="""
    int A1man(){
        return "a" ;
    }
    """
		expect = str(Program([FuncDecl(Id("A1man"),[],IntType(),Block([Return(StringLiteral("a"))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,388))
	def test_89(self):
		"""AST_TEST_89"""
		input="""
    int A1man(){
        return "a" ;
        {
            a;b;v;
        }
    }
    """
		expect = str(Program([FuncDecl(Id("A1man"),[],IntType(),Block([Return(StringLiteral("a")),Block([Id("a"),Id("b"),Id("v")])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,389))
	def test_9(self):
		"""AST_TEST_9"""
		input="""
    int main(){do {{{}}} while 1;}
    """
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([Block([Block([])])])],IntLiteral(1))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,309))
	def test_90(self):
		"""AST_TEST_90"""
		input="""
    int A1man(int b,string cc){
        return "a" ;
    }
    """
		expect = str(Program([FuncDecl(Id("A1man"),[VarDecl("b",IntType()),VarDecl("cc",StringType())],IntType(),Block([Return(StringLiteral("a"))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,390))
	def test_91(self):
		"""AST_TEST_91"""
		input="""
    int main(int b,string cc){
        return true ;
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[VarDecl("b",IntType()),VarDecl("cc",StringType())],IntType(),Block([Return(BooleanLiteral(True))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,391))
	def test_92(self):
		"""AST_TEST_92"""
		input="""
    int main(int b,string cc){
        return false ;
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[VarDecl("b",IntType()),VarDecl("cc",StringType())],IntType(),Block([Return(BooleanLiteral(False))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,392))
	def test_93(self):
		"""AST_TEST_93"""
		input="""
    int main(int b,string cc){
        return false ;
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[VarDecl("b",IntType()),VarDecl("cc",StringType())],IntType(),Block([Return(BooleanLiteral(False))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,393))
	def test_94(self):
		"""AST_TEST_94"""
		input="""
    int main(int b,string cc[]){
        return false ;
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[VarDecl("b",IntType()),VarDecl("cc",ArrayPointerType(StringType()))],IntType(),Block([Return(BooleanLiteral(False))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,394))
	def test_95(self):
		"""AST_TEST_95"""
		input="""
    int main(int b,string cc[]){
        int  a [1];
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[VarDecl("b",IntType()),VarDecl("cc",ArrayPointerType(StringType()))],IntType(),Block([VarDecl("a",ArrayType(1,IntType()))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,395))
	def test_96(self):
		"""AST_TEST_96"""
		input="""
    int main(){
        d+e;
        a+c;
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("+",Id("d"),Id("e")),BinaryOp("+",Id("a"),Id("c"))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,396))
	def test_97(self):
		"""AST_TEST_97"""
		input="""
    int main(){
        if (a<a=b){
            if(a){}else{if(a){}}
        }
        else{
            do a;b;c;while(c);
        }
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("=",BinaryOp("<",Id("a"),Id("a")),Id("b")),Block([If(Id("a"),Block([]),Block([If(Id("a"),Block([]))]))]),Block([Dowhile([Id("a"),Id("b"),Id("c")],Id("c"))]))]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,397))
	def test_98(self):
		"""AST_TEST_98"""
		input="""
    int main(){
        if (a<a=b){
            if(a){}else{if(a){}}
        }
    }
    boolean b(){
        check = true; 
        callme(); 
        println();
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("=",BinaryOp("<",Id("a"),Id("a")),Id("b")),Block([If(Id("a"),Block([]),Block([If(Id("a"),Block([]))]))]))])),FuncDecl(Id("b"),[],BoolType(),Block([BinaryOp("=",Id("check"),BooleanLiteral(True)),CallExpr(Id("callme"),[]),CallExpr(Id("println"),[])]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,398))
	def test_99(self):
		"""AST_TEST_99"""
		input="""
    int main(){
        int a[3], b; 
        float c;
        string u;
    }
    """
		expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("a",ArrayType(3,IntType())),VarDecl("b",IntType()),VarDecl("c",FloatType()),VarDecl("u",StringType())]))]))
		self.assertTrue(TestAST.checkASTGen(input,expect,399))