grammar mC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options {
	language = Python3;
}

program: (var_dec | func_dec)+ EOF;

var_dec: params SM;
func_dec: type_stmt ID LP param_list RP LB func_body RB;

params: type_stmt ID (CM ID)*; // int a,b,c;
param_list: (params (SM params)*)?; // int a,b; float d,e;
// param_list1: one_param SM param_list | one_param;
func_body: ( var_dec | stmt)*;
stmt: ( assignment | call | return_stmt) SM;
assignment: ID EQ exp;
call: ID LP (exp (CM exp)*)? RP;
return_stmt: RETURN exp;

exp
	: exp1 ADD exp
	| exp1
	;
exp1
	: exp2 SUB exp2
	| exp2
	;
exp2
	: exp2 MUL exp3
	| exp2 DIV exp3
	| exp3
	;
exp3
	: INTLIT
	| FLOATLIT
	| ID 
	| call
	| LP exp RP
	;

type_stmt: INT | FLOAT;

fragment LETTER: [a-z];
fragment NUMBER: [0-9];
fragment DOT: '.';

INTLIT: NUMBER+;
FLOATLIT:
	NUMBER+ ((DOT NUMBER+ [eE][+-]?) | (DOT | ([eE][+-]?))) NUMBER+;
INT: 'int';
FLOAT: 'float';
RETURN: 'return';

LB: '{';
RB: '}';
SM: ';';
CM: ',';
EQ: '=';
LP: '(';
RP: ')';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';

COLON: ':';
VAR: 'Var';

ID: LETTER (LETTER | NUMBER)*;

WS: [ \t\r\n\f]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;