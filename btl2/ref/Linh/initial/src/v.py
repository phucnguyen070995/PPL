    
for x in range(100):
    f = open("./test/ASTGenSuite.py", "a+")
    g = open("./test/testcases/" + str(300+x) + ".txt", "r")
    f.write("\tdef test_"+ str(x)+  "(self):\n\t\t\"\"\"AST_TEST_" + str(x)+ "\"\"\"\n")
    f.write("\t\tinput=\"\"\""+ g.read()  +"\"\"\"\n")
    f.write("\t\texpect = \"\"\n")
    f.write("\t\tself.assertTrue(TestAST.checkASTGen(input,expect," + str(300+x)+  "))\n" )    
    f.close()