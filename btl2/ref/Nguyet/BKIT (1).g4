//ID:1927029
grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

program
 : varDeclarList functionList EOF
 ;

varDeclarList
 : noNullVarDeclarList
 |
 ;

noNullVarDeclarList
 : varDeclar noNullVarDeclarList
 | varDeclar
 ;

varDeclar
    : VAR COLON varList SEMI
    ;

varList 
    : var CM varList
    | var
    ;

var
    : nonInit
    | init
    ;

nonInit
    : ID
    | declarArray
    ;

init
    : ID EQUAL literals
    | declarArray EQUAL literals
    ;

literals
    : INTLIT
    | FLOATLIT
    | BOOLLIT
    | STRINGLIT
    ;


declarArray
    : ID arrayOper
    ;

arrayOper
    : LSB INTLIT RSB
    | LSB INTLIT RSB arrayOper
    ;

elmexp
    : ID indexOper
    ;

indexOper
    : LSB expression RSB
    | LSB expression RSB indexOper
    ;

functionList
    : nonNullFunctionList
    |
    ;

nonNullFunctionList
    : funcDeclar nonNullFunctionList
    | funcDeclar
    ;

funcDeclar
    : FUNCTION COLON ID PARAMETER COLON pramList bodyFunc
    | FUNCTION COLON ID bodyFunc
    ;

pramList
    : nonInit CM pramList
    | nonInit
    ;

bodyFunc
    : BEGINFUNC statemtList  ENDFUNC
    ;

BEGINFUNC
    : BODY COLON
    ;
ENDFUNC
    : ENDBODY DOT
    ;

statemtList
    : varDeclarList otherStatementList
    ;

otherStatementList
    : noNullOtherStatementList
    |
    ;

noNullOtherStatementList
    : otherStatement noNullOtherStatementList
    | otherStatement
    ;

otherStatement
    : assignstm
    | ifStm
    | forStm
    | whileStm
    | doWhileStm
    | breakStm
    | continueStm
    | callStm
    | returnstm
    ;

assignstm
    : variable EQUAL expression SEMI
    ;

variable
    : ID
    | elmexp
    ;

expression
    : expression EQINT expression2
    | expression NOTEQINT expression2
    | expression LESS expression2
    | expression GREATER expression2
    | expression LESSEQINT expression2
    | expression GREATEREQINT expression2
    | expression NOTEQF expression2
    | expression LESSF expression2
    | expression GREATERF expression2
    | expression LESSEQF expression2
    | expression GREATEREQF expression2
    | expression2
    ;

expression2
    : expression2 CONJ expression3
    | expression2 DISJ expression3
    | expression3 
    ;

expression3
    : expression3 ADDINT expression4
    | expression3 ADDF expression4
    | expression3 SUBINT expression4
    | expression3 SUBF expression4
    | expression4
    ;

expression4
    : expression4 MULINT expression5
    | expression4 MULF expression5
    | expression4 DIVINT expression5
    | expression4 DIVF expression5
    | expression4 REINT expression5
    | expression5
    ;

expression5
    : NEG expression5
    | expression6
    ;

expression6
    : SUBINT expression6
    | SUBF expression6
    | expression7
    ;


expression7
    : ID
    | literals
    | LP expression RP
    | elmexp
    | callfunc
    ;


callfunc
    : ID LP expList RP
    ;

expList
    : nonNullExpList
    | 
    ;

nonNullExpList
    : expression CM nonNullExpList
    | expression
    ;

ifStm
    : IF expression THEN statemtList (ELSEIF expression THEN statemtList)* (ELSE statemtList)? ENDIF DOT
    ;


forStm
    : FOR LP ID EQUAL expression CM expression CM ID EQUAL expression RP DO statemtList ENDFOR DOT
    ;

whileStm
    : WHILE expression DO statemtList ENDWHILE DOT
    ;

doWhileStm
    : DO statemtList WHILE expression SEMI
    ;

breakStm
    : BREAK SEMI
    ;

continueStm
    : CONTINUE SEMI
    ;

callStm
    : callfunc SEMI
    ;

returnstm
    : RETURN expression SEMI
    | RETURN SEMI
    ;

COMMENT
    : '**' .*? '**' -> skip;


BREAK
    : 'Break';
CONTINUE
    : 'Continue'
    ;
DO
    : 'Do'
    ;
ELSE
    : 'Else'
    ;
ELSEIF
    : 'ElseIf'
    ;
ENDBODY
    : 'EndBody'
    ;
ENDIF
    : 'EndIf'
    ;
ENDFOR
    : 'EndFor'
    ;
ENDWHILE
    : 'EndWhile'
    ;
FOR
    : 'For'
    ;
FUNCTION
    : 'Function'
    ;
IF
    : 'If'
    ;
PARAMETER
    : 'Parameter'
    ;
RETURN
    : 'Return'
    ;
THEN
    : 'Then'
    ;
VAR
    : 'Var'
    ;
WHILE
    : 'While'
    ;
BODY
    : 'Body';

ADDINT
    : '+'
    ;
ADDF
    : '+.'
    ;
SUBINT
    : '-'
    ;
SUBF
    : '-.'
    ;
MULINT
    : '*'
    ;
MULF
    : '*.'
    ;
DIVINT
    : '\\'
    ;
DIVF
    : '/'
    ;
REINT
    : '%'
    ;

CONJ
    : '&&'
    ;
DISJ
    : '||'
    ;

NOTEQF
    : '=/='
    ;
LESSF
    : '<.'
    ;
EQINT
    : '=='
    ;
NOTEQINT
    : '!='
    ;
NEG
    : '!'
    ;
LESS    
    : '<'
    ;
GREATER
    : '>'
    ;
LESSEQINT
    : '<='
    ;
GREATEREQINT
    : '>='
    ;
GREATERF
    : '>.'
    ;
LESSEQF
    : '<=.'
    ;
GREATEREQF
    : '>=.'
    ;

EQUAL
    : '='
    ;

LP
    : '('
    ;
RP
    : ')'
    ;
LSB
    : '['
    ;
RSB 
    : ']'
    ;
COLON
    : ':'
    ;
SEMI
    : ';' 
    ;
DOT
    : '.'
    ;
CM
    : ','
    ;


INTLIT
    : DECIMAL 
    | HEX 
    | OCT
    ;
fragment DECIMAL
    : [0-9]+
    ;
fragment HEX
    :'0'[Xx][0-9A-F]+
    ;
fragment OCT
    : '0'[Oo][0-7]+
    ;
fragment EE
    : [Ee]
    ;


FLOATLIT
    : DECIMAL DECPART? EXPPART?
    ;
fragment DECPART
    : DOT DECIMAL*
    ;
fragment EXPPART
    : EE SIGN? DECIMAL
    ;
fragment SIGN
    : ADDINT | SUBINT
    ;

BOOLLIT
    : TRUE 
    | FALSE
    ;
fragment TRUE
    : 'True'
    ;
fragment FALSE
    : 'False'
    ;

ID
    : [a-z][a-zA-Z_0-9]* 
    ;

STRINGLIT
    : '"' STR_CHAR* '"'
    {
        test = str(self.text)
        self.text = test[1:-1]
    }
    ;

WS 
    : [ \t\r\n]+ -> skip 
    ; // skip spaces, tabs, newlines

UNCLOSE_STRING
    : '"' STR_CHAR* ( [\n\r] | EOF )
	{
		y = str(self.text)
		possible = ['\n', '\r']
		if y[-1] in possible:
			raise UncloseString(y[1:-1])
		else:
			raise UncloseString(y[1:])
	}
    ;

ILLEGAL_ESCAPE
    : '"' STR_CHAR* ESC_ILLEGAL
	{
		y = str(self.text)
		raise IllegalEscape(y[1:])
	}
    ;

fragment STR_CHAR
    : ~[\n\b"'\\] | ESC_SEQ | ('\'' '"') 
    ;
fragment ESC_SEQ
    : '\\' [btnfr"'\\] 
    ;
fragment ESC_ILLEGAL
    : '\\' ~[btnfr"'\\] | ~'\\' 
    ;


ERROR_CHAR
    : .
    ; 
