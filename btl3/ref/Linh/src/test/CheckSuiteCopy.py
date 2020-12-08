    def test0_RedeclaredVariable(self):
        """ double variable b"""
        input = """
        void main(){
            
        }
        int b; 
        float b;
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 400))
    def test1_RedeclaredVariable(self):
        """double variable b"""
        input = """
        float b;
        void main(){
            
        }
        int b; 
        
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 401))
    def test2_RedeclaredVariable(self):
        """ Func name can not be same with Var name in global"""
        input = """
        float b;
        void main(){
            
        }
        int main; 
        
        """
        expect = "Redeclared Variable: main"
        self.assertTrue(TestChecker.test(input, expect, 402))    
    def test3_RedeclaredFunction(self):
        """ same with test2 but different position"""
        input = """
        float b;
        int main;
        void main(){
            
        }
        int main; 
        
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input, expect, 403))
    def test4_RedeclaredFunction(self):
        """ Func name cant be same"""
        input = """
        float b;
        int c;
        void main(int k, float a[], string e ){
            
        }
        void main(){}
        int m; 
        
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input, expect, 404))
    def test5_RedeclaredVariable(self):
        """ para name and var name (scope1) cant be same"""
        input = """
        float b;
        int c;
        void main(int k, float a[], string e ){
            int a; 
            {
                int a; 
            }
        }
        int m; 
        
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 405))        
    def test6_RedeclaredVariable(self):
        """ var name cant be same in the same scope"""
        input = """
        float b;
        int c;
        void main(int k, float a[], string e ){
            int b; 
            {
                int a; 
                string a;
            }
        }
        int m; 
        
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 406))
    def test7_RedeclaredParameter(self):
        """ para cant be same"""
        input = """
        float b;
        int c;
        void main(int k, float a[], string a ){
            int b; 
            {
                int a; 
                
            }
        }
        int m; 
        
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 407))
    def test8_MoreComplex_RedeclaredVariable(self):
        """ same above but more complex"""
        input = """
        float b;
        int c;
        void main(int k, float a[], string e){
            int b; 
            {
                int a; 
                {{{{{{{{{{{{int c;}int c; int c;}}}}}}}}}}}
                
            }
        }
        int m; 
        
        """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 408))
    def test9_MoreComplex_RedeclaredVariable(self):
        """different position of var name"""
        input = """
        float b;
        int c;
        void main(int k, float a[], string e){
            int b; 
            { 
                int k;
                if (true){
                    int k ;
                }
                int k ;
                }
        }
        int m; 
        
        """
        expect = "Redeclared Variable: k"
        self.assertTrue(TestChecker.test(input, expect, 409))
    def test10_Undeclared(self):
        """id must be declared before use"""
        input = """
        float b;
        int c;
        void main(int k, float a[], string e){
            int b; 
            { 
                int k;
                if (true){
                    int k ;
                }
                m = 2;
        }
        }
        
        """
        expect = "Undeclared Identifier: m"
        self.assertTrue(TestChecker.test(input, expect, 410))
    def test11_Undeclared(self):
        """id must be declared before use"""
        input = """
        float b;
        int c;
        void main(int k, float a[], string e){
            int b; 
            { 
                int k;
                if (true){
                    int k ;
                }
                //m = 2;
                foo();
        }}
        
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 411))
    def test12_Undeclared_withFunc(self):
        """  more complex testcase"""
        input = """
        float b;
        int c;
        void main(int k, float a[], string e){
            int b; 
            { 
                int k;
                if (true){
                    int k ;
                }
                //m = 2;
                //foo();
                }
            {
                {
                    {
                        {
                            int a; 
                            a = foo() + 234 * 34 = a;
                        }
                    }
                }
            }
        }
        int m; 
        
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 412))    
    def test13_Undeclared_with_id(self):
        """more complex"""
        input = """
        float b;
        int c;
        void main(int k, float a[], string e){
            int b; 
            { 
                int k;
                if (true){
                    int k ;
                }
                //m = 2;
                //foo();
                }
            {
                {
                    {
                        {
                            int a; 
                            a = foo + 234 * 34 = a;
                        }
                    }
                }
            }
        }
        int m; 
        
        """
        expect = "Undeclared Identifier: foo"
        self.assertTrue(TestChecker.test(input, expect, 413))
    def test14_Undeclared_func_call(self):
        input = """
            void main(){
                
            }
            boolean check(int x, int y, int z){
                return max(x,max(y,z));
            }

        """
        expect = "Undeclared Function: max"
        self.assertTrue(TestChecker.test(input, expect, 414))       
    def test15_Undeclared_withAnotherScope(self):
        input = """
            void main(){
                check(1,1,1);
            }
            boolean check(int x, int y, int z){
                int a;
                {
                    a = a+b;
                }
                int b;
                return true;
            }

        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 415))       
    def test16_TypeMisIf(self):
        """condition in if must be bool"""
        input = """
            void main(){
                sum();
                if (1){{{{{{{{{{{{{{{{{{{{{
                    int a;
                    a= 1;
                }}}}}}}}}}}}}}}}}}}}}
            }
            void sum(){

            }

        """
        expect = "Type Mismatch In Statement: If(IntLiteral(1),Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([VarDecl(a,IntType),BinaryOp(=,Id(a),IntLiteral(1))])])])])])])])])])])])])])])])])])])])])]))"
        self.assertTrue(TestChecker.test(input, expect, 416))       
    def test17_TypeMisIf(self):
        """condition in if must be bool"""
        input = """
            void main(){
                sum();
                if (sum()+1 * 1.2){
                    sum();
                }
            }

            boolean sum(){
                return true;
            }

        """
        expect = "Type Mismatch In Expression: BinaryOp(+,CallExpr(Id(sum),[]),BinaryOp(*,IntLiteral(1),FloatLiteral(1.2)))"
        self.assertTrue(TestChecker.test(input, expect, 417))        
    def test18_TypeMisFor(self):
        """exp1 is not integer"""
        input = """
            float i;
            void main(){
                sum();
                if (true){
                    sum();

                }
                for( i  = 1; i<12;i=i+1){

                }
            }

            boolean sum(){
                return true;
            }

        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),IntLiteral(12));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 418))       
    def test19_TypeMisFor(self):
        """exp3 is not integer"""
        input = """
            int i;
            void main(){
                sum();
                if (true){
                    sum();

                }
                for( i  = 1; i<12;i=i+1.11){

                }
            }

            boolean sum(){
                return true;
            }

        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(i),BinaryOp(+,Id(i),FloatLiteral(1.11)))"
        self.assertTrue(TestChecker.test(input, expect, 419))                      
    def test20_TypeMisFor(self):
        """exp2 is not bool"""
        input = """
            int i;
            void main(){
                sum();
                if (true){
                    sum();

                }
                for( i  = 1; 1;i=i+111){

                }
            }

            boolean sum(){
                return true;
            }

        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));IntLiteral(1);BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(111)));Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 420))      
    def test21_TypeMisWhile(self):
        """condition is not boolean"""
        input = """
            int i;
            void main(){
                sum();
                if (true){
                    sum();

                }
                boolean T;
                for( i  = 1; T = sum();i=i+111){

                }
                do {}
                while (1); 
            }

            boolean sum(){
                return true;
            }

        """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 421))       
    def test22_TypeMisWhile(self):
        """return fail"""
        input = """
            int i;
            void main(){
                sum();
                if (true){
                    sum();

                }
                boolean T;
                for( i  = 1; T = sum();i=i+111){

                }
                do {
                    boolean i;
                    i = sum() && (1 < mul());
                }
                while (true); 
            }

            boolean sum(){
                return true;
            }
            int mul(){
                return 1.1*2;
            }

        """
        expect = "Type Mismatch In Statement: Return(BinaryOp(*,FloatLiteral(1.1),IntLiteral(2)))"
        self.assertTrue(TestChecker.test(input, expect, 422))       
    def test23_TypeReturn(self):
        """return fail with pointer"""
        input = """
            int i;
            void main(){
                sum();
                if (true){
                    sum();

                }
                boolean T;
                for( i  = 1; T = sum();i=i+111){

                }
                do {
                    boolean i;
                    i = sum() && (1 < mul());
                }
                while (true); 
                pointer();
            }

            boolean sum(){
                return true;
            }
            int mul(){
                return 1*2;
            }
            int[] pointer (){
                float a[2];
                return a;
            }

        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 424))       
    def test24_TypeMisReturn(self):
        """return fail with pointer type"""
        input = """
            int i;
            void main(){
                sum();
                if (true){
                    sum();

                }
                boolean T;
                for( i  = 1; T = sum();i=i+111){

                }
                do {
                    boolean i;
                    i = sum() && (1 < mul());
                }
                while (true); 
                int p[2];
                pointer(p);
            }

            boolean sum(){
                return true;
            }
            int mul(){
                return 1*2;
            }
            float[] pointer (int b[]){
                float a[2];
                return b;
            }

        """
        expect = "Type Mismatch In Statement: Return(Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 424))       
    def test25_TypeMisReturn(self):
        """return fail with pointer type"""
        input = """
            int i;
            void main(){
                sum();
                if (true){
                    sum();

                }
                boolean T;
                for( i  = 1; T = sum();i=i+111){

                }
                do {
                    boolean i;
                    i = sum() && (1 < mul());
                }
                while (true); 
                int p[2];
                int k;
                pointer(k);
            }

            boolean sum(){
                return true;
            }
            int mul(){
                return 1*2;
            }
            float[] pointer (int k){
                float a[2];
                return true;
            }

        """
        expect = "Type Mismatch In Statement: Return(BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input, expect, 425))       
    def test26_BuildInFunction(self):
        """BuildInFunc : putInt"""
        input = """
            int i;
            void main(){
                sum();
                if (true){
                    sum();

                }
                boolean T;
                for( i  = 1; T = sum();i=i+111){

                }
                do {
                    boolean i;
                    i = sum() && (1 < mul());
                }
                while (true); 
                int p[2];
                int k;
                pointer(k);
            }

            boolean sum(){
                return true;
            }
            int mul(){
                putInt(2.1);
                return getInt();
            }
            float[] pointer (int k){
                float a[2];
                
                return a;
            }

        """
        expect = "Type Mismatch In Expression: CallExpr(Id(putInt),[FloatLiteral(2.1)])"
        self.assertTrue(TestChecker.test(input, expect, 426))       
    def test27_BuildInFunction(self):
        """ putInt param must be int """
        input = """
            int i;
            void main(){
                sum();
                if (true){
                    sum();

                }
                boolean T;
                for( i  = 1; T = sum();i=i+111){

                }
                do {
                    boolean i;
                    i = sum() && (1 < mul());
                }
                while (true); 
                int p[2];
                int k;
                pointer(k);
            }

            boolean sum(){
                return true;
            }
            int mul(){
                putInt(21);
                putIntLn(true);
                return getInt();
            }
            float[] pointer (int k){
                float a[2];
                
                return a;
            }

        """
        expect = "Type Mismatch In Expression: CallExpr(Id(putIntLn),[BooleanLiteral(true)])"
        self.assertTrue(TestChecker.test(input, expect, 427))       
    def test28_BuildInFunction(self):
        """ putInt param must be int """
        input = """
            int i;
            void main(){
                sum();
                if (true){
                    sum();

                }
                boolean T;
                for( i  = 1; T = sum();i=i+111){

                }
                do {
                    boolean i;
                    i = sum() && (1 < mul());
                }
                while (true); 
                int p[2];
                int k;
                pointer(k);
            }

            boolean sum(){
                return true;
            }
            int mul(){
                putInt(21);
                putIntLn(1);
                return getInt();
            }
            float[] pointer (int k){
                float a[2];
                test();
                return a;
            }
            float test(){
                putFloat(true);
                return getFloat();
            }

        """
        expect = "Type Mismatch In Expression: CallExpr(Id(putFloat),[BooleanLiteral(true)])"
        self.assertTrue(TestChecker.test(input, expect, 428))       
    def test29_BuildInFunction(self):
        """ - unary not apply for bool """
        input = """
            void main(){
                boolean k ;
                putFloat(-1.1);
                putBool(false);
                putFloatLn(-1243252453485645);
                putBoolLn(! true);
                putBoolLn(- true);
            }

        """
        expect = "Type Mismatch In Expression: UnaryOp(-,BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input, expect, 429))                                
    def test30_BuildInFunction(self):
        """ - unary not apply for bool """
        input = """
            void main(){
                boolean k ;
                putLn();
                putFloat(-1.1);
                putBool(false);
                putFloatLn(-1243252453485645);
                putBoolLn(! true);
                putBoolLn(- true);
                
            }

        """
        expect = "Type Mismatch In Expression: UnaryOp(-,BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input, expect, 430))           
    def test31_TypeMisExpr(self):
        """ error in array subcripting"""
        input = """
            void main(){
                float f; 
                float a[123];
                f = a[getInt()+ 1.0] + getFloat();
            }

        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),BinaryOp(+,CallExpr(Id(getInt),[]),FloatLiteral(1.0)))"
        self.assertTrue(TestChecker.test(input, expect, 431))           
    def test32_TypeMisExpr(self):
        """ error in array subcripting"""
        input = """
            void main(){
                float f; 
                float a[123];
                f = f[getInt()+ 1] + getFloat();
            }

        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(f),BinaryOp(+,CallExpr(Id(getInt),[]),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input, expect, 432))
    def test33_TypeMisExpr(self):
        """ error binary expr"""
        input = """
            void main(){
                float f; 
                float a[123];
                f = a[getInt()+ 1] + getFloat();
                string s;
                s = "a" + "b";
            }

        """
        expect = "Type Mismatch In Expression: BinaryOp(+,StringLiteral(a),StringLiteral(b))"
        self.assertTrue(TestChecker.test(input, expect, 433))           
    def test34_TypeMisExpr(self):
        """ error binary expr"""
        input = """
            void main(){
                float f; 
                float a[123];
                f = a[getInt()+ 1] + getFloat();
                string s;
                int k; 
                k = getInt() % 1.1;
            }

        """
        expect = "Type Mismatch In Expression: BinaryOp(%,CallExpr(Id(getInt),[]),FloatLiteral(1.1))"
        self.assertTrue(TestChecker.test(input, expect, 434))    
    def test35_TypeMisExpr(self):
        """ error binary expr"""
        input = """
            void main(){
                float f; 
                float a[123];
                f = a[getInt()+ 1] + getFloat();
                string s;
                int k; 
                k = getInt() % 1;
                boolean b;
                b = true< 1;
            }

        """
        expect = "Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(true),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 435))           
    def test36_TypeMisExpr(self):
        """ error binary expr , == not use for different type """
        input = """
            void main(){
                float f; 
                float a[123];
                f = a[getInt()+ 1] + getFloat();
                string s;
                int k; 
                k = getInt() % 1;
                boolean b;
                b = 1.1 == 1;
            }

        """
        expect = "Type Mismatch In Expression: BinaryOp(==,FloatLiteral(1.1),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 436))       
    def test37_TypeMisExpr(self):
        """ error binary expr , == not use for different type """
        input = """
            void main(){
                float f; 
                float a[123];
                f = a[getInt()+ 1] + getFloat();
                string s;
                int k; 
                k = getInt() % 1;
                boolean b;
                b = 1 == 1;
                f  =false + true;
            }

        """
        expect = "Type Mismatch In Expression: BinaryOp(+,BooleanLiteral(false),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input, expect, 437))           
    def test38_TypeMisExprUnary(self):
        """ "-"  just for int bool"""
        input = """
            void main(){
                float f; 
                float a[123];
                f = a[getInt()+ 1] + getFloat();
                string s;
                int k; 
                k = getInt() % 1;
                boolean b;
                b = 1 == 1;
                f  =-true +(1+1);

            }

        """
        expect = "Type Mismatch In Expression: UnaryOp(-,BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input, expect, 438))    
    def test39_TypeMisExprUnary(self):
        """ ! just for bool"""
        input = """
            void main(){
                float f; 
                float a[123];
                f = a[getInt()+ 1] + getFloat();
                string s;
                int k; 
                k = getInt() % 1;
                boolean b;
                b = 1 == 1;
                f  =-0 +(1+1);
                f = !2;
            }

        """
        expect = "Type Mismatch In Expression: UnaryOp(!,IntLiteral(2))"
        self.assertTrue(TestChecker.test(input, expect, 439))           
    def test40_TypeMisExprFunctioncall(self):
        """ TypeMisFuncall"""
        input = """
            void main(){
                float f; 
                float a[123];
                f = a[getInt()+ 1] + getFloat();
                string s;
                int k; 
                k = getInt() % 1;
                boolean b;
                b = 1 == 1;
                f  =-0 +(1+1);
                b = !false;
                putFloat(1);
                putInt(1.1);
            }

        """
        expect = "Type Mismatch In Expression: CallExpr(Id(putInt),[FloatLiteral(1.1)])"
        self.assertTrue(TestChecker.test(input, expect, 440))           
    def test41_TypeMisExprFunctioncall(self):
        """ TypeMisFuncall """
        input = """
            void main(){
                float f; 
                float a[123];
                f = a[getInt()+ 1] + getFloat();
                string s;
                int k; 
                k = getInt() % 1;
                boolean b;
                b = 1 == 1;
                f  =-0 +(1+1);
                b = !false;
                putFloat(1);
                putInt(11);
                a(2);
            }
            int a(int a){
                return a;
            }

        """
        expect = "Type Mismatch In Expression: CallExpr(Id(a),[IntLiteral(2)])"
        self.assertTrue(TestChecker.test(input, expect, 441))           
    def test42_TypeMisExprFunctioncall(self):
        """ TypeMisFuncall """
        input = """
            void main(){
                float f; 
                float a[123];
                f = a[getInt()+ 1] + getFloat();
                string s;
                int k; 
                k = getInt() % 1;
                boolean b;
                b = 1 == 1;
                f  =-0 +(1+1);
                b = !false;
                putFloat(1);
                putInt(11);
                sum(2.1);
            }
            int sum(int a){
                return a;
            }

        """
        expect = "Type Mismatch In Expression: CallExpr(Id(sum),[FloatLiteral(2.1)])"
        self.assertTrue(TestChecker.test(input, expect, 442))      
    def test43_TypeMisExprFunctioncall(self):
        """ TypeMisFuncall """
        input = """
            void main(){
                float f; 
                float a[123];
                f = a[getInt()+ 1] + getFloat();
                string s;
                int k; 
                k = getInt() % 1;
                boolean b;
                b = 1 == 1;
                f  =-0 +(1+1);
                b = !false;
                putFloat(1);
                putInt(11);
                k =sum(sum(sum(sum(2)))) + foo(a);
            }
            int sum(int a){
                return a;
            }
            int foo(int p[]){
                return 1;
            }

        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a)])"
        self.assertTrue(TestChecker.test(input, expect, 443))          
    def test44_TypeMisExprFunctioncall(self):
        """ TypeMisFuncall """
        input = """
            void main(){
                float f; 
                float a[123];
                f = a[getInt()+ 1] + getFloat();
                string s;
                int k; 
                k = getInt() % 1;
                boolean b;
                b = 1 == 1;
                f  =-0 +(1+1);
                b = !false;
                putFloat(1);
                putInt(11);
                int p[3];
                k =sum(sum(sum(sum(2)))) + foo(p);
            }
            int sum(int a){
                return a;
            }
            int foo(int p[], int x, float y, string z){
                return 1;
            }

        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(p)])"
        self.assertTrue(TestChecker.test(input, expect, 444))           
    def test45_TypeMisExprFunctioncall(self):
        """ TypeMisFuncall  multi_parameter"""
        input = """
            void main(){
                float f; 
                float a[123];
                f = a[getInt()+ 1] + getFloat();
                string s;
                int k; 
                k = getInt() % 1;
                boolean b;
                b = 1 == 1;
                f  =-0 +(1+1);
                b = !false;
                putFloat(1);
                putInt(11);
                int p[3];
                k =sum(sum(sum(sum(2)))) + foo(p,1,-12312, "This is String",True && False || ! True);
            }
            int sum(int a){
                return a;
            }
            int foo(int p[], int x, float y, string z, boolean b){
                return 1;
            }

        """
        expect = "Undeclared Identifier: True"
        self.assertTrue(TestChecker.test(input, expect, 445))           
    def test46_TypeMisExprFunctioncall(self):
        """ TypeMisFuncall  multi_parameter"""
        input = """
            void main(){
                float f; 
                float a[123];
                f = a[getInt()+ 1] + getFloat();
                string s;
                int k; 
                k = getInt() % 1;
                boolean b;
                b = 1 == 1;
                f  =-0 +(1+1);
                b = !false;
                putFloat(1);
                putInt(11);
                int p[3];
                k =sum(sum(sum(sum(2)))) + foo(p,1.1,-12312+1.122232313123, "This is String",true && false || ! true);
            }
            int sum(int a){
                return a;
            }
            int foo(int p[], int x, float y, string z, boolean b){
                return 1;
            }

        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(p),FloatLiteral(1.1),BinaryOp(+,UnaryOp(-,IntLiteral(12312)),FloatLiteral(1.122232313123)),StringLiteral(This is String),BinaryOp(||,BinaryOp(&&,BooleanLiteral(true),BooleanLiteral(false)),UnaryOp(!,BooleanLiteral(true)))])"
        self.assertTrue(TestChecker.test(input, expect, 446))           
    def test47_TypeMisExprFunctioncall(self):
        """ TypeMisFuncall  multi_parameter"""
        input = """
            void main(){
                float f; 
                float a[123];
                f = a[getInt()+ 1] + getFloat();
                string s;
                int k; 
                k = getInt() % 1;
                boolean b;
                b = 1 == 1;
                f  =-0 +(1+1);
                b = !false;
                putFloat(1);
                putInt(11);
                int p[3];
                k =sum(sum(sum(sum(2)))) + foo(p,1.1,-12312+1.122232313123, "This is String",true && false || ! true);
            }
            int sum(int a){
                return a;
            }
            int foo(int p[], int x, float y, string z, boolean b){
                return 1;
            }

        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(p),FloatLiteral(1.1),BinaryOp(+,UnaryOp(-,IntLiteral(12312)),FloatLiteral(1.122232313123)),StringLiteral(This is String),BinaryOp(||,BinaryOp(&&,BooleanLiteral(true),BooleanLiteral(false)),UnaryOp(!,BooleanLiteral(true)))])"
        self.assertTrue(TestChecker.test(input, expect, 447))  
    def test48_TypeMisExprFunctioncall(self):
        """ TypeMisFuncall  multi_parameter"""
        input = """
            void main(){
                float f; 
                float a[123];
                f = a[getInt()+ 1] + getFloat();
                string s;
                int k; 
                k = getInt() % 1;
                boolean b;
                b = 1 == 1;
                f  =-0 +(1+1);
                b = !false;
                putFloat(1);
                putInt(11);
                int p[3];
                k =sum(sum(sum(sum(2)))) + foo(p,1.1,-12312+1.122232313123, "This is String",true && false || ! true);
            }
            int sum(int a){
                return a;
            }
            int foo(int p[], int x, float y, string z, boolean b){
                return 1;
            }

        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(p),FloatLiteral(1.1),BinaryOp(+,UnaryOp(-,IntLiteral(12312)),FloatLiteral(1.122232313123)),StringLiteral(This is String),BinaryOp(||,BinaryOp(&&,BooleanLiteral(true),BooleanLiteral(false)),UnaryOp(!,BooleanLiteral(true)))])"
        self.assertTrue(TestChecker.test(input, expect, 448))
    def test49_TypeMisExprFunctioncall(self):
        """ TypeMisFuncall  multi_parameter"""
        input = """

            void main(){
                float f; 
                float a[123];
                f = a[getInt()+ 1] + getFloat();
                string s;
                int k; 
                k = getInt() % 1;
                boolean b;
                b = 1 == 1;
                f  =-0 +(1+1);
                b = !false;
                putFloat(1);
                putInt(11);
                int p[3];
                int sum;
                k =sum(sum(sum(sum(2)))) + foo(p,1.1,-12312+1.122232313123, "This is String",true && false || ! true);
            }
            int sum(int a){
                return a;
            }
            int foo(int p[], int x, float y, string z, boolean b){
                return 1;
            }

        """
        expect = "Type Mismatch In Expression: CallExpr(Id(sum),[CallExpr(Id(sum),[CallExpr(Id(sum),[CallExpr(Id(sum),[IntLiteral(2)])])])])"
        self.assertTrue(TestChecker.test(input, expect, 449))
    def test50_FunctionNotReturn(self):
        """ Basic error"""
        input = """
            int main(){
                return ;
            }

        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 450))
    def test51_FunctionNotReturn(self):
        """ Basic error"""
        input = """
            float main(){
                return  0;
                sum();
            }
            int sum(){
                for(1;true;1){
                    if(true){
                        {
                            {
                                {
                                    return 1;
                                }
                            }
                        }
                    }
                    else return 1;
                }
            }
        """
        expect = "Function sum Not Return "
        self.assertTrue(TestChecker.test(input, expect, 451))
    def test52_FunctionNotReturn(self):
        """ Basic error"""
        input = """
            float main(){
                return  0;
                sum();
            }
            int sum(){
                for(1;true;1){
                    if(true){
                        {
                            {
                                {
                                    return 1;
                                }
                            }
                        }
                    }
                    else return 1;
                }
                if(!false ){
                    return 1;
                }
            }
        """
        expect = "Function sum Not Return "
        self.assertTrue(TestChecker.test(input, expect, 452))
    def test53_FunctionNotReturn(self):
        """ Error with if path execution"""
        input = """
            float main(){
                return  0;
                sum();
            }
            int sum(){
                for(1;true;1){
                    if(true){
                        {
                            {
                                {
                                    return 1;
                                }
                            }
                        }
                    }
                    else return 1;
                }
                if(!false ){
                    return 1;
                }
                else {
                    if (true) return 1;
                    else {
                        {
                            {
                                
                            }
                        }
                    }
                }
            }
        """
        expect = "Function sum Not Return "
        self.assertTrue(TestChecker.test(input, expect, 453))
    def test54_FunctionNotReturn(self):
        """ Complex error"""
        input = """
            float main(){
                return  0;
                sum();
            }
            int sum(){
                for(1;true;1){
                    if(true){
                        {
                            {
                                {
                                    return 1;
                                }
                            }
                        }
                    }
                    else return 1;
                }
                if(!false ){
                    return 1;
                }
                else {
                    if (true) return 1;
                    else {
                        {
                            {
                                for (1;true; 1){
                                    return 1;
                                }
                            }
                        }
                    }
                }
            }
        """
        expect = "Function sum Not Return "
        self.assertTrue(TestChecker.test(input, expect, 454))
    def test55_FunctionNotReturn(self):
        """ Complex error"""
        input = """
            float main(){
                return  0;
                sum();
            }
            int sum(){
                for(1;true;1){
                    if(true){
                        {
                            {
                                {
                                    return 1;
                                }
                            }
                        }
                    }
                    else return 1;
                }
                if(!false ){
                    return 1;
                }
                else {
                    if (true) return 1;
                    else {
                        {
                            {
                                for (1;true; 1){
                                    return 1;
                                }
                            }
                        }
                        do  {
                            int a;
                            if(false){
                                return 1;
                            }
                            else {
                                {
                                    
                                }
                            }
                        }
                        
                        while(true);
                    }
                }
            }
        """
        expect = "Function sum Not Return "
        self.assertTrue(TestChecker.test(input, expect, 455))
    def test56_FunctionNotReturn(self):
        """ error with more statement"""
        input = """
            float main(){
                return  0;
                sum();
            }
            int sum(){
                for(1;true;1){
                    if(true){
                        { continue;
                            {
                                {
                                    return 1;
                                }
                            }
                        }
                        sum();
                    }
                    else return 1;
                }
                if(!false ){
                    return 1;
                }
                else {
                    if (true) return 1;
                    else {
                        { 
                            int a;
                            a= 1;
                            {
                                for (1;true; 1){
                                    return 1;
                                }
                            }
                        }
                        do  {
                            int a;
                            if(false){
                                return 1;
                            }
                            else {
                                {
                                    
                                }
                            }
                            break;
                        }
                        
                        while(true);
                    }
                }
            }
        """
        expect = "Function sum Not Return "
        self.assertTrue(TestChecker.test(input, expect, 456))
    def test57_FunctionNotReturn(self):
        """ error with more statement"""
        input = """
            float main(){
                return  0;
                sum();
            }
            int sum(){
                for(1;true;1){
                for(1;true;1){
                    if(true){
                        { continue;
                            {
                                {
                                    return 1;
                                }
                            }
                        }
                        sum();
                    }
                    else return 1;
                }
                if(!false ){
                    return 1;
                }
                else {
                    if (true) return 1;
                    else {
                        { 
                            int a;
                            a= 1;
                            {
                                for (1;true; 1){
                                    return 1;
                                }
                            }
                        }
                        do  {
                            int a;
                            if(false){
                                return 1;
                            }
                            else {
                                {
                                    return 1;
                                }
                            }
                            break;
                        }
                        
                        while(true);
                    }
                }
                }
            }
        """
        expect = "Function sum Not Return "
        self.assertTrue(TestChecker.test(input, expect, 457))
    def test58_FunctionNotReturn(self):
        """ error with more statement"""
        input = """
            float main(){
                return  0;
                sum();
            }
            int sum(){
                for(1;true;1){
                for(1;true;1){
                    if(true){
                        { continue;
                            {
                                
                                {
                                    return 1;
                                }
                            }
                        }
                        sum();
                    }
                    else return 1;
                }
                if(!false ){
                    return 1;
                }
                else {
                    if (true) return 1;
                    else {
                        { 
                            int a;
                            a= 1;
                            {
                                for (1;true; 1){
                                    return 1;
                                }
                                a;
                                1;
                                1.1;
                                sum();
                            }
                        }
                        do  {
                            int a;
                            if(false){
                                return 1;
                            }
                            else {
                                {
                                    return 1;
                                }
                            }
                            break;
                        }
                        
                        while(true);
                    }
                }
                }
            }
        """
        expect = "Function sum Not Return "
        self.assertTrue(TestChecker.test(input, expect, 458))
    def test59_FunctionNotReturn(self):
        """ error with more statement"""
        input = """
            float main(){
                return  0;
                sum();
            }
            int sum(){
                do{
                for(1;true;1){
                    if(true){
                        { continue;
                            {
                                
                                {
                                    return 1;
                                }
                            }
                        }
                        sum();
                    }
                    else return 1;
                }
                if(!false ){
                    return 1;
                }
                else {
                    if (true) return 1;
                    else {
                        { 
                            int a;
                            a= 1;
                            {
                                for (1;true; 1){
                                    return 1;
                                }
                                a;
                                1;
                                1.1;
                                sum();
                            }
                        }
                        do  {
                            int a;
                            if(false){
                                return 1;
                            }
                            else {
                                {
                                    
                                }
                            }
                            break;
                        }
                        
                        while(true);
                    }
                }
                }
                while(true);
            }
        """
        expect = "Function sum Not Return "
        self.assertTrue(TestChecker.test(input, expect, 459))
    def test60_Break_Continue(self):
        """ break / continue not in loop"""
        input = """
            void main(){
                if(true){
                    break;
                }
                else{

                }
            }

        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 460))
    def test61_Break_Continue(self):
        """ break / continue not in loop"""
        input = """
            void main(){
                if(true){
                    
                }
                else{
                    break;
                }
            }

        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 461))
    def test62_Break_Continue(self):
        """ break / continue not in loop"""
        input = """
            void main(){
                break;
                if(true){
                    do
                         break; 
                        do break;
                        while(true);
                        break;
                        for(1; true; 1){
                            continue;
                        }
                    while(true);
                }
                else{
                }
            }

        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 462))
    def test63_Break_Continue(self):
        """ break / continue not in loop"""
        input = """
            void main(){
                
                if(true){
                    do
                         
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                        
                    while(true);
                }
                else{
                    break;
                }
            }

        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 463))
    def test64_Break_Continue(self):
        """ break / continue not in loop"""
        input = """
            void main(){
                continue;
                if(true){
                    do
                         
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                        
                    while(true);
                }
                else{
                    do break;
                    while(true);
                }
            }

        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 464))
    def test65_Break_Continue(self):
        """ break / continue not in loop"""
        input = """
            void main(){
                
                if(true){
                    do
                         
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                        
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    continue;
                }
            }

        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 465))
    def test66_Break_Continue(self):
        """ break / continue not in loop"""
        input = """
            void main(){
                do
                if(true){
                    do
                         
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                        
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    
                }
                while(true);
                continue;
            }

        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 466))
    def test67_Break_Continue(self):
        """ break / continue not in loop"""
        input = """
            void main(){
                do
                if(true){
                    do
                         
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                        
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    
                }
                while(true);
                for(2; 1<2; 2){
                    { 
                        string a; 
                        a = "";
                        {
                            int var;
                            {
                                do
                                {

                                }
                                while(true);
                            }
                        }
                    }
                }
                continue;
            }

        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 467))
    def test68_Break_Continue(self):
        """ break / continue not in loop"""
        input = """
            void main(){
                do
                if(true){
                    do
                         
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                        
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    
                }
                while(true);
                continue;
                for(2; 1<2; 2){
                    { 
                        break; 
                        continue;
                        string a; 
                        a = "";
                        {
                            int var;
                            {
                                do
                                {

                                }
                                while(true);
                            }
                        }
                    }
                }
                
            }

        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 468))
    def test69_Break_Continue(self):
        """ break / continue not in loop"""
        input = """
            void main(){
                do
                {
                int complex ;
                complex = 1-------------------------1;
                }
                if(true){
                    do
                         
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                        
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    
                }
                while(true);
                continue;
                for(2; 1<2; 2){
                    { 
                        break; 
                        continue;
                        string a; 
                        a = "";
                        {
                            int var;
                            {
                                do
                                {

                                }
                                while(true);
                            }
                        }
                    }
                    1; 

                }
                
            }

        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 469))
    def test70_NoEntryPoint(self):
        """ program without main"""
        input = """
            void sum(){
                do
                {
                int complex ;
                complex = 1-------------------------1;
                }
                if(true){
                    do
                         
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                        
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    
                }
                while(true);
            }

        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 470))
    def test71_NoEntryPoint(self):
        """ program without main"""
        input = """
            void sum(){
                do
                {
                int complex ;
                complex = 1-------------------------1;
                }
                if(true){
                    do
                         
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                        
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    
                }
                while(true);
            }
            int main;

        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 471))
    def test72_NoEntryPoint(self):
        """ program without main"""
        input = """
        int main;
            void sum(){
                do
                {
                int complex ;
                complex = 1-------------------------1;
                }
                if(true){
                    do
                         
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                        
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    
                }
                while(true);
            }
            

        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 472))
    def test73_NoEntryPoint(self):
        """ program without main"""
        input = """
            void sum(){
                do
                {
                int complex ;
                complex = 1-------------------------1;
                }
                if(true){
                    do
                         
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                        
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    
                }
                while(true);
            }
            void sum1(){}
            void sum2(){}
            void sum3(){}

        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 473))
    def test74_UnreachableFunc(self):
        """ test Unreachable Function"""
        input = """
            void sum(){
                do
                {
                int complex ;
                complex = 1-------------------------1;
                }
                if(true){
                    do
                         
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                        
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    
                }
                while(true);
                sum1();sum2(); sum3();sum();
            }
            void sum1(){sum();}
            void sum2(){}
            void sum3(){}

        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 474))
    def test75_UnreachableFunc(self):
        """ test Unreachable Function"""
        input = """
            void sum(){
                do
                {
                int complex ;
                complex = 1-------------------------1;
                }
                if(true){
                    do
                         
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                        
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    
                }
                while(true);
                sum1();sum2(); sum3();
            }
            void sum1(){}
            void sum2(){}
            void sum3(){}
            void main(){

            }

        """
        expect = "Unreachable Function: sum"
        self.assertTrue(TestChecker.test(input, expect, 475))
    def test76_UnreachableFunc(self):
        """ test Unreachable Function"""
        input = """
            void sum(){
                do
                {
                int complex ;
                complex = 1-------------------------1;
                }
                if(true){
                    do
                         
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                        
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    
                }
                while(true);
                sum();sum2(); sum3();
            }
            void sum1(){}
            void sum2(){}
            void sum3(){}
            void main(){

            }

        """
        expect = "Unreachable Function: sum"
        self.assertTrue(TestChecker.test(input, expect, 476))
    def test77_UnreachableFunc(self):
        """ test Unreachable Function"""
        input = """
            void sum(){
                do
                {
                int complex ;
                complex = 1-------------------------1;
                }
                if(true){
                    do
                         
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                        
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    
                }
                while(true);
                sum();sum2(); sum3();
            }
            void sum1(){sum();}
            void sum2(){}
            void sum3(){}
            void main(){

            }

        """
        expect = "Unreachable Function: sum1"
        self.assertTrue(TestChecker.test(input, expect, 477))
    def test78_UnreachableFunc(self):
        """ test Unreachable Function"""
        input = """
            void sum(){
                do
                {
                int complex ;
                complex = 1-------------------------1;
                }
                if(true){
                    do
                         
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                        
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    
                }
                while(true);
                sum();sum1(); sum3();
            }
            void sum1(){sum();}
            void sum2(){}
            void sum3(){}
            void main(){

            }

        """
        expect = "Unreachable Function: sum2"
        self.assertTrue(TestChecker.test(input, expect, 478))
    def test79_UnreachableFunc(self):
        """ test Unreachable Function"""
        input = """
            void sum(){
                do
                {
                int complex ;
                complex = 1-------------------------1;
                }
                if(true){
                    do
                         
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                        
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    
                }
                while(true);
                sum();sum1(); sum2();
            }
            void sum1(){sum();}
            void sum2(){sum1();}
            void sum3(){}
            void main(){

            }

        """
        expect = "Unreachable Function: sum3"
        self.assertTrue(TestChecker.test(input, expect, 479))
    def test80_UnreachableFunc(self):
        """ test Unreachable Function"""
        input = """
            void sum(){
                do
                {
                int complex ;
                complex = 1-------------------------1;
                }
                if(true){
                    do
                         
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                        
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    
                }
                while(true);
                sum();sum1(); sum();
            }
            void sum1(){sum();}
            void sum2(){sum1();}
            void sum3(){}
            void main(){
                sum();
            }

        """
        expect = "Unreachable Function: sum2"
        self.assertTrue(TestChecker.test(input, expect, 480))
    def test81_NotLeftValue(self):
        """ LHS must be Id(bool, int, float, string) or arrayCell"""
        input = """
            void main(){
                do
                {

                int complex ;
                complex = 1-------------------------1;
                complex = 1= 1;
                }
                if(true){
                    do
                         
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                        
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    
                }
                while(true);
            
            }
            

        """
        expect = "Not Left Value: IntLiteral(1)"
        self.assertTrue(TestChecker.test(input, expect, 481))
    def test82_NotLeftValue(self):
        """ LHS must be Id(bool, int, float, string) or arrayCell"""
        input = """
            void main(){
                do
                {
                float k ;
                int complex ;
                complex = 1-------------------------1;
                 complex =  k =1;
                }
                if(true){
                    do
                         
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                        
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    
                }
                while(true);
            
            }
            

        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(complex),BinaryOp(=,Id(k),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input, expect, 482))
    def test83_NotLeftValue(self):
        """ LHS must be Id(bool, int, float, string) or arrayCell"""
        input = """
            void main(){
                do
                {
                float k ;
                int complex ;
                complex = 1-------------------------1;
                int a[32];
                 a= 1;

                }
                if(true){
                    do
                         
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                        
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    
                }
                while(true);
            
            }
            

        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 483))
    def test84_NotLeftValue(self):
        """ LHS must be Id(bool, int, float, string) or arrayCell"""
        input = """
            void main(int z[]){
                do
                {
                float k ;
                int complex ;
                complex = 1-------------------------1;
                int a[32];
                 z= 1;

                }
                if(true){
                    do
                         
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                        
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    
                }
                while(true);
            
            }
            

        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(z),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 484))
    def test85_NotLeftValue(self):
        """ LHS must be Id(bool, int, float, string) or arrayCell"""
        input = """
            void main(int z[]){
                do
                {
                float k ;
                int complex ;
                complex = 1-------------------------1;
                int a[32];
                 1+2+1----------34 = 1;

                }
                if(true){
                    do
                         
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                        
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    
                }
                while(true);
            
            }
            

        """
        expect = "Not Left Value: BinaryOp(-,BinaryOp(+,BinaryOp(+,IntLiteral(1),IntLiteral(2)),IntLiteral(1)),UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLiteral(34)))))))))))"
        self.assertTrue(TestChecker.test(input, expect, 485))
    def test86_NotLeftValue(self):
        """ LHS must be Id(bool, int, float, string) or arrayCell"""
        input = """
            void main(int z[]){
                do
                {
                float k ;
                int complex ;
                complex = 1-------------------------1;
                int a[32];
                 k = k* 1 =5;

                }
                if(true){
                    do
                         
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                        
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    
                }
                while(true);
            
            }
            

        """
        expect = "Not Left Value: BinaryOp(*,Id(k),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 486))
    def test87_NotLeftValue(self):
        """ LHS must be Id(bool, int, float, string) or arrayCell"""
        input = """
            void main(int z[]){
                do
                {
                float k ;
                int complex ;
                complex = 1-------------------------1;
                int a[32];
                 k = k* 1 ==5;

                }
                if(true){
                    do
                         
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                        
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    
                }
                while(true);
            
            }
            

        """
        expect = "Type Mismatch In Expression: BinaryOp(==,BinaryOp(*,Id(k),IntLiteral(1)),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input, expect, 487))
    def test88_NotLeftValue(self):
        """ LHS must be Id(bool, int, float, string) or arrayCell"""
        input = """
            void main(int z[]){
                do
                {
                float k ;
                int complex ;
                complex = 1-------------------------1;
                int a[32];
                 a[-1]=2 =2;

                }
                if(true){
                    do
                         
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                        
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    
                }
                while(true);
            
            }
            

        """
        expect = "Not Left Value: IntLiteral(2)"
        self.assertTrue(TestChecker.test(input, expect, 488))
    def test89_NotLeftValue(self):
        """ LHS must be Id(bool, int, float, string) or arrayCell"""
        input = """
            int sum(){return 1;}
            void main(int z[]){
                do
                sum();
                {
                float k ;
                int complex ;
                
                int a[32];
                sum = 1;
                }
                if(true){
                    do
                         break;
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                        
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    
                }
                while(true);
            
            }
            

        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(sum),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 489))
    def test90_CheckFullProgram(self):
        """ LHS must be Id(bool, int, float, string) or arrayCell"""
        input = """
            int sum(){return 1;}
            int sum2(int a[]){
                return 1;
            }
            void main(int z[]){
                do
                sum();
                {
                float k ;
                int complex ;
                
                int a[32];
                
                //sum = 1;
                }
                
                sum2(a);
                if(true){
                    do
                         break;
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                    if (true){
                        
                    }
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    
                }
                while(true);
            
            }
            

        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 490))
    def test91_CheckFullProgram(self):
        """ more complex program"""
        input = """
            int sum(){return 1;}
            int sum2(int a[]){
                return 1;
            }
            void main(int z[]){
                do
                sum();
                {
                float k ;
                int complex ;
                
                int a[32];
                
                //sum = 1;
                }
                
                {
                    int a;
                    sum2(a);
                }
                
                if(true){
                    do
                         break;
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                    if (true){
                        
                    }
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    
                }
                while(true);
            
            }
            

        """
        expect = "Type Mismatch In Expression: CallExpr(Id(sum2),[Id(a)])"
        self.assertTrue(TestChecker.test(input, expect, 491))
    def test92_CheckFullProgram(self):
        """ more complex program"""
        input = """
            int sum(){return 1;}
            int sum2(int a[]){
                return 1;
            }
            void main(int z[]){
                float a[32];
                do
                sum();
                {
                float k ;
                int complex ;
                
                
                
                //sum = 1;
                }
                
                {
                    
                    sum2(a);
                }
                
                if(true){
                    do
                         break;
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                    if (true){
                        
                    }
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    
                }
                while(true);
            
            }
            

        """
        expect = "Type Mismatch In Expression: CallExpr(Id(sum2),[Id(a)])"
        self.assertTrue(TestChecker.test(input, expect, 492))
    def test93_CheckFullProgram(self):
        """ more complex program"""
        input = """
            int sum(){return 1;}
            int sum2(int a[]){
                return 1;
            }
            void main(int z[]){
                int a[32];
                do
                sum();
                {
                float k ;
                int complex ;
                
                
                
                //sum = 1;
                }
                
                {
                    
                    sum2(z);
                }
                
                if(true){
                    do
                         break;
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                    if (true){
                        
                    }
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    
                }
                while(true);
                break;
            }
            

        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 493))
    def test94_CheckFullProgram(self):
        """ more complex program"""
        input = """
            int sum(){return 1;}
            int sum2(int a[]){
                return 1;
            }
            int main(int z[]){
                int a[32];
                do
                sum();
                {
                float k ;
                int complex ;
                
                
                
                //sum = 1;
                }
                
                {
                    
                    sum2(z);
                }
                
                if(true){
                    do
                         break;
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                    if (true){
                        
                    }
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    break;
                }
                break;
                
                while(true);
                if (true){
                    int a, b,c[4];
                    
                }
            }
            

        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 494))
    def test95_CheckFullProgram(self):
        """ more complex program"""
        input = """
            int sum(){return 1;}
            int sum2(int a[]){
                return 1;
            }
            int main(int z[]){
                int a[32];
                do
                sum();
                {
                float k ;
                int complex ;
                
                
                
                //sum = 1;
                }
                
                {
                    
                    sum2(z);
                }
                
                if(true){
                    do
                         break;
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                    if (true){
                        
                    }
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    break;
                }
                break;
                return;
                while(true);
                if (true){
                    int a, b,c[4];
                    return 1;
                }
            }
            

        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 495))
    def test96_CheckFullProgram(self):
        """ more complex program"""
        input = """
            int sum(){return 1;}
            int sum2(int a[]){
                return 1;
            }
            int main(int z[]){
                int a[32];
                do
                sum();
                {
                float k ;
                int complex ;
                
                
                
                //sum = 1;
                }
                
                {
                    
                    sum2(z);
                }
                
                if(true){
                    do
                         break;
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                    if (true){
                        
                    }
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    break ;
                }
                break;
                for (1;true;1){
                    return 1;
                }
                while(true);
                if (true){
                    int a, b,c[4];
                    return 1;
                }
            }
            

        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input, expect, 496))
    def test97_CheckFullProgram(self):
        """ more complex program"""
        input = """
            int sum(){return 1;}
            int sum2(int a[]){
                return 1;
            }
            int main(int z[]){
                int a[32];
                do
                sum();
                {
                float k ;
                int complex ;
                
                
                
                //sum = 1;
                }
                
                {
                    
                    sum2(z);
                }
                
                if(true){
                    do
                         break;
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                    if (true){
                        
                    }
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    break ;
                }
                break;
                for (1;true;1){
                    return 1;
                }
                while(true);
                if (true){
                    int a, b,c[4];
                    return 1;
                }
                return 1;
                a = k;
            }
            

        """
        expect = "Undeclared Identifier: k"
        self.assertTrue(TestChecker.test(input, expect, 497))
    def test98_CheckFullProgram(self):
        """ more complex program"""
        input = """
            int sum(){return 1;}
            int sum2(int a[]){
                return 1;
            }
            int main(int z[]){
                int a[32];
                do
                sum();
                {
                float k ;
                int complex ;
                
                
                
                //sum = 1;
                }
                
                {
                    
                    sum2(z);
                }
                
                if(true){
                    do
                         break;
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                    if (true){
                        
                    }
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    break ;
                }
                break;
                for (1;true;1){
                    return 1;
                }
                while(true);
                if (true){
                    int a, b,c[4];
                    return 1;
                }
                return 1;
                a = 1;
            }
            

        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 498))
    def test99_CheckFullProgram(self):
        """ more complex program"""
        input = """
            int sum(){return 1;}
            int sum2(int a[]){
                return 1;
            }
            int main(int z[]){
                int a[32];
                do
                sum();
                {
                float k ;
                int complex ;
                
                
                
                //sum = 1;
                }
                
                {
                    
                    sum2(z);
                }
                
                if(true){
                    do
                         break;
                        do {}
                        while(true);
                        for(1; true; 1){
                            
                        }
                    if (true){
                        
                    }
                    while(true);
                }
                else{
                    do break;
                    while(true);
                    break ;
                }
                break;
                for (1;true;1){
                    return 1;
                }
                while(true);
                if (true){
                    int a, b,c[4];
                    return 1;
                }
                return 1;
                a[main(a)] = a[main(a)+1+sum()+sum2(2)];
            }
            

        """
        expect = "Type Mismatch In Expression: CallExpr(Id(sum2),[IntLiteral(2)])"
        self.assertTrue(TestChecker.test(input, expect, 499))