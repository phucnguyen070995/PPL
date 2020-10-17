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

program:            program_part EOF;
program_part:       (var_dec | func_dec | statement_list) program_part
                    | var_dec
                    | func_dec
                    | statement_list;

//-------------------------------Variable declaration---------------------------------

var_dec:            VAR COLON variable_list SEMI;
variable_list:      (scalar_variable | composite_variable) COMMA variable_list
                    | scalar_variable
                    | composite_variable;
scalar_variable:    ID ASSIG (INTERGER | FLOAT | BOOLEAN | STRING)
                    | ID;
composite_variable: composite_var_name ASSIG ARRAY
                    | composite_var_name;
composite_var_name: ID many_demension;
many_demension:     one_demension many_demension
                    | one_demension;
one_demension:      LB INTERGER RB;

//-------------------------------Function declaration---------------------------------

func_dec:           FUNCTION COLON (ID | ID params) func_body;

params:             PARAMETER COLON param_list;
param_list:         (ID | composite_var_name) COMMA param_list
                    | ID
                    | composite_var_name;

func_body:          BODY (
                        COLON var_dec_list 
                        | COLON statement_list
                        | COLON var_dec_list statement_list) 
                    ENDBODY DOT;

var_dec_list:       var_dec var_dec_list
                    | var_dec;

//-------------------------------Expressions---------------------------------

expression_stm:     term1 relational term1 | term1;
term1:              term1 logical term2 | term2;
term2:              term2 adding term3 | term3;
term3:              term3 multiplying term4 | term4;
term4:              NOT term4 | term5;
term5:              (SUBOP | SUBF) term5 | term6;
term6:              term6 LB expression_stm RB | term7;
term7:              (LP expression_stm RP) | operand;
operand:            ID | FLOAT | INTERGER | STRING | BOOLEAN | ARRAY | callee;

//-------------------------------Call function---------------------------------

callee:             (ID | type_coercions) (LP | LP parameter_callee) RP;
parameter_callee:   expression_stm COMMA parameter_callee
                    | expression_stm;

type_coercions:     'int_of_float' | 'float_of_int' | 'int_of_string' | 'string_of_int' | 'float_of_string' | 'string_of_float' | 'bool_of_string' | 'string_of_bool';

//-------------------------------Statement---------------------------------

statement_list:     statement_part statement_list
                    | statement_part;
statement_part:     if_stm 
                    | assign_stm
                    | do_while_stm SEMI
                    | for_stm
                    | break_stm
                    | continue_stm
                    | return_stm
                    | while_stm
                    | do_while_stm
                    | call_stm;

//-------------------------------Assignment Statement---------------------------------

assign_stm:         expression_stm ASSIG expression_stm SEMI;

//-------------------------------If Statement---------------------------------
                                    
if_stm:             IF expression_stm THEN ( statement_list | statement_list elseif_else) ENDIF DOT;
elseif_else:        elseif_one elseif_else
                    | elseif_one
                    | else_one;
elseif_one:         ELSEIF expression_stm THEN statement_list;
else_one:           ELSE statement_list;

//-------------------------------For Statement---------------------------------

for_stm:            FOR LP ID ASSIG INTERGER COMMA expression_stm COMMA expression_stm RP DO statement_list ENDFOR DOT;

//-------------------------------return Statement---------------------------------

return_stm:         (RETURN | RETURN expression_stm) SEMI;

//-------------------------------While Statement---------------------------------

while_stm:          WHILE expression_stm DO (statement_list ENDWHILE | ENDWHILE) DOT;

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
fragment TRUE:       'True';
fragment FALSE:      'False';
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
INTERGER:            DECIMAL | HEXA | OCTAL;

//-------------------------------Float---------------------------------

fragment EXPONENT:      ('E' | 'e') (ADDOP | SUBOP)? NUMBER+;
fragment DECIMAL_PART:  DOT NUMBER*;
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
fragment EXCEPT_QUOTE:      SINGLE_QUOTE DOUBLE_QUOTE|
                            '\\\'';
fragment DENY_QUOTE:        SINGLE_QUOTE;

STRING:     DOUBLE_QUOTE (STR_CHAR)* DOUBLE_QUOTE;

//-------------------------------ARRAY---------------------------------

ARRAY:                  LCB SPACE (
                            INTERGER (SPACE COMMA SPACE INTERGER)*
                            | FLOAT (SPACE COMMA SPACE FLOAT)*
                            | STRING (SPACE COMMA SPACE STRING)*
                            | ARRAY (SPACE COMMA SPACE ARRAY)*
                            | BOOLEAN (SPACE COMMA SPACE BOOLEAN)*
                        ) SPACE RCB;

fragment SPACE:         [ ]*;
//-------------------------------BOOLEAN---------------------------------

BOOLEAN:    TRUE | FALSE;

//-------------------------------Identifiers---------------------------------

ID: LOWCASE(LOWCASE|UPPERCASE|UNDERCORE|NUMBER)*;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


//ERROR_CHAR: .;
//UNCLOSE_STRING: .;
//ILLEGAL_ESCAPE: .;
//UNTERMINATED_COMMENT: .;

fragment STR_CHAR: ~[\n\b"'\\] | ESCAPE_SEQUENCE | ('\'' '"');
fragment ESC_ILLEGAL: '\\' ~[btnfr'\\] | '\\';

ERROR_CHAR: .;
UNCLOSE_STRING:
	'"' STR_CHAR* ([\n\r] | EOF) {
		y = str(self.text)
		possible = ['\n', '\r']
		if y[-1] in possible:
			raise UncloseString(y[1:-1])
		else:
			raise UncloseString(y[1:])
	};
ILLEGAL_ESCAPE:
	'"' STR_CHAR* ESC_ILLEGAL {
		y = str(self.text)
		raise IllegalEscape(y[1:])
	};
UNTERMINATED_COMMENT:
	'**' .*? (~'*' ~'*' (EOF) | ~'*' '*' EOF) { raise UnterminatedComment() };