import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
		def test_0(self):
		"""AST_TEST_0"""
		input=""" int a[1];"""
		Program([VarDecl(a,ArrayType(IntType,1))])
		self.assertTrue(TestAST.checkASTGen(input,expect,300))
	def test_1(self):
		"""AST_TEST_1"""
		input=""" void main(int d){a;}"""
		Program([FuncDecl(Id(main),[VarDecl(d,IntType)],VoidType,Block([Id(a)]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,301))
	def test_10(self):
		"""AST_TEST_10"""
		input="""
    int am(){
        a = b + c*d;
    }
    """
		Program([FuncDecl(Id(am),[],IntType,Block([BinaryOp(=,Id(a),BinaryOp(+,Id(b),BinaryOp(*,Id(c),Id(d))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,310))
	def test_11(self):
		"""AST_TEST_11"""
		input=""" 
    void linh(){
        if(a<b) a=b;
    }
    """
		Program([FuncDecl(Id(linh),[],VoidType,Block([If(BinaryOp(<,Id(a),Id(b)),BinaryOp(=,Id(a),Id(b)))]))])
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
		Program([FuncDecl(Id(maxlist),[VarDecl(lst,IntType)],VoidType,Block([For(Id(i);BinaryOp(<,Id(i),IntLiteral(1));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([For(Id(a);Id(a);Id(a);Block([]))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,312))
	def test_13(self):
		"""AST_TEST_13"""
		input="""
    void linh(){
        if(a<b) a=b;
    }
    """
		Program([FuncDecl(Id(linh),[],VoidType,Block([If(BinaryOp(<,Id(a),Id(b)),BinaryOp(=,Id(a),Id(b)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,313))
	def test_14(self):
		"""AST_TEST_14"""
		input="""
    void l(){ 
        a=(a*b)-c+c/e%q||a;
    }
    """
		Program([FuncDecl(Id(l),[],VoidType,Block([BinaryOp(=,Id(a),BinaryOp(||,BinaryOp(+,BinaryOp(-,BinaryOp(*,Id(a),Id(b)),Id(c)),BinaryOp(%,BinaryOp(/,Id(c),Id(e)),Id(q))),Id(a)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,314))
	def test_15(self):
		"""AST_TEST_15"""
		input="""
    int a,b;
    void main(){

    }
    int a[2];
    """
		Program([VarDecl(a,IntType),VarDecl(b,IntType),FuncDecl(Id(main),[],VoidType,Block([])),VarDecl(a,ArrayType(IntType,2))])
		self.assertTrue(TestAST.checkASTGen(input,expect,315))
	def test_16(self):
		"""AST_TEST_16"""
		input="""
    /*bascnsdvnnio2io3n1io2ks*//*assnajnjnfjasndasnj*/
    void main(){}
    """
		Program([FuncDecl(Id(main),[],VoidType,Block([]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,316))
	def test_17(self):
		"""AST_TEST_17"""
		input="""
    void main(){
        break;
    }
    """
		Program([FuncDecl(Id(main),[],VoidType,Block([Break()]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,317))
	def test_18(self):
		"""AST_TEST_18"""
		input="""
    void main(){
        break;
    }
    """
		Program([FuncDecl(Id(main),[],VoidType,Block([Break()]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,318))
	def test_19(self):
		"""AST_TEST_19"""
		input="""
    int main(){
        Break;
    }
    """
		Program([FuncDecl(Id(main),[],IntType,Block([Id(Break)]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,319))
	def test_2(self):
		"""AST_TEST_2"""
		input=""" int a,b,c,list[3]; """
		Program([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,IntType),VarDecl(list,ArrayType(IntType,3))])
		self.assertTrue(TestAST.checkASTGen(input,expect,302))
	def test_20(self):
		"""AST_TEST_20"""
		input="""
    int main(){
        countinue;
    }
    """
		Program([FuncDecl(Id(main),[],IntType,Block([Id(countinue)]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,320))
	def test_21(self):
		"""AST_TEST_21"""
		input="""
    int main(){
        continue;
    }
    """
		Program([FuncDecl(Id(main),[],IntType,Block([Continue()]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,321))
	def test_22(self):
		"""AST_TEST_22"""
		input="""
    int main(){
       {{{ continue;}}{a;}}
    }
    """
		Program([FuncDecl(Id(main),[],IntType,Block([Block([Block([Block([Continue()])]),Block([Id(a)])])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,322))
	def test_23(self):
		"""AST_TEST_23"""
		input="""
    int main(){
        if ((a<1))  {c=a+1;}
    }
    """
		Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(<,Id(a),IntLiteral(1)),Block([BinaryOp(=,Id(c),BinaryOp(+,Id(a),IntLiteral(1)))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,323))
	def test_24(self):
		"""AST_TEST_24"""
		input="""
    int main(){
        if ((a<1))  {c=a+1;}
        else {{{{{{{}}}}}}}
    }
    """
		Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(<,Id(a),IntLiteral(1)),Block([BinaryOp(=,Id(c),BinaryOp(+,Id(a),IntLiteral(1)))]),Block([Block([Block([Block([Block([Block([Block([])])])])])])]))]))])
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
		Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(<,Id(a),IntLiteral(1)),Block([BinaryOp(=,Id(c),BinaryOp(+,Id(a),IntLiteral(1)))]),If(Id(a),Block([]),Block([])))]))])
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
		Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(<,Id(a),IntLiteral(1)),Block([BinaryOp(=,Id(c),BinaryOp(+,Id(a),IntLiteral(1)))]),If(Id(a),Block([]),Block([BinaryOp(+,Id(a),IntLiteral(1))])))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,326))
	def test_27(self):
		"""AST_TEST_27"""
		input="""
    int man(){
        a = a+1 = b+1;
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([BinaryOp(=,Id(a),BinaryOp(=,BinaryOp(+,Id(a),IntLiteral(1)),BinaryOp(+,Id(b),IntLiteral(1))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,327))
	def test_28(self):
		"""AST_TEST_28"""
		input="""
    int man(){
        a|| a && a+1 = b+1;
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([BinaryOp(=,BinaryOp(||,Id(a),BinaryOp(&&,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))),BinaryOp(+,Id(b),IntLiteral(1)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,328))
	def test_29(self):
		"""AST_TEST_29"""
		input="""
    int man(){
        a ---------b;
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([BinaryOp(-,Id(a),UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,Id(b))))))))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,329))
	def test_3(self):
		"""AST_TEST_3"""
		input="""int b[1], c;
        float c; 
        string k; 
        boolean n;
    """
		Program([VarDecl(b,ArrayType(IntType,1)),VarDecl(c,IntType),VarDecl(c,FloatType),VarDecl(k,StringType),VarDecl(n,BoolType)])
		self.assertTrue(TestAST.checkASTGen(input,expect,303))
	def test_30(self):
		"""AST_TEST_30"""
		input="""
    int man(){
        a[1] -b[n];
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([BinaryOp(-,ArrayCell(Id(a),IntLiteral(1)),ArrayCell(Id(b),Id(n)))]))])
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
		Program([FuncDecl(Id(man),[],IntType,Block([BinaryOp(-,ArrayCell(Id(a),IntLiteral(1)),ArrayCell(Id(b),Id(n))),CallExpr(Id(call),[]),CallExpr(Id(pull),[])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,331))
	def test_32(self):
		"""AST_TEST_32"""
		input="""
    int man(){
        call();
        pull();
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([CallExpr(Id(call),[]),CallExpr(Id(pull),[])]))])
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
		Program([FuncDecl(Id(man),[],IntType,Block([Dowhile([Id(a),Id(b),Id(c),Id(d)],Id(cc))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,333))
	def test_34(self):
		"""AST_TEST_34"""
		input="""
    int man(){
        {}{}{}{a;}
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([Block([]),Block([]),Block([]),Block([Id(a)])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,334))
	def test_35(self):
		"""AST_TEST_35"""
		input="""
    int man(){
        return ;
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([Return()]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,335))
	def test_36(self):
		"""AST_TEST_36"""
		input="""
    int man(){
        return a= 1 ;
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([Return(BinaryOp(=,Id(a),IntLiteral(1)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,336))
	def test_37(self):
		"""AST_TEST_37"""
		input="""
    int man(){
        return "a" ;
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([Return(StringLiteral(a))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,337))
	def test_38(self):
		"""AST_TEST_38"""
		input="""
    int A1man(){
        return "a" ;
    }
    """
		Program([FuncDecl(Id(A1man),[],IntType,Block([Return(StringLiteral(a))]))])
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
		Program([FuncDecl(Id(A1man),[],IntType,Block([Return(StringLiteral(a)),Block([Id(a),Id(b),Id(v)])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,339))
	def test_4(self):
		"""AST_TEST_4"""
		input="""
    int m,n;
    void a(int b, string c){}
    """
		Program([VarDecl(m,IntType),VarDecl(n,IntType),FuncDecl(Id(a),[VarDecl(b,IntType),VarDecl(c,StringType)],VoidType,Block([]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,304))
	def test_40(self):
		"""AST_TEST_40"""
		input="""
    int A1man(int b,string cc){
        return "a" ;
    }
    """
		Program([FuncDecl(Id(A1man),[VarDecl(b,IntType),VarDecl(cc,StringType)],IntType,Block([Return(StringLiteral(a))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,340))
	def test_41(self):
		"""AST_TEST_41"""
		input="""
    int main(int b,string cc){
        return true ;
    }
    """
		Program([FuncDecl(Id(main),[VarDecl(b,IntType),VarDecl(cc,StringType)],IntType,Block([Return(BooleanLiteral(true))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,341))
	def test_42(self):
		"""AST_TEST_42"""
		input="""
    int main(int b,string cc){
        return false ;
    }
    """
		Program([FuncDecl(Id(main),[VarDecl(b,IntType),VarDecl(cc,StringType)],IntType,Block([Return(BooleanLiteral(false))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,342))
	def test_43(self):
		"""AST_TEST_43"""
		input="""
    int main(int b,string cc){
        return false ;
    }
    """
		Program([FuncDecl(Id(main),[VarDecl(b,IntType),VarDecl(cc,StringType)],IntType,Block([Return(BooleanLiteral(false))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,343))
	def test_44(self):
		"""AST_TEST_44"""
		input="""
    int main(int b,string cc[]){
        return false ;
    }
    """
		Program([FuncDecl(Id(main),[VarDecl(b,IntType),VarDecl(cc,ArrayTypePointer(StringType))],IntType,Block([Return(BooleanLiteral(false))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,344))
	def test_45(self):
		"""AST_TEST_45"""
		input="""
    int main(int b,string cc[]){
        int  a [1];
    }
    """
		Program([FuncDecl(Id(main),[VarDecl(b,IntType),VarDecl(cc,ArrayTypePointer(StringType))],IntType,Block([VarDecl(a,ArrayType(IntType,1))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,345))
	def test_46(self):
		"""AST_TEST_46"""
		input="""
    int main(){
        d+e;
        a+c;
    }
    """
		Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(+,Id(d),Id(e)),BinaryOp(+,Id(a),Id(c))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,346))
	def test_47(self):
		"""AST_TEST_47"""
		input="""
    int main(){
        d+e;a+c;
    }
    """
		Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(+,Id(d),Id(e)),BinaryOp(+,Id(a),Id(c))]))])
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
		Program([FuncDecl(Id(man),[],IntType,Block([Dowhile([Id(a),Id(b),Id(c),Id(d)],Id(cc))]))])
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
		Program([FuncDecl(Id(man),[],IntType,Block([Dowhile([Id(a),Id(b),Id(c),Id(d)],Id(cc)),Dowhile([Id(a),Dowhile([Id(a),Id(b),Id(c),Id(d)],Id(a))],Id(a))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,349))
	def test_5(self):
		"""AST_TEST_5"""
		input="""
    void call(){ print("a"); }
    void main(){
        call();  // this is call functions
    }
    """
		Program([FuncDecl(Id(call),[],VoidType,Block([CallExpr(Id(print),[StringLiteral(a)])])),FuncDecl(Id(main),[],VoidType,Block([CallExpr(Id(call),[])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,305))
	def test_50(self):
		"""AST_TEST_50"""
		input="""
    void  main(){
    if (a<c||a =c) {}
    }
    """
		Program([FuncDecl(Id(main),[],VoidType,Block([If(BinaryOp(=,BinaryOp(||,BinaryOp(<,Id(a),Id(c)),Id(a)),Id(c)),Block([]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,350))
	def test_51(self):
		"""AST_TEST_51"""
		input="""
    void main(){
        break; break; continue;
    }
    """
		Program([FuncDecl(Id(main),[],VoidType,Block([Break(),Break(),Continue()]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,351))
	def test_52(self):
		"""AST_TEST_52"""
		input="""
    void main(){
        for(a;b;c){}
    }
    """
		Program([FuncDecl(Id(main),[],VoidType,Block([For(Id(a);Id(b);Id(c);Block([]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,352))
	def test_53(self):
		"""AST_TEST_53"""
		input="""
    void main(){
        if(a<a=b<c){

        }
    }
    """
		Program([FuncDecl(Id(main),[],VoidType,Block([If(BinaryOp(=,BinaryOp(<,Id(a),Id(a)),BinaryOp(<,Id(b),Id(c))),Block([]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,353))
	def test_54(self):
		"""AST_TEST_54"""
		input="""
    void main(){
        if(!a=a=bc){

        }
    }
    """
		Program([FuncDecl(Id(main),[],VoidType,Block([If(BinaryOp(=,UnaryOp(!,Id(a)),BinaryOp(=,Id(a),Id(bc))),Block([]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,354))
	def test_55(self):
		"""AST_TEST_55"""
		input="""
    void main(){
        if(true = false){

        }
    }
    """
		Program([FuncDecl(Id(main),[],VoidType,Block([If(BinaryOp(=,BooleanLiteral(true),BooleanLiteral(false)),Block([]))]))])
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
		Program([FuncDecl(Id(main),[],VoidType,Block([If(BinaryOp(=,BooleanLiteral(true),BooleanLiteral(false)),Block([BinaryOp(+,BooleanLiteral(true),Id(False))]))]))])
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
		Program([FuncDecl(Id(main),[],VoidType,Block([If(BinaryOp(=,BooleanLiteral(true),BooleanLiteral(false)),Block([BinaryOp(+,BooleanLiteral(true),Id(False))]))]))])
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
		Program([FuncDecl(Id(main),[],VoidType,Block([If(BinaryOp(=,BooleanLiteral(true),BooleanLiteral(false)),Block([BinaryOp(-,BinaryOp(+,UnaryOp(!,Id(a)),Id(b)),CallExpr(Id(iCallYou),[CallExpr(Id(calyou),[Id(a)])]))]))]))])
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
		Program([FuncDecl(Id(main),[],VoidType,Block([If(BinaryOp(=,BooleanLiteral(true),BooleanLiteral(false)),Block([If(Id(a),Block([]),Block([Id(a)]))]))]))])
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
		Program([FuncDecl(Id(main),[VarDecl(a,IntType),VarDecl(b,StringType)],VoidType,Block([Dowhile([Block([]),Block([]),Block([])],IntLiteral(1))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,306))
	def test_60(self):
		"""AST_TEST_60"""
		input="""
    void main(){
        a = true;
    }
    """
		Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),BooleanLiteral(true))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,360))
	def test_61(self):
		"""AST_TEST_61"""
		input="""
    void main(){
        b= e= true = fals;
    }
    """
		Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(b),BinaryOp(=,Id(e),BinaryOp(=,BooleanLiteral(true),Id(fals))))]))])
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
		Program([FuncDecl(Id(maxlist),[VarDecl(lst,IntType)],VoidType,Block([For(Id(i);BinaryOp(<,Id(i),IntLiteral(1));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([For(Id(a);Id(a);Id(a);Block([]))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,362))
	def test_63(self):
		"""AST_TEST_63"""
		input="""
    void linh(){
        if(a<b) a=b;
    }
    """
		Program([FuncDecl(Id(linh),[],VoidType,Block([If(BinaryOp(<,Id(a),Id(b)),BinaryOp(=,Id(a),Id(b)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,363))
	def test_64(self):
		"""AST_TEST_64"""
		input="""
    void l(){ 
        a=(a*b)-c+c/e%q||a;
    }
    """
		Program([FuncDecl(Id(l),[],VoidType,Block([BinaryOp(=,Id(a),BinaryOp(||,BinaryOp(+,BinaryOp(-,BinaryOp(*,Id(a),Id(b)),Id(c)),BinaryOp(%,BinaryOp(/,Id(c),Id(e)),Id(q))),Id(a)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,364))
	def test_65(self):
		"""AST_TEST_65"""
		input="""
    int a,b;
    void main(){

    }
    int a[2];
    """
		Program([VarDecl(a,IntType),VarDecl(b,IntType),FuncDecl(Id(main),[],VoidType,Block([])),VarDecl(a,ArrayType(IntType,2))])
		self.assertTrue(TestAST.checkASTGen(input,expect,365))
	def test_66(self):
		"""AST_TEST_66"""
		input="""
    /*bascnsdvnnio2io3n1io2ks*//*assnajnjnfjasndasnj*/
    void main(){}
    """
		Program([FuncDecl(Id(main),[],VoidType,Block([]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,366))
	def test_67(self):
		"""AST_TEST_67"""
		input="""
    void main(){
        break;
    }
    """
		Program([FuncDecl(Id(main),[],VoidType,Block([Break()]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,367))
	def test_68(self):
		"""AST_TEST_68"""
		input="""
    void main(){
        break;
    }
    """
		Program([FuncDecl(Id(main),[],VoidType,Block([Break()]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,368))
	def test_69(self):
		"""AST_TEST_69"""
		input="""
    int main(){
        Break;
    }
    """
		Program([FuncDecl(Id(main),[],IntType,Block([Id(Break)]))])
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
		Program([FuncDecl(Id(a),[],VoidType,Block([])),FuncDecl(Id(b),[],IntType,Block([])),FuncDecl(Id(c),[],StringType,Block([])),FuncDecl(Id(d),[],FloatType,Block([]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,307))
	def test_70(self):
		"""AST_TEST_70"""
		input="""
    int main(){
        countinue;
    }
    """
		Program([FuncDecl(Id(main),[],IntType,Block([Id(countinue)]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,370))
	def test_71(self):
		"""AST_TEST_71"""
		input="""
    int main(){
        continue;
    }
    """
		Program([FuncDecl(Id(main),[],IntType,Block([Continue()]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,371))
	def test_72(self):
		"""AST_TEST_72"""
		input="""
    int main(){
       {{{ continue;}}{a;}}
    }
    """
		Program([FuncDecl(Id(main),[],IntType,Block([Block([Block([Block([Continue()])]),Block([Id(a)])])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,372))
	def test_73(self):
		"""AST_TEST_73"""
		input="""
    int main(){
        if ((a<1))  {c=a+1;}
    }
    """
		Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(<,Id(a),IntLiteral(1)),Block([BinaryOp(=,Id(c),BinaryOp(+,Id(a),IntLiteral(1)))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,373))
	def test_74(self):
		"""AST_TEST_74"""
		input="""
    int main(){
        if ((a<1))  {c=a+1;}
        else {{{{{{{}}}}}}}
    }
    """
		Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(<,Id(a),IntLiteral(1)),Block([BinaryOp(=,Id(c),BinaryOp(+,Id(a),IntLiteral(1)))]),Block([Block([Block([Block([Block([Block([Block([])])])])])])]))]))])
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
		Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(<,Id(a),IntLiteral(1)),Block([BinaryOp(=,Id(c),BinaryOp(+,Id(a),IntLiteral(1)))]),If(Id(a),Block([]),Block([])))]))])
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
		Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(<,Id(a),IntLiteral(1)),Block([BinaryOp(=,Id(c),BinaryOp(+,Id(a),IntLiteral(1)))]),If(Id(a),Block([]),Block([BinaryOp(+,Id(a),IntLiteral(1))])))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,376))
	def test_77(self):
		"""AST_TEST_77"""
		input="""
    int man(){
        a = a+1 = b+1;
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([BinaryOp(=,Id(a),BinaryOp(=,BinaryOp(+,Id(a),IntLiteral(1)),BinaryOp(+,Id(b),IntLiteral(1))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,377))
	def test_78(self):
		"""AST_TEST_78"""
		input="""
    int man(){
        a|| a && a+1 = b+1;
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([BinaryOp(=,BinaryOp(||,Id(a),BinaryOp(&&,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))),BinaryOp(+,Id(b),IntLiteral(1)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,378))
	def test_79(self):
		"""AST_TEST_79"""
		input="""
    int man(){
        a ---------b;
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([BinaryOp(-,Id(a),UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,Id(b))))))))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,379))
	def test_8(self):
		"""AST_TEST_8"""
		input="""
    int a; int[] main(int a[], boolean b){}
    """
		Program([VarDecl(a,IntType),FuncDecl(Id(main),[VarDecl(a,ArrayTypePointer(IntType)),VarDecl(b,BoolType)],ArrayTypePointer(IntType),Block([]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,308))
	def test_80(self):
		"""AST_TEST_80"""
		input="""
    int man(){
        a[1] -b[n];
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([BinaryOp(-,ArrayCell(Id(a),IntLiteral(1)),ArrayCell(Id(b),Id(n)))]))])
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
		Program([FuncDecl(Id(man),[],IntType,Block([BinaryOp(-,ArrayCell(Id(a),IntLiteral(1)),ArrayCell(Id(b),Id(n))),CallExpr(Id(call),[]),CallExpr(Id(pull),[])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,381))
	def test_82(self):
		"""AST_TEST_82"""
		input="""
    int man(){
        call();
        pull();
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([CallExpr(Id(call),[]),CallExpr(Id(pull),[])]))])
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
		Program([FuncDecl(Id(man),[],IntType,Block([Dowhile([Id(a),Id(b),Id(c),Id(d)],Id(cc))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,383))
	def test_84(self):
		"""AST_TEST_84"""
		input="""
    int man(){
        {}{}{}{a;}
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([Block([]),Block([]),Block([]),Block([Id(a)])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,384))
	def test_85(self):
		"""AST_TEST_85"""
		input="""
    int man(){
        return ;
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([Return()]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,385))
	def test_86(self):
		"""AST_TEST_86"""
		input="""
    int man(){
        return a= 1 ;
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([Return(BinaryOp(=,Id(a),IntLiteral(1)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,386))
	def test_87(self):
		"""AST_TEST_87"""
		input="""
    int man(){
        return "a" ;
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([Return(StringLiteral(a))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,387))
	def test_88(self):
		"""AST_TEST_88"""
		input="""
    int A1man(){
        return "a" ;
    }
    """
		Program([FuncDecl(Id(A1man),[],IntType,Block([Return(StringLiteral(a))]))])
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
		Program([FuncDecl(Id(A1man),[],IntType,Block([Return(StringLiteral(a)),Block([Id(a),Id(b),Id(v)])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,389))
	def test_9(self):
		"""AST_TEST_9"""
		input="""
    int main(){do {{{}}} while 1;}
    """
		Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Block([Block([Block([])])])],IntLiteral(1))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,309))
	def test_90(self):
		"""AST_TEST_90"""
		input="""
    int A1man(int b,string cc){
        return "a" ;
    }
    """
		Program([FuncDecl(Id(A1man),[VarDecl(b,IntType),VarDecl(cc,StringType)],IntType,Block([Return(StringLiteral(a))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,390))
	def test_91(self):
		"""AST_TEST_91"""
		input="""
    int main(int b,string cc){
        return true ;
    }
    """
		Program([FuncDecl(Id(main),[VarDecl(b,IntType),VarDecl(cc,StringType)],IntType,Block([Return(BooleanLiteral(true))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,391))
	def test_92(self):
		"""AST_TEST_92"""
		input="""
    int main(int b,string cc){
        return false ;
    }
    """
		Program([FuncDecl(Id(main),[VarDecl(b,IntType),VarDecl(cc,StringType)],IntType,Block([Return(BooleanLiteral(false))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,392))
	def test_93(self):
		"""AST_TEST_93"""
		input="""
    int main(int b,string cc){
        return false ;
    }
    """
		Program([FuncDecl(Id(main),[VarDecl(b,IntType),VarDecl(cc,StringType)],IntType,Block([Return(BooleanLiteral(false))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,393))
	def test_94(self):
		"""AST_TEST_94"""
		input="""
    int main(int b,string cc[]){
        return false ;
    }
    """
		Program([FuncDecl(Id(main),[VarDecl(b,IntType),VarDecl(cc,ArrayTypePointer(StringType))],IntType,Block([Return(BooleanLiteral(false))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,394))
	def test_95(self):
		"""AST_TEST_95"""
		input="""
    int main(int b,string cc[]){
        int  a [1];
    }
    """
		Program([FuncDecl(Id(main),[VarDecl(b,IntType),VarDecl(cc,ArrayTypePointer(StringType))],IntType,Block([VarDecl(a,ArrayType(IntType,1))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,395))
	def test_96(self):
		"""AST_TEST_96"""
		input="""
    int main(){
        d+e;
        a+c;
    }
    """
		Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(+,Id(d),Id(e)),BinaryOp(+,Id(a),Id(c))]))])
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
		Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(=,BinaryOp(<,Id(a),Id(a)),Id(b)),Block([If(Id(a),Block([]),Block([If(Id(a),Block([]))]))]),Block([Dowhile([Id(a),Id(b),Id(c)],Id(c))]))]))])
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
		Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(=,BinaryOp(<,Id(a),Id(a)),Id(b)),Block([If(Id(a),Block([]),Block([If(Id(a),Block([]))]))]))])),FuncDecl(Id(b),[],BoolType,Block([BinaryOp(=,Id(check),BooleanLiteral(true)),CallExpr(Id(callme),[]),CallExpr(Id(println),[])]))])
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
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,ArrayType(IntType,3)),VarDecl(b,IntType),VarDecl(c,FloatType),VarDecl(u,StringType)]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,399))
	def test_1(self):
		"""AST_TEST_1"""
		input="""
            int main(){}
        """
		Program([FuncDecl(Id(main),[],IntType,Block([]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,201))
	def test_10(self):
		"""AST_TEST_10"""
		input="""
            string str;
            string str1, str2;
            string str3, str4, str5;
            string str6, str7, str8, str9;
        """
		Program([VarDecl(str,StringType),VarDecl(str1,StringType),VarDecl(str2,StringType),VarDecl(str3,StringType),VarDecl(str4,StringType),VarDecl(str5,StringType),VarDecl(str6,StringType),VarDecl(str7,StringType),VarDecl(str8,StringType),VarDecl(str9,StringType)])
		self.assertTrue(TestAST.checkASTGen(input,expect,210))
	def test_0(self):
		"""AST_TEST_0"""
		input="""
            boolean isPerfect(int x){
                int s, i;
                s = 0;
                for (i = 1; i < x; i = i + 1){
                    if (x % i == 0) 
                        s = s + i;
                }
                if (s == x) 
                    return true;
                else 
                    return false;
            }
        """
		Program([FuncDecl(Id(isPerfect),[VarDecl(x,IntType)],BoolType,Block([VarDecl(s,IntType),VarDecl(i,IntType),BinaryOp(=,Id(s),IntLiteral(0)),For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),Id(x));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,Id(x),Id(i)),IntLiteral(0)),BinaryOp(=,Id(s),BinaryOp(+,Id(s),Id(i))))])),If(BinaryOp(==,Id(s),Id(x)),Return(BooleanLiteral(true)),Return(BooleanLiteral(false)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,300))
	def test_11(self):
		"""AST_TEST_11"""
		input="""
            int[] foo_of_foo(int x, float y){}
        """
		Program([FuncDecl(Id(foo_of_foo),[VarDecl(x,IntType),VarDecl(y,FloatType)],ArrayTypePointer(IntType),Block([]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,211))
	def test_12(self):
		"""AST_TEST_12"""
		input="""
            int[] foo_of_foo(int x, float y[]){}
        """
		Program([FuncDecl(Id(foo_of_foo),[VarDecl(x,IntType),VarDecl(y,ArrayTypePointer(FloatType))],ArrayTypePointer(IntType),Block([]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,212))
	def test_13(self):
		"""AST_TEST_13"""
		input="""
            int foo(){}
        """
		Program([FuncDecl(Id(foo),[],IntType,Block([]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,213))
	def test_14(self):
		"""AST_TEST_14"""
		input="""
            boolean a;
            int foo(){}
            int b;
            float x[9];
        """
		Program([VarDecl(a,BoolType),FuncDecl(Id(foo),[],IntType,Block([])),VarDecl(b,IntType),VarDecl(x,ArrayType(FloatType,9))])
		self.assertTrue(TestAST.checkASTGen(input,expect,214))
	def test_15(self):
		"""AST_TEST_15"""
		input="""
            boolean a;
            int foo(string str, int y, float z[]){}
            int b;
            float x[9];
        """
		Program([VarDecl(a,BoolType),FuncDecl(Id(foo),[VarDecl(str,StringType),VarDecl(y,IntType),VarDecl(z,ArrayTypePointer(FloatType))],IntType,Block([])),VarDecl(b,IntType),VarDecl(x,ArrayType(FloatType,9))])
		self.assertTrue(TestAST.checkASTGen(input,expect,215))
	def test_16(self):
		"""AST_TEST_16"""
		input="""
            string[] foo(){}
        """
		Program([FuncDecl(Id(foo),[],ArrayTypePointer(StringType),Block([]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,216))
	def test_17(self):
		"""AST_TEST_17"""
		input="""
            string[] foo(int a, float b[], string c, boolean d[]){}
        """
		Program([FuncDecl(Id(foo),[VarDecl(a,IntType),VarDecl(b,ArrayTypePointer(FloatType)),VarDecl(c,StringType),VarDecl(d,ArrayTypePointer(BoolType))],ArrayTypePointer(StringType),Block([]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,217))
	def test_18(self):
		"""AST_TEST_18"""
		input="""
            int main(){
                x = y = 5;
                x || y && z;
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,Id(x),BinaryOp(=,Id(y),IntLiteral(5))),BinaryOp(||,Id(x),BinaryOp(&&,Id(y),Id(z)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,218))
	def test_19(self):
		"""AST_TEST_19"""
		input="""
            int main(){
                x = y = 5;
                x || y && z;
                x == y;
                y != z;
                z > t;
                t >= a;
                a <= b;
                b < c;
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,Id(x),BinaryOp(=,Id(y),IntLiteral(5))),BinaryOp(||,Id(x),BinaryOp(&&,Id(y),Id(z))),BinaryOp(==,Id(x),Id(y)),BinaryOp(!=,Id(y),Id(z)),BinaryOp(>,Id(z),Id(t)),BinaryOp(>=,Id(t),Id(a)),BinaryOp(<=,Id(a),Id(b)),BinaryOp(<,Id(b),Id(c))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,219))
	def test_2(self):
		"""AST_TEST_2"""
		input="""
            int main(){
            putInt(10);
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(putInt),[IntLiteral(10)])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,202))
	def test_20(self):
		"""AST_TEST_20"""
		input="""
            int main(){
                a + b - c = 5;
                b - c + d = 9;
                a * b / c - d = 12;
                a / b % c * d = 36;
                a > b * c + d - e = 1;
                -a;
                !x;
                y[18];
                z(5);
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,BinaryOp(-,BinaryOp(+,Id(a),Id(b)),Id(c)),IntLiteral(5)),BinaryOp(=,BinaryOp(+,BinaryOp(-,Id(b),Id(c)),Id(d)),IntLiteral(9)),BinaryOp(=,BinaryOp(-,BinaryOp(/,BinaryOp(*,Id(a),Id(b)),Id(c)),Id(d)),IntLiteral(12)),BinaryOp(=,BinaryOp(*,BinaryOp(%,BinaryOp(/,Id(a),Id(b)),Id(c)),Id(d)),IntLiteral(36)),BinaryOp(=,BinaryOp(>,Id(a),BinaryOp(-,BinaryOp(+,BinaryOp(*,Id(b),Id(c)),Id(d)),Id(e))),IntLiteral(1)),UnaryOp(-,Id(a)),UnaryOp(!,Id(x)),ArrayCell(Id(y),IntLiteral(18)),CallExpr(Id(z),[IntLiteral(5)])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,220))
	def test_21(self):
		"""AST_TEST_21"""
		input="""
            int main(){
            x[y[z[t[a[b[c[d]]]]]]];
        }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([ArrayCell(Id(x),ArrayCell(Id(y),ArrayCell(Id(z),ArrayCell(Id(t),ArrayCell(Id(a),ArrayCell(Id(b),ArrayCell(Id(c),Id(d))))))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,221))
	def test_22(self):
		"""AST_TEST_22"""
		input="""
            int main(){
            .2E-2 + false && true - "MATH007" * 18 / 9 % 35;
        }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(&&,BinaryOp(+,FloatLiteral(0.002),BooleanLiteral(false)),BinaryOp(-,BooleanLiteral(true),BinaryOp(%,BinaryOp(/,BinaryOp(*,StringLiteral(MATH007),IntLiteral(18)),IntLiteral(9)),IntLiteral(35))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,222))
	def test_23(self):
		"""AST_TEST_23"""
		input="""
            int main(){
                foo(30)[38+x] = a[b[29]] + 37 - 1 * 12 % 3[5];
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,ArrayCell(CallExpr(Id(foo),[IntLiteral(30)]),BinaryOp(+,IntLiteral(38),Id(x))),BinaryOp(-,BinaryOp(+,ArrayCell(Id(a),ArrayCell(Id(b),IntLiteral(29))),IntLiteral(37)),BinaryOp(%,BinaryOp(*,IntLiteral(1),IntLiteral(12)),ArrayCell(IntLiteral(3),IntLiteral(5)))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,223))
	def test_24(self):
		"""AST_TEST_24"""
		input="""
            int main(){
            x[y[z[t[a[b[c[d + 1] + 2] + 3] + 4] + 5] + 6] + 7] + 8;
        }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(+,ArrayCell(Id(x),BinaryOp(+,ArrayCell(Id(y),BinaryOp(+,ArrayCell(Id(z),BinaryOp(+,ArrayCell(Id(t),BinaryOp(+,ArrayCell(Id(a),BinaryOp(+,ArrayCell(Id(b),BinaryOp(+,ArrayCell(Id(c),BinaryOp(+,Id(d),IntLiteral(1))),IntLiteral(2))),IntLiteral(3))),IntLiteral(4))),IntLiteral(5))),IntLiteral(6))),IntLiteral(7))),IntLiteral(8))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,224))
	def test_25(self):
		"""AST_TEST_25"""
		input="""
            int main(){
            x[y[z[t[a[b[c[d + 1] + 2] + 3] + 4] + 5] + 6] + 7] + 8 = x[y[z[t[a[b[c[d]]]]]]];
        }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,BinaryOp(+,ArrayCell(Id(x),BinaryOp(+,ArrayCell(Id(y),BinaryOp(+,ArrayCell(Id(z),BinaryOp(+,ArrayCell(Id(t),BinaryOp(+,ArrayCell(Id(a),BinaryOp(+,ArrayCell(Id(b),BinaryOp(+,ArrayCell(Id(c),BinaryOp(+,Id(d),IntLiteral(1))),IntLiteral(2))),IntLiteral(3))),IntLiteral(4))),IntLiteral(5))),IntLiteral(6))),IntLiteral(7))),IntLiteral(8)),ArrayCell(Id(x),ArrayCell(Id(y),ArrayCell(Id(z),ArrayCell(Id(t),ArrayCell(Id(a),ArrayCell(Id(b),ArrayCell(Id(c),Id(d)))))))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,225))
	def test_26(self):
		"""AST_TEST_26"""
		input="""
            int main(){
                int i,j;
                float x;
                if (i < j) 
                    i = i + 1; 
                    x = i * j;
                return x * x;
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(i,IntType),VarDecl(j,IntType),VarDecl(x,FloatType),If(BinaryOp(<,Id(i),Id(j)),BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)))),BinaryOp(=,Id(x),BinaryOp(*,Id(i),Id(j))),Return(BinaryOp(*,Id(x),Id(x)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,226))
	def test_27(self):
		"""AST_TEST_27"""
		input="""
            int Recursive(int n){
            if (n <= 0)
                return 1;
            else return n*Recursive(n - 1);    
        }
        """
		Program([FuncDecl(Id(Recursive),[VarDecl(n,IntType)],IntType,Block([If(BinaryOp(<=,Id(n),IntLiteral(0)),Return(IntLiteral(1)),Return(BinaryOp(*,Id(n),CallExpr(Id(Recursive),[BinaryOp(-,Id(n),IntLiteral(1))]))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,227))
	def test_28(self):
		"""AST_TEST_28"""
		input="""
            int main(){
            int i,j;
            float x;
            if (i < j) 
                i = i + 1;
            else if (i > j) 
                j = j + 1;
            else 
                x = i * j;
            return x + i + j;
        }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(i,IntType),VarDecl(j,IntType),VarDecl(x,FloatType),If(BinaryOp(<,Id(i),Id(j)),BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1))),If(BinaryOp(>,Id(i),Id(j)),BinaryOp(=,Id(j),BinaryOp(+,Id(j),IntLiteral(1))),BinaryOp(=,Id(x),BinaryOp(*,Id(i),Id(j))))),Return(BinaryOp(+,BinaryOp(+,Id(x),Id(i)),Id(j)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,228))
	def test_29(self):
		"""AST_TEST_29"""
		input="""
            int main(){
            int n,m,p;
            float x;
            if (m <= 0){
                if (n <= 0){
                    if (p <= 0) 
                        print("MATH007!");
                    else
                        p = p + 1;
                }
                else 
                    n = n + 1;
            }
            else 
                x = x * (m + n + p);
                m = m + 1;
        }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(n,IntType),VarDecl(m,IntType),VarDecl(p,IntType),VarDecl(x,FloatType),If(BinaryOp(<=,Id(m),IntLiteral(0)),Block([If(BinaryOp(<=,Id(n),IntLiteral(0)),Block([If(BinaryOp(<=,Id(p),IntLiteral(0)),CallExpr(Id(print),[StringLiteral(MATH007!)]),BinaryOp(=,Id(p),BinaryOp(+,Id(p),IntLiteral(1))))]),BinaryOp(=,Id(n),BinaryOp(+,Id(n),IntLiteral(1))))]),BinaryOp(=,Id(x),BinaryOp(*,Id(x),BinaryOp(+,BinaryOp(+,Id(m),Id(n)),Id(p))))),BinaryOp(=,Id(m),BinaryOp(+,Id(m),IntLiteral(1)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,229))
	def test_3(self):
		"""AST_TEST_3"""
		input="""
            int main(){
            int a, b, c[9];
            float x, y, z;
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,ArrayType(IntType,9)),VarDecl(x,FloatType),VarDecl(y,FloatType),VarDecl(z,FloatType)]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,203))
	def test_30(self):
		"""AST_TEST_30"""
		input="""
            int foo(){
            int a, b, c; 
            a = b = c = 5; 
            float f[5]; 
            if (a==b) f[0] = 1.0E-2;
        } 
        """
		Program([FuncDecl(Id(foo),[],IntType,Block([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,IntType),BinaryOp(=,Id(a),BinaryOp(=,Id(b),BinaryOp(=,Id(c),IntLiteral(5)))),VarDecl(f,ArrayType(FloatType,5)),If(BinaryOp(==,Id(a),Id(b)),BinaryOp(=,ArrayCell(Id(f),IntLiteral(0)),FloatLiteral(0.01)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,230))
	def test_31(self):
		"""AST_TEST_31"""
		input="""
            int main(){
                string test, str;
                test = " MATH007 ";
                str = "The Beauty of Mathematics";
                print(test + str + " ");
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(test,StringType),VarDecl(str,StringType),BinaryOp(=,Id(test),StringLiteral( MATH007 )),BinaryOp(=,Id(str),StringLiteral(The Beauty of Mathematics)),CallExpr(Id(print),[BinaryOp(+,BinaryOp(+,Id(test),Id(str)),StringLiteral( ))])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,231))
	def test_32(self):
		"""AST_TEST_32"""
		input="""
            int main(){
                int a,b,c;
                float x,y,z;
                if (!true){
                    float s;
                    s = s *(a + b + c) * (x + y + z);
                }
                print(s); 
                return 0;  
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,IntType),VarDecl(x,FloatType),VarDecl(y,FloatType),VarDecl(z,FloatType),If(UnaryOp(!,BooleanLiteral(true)),Block([VarDecl(s,FloatType),BinaryOp(=,Id(s),BinaryOp(*,BinaryOp(*,Id(s),BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(c))),BinaryOp(+,BinaryOp(+,Id(x),Id(y)),Id(z))))])),CallExpr(Id(print),[Id(s)]),Return(IntLiteral(0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,232))
	def test_33(self):
		"""AST_TEST_33"""
		input="""
            int main(){
            int n;
            print(n*n);
            print("\t\n\r\b");
            system("pause");
            return 0;
        }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(n,IntType),CallExpr(Id(print),[BinaryOp(*,Id(n),Id(n))]),CallExpr(Id(print),[StringLiteral(\t\n\r\b)]),CallExpr(Id(system),[StringLiteral(pause)]),Return(IntLiteral(0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,233))
	def test_34(self):
		"""AST_TEST_34"""
		input="""
            int foo(int a, float b[]){
            boolean c;
            int i;
            i = a + 3;
            if (i > 0){
                int d;
                d = i + 3;
                putInt(d);
            }
            return i;
        }
        """
		Program([FuncDecl(Id(foo),[VarDecl(a,IntType),VarDecl(b,ArrayTypePointer(FloatType))],IntType,Block([VarDecl(c,BoolType),VarDecl(i,IntType),BinaryOp(=,Id(i),BinaryOp(+,Id(a),IntLiteral(3))),If(BinaryOp(>,Id(i),IntLiteral(0)),Block([VarDecl(d,IntType),BinaryOp(=,Id(d),BinaryOp(+,Id(i),IntLiteral(3))),CallExpr(Id(putInt),[Id(d)])])),Return(Id(i))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,234))
	def test_35(self):
		"""AST_TEST_35"""
		input="""
            int i;
            int f(){
                return 200;
            }
            void main(){
                int main;
                main = f();
                putIntLn(main);
                {
                    int i;
                    int main;
                    int f;
                    main = f = i = 100;
                    putIntLn(i);
                    putIntLn(main);
                    putIntLn(f);
                }
            putIntLn(main);
            }
        """
		Program([VarDecl(i,IntType),FuncDecl(Id(f),[],IntType,Block([Return(IntLiteral(200))])),FuncDecl(Id(main),[],VoidType,Block([VarDecl(main,IntType),BinaryOp(=,Id(main),CallExpr(Id(f),[])),CallExpr(Id(putIntLn),[Id(main)]),Block([VarDecl(i,IntType),VarDecl(main,IntType),VarDecl(f,IntType),BinaryOp(=,Id(main),BinaryOp(=,Id(f),BinaryOp(=,Id(i),IntLiteral(100)))),CallExpr(Id(putIntLn),[Id(i)]),CallExpr(Id(putIntLn),[Id(main)]),CallExpr(Id(putIntLn),[Id(f)])]),CallExpr(Id(putIntLn),[Id(main)])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,235))
	def test_36(self):
		"""AST_TEST_36"""
		input="""
            int foo(int a, int b, int c){return a + b + c;}
            int main(){
                a = foo(1,2,3);
                b = foo(2,3,4);
                int c;
                c = a + b;
                print(c);
                system("pause");
                return 0;
            }
        """
		Program([FuncDecl(Id(foo),[VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,IntType)],IntType,Block([Return(BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(c)))])),FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,Id(a),CallExpr(Id(foo),[IntLiteral(1),IntLiteral(2),IntLiteral(3)])),BinaryOp(=,Id(b),CallExpr(Id(foo),[IntLiteral(2),IntLiteral(3),IntLiteral(4)])),VarDecl(c,IntType),BinaryOp(=,Id(c),BinaryOp(+,Id(a),Id(b))),CallExpr(Id(print),[Id(c)]),CallExpr(Id(system),[StringLiteral(pause)]),Return(IntLiteral(0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,236))
	def test_37(self):
		"""AST_TEST_37"""
		input="""
            int main(){
            a[b[c[d]]] = 96;
            do{
                a;  
            } 
            while b;
            print("Error");
            system("pause");
            return 0;
        }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,ArrayCell(Id(a),ArrayCell(Id(b),ArrayCell(Id(c),Id(d)))),IntLiteral(96)),Dowhile([Block([Id(a)])],Id(b)),CallExpr(Id(print),[StringLiteral(Error)]),CallExpr(Id(system),[StringLiteral(pause)]),Return(IntLiteral(0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,237))
	def test_38(self):
		"""AST_TEST_38"""
		input="""
            void main(){
                continue;
                break;
                return;
            }
        """
		Program([FuncDecl(Id(main),[],VoidType,Block([Continue(),Break(),Return()]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,238))
	def test_39(self):
		"""AST_TEST_39"""
		input="""
            void main(int a[], float x[]){
                return;
            }
            int main(int b[], float y[]){
                return 0;
            }
        """
		Program([FuncDecl(Id(main),[VarDecl(a,ArrayTypePointer(IntType)),VarDecl(x,ArrayTypePointer(FloatType))],VoidType,Block([Return()])),FuncDecl(Id(main),[VarDecl(b,ArrayTypePointer(IntType)),VarDecl(y,ArrayTypePointer(FloatType))],IntType,Block([Return(IntLiteral(0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,239))
	def test_4(self):
		"""AST_TEST_4"""
		input="""
            int main(){
            int a, b, c[9];
            float x, y, z;
            boolean c, d, e[10];
            string g, h, i[5];
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,ArrayType(IntType,9)),VarDecl(x,FloatType),VarDecl(y,FloatType),VarDecl(z,FloatType),VarDecl(c,BoolType),VarDecl(d,BoolType),VarDecl(e,ArrayType(BoolType,10)),VarDecl(g,StringType),VarDecl(h,StringType),VarDecl(i,ArrayType(StringType,5))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,204))
	def test_40(self):
		"""AST_TEST_40"""
		input="""
            int foo(int n){
                return foo(n - 1);
            }
            int main(){
                foo(1) + foo(2) + foo(3);
                return 0;
            }
        """
		Program([FuncDecl(Id(foo),[VarDecl(n,IntType)],IntType,Block([Return(CallExpr(Id(foo),[BinaryOp(-,Id(n),IntLiteral(1))]))])),FuncDecl(Id(main),[],IntType,Block([BinaryOp(+,BinaryOp(+,CallExpr(Id(foo),[IntLiteral(1)]),CallExpr(Id(foo),[IntLiteral(2)])),CallExpr(Id(foo),[IntLiteral(3)])),Return(IntLiteral(0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,240))
	def test_41(self):
		"""AST_TEST_41"""
		input="""
            int main(){
            do{
                if (!true){
                
                } 
                if (!true){
                
                }
                if (!true){
                
                }
            }while "statement";
        }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Block([If(UnaryOp(!,BooleanLiteral(true)),Block([])),If(UnaryOp(!,BooleanLiteral(true)),Block([])),If(UnaryOp(!,BooleanLiteral(true)),Block([]))])],StringLiteral(statement))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,241))
	def test_42(self):
		"""AST_TEST_42"""
		input="""
            int main(){
            do {
                if (!true){
                
                } 
                else if (!true){
                
                }
                else{
                
                }
            }while "MATH007";
        }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Block([If(UnaryOp(!,BooleanLiteral(true)),Block([]),If(UnaryOp(!,BooleanLiteral(true)),Block([]),Block([])))])],StringLiteral(MATH007))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,242))
	def test_43(self):
		"""AST_TEST_43"""
		input="""
            int main(){
            do {
                do{
                    do{
                    
                    }while " ";
                }while " ";
            }while " ";
        }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Block([Dowhile([Block([Dowhile([Block([])],StringLiteral( ))])],StringLiteral( ))])],StringLiteral( ))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,243))
	def test_44(self):
		"""AST_TEST_44"""
		input="""
            int main(){
                int i;
                for(i = 0;i <= n; i =  i + 1){
                    print(i);
                }
            } 
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(i,IntType),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<=,Id(i),Id(n));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([CallExpr(Id(print),[Id(i)])]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,244))
	def test_45(self):
		"""AST_TEST_45"""
		input="""
            int main(){
                int n, i, j;
                for(i = 0; i <= n; i = i + 1){
                    for(j = 0; j <= n; j = j + 1){
                            int sum;
                            sum = sum+(i*j);
                    }
                }
                print(sum);
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(n,IntType),VarDecl(i,IntType),VarDecl(j,IntType),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<=,Id(i),Id(n));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([For(BinaryOp(=,Id(j),IntLiteral(0));BinaryOp(<=,Id(j),Id(n));BinaryOp(=,Id(j),BinaryOp(+,Id(j),IntLiteral(1)));Block([VarDecl(sum,IntType),BinaryOp(=,Id(sum),BinaryOp(+,Id(sum),BinaryOp(*,Id(i),Id(j))))]))])),CallExpr(Id(print),[Id(sum)])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,245))
	def test_46(self):
		"""AST_TEST_46"""
		input="""
            int main(){
                int n, i, j;
                for(i = 0; i <= n; i = i + 1){
                    do{
                        j = 0;
                        if (i == j){
                            int sum;
                            sum = sum+(i*j);
                        } 
                        j = j + 1;
                    }while j <= n;
                }
                print(sum);
                return 0;
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(n,IntType),VarDecl(i,IntType),VarDecl(j,IntType),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<=,Id(i),Id(n));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([Dowhile([Block([BinaryOp(=,Id(j),IntLiteral(0)),If(BinaryOp(==,Id(i),Id(j)),Block([VarDecl(sum,IntType),BinaryOp(=,Id(sum),BinaryOp(+,Id(sum),BinaryOp(*,Id(i),Id(j))))])),BinaryOp(=,Id(j),BinaryOp(+,Id(j),IntLiteral(1)))])],BinaryOp(<=,Id(j),Id(n)))])),CallExpr(Id(print),[Id(sum)]),Return(IntLiteral(0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,246))
	def test_47(self):
		"""AST_TEST_47"""
		input="""
            int main(){
                //;;;;;;;;;;;;;;;;;;;;;;;;
                // foo(1) + foo(2) - foo(3);
                // "Block statment";
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,247))
	def test_48(self):
		"""AST_TEST_48"""
		input="""
            int main(){
                /*
                    ;;;;;;;;;;;;;;;;;;;;;;;;
                    foo(1) + foo(2) - foo(3);
                    "Block statment";
                */
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,248))
	def test_49(self):
		"""AST_TEST_49"""
		input="""
            int main(){
                /*
                    //;;;;;;;;;;;;;;;;;;;;;;;;
                    //foo(1) + foo(2) - foo(3);
                    //"Block statment";
                */
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,249))
	def test_5(self):
		"""AST_TEST_5"""
		input="""
            int main(){
            int a[1], b[2], c[3];
            float x[4], y[5], z[6];
            boolean c[7], d[8], e[9];
            string g[10], h[11], i[12];
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,ArrayType(IntType,1)),VarDecl(b,ArrayType(IntType,2)),VarDecl(c,ArrayType(IntType,3)),VarDecl(x,ArrayType(FloatType,4)),VarDecl(y,ArrayType(FloatType,5)),VarDecl(z,ArrayType(FloatType,6)),VarDecl(c,ArrayType(BoolType,7)),VarDecl(d,ArrayType(BoolType,8)),VarDecl(e,ArrayType(BoolType,9)),VarDecl(g,ArrayType(StringType,10)),VarDecl(h,ArrayType(StringType,11)),VarDecl(i,ArrayType(StringType,12))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,205))
	def test_50(self):
		"""AST_TEST_50"""
		input="""
            int main(){
                // /*;;;;;;;;;;;;;;;;;;;;;;;;
                foo(1) + foo(2) - foo(3);
                // /*"Block statment";*/
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(-,BinaryOp(+,CallExpr(Id(foo),[IntLiteral(1)]),CallExpr(Id(foo),[IntLiteral(2)])),CallExpr(Id(foo),[IntLiteral(3)]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,250))
	def test_51(self):
		"""AST_TEST_51"""
		input="""
            int main() {
            foo()[foo()[foo(foo()[100])]];
        }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([ArrayCell(CallExpr(Id(foo),[]),ArrayCell(CallExpr(Id(foo),[]),CallExpr(Id(foo),[ArrayCell(CallExpr(Id(foo),[]),IntLiteral(100))])))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,251))
	def test_52(self):
		"""AST_TEST_52"""
		input="""
            void f(){
                int i, j, k;
                float x, y, z;
                string str;
                str = "MATH007";
                boolean y;
                if(y == "true") print(i,j,k);
                else print(x,y,z);
            }
            void main(){
                f();
                return;
            }
        """
		Program([FuncDecl(Id(f),[],VoidType,Block([VarDecl(i,IntType),VarDecl(j,IntType),VarDecl(k,IntType),VarDecl(x,FloatType),VarDecl(y,FloatType),VarDecl(z,FloatType),VarDecl(str,StringType),BinaryOp(=,Id(str),StringLiteral(MATH007)),VarDecl(y,BoolType),If(BinaryOp(==,Id(y),StringLiteral(true)),CallExpr(Id(print),[Id(i),Id(j),Id(k)]),CallExpr(Id(print),[Id(x),Id(y),Id(z)]))])),FuncDecl(Id(main),[],VoidType,Block([CallExpr(Id(f),[]),Return()]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,252))
	def test_53(self):
		"""AST_TEST_53"""
		input="""
            int main(){
            int n, i, count, c;
            n = 1000000;
            i = 3;
            if ( n >= 1 ){
                printf("Error");
            }
            for (count = 2;count <= n; " ")
            {
                for (c = 2;c <= i - 1;c = c + 1){
                    if ( i % c == 0 ) break;
                }
                if ( c == i ){
                    count = count + 1;
                }
                i = i + 1;
            }
            return 0;
        }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(n,IntType),VarDecl(i,IntType),VarDecl(count,IntType),VarDecl(c,IntType),BinaryOp(=,Id(n),IntLiteral(1000000)),BinaryOp(=,Id(i),IntLiteral(3)),If(BinaryOp(>=,Id(n),IntLiteral(1)),Block([CallExpr(Id(printf),[StringLiteral(Error)])])),For(BinaryOp(=,Id(count),IntLiteral(2));BinaryOp(<=,Id(count),Id(n));StringLiteral( );Block([For(BinaryOp(=,Id(c),IntLiteral(2));BinaryOp(<=,Id(c),BinaryOp(-,Id(i),IntLiteral(1)));BinaryOp(=,Id(c),BinaryOp(+,Id(c),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,Id(i),Id(c)),IntLiteral(0)),Break())])),If(BinaryOp(==,Id(c),Id(i)),Block([BinaryOp(=,Id(count),BinaryOp(+,Id(count),IntLiteral(1)))])),BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)))])),Return(IntLiteral(0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,253))
	def test_54(self):
		"""AST_TEST_54"""
		input="""
            int main() {
            int n, a;
            n = 400;
            if(n>0){ 
                a=sqrt(n);
                if((a*a)==n) printf("True");
                else printf("False");
            }
        }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(n,IntType),VarDecl(a,IntType),BinaryOp(=,Id(n),IntLiteral(400)),If(BinaryOp(>,Id(n),IntLiteral(0)),Block([BinaryOp(=,Id(a),CallExpr(Id(sqrt),[Id(n)])),If(BinaryOp(==,BinaryOp(*,Id(a),Id(a)),Id(n)),CallExpr(Id(printf),[StringLiteral(True)]),CallExpr(Id(printf),[StringLiteral(False)]))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,254))
	def test_55(self):
		"""AST_TEST_55"""
		input="""
            int main() {
            int a, b, i, x;
            a = 12;
            b = 16;
            for(i = 1; i <= a || i <= b; i = i + 1) {
            if( a % i == 0 && b % i == 0 )
                x = i;
            }
            printf(x); 
            return 0;
        }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(i,IntType),VarDecl(x,IntType),BinaryOp(=,Id(a),IntLiteral(12)),BinaryOp(=,Id(b),IntLiteral(16)),For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(||,BinaryOp(<=,Id(i),Id(a)),BinaryOp(<=,Id(i),Id(b)));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(&&,BinaryOp(==,BinaryOp(%,Id(a),Id(i)),IntLiteral(0)),BinaryOp(==,BinaryOp(%,Id(b),Id(i)),IntLiteral(0))),BinaryOp(=,Id(x),Id(i)))])),CallExpr(Id(printf),[Id(x)]),Return(IntLiteral(0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,255))
	def test_56(self):
		"""AST_TEST_56"""
		input="""
            int main(){
                a == (b == c) >= (d <= e);
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(==,Id(a),BinaryOp(>=,BinaryOp(==,Id(b),Id(c)),BinaryOp(<=,Id(d),Id(e))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,256))
	def test_57(self):
		"""AST_TEST_57"""
		input="""
            int main(){
                a == (b == c) >= (d <= e);
                a >= (b <= (c < (d > e)));
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(==,Id(a),BinaryOp(>=,BinaryOp(==,Id(b),Id(c)),BinaryOp(<=,Id(d),Id(e)))),BinaryOp(>=,Id(a),BinaryOp(<=,Id(b),BinaryOp(<,Id(c),BinaryOp(>,Id(d),Id(e)))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,257))
	def test_58(self):
		"""AST_TEST_58"""
		input="""
            void Fibonacci(int n){  
                int n1, n2, n3;
                n1=0;
                n2=1;
                if(n > 0){  
                    n3 = n1 + n2;  
                    n1 = n2;  
                    n2 = n3;  
                    printf("%d ",n3);  
                    Fibonacci(n-1);  
                }
            }
        """
		Program([FuncDecl(Id(Fibonacci),[VarDecl(n,IntType)],VoidType,Block([VarDecl(n1,IntType),VarDecl(n2,IntType),VarDecl(n3,IntType),BinaryOp(=,Id(n1),IntLiteral(0)),BinaryOp(=,Id(n2),IntLiteral(1)),If(BinaryOp(>,Id(n),IntLiteral(0)),Block([BinaryOp(=,Id(n3),BinaryOp(+,Id(n1),Id(n2))),BinaryOp(=,Id(n1),Id(n2)),BinaryOp(=,Id(n2),Id(n3)),CallExpr(Id(printf),[StringLiteral(%d ),Id(n3)]),CallExpr(Id(Fibonacci),[BinaryOp(-,Id(n),IntLiteral(1))])]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,258))
	def test_59(self):
		"""AST_TEST_59"""
		input="""
            int main() {
                int year;
                year = 2020;
                
                if (((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0)){
                    printf("Yes");
                    printf("%d", year);
                    }
                else{
                    printf("No");
                    printf("%d", year);
                    }
                return 0;
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(year,IntType),BinaryOp(=,Id(year),IntLiteral(2020)),If(BinaryOp(||,BinaryOp(&&,BinaryOp(==,BinaryOp(%,Id(year),IntLiteral(4)),IntLiteral(0)),BinaryOp(!=,BinaryOp(%,Id(year),IntLiteral(100)),IntLiteral(0))),BinaryOp(==,BinaryOp(%,Id(year),IntLiteral(400)),IntLiteral(0))),Block([CallExpr(Id(printf),[StringLiteral(Yes)]),CallExpr(Id(printf),[StringLiteral(%d),Id(year)])]),Block([CallExpr(Id(printf),[StringLiteral(No)]),CallExpr(Id(printf),[StringLiteral(%d),Id(year)])])),Return(IntLiteral(0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,259))
	def test_6(self):
		"""AST_TEST_6"""
		input="""
            int main(){
            string str;
            string str1, str2;
            string str3, str4, str5;
            string str6, str7, str8, str9;
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(str,StringType),VarDecl(str1,StringType),VarDecl(str2,StringType),VarDecl(str3,StringType),VarDecl(str4,StringType),VarDecl(str5,StringType),VarDecl(str6,StringType),VarDecl(str7,StringType),VarDecl(str8,StringType),VarDecl(str9,StringType)]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,206))
	def test_60(self):
		"""AST_TEST_60"""
		input="""
            int main(){  
                int i, s, n;  
                n = 100;
                s = 1;
                for(i = 1; i <= n; i = i + 1){  
                    s = s * i;  
                }
                return s;
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(i,IntType),VarDecl(s,IntType),VarDecl(n,IntType),BinaryOp(=,Id(n),IntLiteral(100)),BinaryOp(=,Id(s),IntLiteral(1)),For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<=,Id(i),Id(n));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,Id(s),BinaryOp(*,Id(s),Id(i)))])),Return(Id(s))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,260))
	def test_61(self):
		"""AST_TEST_61"""
		input="""     
            int main() {  
                int a[10], n, i;  
                n = 100;
                for(i = 0; n > 0; i = i + 1){  
                    a[i] = n % 2;  
                    n = n / 2;  
                }  
                for(i=i-1;i>=0;i = i - 1){  
                    printf("%d", a[i]);  
                }
                return 0;  
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,ArrayType(IntType,10)),VarDecl(n,IntType),VarDecl(i,IntType),BinaryOp(=,Id(n),IntLiteral(100)),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(>,Id(n),IntLiteral(0));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,ArrayCell(Id(a),Id(i)),BinaryOp(%,Id(n),IntLiteral(2))),BinaryOp(=,Id(n),BinaryOp(/,Id(n),IntLiteral(2)))])),For(BinaryOp(=,Id(i),BinaryOp(-,Id(i),IntLiteral(1)));BinaryOp(>=,Id(i),IntLiteral(0));BinaryOp(=,Id(i),BinaryOp(-,Id(i),IntLiteral(1)));Block([CallExpr(Id(printf),[StringLiteral(%d),ArrayCell(Id(a),Id(i))])])),Return(IntLiteral(0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,261))
	def test_62(self):
		"""AST_TEST_62"""
		input="""
            int main()  {  
                int i, j, k, l, n;  
                n = 100;
                for(i = 1; i <= n; i = i + 1){  
                    for(j = 1; j <= n - i; j = j + 1){  
                        printf(" ");  
                    }  
                    for(k = 1; k <= i; k = k + 1){  
                        printf("%d", k);  
                    }  
                    for(l = i-1; l >= 1; l = l - 1){  
                        printf("%d", l);  
                    }  
                }
            } 
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(i,IntType),VarDecl(j,IntType),VarDecl(k,IntType),VarDecl(l,IntType),VarDecl(n,IntType),BinaryOp(=,Id(n),IntLiteral(100)),For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<=,Id(i),Id(n));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([For(BinaryOp(=,Id(j),IntLiteral(1));BinaryOp(<=,Id(j),BinaryOp(-,Id(n),Id(i)));BinaryOp(=,Id(j),BinaryOp(+,Id(j),IntLiteral(1)));Block([CallExpr(Id(printf),[StringLiteral( )])])),For(BinaryOp(=,Id(k),IntLiteral(1));BinaryOp(<=,Id(k),Id(i));BinaryOp(=,Id(k),BinaryOp(+,Id(k),IntLiteral(1)));Block([CallExpr(Id(printf),[StringLiteral(%d),Id(k)])])),For(BinaryOp(=,Id(l),BinaryOp(-,Id(i),IntLiteral(1)));BinaryOp(>=,Id(l),IntLiteral(1));BinaryOp(=,Id(l),BinaryOp(-,Id(l),IntLiteral(1)));Block([CallExpr(Id(printf),[StringLiteral(%d),Id(l)])]))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,262))
	def test_63(self):
		"""AST_TEST_63"""
		input="""
            int main(){
                int i, j;
                for(i = 1; i <= 10; i = i + 1){
                    printf("\n--------BANG NHAN %d--------\n", i);
                    for(j = 0; j < 10; j = j + 1){
                        printf("\t %d x %d = %d \n", i, j, i*j);
                    }
                }
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(i,IntType),VarDecl(j,IntType),For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<=,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([CallExpr(Id(printf),[StringLiteral(\n--------BANG NHAN %d--------\n),Id(i)]),For(BinaryOp(=,Id(j),IntLiteral(0));BinaryOp(<,Id(j),IntLiteral(10));BinaryOp(=,Id(j),BinaryOp(+,Id(j),IntLiteral(1)));Block([CallExpr(Id(printf),[StringLiteral(\t %d x %d = %d \n),Id(i),Id(j),BinaryOp(*,Id(i),Id(j))])]))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,263))
	def test_64(self):
		"""AST_TEST_64"""
		input="""
            int GTLN(int a[], int n){
                int max, i;
                max = a[0];
                for(i=1; i < n; i = i + 1){
                    if(a[i] > max)
                        max = a[i];
                }
                return max;
            }
        """
		Program([FuncDecl(Id(GTLN),[VarDecl(a,ArrayTypePointer(IntType)),VarDecl(n,IntType)],IntType,Block([VarDecl(max,IntType),VarDecl(i,IntType),BinaryOp(=,Id(max),ArrayCell(Id(a),IntLiteral(0))),For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),Id(n));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(>,ArrayCell(Id(a),Id(i)),Id(max)),BinaryOp(=,Id(max),ArrayCell(Id(a),Id(i))))])),Return(Id(max))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,264))
	def test_65(self):
		"""AST_TEST_65"""
		input="""
            int GTNN(int a[], int n) {
                int min, i;
                min = a[0];
                for(i=1; i<n; i = i + 1){
                    if(a[i] > min)
                        min = a[i];
                }
                return min;
            }
        """
		Program([FuncDecl(Id(GTNN),[VarDecl(a,ArrayTypePointer(IntType)),VarDecl(n,IntType)],IntType,Block([VarDecl(min,IntType),VarDecl(i,IntType),BinaryOp(=,Id(min),ArrayCell(Id(a),IntLiteral(0))),For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),Id(n));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(>,ArrayCell(Id(a),Id(i)),Id(min)),BinaryOp(=,Id(min),ArrayCell(Id(a),Id(i))))])),Return(Id(min))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,265))
	def test_66(self):
		"""AST_TEST_66"""
		input="""
            int main(){}
            void _(){}
            string foo(){}
            boolean foo2(){}
            float foo3(){}

        """
		Program([FuncDecl(Id(main),[],IntType,Block([])),FuncDecl(Id(_),[],VoidType,Block([])),FuncDecl(Id(foo),[],StringType,Block([])),FuncDecl(Id(foo2),[],BoolType,Block([])),FuncDecl(Id(foo3),[],FloatType,Block([]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,266))
	def test_67(self):
		"""AST_TEST_67"""
		input="""
            int main(){
                float a, b;
                a = 0;
                b = 0;
                if (a == 0){
                    if (b == 0)
                        printf("PT VSN");
                    else
                        printf("PT VN");
                }
                else
                    printf("Phuong trinh co mot nghiem la x: %d", -b / a);
                system("pause");
                return 0;
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,FloatType),VarDecl(b,FloatType),BinaryOp(=,Id(a),IntLiteral(0)),BinaryOp(=,Id(b),IntLiteral(0)),If(BinaryOp(==,Id(a),IntLiteral(0)),Block([If(BinaryOp(==,Id(b),IntLiteral(0)),CallExpr(Id(printf),[StringLiteral(PT VSN)]),CallExpr(Id(printf),[StringLiteral(PT VN)]))]),CallExpr(Id(printf),[StringLiteral(Phuong trinh co mot nghiem la x: %d),BinaryOp(/,UnaryOp(-,Id(b)),Id(a))])),CallExpr(Id(system),[StringLiteral(pause)]),Return(IntLiteral(0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,267))
	def test_68(self):
		"""AST_TEST_68"""
		input="""
            int main(){
                float a,b,c,d;
                a = 1;
                b = -2;
                c = 1;
                if(a == 0)
                {
                    if(b == 0)
                        {
                            if(c == 0)
                                printf("PT VSN!");
                            else
                                printf("PT VN!");
                        }
                    else
                        printf("PT co 1 Nghiem la: %f", -c/b);
                }
                else
                {
                    d = b*b - 4*a*c;
                    if (d < 0)
                        printf("PT VN!");
                    else if (d == 0)
                        printf("PT co Nghiem kep la: %f",-b/(2*a));
                    else
                        printf("PT co 2 Nghiem PB la: %f,%f",(-b+sqrt(d))/(2*a),(-b-sqrt(d))/(2*a));    
                }    
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,FloatType),VarDecl(b,FloatType),VarDecl(c,FloatType),VarDecl(d,FloatType),BinaryOp(=,Id(a),IntLiteral(1)),BinaryOp(=,Id(b),UnaryOp(-,IntLiteral(2))),BinaryOp(=,Id(c),IntLiteral(1)),If(BinaryOp(==,Id(a),IntLiteral(0)),Block([If(BinaryOp(==,Id(b),IntLiteral(0)),Block([If(BinaryOp(==,Id(c),IntLiteral(0)),CallExpr(Id(printf),[StringLiteral(PT VSN!)]),CallExpr(Id(printf),[StringLiteral(PT VN!)]))]),CallExpr(Id(printf),[StringLiteral(PT co 1 Nghiem la: %f),BinaryOp(/,UnaryOp(-,Id(c)),Id(b))]))]),Block([BinaryOp(=,Id(d),BinaryOp(-,BinaryOp(*,Id(b),Id(b)),BinaryOp(*,BinaryOp(*,IntLiteral(4),Id(a)),Id(c)))),If(BinaryOp(<,Id(d),IntLiteral(0)),CallExpr(Id(printf),[StringLiteral(PT VN!)]),If(BinaryOp(==,Id(d),IntLiteral(0)),CallExpr(Id(printf),[StringLiteral(PT co Nghiem kep la: %f),BinaryOp(/,UnaryOp(-,Id(b)),BinaryOp(*,IntLiteral(2),Id(a)))]),CallExpr(Id(printf),[StringLiteral(PT co 2 Nghiem PB la: %f,%f),BinaryOp(/,BinaryOp(+,UnaryOp(-,Id(b)),CallExpr(Id(sqrt),[Id(d)])),BinaryOp(*,IntLiteral(2),Id(a))),BinaryOp(/,BinaryOp(-,UnaryOp(-,Id(b)),CallExpr(Id(sqrt),[Id(d)])),BinaryOp(*,IntLiteral(2),Id(a)))])))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,268))
	def test_69(self):
		"""AST_TEST_69"""
		input="""
            int main(){
                int n1, n2;
                n1 = 100;
                n2 = 50;
                do
                {
                    if(n1 > n2)
                        n1 = n1 - n2;
                    else
                        n2 = n2 - n1;
                }while (n1 != n2);
                printf("GCD = %d", n1);
                return 0;
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(n1,IntType),VarDecl(n2,IntType),BinaryOp(=,Id(n1),IntLiteral(100)),BinaryOp(=,Id(n2),IntLiteral(50)),Dowhile([Block([If(BinaryOp(>,Id(n1),Id(n2)),BinaryOp(=,Id(n1),BinaryOp(-,Id(n1),Id(n2))),BinaryOp(=,Id(n2),BinaryOp(-,Id(n2),Id(n1))))])],BinaryOp(!=,Id(n1),Id(n2))),CallExpr(Id(printf),[StringLiteral(GCD = %d),Id(n1)]),Return(IntLiteral(0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,269))
	def test_7(self):
		"""AST_TEST_7"""
		input="""
            int a, b, c[9];
            float x, y, z;
        """
		Program([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,ArrayType(IntType,9)),VarDecl(x,FloatType),VarDecl(y,FloatType),VarDecl(z,FloatType)])
		self.assertTrue(TestAST.checkASTGen(input,expect,207))
	def test_70(self):
		"""AST_TEST_70"""
		input="""
            int main(){
                int n;
                n = 20;

                if(n % 2 == 0)
                    printf("%d is even.", n);
                else
                    printf("%d is odd.", n);
                return 0;
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(n,IntType),BinaryOp(=,Id(n),IntLiteral(20)),If(BinaryOp(==,BinaryOp(%,Id(n),IntLiteral(2)),IntLiteral(0)),CallExpr(Id(printf),[StringLiteral(%d is even.),Id(n)]),CallExpr(Id(printf),[StringLiteral(%d is odd.),Id(n)])),Return(IntLiteral(0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,270))
	def test_71(self):
		"""AST_TEST_71"""
		input="""
            int main(){
                float n1, n2, n3;
                n1 = 2;
                n2 = 3;
                n3 = 1;
                if( n1 >= n2 && n1 >= n3 )
                    printf(n1);
                if( n2 >= n1 && n2 >= n3 )
                    printf(n2);
                if( n3 >= n1 && n3 >= n2 )
                    printf(n3);
                return 0;
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(n1,FloatType),VarDecl(n2,FloatType),VarDecl(n3,FloatType),BinaryOp(=,Id(n1),IntLiteral(2)),BinaryOp(=,Id(n2),IntLiteral(3)),BinaryOp(=,Id(n3),IntLiteral(1)),If(BinaryOp(&&,BinaryOp(>=,Id(n1),Id(n2)),BinaryOp(>=,Id(n1),Id(n3))),CallExpr(Id(printf),[Id(n1)])),If(BinaryOp(&&,BinaryOp(>=,Id(n2),Id(n1)),BinaryOp(>=,Id(n2),Id(n3))),CallExpr(Id(printf),[Id(n2)])),If(BinaryOp(&&,BinaryOp(>=,Id(n3),Id(n1)),BinaryOp(>=,Id(n3),Id(n2))),CallExpr(Id(printf),[Id(n3)])),Return(IntLiteral(0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,271))
	def test_72(self):
		"""AST_TEST_72"""
		input="""
            int main(){
                float n1, n2, n3;
                n1 = 0;
                n2 = 0;
                n3 = 0;
                if (n1 >= n2)
                {
                    if(n1 >= n3)
                        printf(n1);
                    else
                        printf(n3);
                }
                else
                {
                    if(n2 >= n3)
                        printf(n2);
                    else
                        printf(n3);
                }
                
                return 0;
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(n1,FloatType),VarDecl(n2,FloatType),VarDecl(n3,FloatType),BinaryOp(=,Id(n1),IntLiteral(0)),BinaryOp(=,Id(n2),IntLiteral(0)),BinaryOp(=,Id(n3),IntLiteral(0)),If(BinaryOp(>=,Id(n1),Id(n2)),Block([If(BinaryOp(>=,Id(n1),Id(n3)),CallExpr(Id(printf),[Id(n1)]),CallExpr(Id(printf),[Id(n3)]))]),Block([If(BinaryOp(>=,Id(n2),Id(n3)),CallExpr(Id(printf),[Id(n2)]),CallExpr(Id(printf),[Id(n3)]))])),Return(IntLiteral(0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,272))
	def test_73(self):
		"""AST_TEST_73"""
		input="""
            int main(){
                float n;
                n = 1.2E-12;
                if (number <= 0.0)
                {
                    if (number == 0.0)
                        printf("You entered 0!");
                    else
                        printf("You entered a negative number!");
                }
                else
                    printf("You entered a positive number!");
                return 0;
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(n,FloatType),BinaryOp(=,Id(n),FloatLiteral(1.2e-12)),If(BinaryOp(<=,Id(number),FloatLiteral(0.0)),Block([If(BinaryOp(==,Id(number),FloatLiteral(0.0)),CallExpr(Id(printf),[StringLiteral(You entered 0!)]),CallExpr(Id(printf),[StringLiteral(You entered a negative number!)]))]),CallExpr(Id(printf),[StringLiteral(You entered a positive number!)])),Return(IntLiteral(0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,273))
	def test_74(self):
		"""AST_TEST_74"""
		input="""
            int main(){
                int n, i, s;
                n = 100;
                s = 0;
                for(i = 1; i <= n; i = i + 1)
                {
                    s = s + i;
                }
                printf(s);
                return 0;
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(n,IntType),VarDecl(i,IntType),VarDecl(s,IntType),BinaryOp(=,Id(n),IntLiteral(100)),BinaryOp(=,Id(s),IntLiteral(0)),For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<=,Id(i),Id(n));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,Id(s),BinaryOp(+,Id(s),Id(i)))])),CallExpr(Id(printf),[Id(s)]),Return(IntLiteral(0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,274))
	def test_75(self):
		"""AST_TEST_75"""
		input="""
            int main(){
                int n, i, s;
                n = 100;
                s = 1;
                for(i = 2; i <= n; i = i + 1)
                {
                    s = s * i;
                }
                printf(s);
                return 0;
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(n,IntType),VarDecl(i,IntType),VarDecl(s,IntType),BinaryOp(=,Id(n),IntLiteral(100)),BinaryOp(=,Id(s),IntLiteral(1)),For(BinaryOp(=,Id(i),IntLiteral(2));BinaryOp(<=,Id(i),Id(n));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,Id(s),BinaryOp(*,Id(s),Id(i)))])),CallExpr(Id(printf),[Id(s)]),Return(IntLiteral(0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,275))
	def test_76(self):
		"""AST_TEST_76"""
		input="""
            int main(){
                int n, reversedNumber, remainder;
                n = 18071999;
                reversedNumber = 0;
                for(n; n != 0; n = n / 10){
                    remainder = n % 10;
                    reversedNumber = reversedNumber*10 + remainder;
                }
                printf(reversedNumber);
                return 0;
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(n,IntType),VarDecl(reversedNumber,IntType),VarDecl(remainder,IntType),BinaryOp(=,Id(n),IntLiteral(18071999)),BinaryOp(=,Id(reversedNumber),IntLiteral(0)),For(Id(n);BinaryOp(!=,Id(n),IntLiteral(0));BinaryOp(=,Id(n),BinaryOp(/,Id(n),IntLiteral(10)));Block([BinaryOp(=,Id(remainder),BinaryOp(%,Id(n),IntLiteral(10))),BinaryOp(=,Id(reversedNumber),BinaryOp(+,BinaryOp(*,Id(reversedNumber),IntLiteral(10)),Id(remainder)))])),CallExpr(Id(printf),[Id(reversedNumber)]),Return(IntLiteral(0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,276))
	def test_77(self):
		"""AST_TEST_77"""
		input="""
            int main(){
                int n, reversedInteger, remainder, originalInteger;
                n = 18071999;
                reversedInteger = 0;   
                originalInteger = n;
                for(n; n != 0; n = n / 10){
                    remainder = n % 10;
                    reversedInteger = reversedInteger*10 + remainder;
                }
                if (originalInteger == reversedInteger)
                    printf("%d is a palindrome.", originalInteger);
                else
                    printf("%d is not a palindrome.", originalInteger);
                return 0;
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(n,IntType),VarDecl(reversedInteger,IntType),VarDecl(remainder,IntType),VarDecl(originalInteger,IntType),BinaryOp(=,Id(n),IntLiteral(18071999)),BinaryOp(=,Id(reversedInteger),IntLiteral(0)),BinaryOp(=,Id(originalInteger),Id(n)),For(Id(n);BinaryOp(!=,Id(n),IntLiteral(0));BinaryOp(=,Id(n),BinaryOp(/,Id(n),IntLiteral(10)));Block([BinaryOp(=,Id(remainder),BinaryOp(%,Id(n),IntLiteral(10))),BinaryOp(=,Id(reversedInteger),BinaryOp(+,BinaryOp(*,Id(reversedInteger),IntLiteral(10)),Id(remainder)))])),If(BinaryOp(==,Id(originalInteger),Id(reversedInteger)),CallExpr(Id(printf),[StringLiteral(%d is a palindrome.),Id(originalInteger)]),CallExpr(Id(printf),[StringLiteral(%d is not a palindrome.),Id(originalInteger)])),Return(IntLiteral(0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,277))
	def test_78(self):
		"""AST_TEST_78"""
		input="""
            int main(){
                int n, i, flag;
                n = 100;
                flag = 0;
                for(i = 2; i <= n/2; i = i + 1)
                {
                    if(n % i == 0)
                    {
                        flag = 1;
                        break;
                    }
                }
                if (n == 1){
                    printf("1 is neither a prime nor a composite number.");
                }
                else{
                    if (flag == 0)
                        printf("%d is a prime number.", n);
                    else
                        printf("%d is not a prime number.", n);
                }
                return 0;
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(n,IntType),VarDecl(i,IntType),VarDecl(flag,IntType),BinaryOp(=,Id(n),IntLiteral(100)),BinaryOp(=,Id(flag),IntLiteral(0)),For(BinaryOp(=,Id(i),IntLiteral(2));BinaryOp(<=,Id(i),BinaryOp(/,Id(n),IntLiteral(2)));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,Id(n),Id(i)),IntLiteral(0)),Block([BinaryOp(=,Id(flag),IntLiteral(1)),Break()]))])),If(BinaryOp(==,Id(n),IntLiteral(1)),Block([CallExpr(Id(printf),[StringLiteral(1 is neither a prime nor a composite number.)])]),Block([If(BinaryOp(==,Id(flag),IntLiteral(0)),CallExpr(Id(printf),[StringLiteral(%d is a prime number.),Id(n)]),CallExpr(Id(printf),[StringLiteral(%d is not a prime number.),Id(n)]))])),Return(IntLiteral(0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,278))
	def test_79(self):
		"""AST_TEST_79"""
		input="""
            int main(){
                int n, originalNumber, remainder, result;
                n = 7;
                result = 0;
                originalNumber = number;
                for(originalNumber; originalNumber != 0; originalNumber = originalNumber / 10){
                    remainder = originalNumber % 10;
                    result = result + remainder * remainder * remainder;
                }
                if(result == number)
                    printf("%d is an Armstrong number.", number);
                else
                    printf("%d is not an Armstrong number.", number);
                return 0;
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(n,IntType),VarDecl(originalNumber,IntType),VarDecl(remainder,IntType),VarDecl(result,IntType),BinaryOp(=,Id(n),IntLiteral(7)),BinaryOp(=,Id(result),IntLiteral(0)),BinaryOp(=,Id(originalNumber),Id(number)),For(Id(originalNumber);BinaryOp(!=,Id(originalNumber),IntLiteral(0));BinaryOp(=,Id(originalNumber),BinaryOp(/,Id(originalNumber),IntLiteral(10)));Block([BinaryOp(=,Id(remainder),BinaryOp(%,Id(originalNumber),IntLiteral(10))),BinaryOp(=,Id(result),BinaryOp(+,Id(result),BinaryOp(*,BinaryOp(*,Id(remainder),Id(remainder)),Id(remainder))))])),If(BinaryOp(==,Id(result),Id(number)),CallExpr(Id(printf),[StringLiteral(%d is an Armstrong number.),Id(number)]),CallExpr(Id(printf),[StringLiteral(%d is not an Armstrong number.),Id(number)])),Return(IntLiteral(0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,279))
	def test_8(self):
		"""AST_TEST_8"""
		input="""
            int a, b, c[9];
            float x, y, z;
            boolean c, d, e[10];
            string g, h, i[5];
        """
		Program([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,ArrayType(IntType,9)),VarDecl(x,FloatType),VarDecl(y,FloatType),VarDecl(z,FloatType),VarDecl(c,BoolType),VarDecl(d,BoolType),VarDecl(e,ArrayType(BoolType,10)),VarDecl(g,StringType),VarDecl(h,StringType),VarDecl(i,ArrayType(StringType,5))])
		self.assertTrue(TestAST.checkASTGen(input,expect,208))
	def test_80(self):
		"""AST_TEST_80"""
		input="""
            int main(){
                int number, i;
                number = 37;
                for(i=1; i <= number; i = i + 1)
                {
                    if (number % i == 0)
                        printf(i);
                }
                return 0;
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(number,IntType),VarDecl(i,IntType),BinaryOp(=,Id(number),IntLiteral(37)),For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<=,Id(i),Id(number));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,Id(number),Id(i)),IntLiteral(0)),CallExpr(Id(printf),[Id(i)]))])),Return(IntLiteral(0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,280))
	def test_81(self):
		"""AST_TEST_81"""
		input="""
            int main(){
                int i, j, rows;
                rows = 10;
                for(i = 1; i<=rows; i = i + 1){
                    for(j = 1; j<=i; j = j + 1){
                        printf("* ");
                    }
                    printf("\n");
                }
                return 0;
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(i,IntType),VarDecl(j,IntType),VarDecl(rows,IntType),BinaryOp(=,Id(rows),IntLiteral(10)),For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<=,Id(i),Id(rows));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([For(BinaryOp(=,Id(j),IntLiteral(1));BinaryOp(<=,Id(j),Id(i));BinaryOp(=,Id(j),BinaryOp(+,Id(j),IntLiteral(1)));Block([CallExpr(Id(printf),[StringLiteral(* )])])),CallExpr(Id(printf),[StringLiteral(\n)])])),Return(IntLiteral(0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,281))
	def test_82(self):
		"""AST_TEST_82"""
		input="""
            int main(){
                int i, j, rows;
                rows = 10;
                for(i=rows; i>=1; --i){
                    for(j=1; j<=i; j = j + 1){
                        printf("* ");
                    }
                    printf("\n");
                }
                return 0;
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(i,IntType),VarDecl(j,IntType),VarDecl(rows,IntType),BinaryOp(=,Id(rows),IntLiteral(10)),For(BinaryOp(=,Id(i),Id(rows));BinaryOp(>=,Id(i),IntLiteral(1));UnaryOp(-,UnaryOp(-,Id(i)));Block([For(BinaryOp(=,Id(j),IntLiteral(1));BinaryOp(<=,Id(j),Id(i));BinaryOp(=,Id(j),BinaryOp(+,Id(j),IntLiteral(1)));Block([CallExpr(Id(printf),[StringLiteral(* )])])),CallExpr(Id(printf),[StringLiteral(\n)])])),Return(IntLiteral(0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,282))
	def test_83(self):
		"""AST_TEST_83"""
		input="""
            int foo(){
                int n, i, flag;
                flag = 1;
                for(i = 2; i <= n / 2; i = i + 1){
                    if(n % i == 0){
                        flag = 0;
                        break;
                    }
                }
                return flag;
            }
        """
		Program([FuncDecl(Id(foo),[],IntType,Block([VarDecl(n,IntType),VarDecl(i,IntType),VarDecl(flag,IntType),BinaryOp(=,Id(flag),IntLiteral(1)),For(BinaryOp(=,Id(i),IntLiteral(2));BinaryOp(<=,Id(i),BinaryOp(/,Id(n),IntLiteral(2)));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,Id(n),Id(i)),IntLiteral(0)),Block([BinaryOp(=,Id(flag),IntLiteral(0)),Break()]))])),Return(Id(flag))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,283))
	def test_84(self):
		"""AST_TEST_84"""
		input="""
            int addNumbers(int n){
                if(n != 0)
                    return n + addNumbers(n-1);
                else
                    return n;
            }
        """
		Program([FuncDecl(Id(addNumbers),[VarDecl(n,IntType)],IntType,Block([If(BinaryOp(!=,Id(n),IntLiteral(0)),Return(BinaryOp(+,Id(n),CallExpr(Id(addNumbers),[BinaryOp(-,Id(n),IntLiteral(1))]))),Return(Id(n)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,284))
	def test_85(self):
		"""AST_TEST_85"""
		input="""
            int foo(int n1, int n2){
                if (n2 != 0)
                return foo(n2, n1 % n2);
                else 
                return n1;
            }

        """
		Program([FuncDecl(Id(foo),[VarDecl(n1,IntType),VarDecl(n2,IntType)],IntType,Block([If(BinaryOp(!=,Id(n2),IntLiteral(0)),Return(CallExpr(Id(foo),[Id(n2),BinaryOp(%,Id(n1),Id(n2))])),Return(Id(n1)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,285))
	def test_86(self):
		"""AST_TEST_86"""
		input="""
            int convertDecimalToBinary(int n){
                int binaryNumber;
                binaryNumber = 0;
                int remainder, i, step;
                i = 1; 
                step = 1;
                for(n; n != 0; n = n / 2)
                {
                    remainder = n % 2;
                    printf("Step %d: %d / 2, Remainder = %d, Quotient = %d\n", step = step + 1, n, remainder, n / 2);
                    binaryNumber = binaryNumber + remainder*i;
                    i = i * 10;
                }
                return binaryNumber;
            }
        """
		Program([FuncDecl(Id(convertDecimalToBinary),[VarDecl(n,IntType)],IntType,Block([VarDecl(binaryNumber,IntType),BinaryOp(=,Id(binaryNumber),IntLiteral(0)),VarDecl(remainder,IntType),VarDecl(i,IntType),VarDecl(step,IntType),BinaryOp(=,Id(i),IntLiteral(1)),BinaryOp(=,Id(step),IntLiteral(1)),For(Id(n);BinaryOp(!=,Id(n),IntLiteral(0));BinaryOp(=,Id(n),BinaryOp(/,Id(n),IntLiteral(2)));Block([BinaryOp(=,Id(remainder),BinaryOp(%,Id(n),IntLiteral(2))),CallExpr(Id(printf),[StringLiteral(Step %d: %d / 2, Remainder = %d, Quotient = %d\n),BinaryOp(=,Id(step),BinaryOp(+,Id(step),IntLiteral(1))),Id(n),Id(remainder),BinaryOp(/,Id(n),IntLiteral(2))]),BinaryOp(=,Id(binaryNumber),BinaryOp(+,Id(binaryNumber),BinaryOp(*,Id(remainder),Id(i)))),BinaryOp(=,Id(i),BinaryOp(*,Id(i),IntLiteral(10)))])),Return(Id(binaryNumber))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,286))
	def test_87(self):
		"""AST_TEST_87"""
		input="""
            int convertDecimalToOctal(int decimalNumber){
                int octalNumber, i;
                octalNumber = 0;
                i = 1;
                for(decimalNumber; decimalNumber != 0; decimalNumber = decimalNumber / 8){
                    octalNumber = octalNumber + (decimalNumber % 8) * i;
                    i = i * 10;
                }
                return octalNumber;
            }
        """
		Program([FuncDecl(Id(convertDecimalToOctal),[VarDecl(decimalNumber,IntType)],IntType,Block([VarDecl(octalNumber,IntType),VarDecl(i,IntType),BinaryOp(=,Id(octalNumber),IntLiteral(0)),BinaryOp(=,Id(i),IntLiteral(1)),For(Id(decimalNumber);BinaryOp(!=,Id(decimalNumber),IntLiteral(0));BinaryOp(=,Id(decimalNumber),BinaryOp(/,Id(decimalNumber),IntLiteral(8)));Block([BinaryOp(=,Id(octalNumber),BinaryOp(+,Id(octalNumber),BinaryOp(*,BinaryOp(%,Id(decimalNumber),IntLiteral(8)),Id(i)))),BinaryOp(=,Id(i),BinaryOp(*,Id(i),IntLiteral(10)))])),Return(Id(octalNumber))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,287))
	def test_88(self):
		"""AST_TEST_88"""
		input="""
            int power(int base, int powerRaised){
                if (powerRaised != 0)
                    return (base * power(base, powerRaised - 1));
                else
                    return 1;
            }
        """
		Program([FuncDecl(Id(power),[VarDecl(base,IntType),VarDecl(powerRaised,IntType)],IntType,Block([If(BinaryOp(!=,Id(powerRaised),IntLiteral(0)),Return(BinaryOp(*,Id(base),CallExpr(Id(power),[Id(base),BinaryOp(-,Id(powerRaised),IntLiteral(1))]))),Return(IntLiteral(1)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,288))
	def test_89(self):
		"""AST_TEST_89"""
		input="""
            int main(){
                int n, i;
                float num[100], sum, average;
                n = 100;
                sum = 0.0;  
                for(i = 0; i < n; i = i + 1){ 
                    sum = sum + num[i];
                }
                average = sum / n;
                printf(average);
                return 0;
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(n,IntType),VarDecl(i,IntType),VarDecl(num,ArrayType(FloatType,100)),VarDecl(sum,FloatType),VarDecl(average,FloatType),BinaryOp(=,Id(n),IntLiteral(100)),BinaryOp(=,Id(sum),FloatLiteral(0.0)),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),Id(n));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,Id(sum),BinaryOp(+,Id(sum),ArrayCell(Id(num),Id(i))))])),BinaryOp(=,Id(average),BinaryOp(/,Id(sum),Id(n))),CallExpr(Id(printf),[Id(average)]),Return(IntLiteral(0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,289))
	def test_9(self):
		"""AST_TEST_9"""
		input="""
            int a[1], b[2], c[3];
            float x[4], y[5], z[6];
            boolean c[7], d[8], e[9];
            string g[10], h[11], i[12];
        """
		Program([VarDecl(a,ArrayType(IntType,1)),VarDecl(b,ArrayType(IntType,2)),VarDecl(c,ArrayType(IntType,3)),VarDecl(x,ArrayType(FloatType,4)),VarDecl(y,ArrayType(FloatType,5)),VarDecl(z,ArrayType(FloatType,6)),VarDecl(c,ArrayType(BoolType,7)),VarDecl(d,ArrayType(BoolType,8)),VarDecl(e,ArrayType(BoolType,9)),VarDecl(g,ArrayType(StringType,10)),VarDecl(h,ArrayType(StringType,11)),VarDecl(i,ArrayType(StringType,12))])
		self.assertTrue(TestAST.checkASTGen(input,expect,209))
	def test_90(self):
		"""AST_TEST_90"""
		input="""
            int main(){
                int i, n;
                float arr[100];
                n = 10;
                for(i = 1; i < n; i = i + 1){
                if(arr[0] < arr[i])
                    arr[0] = arr[i];
                }
                printf(arr[0]);
                return 0;
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(i,IntType),VarDecl(n,IntType),VarDecl(arr,ArrayType(FloatType,100)),BinaryOp(=,Id(n),IntLiteral(10)),For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),Id(n));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(<,ArrayCell(Id(arr),IntLiteral(0)),ArrayCell(Id(arr),Id(i))),BinaryOp(=,ArrayCell(Id(arr),IntLiteral(0)),ArrayCell(Id(arr),Id(i))))])),CallExpr(Id(printf),[ArrayCell(Id(arr),IntLiteral(0))]),Return(IntLiteral(0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,290))
	def test_91(self):
		"""AST_TEST_91"""
		input="""
            void Swap(int a, int b, int c){
                int temp;
                temp = b;
                b = a;
                a = c;
                c = temp;
            }
        """
		Program([FuncDecl(Id(Swap),[VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,IntType)],VoidType,Block([VarDecl(temp,IntType),BinaryOp(=,Id(temp),Id(b)),BinaryOp(=,Id(b),Id(a)),BinaryOp(=,Id(a),Id(c)),BinaryOp(=,Id(c),Id(temp))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,291))
	def test_92(self):
		"""AST_TEST_92"""
		input="""
            float CV(float a, float b, float c){
                int p;
                p = 0;
                if (a < b + c || b < a + c || c < a + b){
                    p = a + b + c;
                    return p;
                }
                else printf("Error!");
            }
        """
		Program([FuncDecl(Id(CV),[VarDecl(a,FloatType),VarDecl(b,FloatType),VarDecl(c,FloatType)],FloatType,Block([VarDecl(p,IntType),BinaryOp(=,Id(p),IntLiteral(0)),If(BinaryOp(||,BinaryOp(||,BinaryOp(<,Id(a),BinaryOp(+,Id(b),Id(c))),BinaryOp(<,Id(b),BinaryOp(+,Id(a),Id(c)))),BinaryOp(<,Id(c),BinaryOp(+,Id(a),Id(b)))),Block([BinaryOp(=,Id(p),BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(c))),Return(Id(p))]),CallExpr(Id(printf),[StringLiteral(Error!)]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,292))
	def test_93(self):
		"""AST_TEST_93"""
		input="""
            float S(float a, float b, float c){
                int s, p;
                p = 0;
                s = 1;
                if (a < b + c || b < a + c || c < a + b){
                    p = (a + b + c) / 2;
                    s = sqrt(p*(p - a)*(p - b)*(p - c));
                    return s;
                }
                else{ 
                    printf("Error!");
                    return 0;
                    }
            }
        """
		Program([FuncDecl(Id(S),[VarDecl(a,FloatType),VarDecl(b,FloatType),VarDecl(c,FloatType)],FloatType,Block([VarDecl(s,IntType),VarDecl(p,IntType),BinaryOp(=,Id(p),IntLiteral(0)),BinaryOp(=,Id(s),IntLiteral(1)),If(BinaryOp(||,BinaryOp(||,BinaryOp(<,Id(a),BinaryOp(+,Id(b),Id(c))),BinaryOp(<,Id(b),BinaryOp(+,Id(a),Id(c)))),BinaryOp(<,Id(c),BinaryOp(+,Id(a),Id(b)))),Block([BinaryOp(=,Id(p),BinaryOp(/,BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(c)),IntLiteral(2))),BinaryOp(=,Id(s),CallExpr(Id(sqrt),[BinaryOp(*,BinaryOp(*,BinaryOp(*,Id(p),BinaryOp(-,Id(p),Id(a))),BinaryOp(-,Id(p),Id(b))),BinaryOp(-,Id(p),Id(c)))])),Return(Id(s))]),Block([CallExpr(Id(printf),[StringLiteral(Error!)]),Return(IntLiteral(0))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,293))
	def test_94(self):
		"""AST_TEST_94"""
		input="""
            float CV(float R){
                int PI, p;
                p = 1;
                if (n > 0){
                    p = 2 * PI * R;
                    return p;
                }
                else{ 
                    printf("MATH007!");
                    return 0;
                    }
            }
        """
		Program([FuncDecl(Id(CV),[VarDecl(R,FloatType)],FloatType,Block([VarDecl(PI,IntType),VarDecl(p,IntType),BinaryOp(=,Id(p),IntLiteral(1)),If(BinaryOp(>,Id(n),IntLiteral(0)),Block([BinaryOp(=,Id(p),BinaryOp(*,BinaryOp(*,IntLiteral(2),Id(PI)),Id(R))),Return(Id(p))]),Block([CallExpr(Id(printf),[StringLiteral(MATH007!)]),Return(IntLiteral(0))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,294))
	def test_95(self):
		"""AST_TEST_95"""
		input="""
            float S(float R){
                int s, PI;
                s = 1;
                if (R > 0){
                    s = PI * R * R;
                    return s;
                }
                else{ 
                    printf("MATH007!");
                    return 0;
                    }
            }
        """
		Program([FuncDecl(Id(S),[VarDecl(R,FloatType)],FloatType,Block([VarDecl(s,IntType),VarDecl(PI,IntType),BinaryOp(=,Id(s),IntLiteral(1)),If(BinaryOp(>,Id(R),IntLiteral(0)),Block([BinaryOp(=,Id(s),BinaryOp(*,BinaryOp(*,Id(PI),Id(R)),Id(R))),Return(Id(s))]),Block([CallExpr(Id(printf),[StringLiteral(MATH007!)]),Return(IntLiteral(0))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,295))
	def test_96(self):
		"""AST_TEST_96"""
		input="""
            int main(){
                int n;
                n = 100;
                if (n > 1) {
                    int i;
                    for (i = 2; i <= n; i = i + 1) {
                            int sus, j;
                            sus = 0;
                            for (j = 1; j <= i; j = j + 1) {
                                if ((i % j) == 0)
                                sus = sus + 1;
                            }
                            if (sus == 2)
                                printf(i);
                    }
                }       
                else printf("MATH007");
                return 0;
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(n,IntType),BinaryOp(=,Id(n),IntLiteral(100)),If(BinaryOp(>,Id(n),IntLiteral(1)),Block([VarDecl(i,IntType),For(BinaryOp(=,Id(i),IntLiteral(2));BinaryOp(<=,Id(i),Id(n));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([VarDecl(sus,IntType),VarDecl(j,IntType),BinaryOp(=,Id(sus),IntLiteral(0)),For(BinaryOp(=,Id(j),IntLiteral(1));BinaryOp(<=,Id(j),Id(i));BinaryOp(=,Id(j),BinaryOp(+,Id(j),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,Id(i),Id(j)),IntLiteral(0)),BinaryOp(=,Id(sus),BinaryOp(+,Id(sus),IntLiteral(1))))])),If(BinaryOp(==,Id(sus),IntLiteral(2)),CallExpr(Id(printf),[Id(i)]))]))]),CallExpr(Id(printf),[StringLiteral(MATH007)])),Return(IntLiteral(0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,296))
	def test_97(self):
		"""AST_TEST_97"""
		input="""
            int main(){
                int n; 
                n = 100;
                float res, temp;
                res = 1.0;
                temp = 1.0;
                int i;
                for (i=0; i <= n; i = i + 1){
                    temp = temp * (2.0 * (i + 1.0)) / (2.0 * i + 3.0);
                    res = res + temp;
                }
            printf(res);
            return 0;
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(n,IntType),BinaryOp(=,Id(n),IntLiteral(100)),VarDecl(res,FloatType),VarDecl(temp,FloatType),BinaryOp(=,Id(res),FloatLiteral(1.0)),BinaryOp(=,Id(temp),FloatLiteral(1.0)),VarDecl(i,IntType),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<=,Id(i),Id(n));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,Id(temp),BinaryOp(/,BinaryOp(*,Id(temp),BinaryOp(*,FloatLiteral(2.0),BinaryOp(+,Id(i),FloatLiteral(1.0)))),BinaryOp(+,BinaryOp(*,FloatLiteral(2.0),Id(i)),FloatLiteral(3.0)))),BinaryOp(=,Id(res),BinaryOp(+,Id(res),Id(temp)))])),CallExpr(Id(printf),[Id(res)]),Return(IntLiteral(0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,297))
	def test_98(self):
		"""AST_TEST_98"""
		input="""
            int main(){
                int a, b, sa, sb, i;
                a = 100;
                b = 200;
                sa = 0; 
                sb = 0;
                for (i = 1; i < a; i = i + 1) {
                    if (a % i == 0)
                        sa = sa + i;
                }
                for (i = 1; i < b; i = i + 1) {
                    if (b % i == 0)
                        sb = sb + i;
                }
                if (sa == b && sb == a) 
                    printf("YES");
                else 
                    printf("NO");
                printf("\n"); 
                return 0;
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(sa,IntType),VarDecl(sb,IntType),VarDecl(i,IntType),BinaryOp(=,Id(a),IntLiteral(100)),BinaryOp(=,Id(b),IntLiteral(200)),BinaryOp(=,Id(sa),IntLiteral(0)),BinaryOp(=,Id(sb),IntLiteral(0)),For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),Id(a));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,Id(a),Id(i)),IntLiteral(0)),BinaryOp(=,Id(sa),BinaryOp(+,Id(sa),Id(i))))])),For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),Id(b));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,Id(b),Id(i)),IntLiteral(0)),BinaryOp(=,Id(sb),BinaryOp(+,Id(sb),Id(i))))])),If(BinaryOp(&&,BinaryOp(==,Id(sa),Id(b)),BinaryOp(==,Id(sb),Id(a))),CallExpr(Id(printf),[StringLiteral(YES)]),CallExpr(Id(printf),[StringLiteral(NO)])),CallExpr(Id(printf),[StringLiteral(\n)]),Return(IntLiteral(0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,298))
	def test_99(self):
		"""AST_TEST_99"""
		input="""
            int main(){
                int n, a, b, i, j;
                a = 1;
                b = 0;
                if (n < 5) 
                    printf("Error!");
                else{
                    for (i = 1; i < n; i = i + 1){
                        for (j = i + 1; j < n; j = j + 1){
                            float z;
                            z = sqrt(i * i + j * j);
                        }
                    }
                    printf(z);
                }
                return 0;
            }
        """
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(n,IntType),VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(i,IntType),VarDecl(j,IntType),BinaryOp(=,Id(a),IntLiteral(1)),BinaryOp(=,Id(b),IntLiteral(0)),If(BinaryOp(<,Id(n),IntLiteral(5)),CallExpr(Id(printf),[StringLiteral(Error!)]),Block([For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),Id(n));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([For(BinaryOp(=,Id(j),BinaryOp(+,Id(i),IntLiteral(1)));BinaryOp(<,Id(j),Id(n));BinaryOp(=,Id(j),BinaryOp(+,Id(j),IntLiteral(1)));Block([VarDecl(z,FloatType),BinaryOp(=,Id(z),CallExpr(Id(sqrt),[BinaryOp(+,BinaryOp(*,Id(i),Id(i)),BinaryOp(*,Id(j),Id(j)))]))]))])),CallExpr(Id(printf),[Id(z)])])),Return(IntLiteral(0))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,299))
	def test_0(self):
		"""AST_TEST_0"""
		input=""" int a[1];"""
		Program([VarDecl(a,ArrayType(IntType,1))])
		self.assertTrue(TestAST.checkASTGen(input,expect,300))
	def test_1(self):
		"""AST_TEST_1"""
		input=""" void main(int d){a;}"""
		Program([FuncDecl(Id(main),[VarDecl(d,IntType)],VoidType,Block([Id(a)]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,301))
	def test_10(self):
		"""AST_TEST_10"""
		input="""
    int am(){
        a = b + c*d;
    }
    """
		Program([FuncDecl(Id(am),[],IntType,Block([BinaryOp(=,Id(a),BinaryOp(+,Id(b),BinaryOp(*,Id(c),Id(d))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,310))
	def test_11(self):
		"""AST_TEST_11"""
		input=""" 
    void linh(){
        if(a<b) a=b;
    }
    """
		Program([FuncDecl(Id(linh),[],VoidType,Block([If(BinaryOp(<,Id(a),Id(b)),BinaryOp(=,Id(a),Id(b)))]))])
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
		Program([FuncDecl(Id(maxlist),[VarDecl(lst,IntType)],VoidType,Block([For(Id(i);BinaryOp(<,Id(i),IntLiteral(1));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([For(Id(a);Id(a);Id(a);Block([]))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,312))
	def test_13(self):
		"""AST_TEST_13"""
		input="""
    void linh(){
        if(a<b) a=b;
    }
    """
		Program([FuncDecl(Id(linh),[],VoidType,Block([If(BinaryOp(<,Id(a),Id(b)),BinaryOp(=,Id(a),Id(b)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,313))
	def test_14(self):
		"""AST_TEST_14"""
		input="""
    void l(){ 
        a=(a*b)-c+c/e%q||a;
    }
    """
		Program([FuncDecl(Id(l),[],VoidType,Block([BinaryOp(=,Id(a),BinaryOp(||,BinaryOp(+,BinaryOp(-,BinaryOp(*,Id(a),Id(b)),Id(c)),BinaryOp(%,BinaryOp(/,Id(c),Id(e)),Id(q))),Id(a)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,314))
	def test_15(self):
		"""AST_TEST_15"""
		input="""
    int a,b;
    void main(){

    }
    int a[2];
    """
		Program([VarDecl(a,IntType),VarDecl(b,IntType),FuncDecl(Id(main),[],VoidType,Block([])),VarDecl(a,ArrayType(IntType,2))])
		self.assertTrue(TestAST.checkASTGen(input,expect,315))
	def test_16(self):
		"""AST_TEST_16"""
		input="""
    /*bascnsdvnnio2io3n1io2ks*//*assnajnjnfjasndasnj*/
    void main(){}
    """
		Program([FuncDecl(Id(main),[],VoidType,Block([]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,316))
	def test_17(self):
		"""AST_TEST_17"""
		input="""
    void main(){
        break;
    }
    """
		Program([FuncDecl(Id(main),[],VoidType,Block([Break()]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,317))
	def test_18(self):
		"""AST_TEST_18"""
		input="""
    void main(){
        break;
    }
    """
		Program([FuncDecl(Id(main),[],VoidType,Block([Break()]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,318))
	def test_19(self):
		"""AST_TEST_19"""
		input="""
    int main(){
        Break;
    }
    """
		Program([FuncDecl(Id(main),[],IntType,Block([Id(Break)]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,319))
	def test_2(self):
		"""AST_TEST_2"""
		input=""" int a,b,c,list[3]; """
		Program([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,IntType),VarDecl(list,ArrayType(IntType,3))])
		self.assertTrue(TestAST.checkASTGen(input,expect,302))
	def test_20(self):
		"""AST_TEST_20"""
		input="""
    int main(){
        countinue;
    }
    """
		Program([FuncDecl(Id(main),[],IntType,Block([Id(countinue)]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,320))
	def test_21(self):
		"""AST_TEST_21"""
		input="""
    int main(){
        continue;
    }
    """
		Program([FuncDecl(Id(main),[],IntType,Block([Continue()]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,321))
	def test_22(self):
		"""AST_TEST_22"""
		input="""
    int main(){
       {{{ continue;}}{a;}}
    }
    """
		Program([FuncDecl(Id(main),[],IntType,Block([Block([Block([Block([Continue()])]),Block([Id(a)])])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,322))
	def test_23(self):
		"""AST_TEST_23"""
		input="""
    int main(){
        if ((a<1))  {c=a+1;}
    }
    """
		Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(<,Id(a),IntLiteral(1)),Block([BinaryOp(=,Id(c),BinaryOp(+,Id(a),IntLiteral(1)))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,323))
	def test_24(self):
		"""AST_TEST_24"""
		input="""
    int main(){
        if ((a<1))  {c=a+1;}
        else {{{{{{{}}}}}}}
    }
    """
		Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(<,Id(a),IntLiteral(1)),Block([BinaryOp(=,Id(c),BinaryOp(+,Id(a),IntLiteral(1)))]),Block([Block([Block([Block([Block([Block([Block([])])])])])])]))]))])
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
		Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(<,Id(a),IntLiteral(1)),Block([BinaryOp(=,Id(c),BinaryOp(+,Id(a),IntLiteral(1)))]),If(Id(a),Block([]),Block([])))]))])
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
		Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(<,Id(a),IntLiteral(1)),Block([BinaryOp(=,Id(c),BinaryOp(+,Id(a),IntLiteral(1)))]),If(Id(a),Block([]),Block([BinaryOp(+,Id(a),IntLiteral(1))])))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,326))
	def test_27(self):
		"""AST_TEST_27"""
		input="""
    int man(){
        a = a+1 = b+1;
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([BinaryOp(=,Id(a),BinaryOp(=,BinaryOp(+,Id(a),IntLiteral(1)),BinaryOp(+,Id(b),IntLiteral(1))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,327))
	def test_28(self):
		"""AST_TEST_28"""
		input="""
    int man(){
        a|| a && a+1 = b+1;
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([BinaryOp(=,BinaryOp(||,Id(a),BinaryOp(&&,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))),BinaryOp(+,Id(b),IntLiteral(1)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,328))
	def test_29(self):
		"""AST_TEST_29"""
		input="""
    int man(){
        a ---------b;
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([BinaryOp(-,Id(a),UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,Id(b))))))))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,329))
	def test_3(self):
		"""AST_TEST_3"""
		input="""int b[1], c;
        float c; 
        string k; 
        boolean n;
    """
		Program([VarDecl(b,ArrayType(IntType,1)),VarDecl(c,IntType),VarDecl(c,FloatType),VarDecl(k,StringType),VarDecl(n,BoolType)])
		self.assertTrue(TestAST.checkASTGen(input,expect,303))
	def test_30(self):
		"""AST_TEST_30"""
		input="""
    int man(){
        a[1] -b[n];
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([BinaryOp(-,ArrayCell(Id(a),IntLiteral(1)),ArrayCell(Id(b),Id(n)))]))])
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
		Program([FuncDecl(Id(man),[],IntType,Block([BinaryOp(-,ArrayCell(Id(a),IntLiteral(1)),ArrayCell(Id(b),Id(n))),CallExpr(Id(call),[]),CallExpr(Id(pull),[])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,331))
	def test_32(self):
		"""AST_TEST_32"""
		input="""
    int man(){
        call();
        pull();
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([CallExpr(Id(call),[]),CallExpr(Id(pull),[])]))])
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
		Program([FuncDecl(Id(man),[],IntType,Block([Dowhile([Id(a),Id(b),Id(c),Id(d)],Id(cc))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,333))
	def test_34(self):
		"""AST_TEST_34"""
		input="""
    int man(){
        {}{}{}{a;}
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([Block([]),Block([]),Block([]),Block([Id(a)])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,334))
	def test_35(self):
		"""AST_TEST_35"""
		input="""
    int man(){
        return ;
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([Return()]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,335))
	def test_36(self):
		"""AST_TEST_36"""
		input="""
    int man(){
        return a= 1 ;
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([Return(BinaryOp(=,Id(a),IntLiteral(1)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,336))
	def test_37(self):
		"""AST_TEST_37"""
		input="""
    int man(){
        return "a" ;
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([Return(StringLiteral(a))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,337))
	def test_38(self):
		"""AST_TEST_38"""
		input="""
    int A1man(){
        return "a" ;
    }
    """
		Program([FuncDecl(Id(A1man),[],IntType,Block([Return(StringLiteral(a))]))])
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
		Program([FuncDecl(Id(A1man),[],IntType,Block([Return(StringLiteral(a)),Block([Id(a),Id(b),Id(v)])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,339))
	def test_4(self):
		"""AST_TEST_4"""
		input="""
    int m,n;
    void a(int b, string c){}
    """
		Program([VarDecl(m,IntType),VarDecl(n,IntType),FuncDecl(Id(a),[VarDecl(b,IntType),VarDecl(c,StringType)],VoidType,Block([]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,304))
	def test_40(self):
		"""AST_TEST_40"""
		input="""
    int A1man(int b,string cc){
        return "a" ;
    }
    """
		Program([FuncDecl(Id(A1man),[VarDecl(b,IntType),VarDecl(cc,StringType)],IntType,Block([Return(StringLiteral(a))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,340))
	def test_41(self):
		"""AST_TEST_41"""
		input="""
    int main(int b,string cc){
        return true ;
    }
    """
		Program([FuncDecl(Id(main),[VarDecl(b,IntType),VarDecl(cc,StringType)],IntType,Block([Return(BooleanLiteral(true))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,341))
	def test_42(self):
		"""AST_TEST_42"""
		input="""
    int main(int b,string cc){
        return false ;
    }
    """
		Program([FuncDecl(Id(main),[VarDecl(b,IntType),VarDecl(cc,StringType)],IntType,Block([Return(BooleanLiteral(false))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,342))
	def test_43(self):
		"""AST_TEST_43"""
		input="""
    int main(int b,string cc){
        return false ;
    }
    """
		Program([FuncDecl(Id(main),[VarDecl(b,IntType),VarDecl(cc,StringType)],IntType,Block([Return(BooleanLiteral(false))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,343))
	def test_44(self):
		"""AST_TEST_44"""
		input="""
    int main(int b,string cc[]){
        return false ;
    }
    """
		Program([FuncDecl(Id(main),[VarDecl(b,IntType),VarDecl(cc,ArrayTypePointer(StringType))],IntType,Block([Return(BooleanLiteral(false))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,344))
	def test_45(self):
		"""AST_TEST_45"""
		input="""
    int main(int b,string cc[]){
        int  a [1];
    }
    """
		Program([FuncDecl(Id(main),[VarDecl(b,IntType),VarDecl(cc,ArrayTypePointer(StringType))],IntType,Block([VarDecl(a,ArrayType(IntType,1))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,345))
	def test_46(self):
		"""AST_TEST_46"""
		input="""
    int main(){
        d+e;
        a+c;
    }
    """
		Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(+,Id(d),Id(e)),BinaryOp(+,Id(a),Id(c))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,346))
	def test_47(self):
		"""AST_TEST_47"""
		input="""
    int main(){
        d+e;a+c;
    }
    """
		Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(+,Id(d),Id(e)),BinaryOp(+,Id(a),Id(c))]))])
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
		Program([FuncDecl(Id(man),[],IntType,Block([Dowhile([Id(a),Id(b),Id(c),Id(d)],Id(cc))]))])
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
		Program([FuncDecl(Id(man),[],IntType,Block([Dowhile([Id(a),Id(b),Id(c),Id(d)],Id(cc)),Dowhile([Id(a),Dowhile([Id(a),Id(b),Id(c),Id(d)],Id(a))],Id(a))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,349))
	def test_5(self):
		"""AST_TEST_5"""
		input="""
    void call(){ print("a"); }
    void main(){
        call();  // this is call functions
    }
    """
		Program([FuncDecl(Id(call),[],VoidType,Block([CallExpr(Id(print),[StringLiteral(a)])])),FuncDecl(Id(main),[],VoidType,Block([CallExpr(Id(call),[])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,305))
	def test_50(self):
		"""AST_TEST_50"""
		input="""
    void  main(){
    if (a<c||a =c) {}
    }
    """
		Program([FuncDecl(Id(main),[],VoidType,Block([If(BinaryOp(=,BinaryOp(||,BinaryOp(<,Id(a),Id(c)),Id(a)),Id(c)),Block([]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,350))
	def test_51(self):
		"""AST_TEST_51"""
		input="""
    void main(){
        break; break; continue;
    }
    """
		Program([FuncDecl(Id(main),[],VoidType,Block([Break(),Break(),Continue()]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,351))
	def test_52(self):
		"""AST_TEST_52"""
		input="""
    void main(){
        for(a;b;c){}
    }
    """
		Program([FuncDecl(Id(main),[],VoidType,Block([For(Id(a);Id(b);Id(c);Block([]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,352))
	def test_53(self):
		"""AST_TEST_53"""
		input="""
    void main(){
        if(a<a=b<c){

        }
    }
    """
		Program([FuncDecl(Id(main),[],VoidType,Block([If(BinaryOp(=,BinaryOp(<,Id(a),Id(a)),BinaryOp(<,Id(b),Id(c))),Block([]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,353))
	def test_54(self):
		"""AST_TEST_54"""
		input="""
    void main(){
        if(!a=a=bc){

        }
    }
    """
		Program([FuncDecl(Id(main),[],VoidType,Block([If(BinaryOp(=,UnaryOp(!,Id(a)),BinaryOp(=,Id(a),Id(bc))),Block([]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,354))
	def test_55(self):
		"""AST_TEST_55"""
		input="""
    void main(){
        if(true = false){

        }
    }
    """
		Program([FuncDecl(Id(main),[],VoidType,Block([If(BinaryOp(=,BooleanLiteral(true),BooleanLiteral(false)),Block([]))]))])
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
		Program([FuncDecl(Id(main),[],VoidType,Block([If(BinaryOp(=,BooleanLiteral(true),BooleanLiteral(false)),Block([BinaryOp(+,BooleanLiteral(true),Id(False))]))]))])
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
		Program([FuncDecl(Id(main),[],VoidType,Block([If(BinaryOp(=,BooleanLiteral(true),BooleanLiteral(false)),Block([BinaryOp(+,BooleanLiteral(true),Id(False))]))]))])
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
		Program([FuncDecl(Id(main),[],VoidType,Block([If(BinaryOp(=,BooleanLiteral(true),BooleanLiteral(false)),Block([BinaryOp(-,BinaryOp(+,UnaryOp(!,Id(a)),Id(b)),CallExpr(Id(iCallYou),[CallExpr(Id(calyou),[Id(a)])]))]))]))])
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
		Program([FuncDecl(Id(main),[],VoidType,Block([If(BinaryOp(=,BooleanLiteral(true),BooleanLiteral(false)),Block([If(Id(a),Block([]),Block([Id(a)]))]))]))])
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
		Program([FuncDecl(Id(main),[VarDecl(a,IntType),VarDecl(b,StringType)],VoidType,Block([Dowhile([Block([]),Block([]),Block([])],IntLiteral(1))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,306))
	def test_60(self):
		"""AST_TEST_60"""
		input="""
    void main(){
        a = true;
    }
    """
		Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),BooleanLiteral(true))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,360))
	def test_61(self):
		"""AST_TEST_61"""
		input="""
    void main(){
        b= e= true = fals;
    }
    """
		Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(b),BinaryOp(=,Id(e),BinaryOp(=,BooleanLiteral(true),Id(fals))))]))])
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
		Program([FuncDecl(Id(maxlist),[VarDecl(lst,IntType)],VoidType,Block([For(Id(i);BinaryOp(<,Id(i),IntLiteral(1));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([For(Id(a);Id(a);Id(a);Block([]))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,362))
	def test_63(self):
		"""AST_TEST_63"""
		input="""
    void linh(){
        if(a<b) a=b;
    }
    """
		Program([FuncDecl(Id(linh),[],VoidType,Block([If(BinaryOp(<,Id(a),Id(b)),BinaryOp(=,Id(a),Id(b)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,363))
	def test_64(self):
		"""AST_TEST_64"""
		input="""
    void l(){ 
        a=(a*b)-c+c/e%q||a;
    }
    """
		Program([FuncDecl(Id(l),[],VoidType,Block([BinaryOp(=,Id(a),BinaryOp(||,BinaryOp(+,BinaryOp(-,BinaryOp(*,Id(a),Id(b)),Id(c)),BinaryOp(%,BinaryOp(/,Id(c),Id(e)),Id(q))),Id(a)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,364))
	def test_65(self):
		"""AST_TEST_65"""
		input="""
    int a,b;
    void main(){

    }
    int a[2];
    """
		Program([VarDecl(a,IntType),VarDecl(b,IntType),FuncDecl(Id(main),[],VoidType,Block([])),VarDecl(a,ArrayType(IntType,2))])
		self.assertTrue(TestAST.checkASTGen(input,expect,365))
	def test_66(self):
		"""AST_TEST_66"""
		input="""
    /*bascnsdvnnio2io3n1io2ks*//*assnajnjnfjasndasnj*/
    void main(){}
    """
		Program([FuncDecl(Id(main),[],VoidType,Block([]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,366))
	def test_67(self):
		"""AST_TEST_67"""
		input="""
    void main(){
        break;
    }
    """
		Program([FuncDecl(Id(main),[],VoidType,Block([Break()]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,367))
	def test_68(self):
		"""AST_TEST_68"""
		input="""
    void main(){
        break;
    }
    """
		Program([FuncDecl(Id(main),[],VoidType,Block([Break()]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,368))
	def test_69(self):
		"""AST_TEST_69"""
		input="""
    int main(){
        Break;
    }
    """
		Program([FuncDecl(Id(main),[],IntType,Block([Id(Break)]))])
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
		Program([FuncDecl(Id(a),[],VoidType,Block([])),FuncDecl(Id(b),[],IntType,Block([])),FuncDecl(Id(c),[],StringType,Block([])),FuncDecl(Id(d),[],FloatType,Block([]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,307))
	def test_70(self):
		"""AST_TEST_70"""
		input="""
    int main(){
        countinue;
    }
    """
		Program([FuncDecl(Id(main),[],IntType,Block([Id(countinue)]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,370))
	def test_71(self):
		"""AST_TEST_71"""
		input="""
    int main(){
        continue;
    }
    """
		Program([FuncDecl(Id(main),[],IntType,Block([Continue()]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,371))
	def test_72(self):
		"""AST_TEST_72"""
		input="""
    int main(){
       {{{ continue;}}{a;}}
    }
    """
		Program([FuncDecl(Id(main),[],IntType,Block([Block([Block([Block([Continue()])]),Block([Id(a)])])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,372))
	def test_73(self):
		"""AST_TEST_73"""
		input="""
    int main(){
        if ((a<1))  {c=a+1;}
    }
    """
		Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(<,Id(a),IntLiteral(1)),Block([BinaryOp(=,Id(c),BinaryOp(+,Id(a),IntLiteral(1)))]))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,373))
	def test_74(self):
		"""AST_TEST_74"""
		input="""
    int main(){
        if ((a<1))  {c=a+1;}
        else {{{{{{{}}}}}}}
    }
    """
		Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(<,Id(a),IntLiteral(1)),Block([BinaryOp(=,Id(c),BinaryOp(+,Id(a),IntLiteral(1)))]),Block([Block([Block([Block([Block([Block([Block([])])])])])])]))]))])
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
		Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(<,Id(a),IntLiteral(1)),Block([BinaryOp(=,Id(c),BinaryOp(+,Id(a),IntLiteral(1)))]),If(Id(a),Block([]),Block([])))]))])
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
		Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(<,Id(a),IntLiteral(1)),Block([BinaryOp(=,Id(c),BinaryOp(+,Id(a),IntLiteral(1)))]),If(Id(a),Block([]),Block([BinaryOp(+,Id(a),IntLiteral(1))])))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,376))
	def test_77(self):
		"""AST_TEST_77"""
		input="""
    int man(){
        a = a+1 = b+1;
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([BinaryOp(=,Id(a),BinaryOp(=,BinaryOp(+,Id(a),IntLiteral(1)),BinaryOp(+,Id(b),IntLiteral(1))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,377))
	def test_78(self):
		"""AST_TEST_78"""
		input="""
    int man(){
        a|| a && a+1 = b+1;
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([BinaryOp(=,BinaryOp(||,Id(a),BinaryOp(&&,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))),BinaryOp(+,Id(b),IntLiteral(1)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,378))
	def test_79(self):
		"""AST_TEST_79"""
		input="""
    int man(){
        a ---------b;
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([BinaryOp(-,Id(a),UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,Id(b))))))))))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,379))
	def test_8(self):
		"""AST_TEST_8"""
		input="""
    int a; int[] main(int a[], boolean b){}
    """
		Program([VarDecl(a,IntType),FuncDecl(Id(main),[VarDecl(a,ArrayTypePointer(IntType)),VarDecl(b,BoolType)],ArrayTypePointer(IntType),Block([]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,308))
	def test_80(self):
		"""AST_TEST_80"""
		input="""
    int man(){
        a[1] -b[n];
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([BinaryOp(-,ArrayCell(Id(a),IntLiteral(1)),ArrayCell(Id(b),Id(n)))]))])
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
		Program([FuncDecl(Id(man),[],IntType,Block([BinaryOp(-,ArrayCell(Id(a),IntLiteral(1)),ArrayCell(Id(b),Id(n))),CallExpr(Id(call),[]),CallExpr(Id(pull),[])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,381))
	def test_82(self):
		"""AST_TEST_82"""
		input="""
    int man(){
        call();
        pull();
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([CallExpr(Id(call),[]),CallExpr(Id(pull),[])]))])
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
		Program([FuncDecl(Id(man),[],IntType,Block([Dowhile([Id(a),Id(b),Id(c),Id(d)],Id(cc))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,383))
	def test_84(self):
		"""AST_TEST_84"""
		input="""
    int man(){
        {}{}{}{a;}
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([Block([]),Block([]),Block([]),Block([Id(a)])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,384))
	def test_85(self):
		"""AST_TEST_85"""
		input="""
    int man(){
        return ;
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([Return()]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,385))
	def test_86(self):
		"""AST_TEST_86"""
		input="""
    int man(){
        return a= 1 ;
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([Return(BinaryOp(=,Id(a),IntLiteral(1)))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,386))
	def test_87(self):
		"""AST_TEST_87"""
		input="""
    int man(){
        return "a" ;
    }
    """
		Program([FuncDecl(Id(man),[],IntType,Block([Return(StringLiteral(a))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,387))
	def test_88(self):
		"""AST_TEST_88"""
		input="""
    int A1man(){
        return "a" ;
    }
    """
		Program([FuncDecl(Id(A1man),[],IntType,Block([Return(StringLiteral(a))]))])
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
		Program([FuncDecl(Id(A1man),[],IntType,Block([Return(StringLiteral(a)),Block([Id(a),Id(b),Id(v)])]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,389))
	def test_9(self):
		"""AST_TEST_9"""
		input="""
    int main(){do {{{}}} while 1;}
    """
		Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Block([Block([Block([])])])],IntLiteral(1))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,309))
	def test_90(self):
		"""AST_TEST_90"""
		input="""
    int A1man(int b,string cc){
        return "a" ;
    }
    """
		Program([FuncDecl(Id(A1man),[VarDecl(b,IntType),VarDecl(cc,StringType)],IntType,Block([Return(StringLiteral(a))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,390))
	def test_91(self):
		"""AST_TEST_91"""
		input="""
    int main(int b,string cc){
        return true ;
    }
    """
		Program([FuncDecl(Id(main),[VarDecl(b,IntType),VarDecl(cc,StringType)],IntType,Block([Return(BooleanLiteral(true))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,391))
	def test_92(self):
		"""AST_TEST_92"""
		input="""
    int main(int b,string cc){
        return false ;
    }
    """
		Program([FuncDecl(Id(main),[VarDecl(b,IntType),VarDecl(cc,StringType)],IntType,Block([Return(BooleanLiteral(false))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,392))
	def test_93(self):
		"""AST_TEST_93"""
		input="""
    int main(int b,string cc){
        return false ;
    }
    """
		Program([FuncDecl(Id(main),[VarDecl(b,IntType),VarDecl(cc,StringType)],IntType,Block([Return(BooleanLiteral(false))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,393))
	def test_94(self):
		"""AST_TEST_94"""
		input="""
    int main(int b,string cc[]){
        return false ;
    }
    """
		Program([FuncDecl(Id(main),[VarDecl(b,IntType),VarDecl(cc,ArrayTypePointer(StringType))],IntType,Block([Return(BooleanLiteral(false))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,394))
	def test_95(self):
		"""AST_TEST_95"""
		input="""
    int main(int b,string cc[]){
        int  a [1];
    }
    """
		Program([FuncDecl(Id(main),[VarDecl(b,IntType),VarDecl(cc,ArrayTypePointer(StringType))],IntType,Block([VarDecl(a,ArrayType(IntType,1))]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,395))
	def test_96(self):
		"""AST_TEST_96"""
		input="""
    int main(){
        d+e;
        a+c;
    }
    """
		Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(+,Id(d),Id(e)),BinaryOp(+,Id(a),Id(c))]))])
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
		Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(=,BinaryOp(<,Id(a),Id(a)),Id(b)),Block([If(Id(a),Block([]),Block([If(Id(a),Block([]))]))]),Block([Dowhile([Id(a),Id(b),Id(c)],Id(c))]))]))])
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
		Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(=,BinaryOp(<,Id(a),Id(a)),Id(b)),Block([If(Id(a),Block([]),Block([If(Id(a),Block([]))]))]))])),FuncDecl(Id(b),[],BoolType,Block([BinaryOp(=,Id(check),BooleanLiteral(true)),CallExpr(Id(callme),[]),CallExpr(Id(println),[])]))])
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
		Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,ArrayType(IntType,3)),VarDecl(b,IntType),VarDecl(c,FloatType),VarDecl(u,StringType)]))])
		self.assertTrue(TestAST.checkASTGen(input,expect,399))
