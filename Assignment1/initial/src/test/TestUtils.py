import sys,os
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener,ErrorListener
if not './main/mc/parser/' in sys.path:
    sys.path.append('./main/mc/parser/')
if os.path.isdir('../target/main/mc/parser') and not '../target/main/mc/parser/' in sys.path:
    sys.path.append('../target/main/mc/parser/')
from MCLexer import MCLexer
from MCParser import MCParser
from lexererr import *
def TokenText():
    src="../target/main/mc/parser/MC.tokens"
    f=open(src,'r',encoding='utf-8')
    temp=f.readline()
    arr=[]
    while temp:
        stri=temp.split('=')
        arr.append(stri[0])
        temp=f.readline()
    f.close()
    return arr
class TestUtil:
    @staticmethod
    def makeSource(inputStr,num):
        filename = "./test/testcases/" + str(num) + ".txt"
        file = open(filename,"w")
        file.write(inputStr)
        file.close()
        return FileStream(filename)


class TestLexer:
    @staticmethod
    def checkLexeme(input,expect,num):
        inputfile = TestUtil.makeSource(input,num)
        dest = open("./test/solutions/" + str(num) + ".txt","w")
        destDetail = open("./test/solutions/" + "testDetail.txt","w")
        lexer = MCLexer(inputfile)
        try:
            TestLexer.printLexeme(dest,lexer, destDetail)
        except (ErrorToken,UncloseString,IllegalEscape) as err:
            dest.write(err.message)
            destDetail.write(err.message)
        finally:
            dest.close()
            destDetail.close() 
        dest = open("./test/solutions/" + str(num) + ".txt","r")
        line = dest.read()
        return line == expect

    
    @staticmethod    
    def printLexeme(dest,lexer,destDetail):
        tok = lexer.nextToken()
        if tok.type != Token.EOF:
            dest.write(tok.text+",")
            List =  TokenText()
            destDetail.write(List[tok.type-1]+" "+tok.text+"\n")
            #dest.write(List[tok.type-1]+" "+tok.text+"\n")
            TestLexer.printLexeme(dest,lexer,destDetail)
        else:
            dest.write("<EOF>")
class NewErrorListener(ConsoleErrorListener):
    INSTANCE = None
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxException("Error on line "+ str(line) + " col " + str(column)+ ": " + offendingSymbol.text)
NewErrorListener.INSTANCE = NewErrorListener()

class SyntaxException(Exception):
    def __init__(self,msg):
        self.message = msg

class TestParser:
    @staticmethod
    def createErrorListener():
         return NewErrorListener.INSTANCE

    @staticmethod
    def checkParser(input,expect,num):
        inputfile = TestUtil.makeSource(input,num)
        dest = open("./test/solutions/" + str(num) + ".txt","w")
        lexer = MCLexer(inputfile)
        listener = TestParser.createErrorListener()

        tokens = CommonTokenStream(lexer)

        parser = MCParser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(listener)
        try:
            parser.program()
            dest.write("successful")
        except SyntaxException as f:
            dest.write(f.message)
        except Exception as e:
            dest.write(str(e))
        finally:
            dest.close()
            
        dest = open("./test/solutions/" + str(num) + ".txt","r")
        line = dest.read()
        return line == expect


        