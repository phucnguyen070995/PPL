//1927030
//NGUYEN HOANG PHUC
grammar BKIT;

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

options{
	language=Python3;
}

program  : (var_dec | func_dec | statement_list)+ EOF;

//-------------------------------Variable declaration---------------------------------

var_dec:            VAR COLON variable_list SEMI;
variable_list:      (scalar_variable | composite_variable) COMMA variable_list
                    | scalar_variable
                    | composite_variable;
scalar_variable:    ID ASSIG (INTERGER | FLOAT | BOOLEAN | STRING)
                    | ID;
composite_variable: composite_var_name ASSIG ARRAY
                    | composite_var_name;
composite_var_name: ID (LB INTERGER RB)+;


//-------------------------------Function declaration---------------------------------

func_dec:           FUNCTION COLON ID param_list? func_body;

params:             PARAMETER COLON param_list;
param_list:         (ID | composite_var_name) COMMA param_list
                    | ID
                    | composite_var_name;

func_body:          BODY COLON ( var_dec | statement_list)* ENDBODY DOT;
// statement:          ( assignment | call | return_stmt) SEMI;
// assignment:         ID ASSIG expression_stm;
call:               ID LP (expression_stm (COMMA expression_stm)*)? RP;
return_stmt:        RETURN expression_stm;

expression_stm:     term1 ASSIG term1 | term1;
term1:              term2 relational term2 | term2;
term2:              term3 logical term2 | term3;
term3:              term4 adding term3 | term4;
term4:              term5 multiplying term4 | term5;
term5:              NOT term5 | term6;
term6:              (SUBOP | SUBF) term6 | term7;
term7:              term8 (LB expression_stm RB) | term8;
term8:              (LP expression_stm RP) | operand;
operand:            BOOLEAN | FLOAT | INTERGER | STRING | composite_var_name | ID | callee;

//-------------------------------Call function---------------------------------

callee:             ID LP (expression_stm (COMMA expression_stm)*)? RP;

//-------------------------------Statement---------------------------------

statement_list:     statement_part statement_list
                    | statement_part;
statement_part:     if_stm 
                    | do_while_stm SEMI
                    | for_stm
                    | break_stm
                    | continue_stm
                    | return_stm
                    | while_stm
                    | do_while_stm
                    | call_stm
                    | expression_stm SEMI;

//-------------------------------If Statement---------------------------------
                                    
if_stm:             IF expression_stm (THEN statement_list | THEN statement_list elseif_else) ENDIF DOT;
elseif_else:        elseif_one elseif_else
                    | elseif_one
                    | else_one;
elseif_one:         ELSEIF expression_stm THEN statement_list;
else_one:               ELSE statement_list;

//-------------------------------For Statement---------------------------------

for_stm:            FOR LP expression_stm SEMI expression_stm SEMI expression_stm RP statement_list;

//-------------------------------return Statement---------------------------------

return_stm:         (RETURN | RETURN expression_stm) SEMI;

//-------------------------------While Statement---------------------------------

while_stm:          WHILE expression_stm DO (statement_list ENDWHILE | ENDWHILE) ENDWHILE DOT;

//-------------------------------Do-While Statement---------------------------------

do_while_stm:       DO (statement_list WHILE | WHILE) expression_stm ENDDO DOT;

//-------------------------------Other Statement---------------------------------

break_stm:          BREAK SEMI;
continue_stm:       CONTINUE SEMI;
call_stm:           callee SEMI;

//-------------------------------Operator Group---------------------------------

multiplying:        MULOP | MULF | DIVOP | DIVF | MODOP;
adding:             ADDOP | ADDF | SUBOP | SUBF;
logical:            AND | OR;
relational:         EQ | NEQ | LT | GT | LTE | GTE | NEQF | LTF | GTF | LTEF | GTEF;

//-------------------------------Separators---------------------------------

LP          :'(';
RP          :')';
LB          :'[';
RB          :']';
COLON       :':';
DOT         :'.';
COMMA       :',';
SEMI        :';';
LCB         :'{';
RCB         :'}';

//-------------------------------Operators---------------------------------

ADDOP       :'+';
ADDF        :'+.';
SUBOP       :'-';
SUBF        :'-.';
MULOP       :'*';
MULF        :'*.';
DIVOP       :'\\';
DIVF        :'\\.';
MODOP       :'%';
NOT         :'!';
AND         :'&&';
OR          :'||';
EQ          :'==';
NEQ         :'!=';
LT          :'<';
GT          :'>';
LTE         :'<=';
GTE         :'>=';
NEQF        :'=/=';
LTF         :'<.';
GTF         :'>.';
LTEF        :'<=.';
GTEF        :'>=.';
ASSIG       :'=';

//-------------------------------Keywords---------------------------------

BODY:       'Body';
BREAK:      'Break';
CONTINUE:   'Continue';
DO:         'Do';
ELSE:       'Else';
ELSEIF:     'ElseIf';
ENDBODY:    'EndBody';
ENDIF:      'EndIf';
ENDFOR:     'EndFor';
ENDWHILE:   'EndWhile';
FOR:        'For';
FUNCTION:   'Function';
IF:         'If';
PARAMETER:  'Parameter';
RETURN:     'Return';
THEN:       'Then';
VAR:        'Var';
WHILE:      'While';
TRUE:       'True';
FALSE:      'False';
ENDDO:      'EndDo';

//-------------------------------FRAGMENT---------------------------------

fragment LOWCASE:       [a-z];
fragment UPPERCASE:     [A-Z];
fragment NUMBER:        [0-9];
fragment UNDERCORE:     '_';
fragment BACKSPACE:     '\\b';
fragment FORMFEED:      '\\f';
fragment CARRIAGE_RETURN:'\\r';
fragment NEWLINE:       '\\n';
fragment HORIZONTAL_TAB:'\\t';
fragment SINGLE_QUOTE:  '\'';
fragment DOUBLE_QUOTE:  '"';
fragment BACK_SLASH:    '\\\\';

//-------------------------------Literals---------------------------------
//-------------------------------Integer---------------------------------

fragment HEXA:       '0'('x' | 'X') [1-9A-F] (NUMBER | [A-F])*;
fragment DECIMAL:    [1-9] NUMBER* | '0';
fragment OCTAL:      '0'('o' | 'O') [1-7][0-7]*;
INTERGER:   DECIMAL | HEXA | OCTAL;

//-------------------------------Float---------------------------------

fragment EXPONENT:  ('E' | 'e') (ADDOP | SUBOP)? NUMBER+;
fragment DECIMAL_PART: DOT NUMBER*;
FLOAT:              [1-9] NUMBER* (DECIMAL_PART 
                        | EXPONENT
                        | DECIMAL_PART EXPONENT
                        | DECIMAL_PART)?;

//-------------------------------String---------------------------------

fragment ESCAPE_SEQUENCE    :   BACKSPACE
                            |   FORMFEED
                            |   CARRIAGE_RETURN
                            |   NEWLINE
                            |   HORIZONTAL_TAB
                            |   SINGLE_QUOTE
                            |   BACK_SLASH
                            ;

STRING:     DOUBLE_QUOTE (
                SINGLE_QUOTE DOUBLE_QUOTE
                | ESCAPE_SEQUENCE
                | ~[\nEOF"]
            )*
            DOUBLE_QUOTE;

//-------------------------------ARRAY---------------------------------

ARRAY:  LCB (
            INTERGER (COMMA INTERGER)*
            | FLOAT (COMMA FLOAT)*
            | STRING (COMMA STRING)*
            | ARRAY (COMMA ARRAY)*
            | BOOLEAN (COMMA BOOLEAN)*
        ) RCB;

//-------------------------------BOOLEAN---------------------------------

BOOLEAN:    TRUE | FALSE;
//-------------------------------Identifiers---------------------------------

ID: LOWCASE(LOWCASE|UPPERCASE|UNDERCORE|NUMBER)*;



WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;
