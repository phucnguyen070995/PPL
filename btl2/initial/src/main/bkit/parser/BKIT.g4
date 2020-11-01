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

program:            var_dec_many func_dec_many EOF;

var_dec_many:       var_dec var_dec_many
                    | var_dec
                    | ;

func_dec_many:      func_dec func_dec_many
                    | func_dec
                    | ;

//-------------------------------Variable declaration---------------------------------

var_dec:            VAR COLON var_list SEMI;

var_list:           var_one COMMA var_list
                    | var_one;

var_one:            scalar_variable | composite_variable;

scalar_variable:    ID ASSIG (INTERGER | FLOAT | BOOLEAN | STRING)
                    | ID;

composite_variable: composite_var_name ASSIG ARRAY
                    | composite_var_name;

composite_var_name: ID many_demension;

many_demension:     one_demension many_demension
                    | one_demension;

one_demension:      LB INTERGER RB;

//-------------------------------Function declaration---------------------------------

func_dec:           FUNCTION COLON ID params func_body;

params:             PARAMETER COLON param_list
                    | ;
param_list:         param_one COMMA param_list
                    | param_one;

param_one:          ID | composite_var_name;

func_body:          BODY COLON var_dec_many statement_list ENDBODY DOT;

//-------------------------------Expressions---------------------------------

expression:         term1 relational term1 | term1;
term1:              term1 logical term2 | term2;
term2:              term2 adding term3 | term3;
term3:              term3 multiplying term4 | term4;
term4:              NOT term4 | term5;
term5:              (SUBOP | SUBF) term5 | term6;
term6:              term6 LB expression RB | term7;
term7:              (LP expression RP) | operand;
operand:            ID | FLOAT | INTERGER | STRING | BOOLEAN | ARRAY | callee;

//-------------------------------Call function---------------------------------

callee:             ID LP parameter_callee RP;
parameter_callee:   expression COMMA parameter_callee
                    | expression
                    | ;

//-------------------------------Call coercions (su dung assignment sau)---------------------------------
// coercions:          TYPE_COERCIONS LP expression RP;
// TYPE_COERCIONS:     'int_of_float' | 'float_of_int' | 'int_of_string' | 'string_of_int' | 'float_of_string' | 'string_of_float' | 'bool_of_string' | 'string_of_bool';

//-------------------------------Statement---------------------------------

statement_list:     statement_part statement_list
                    | statement_part
                    | ;
statement_part:     if_stm
                    | assign_stm
                    | for_stm
                    | break_stm
                    | continue_stm
                    | return_stm
                    | while_stm
                    | do_while_stm
                    | call_stm;

//-------------------------------Assignment Statement---------------------------------

assign_stm:         assign SEMI;
assign:             ID (many_index | ) ASSIG expression;
many_index:         one_index many_index
                    | one_index;
one_index:          LB expression RB;

//-------------------------------If Statement---------------------------------
                                    
if_stm:             IF expression THEN var_dec_many statement_list elseif_else ENDIF DOT;
elseif_else:        elseif_one elseif_else
                    | elseif_one
                    | else_one
                    | ;
elseif_one:         ELSEIF expression THEN var_dec_many statement_list;
else_one:           ELSE var_dec_many statement_list;

//-------------------------------For Statement---------------------------------

for_stm:            FOR LP ID ASSIG expression COMMA expression COMMA expression RP DO var_dec_many statement_list ENDFOR DOT;

//-------------------------------return Statement---------------------------------

return_stm:         RETURN ( | expression) SEMI;

//-------------------------------While Statement---------------------------------

while_stm:          WHILE expression DO var_dec_many statement_list ENDWHILE DOT;

//-------------------------------Do-While Statement---------------------------------

do_while_stm:       DO var_dec_many statement_list WHILE expression ENDDO DOT;

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
LCB:        '{';
RCB:        '}';

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
fragment TRUE:   'True';
fragment FALSE:  'False';
ENDDO:      'EndDo';

//-------------------------------FRAGMENT---------------------------------

fragment LOWCASE:       [a-z];
fragment UPPERCASE:     [A-Z];
fragment NUMBER:        [0-9];
fragment UNDERCORE:     '_';
fragment SINGLE_QUOTE:  '\'';
fragment DOUBLE_QUOTE:  '"';

//-------------------------------Literals---------------------------------
//-------------------------------Integer---------------------------------

fragment HEXA:       '0'('x' | 'X') [1-9A-F] (NUMBER | [A-F])*;
fragment DECIMAL:    [1-9] NUMBER* | '0';
fragment OCTAL:      '0'('o' | 'O') [1-7][0-7]*;
INTERGER:            DECIMAL | HEXA | OCTAL;

//-------------------------------Float---------------------------------

fragment EXPONENT:      ('E' | 'e') (ADDOP | SUBOP)? NUMBER+;
fragment DECIMAL_PART:  DOT NUMBER*;
FLOAT:                  DECIMAL (DECIMAL_PART 
                        | EXPONENT
                        | DECIMAL_PART EXPONENT
                        | DECIMAL_PART);

//-------------------------------String---------------------------------

fragment ESCAPE_SEQUENCE:  '\\' [btnfr'\\];

STRING:                     DOUBLE_QUOTE (CHAR)*? DOUBLE_QUOTE {
                                self.text = self.text[1:-1]
                            };

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

ID:         LOWCASE(LOWCASE|UPPERCASE|UNDERCORE|NUMBER)*;

//-------------------------------Skip token---------------------------------

WS:         [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
COMMENT     : '**' COMMENT_BODY*? '**' -> skip;

// ERROR_CHAR: .;
// UNCLOSE_STRING: .;
// ILLEGAL_ESCAPE: .;
// UNTERMINATED_COMMENT: .;

fragment CHAR:              ~[\n"'\\] | ESCAPE_SEQUENCE | '\'' '"';
fragment ESCAPE_ILLEGAL:    '\\' ~[btnfr'\\] | '\\' | ['] ~["];
fragment COMMENT_BODY:      ~[*] | [*] ~[*] | [*] EOF;

ERROR_CHAR: .;
UNCLOSE_STRING:
	'"' CHAR* ([\n\r] | EOF) {
		y = str(self.text)
		impossible = ['\n', '\r']
		if y[-1] in impossible:
			raise UncloseString(y[1:-1])
		else:
			raise UncloseString(y[1:])
	};
ILLEGAL_ESCAPE:
	'"' CHAR* ESCAPE_ILLEGAL {
		y = str(self.text)
		raise IllegalEscape(y[1:])
	};
UNTERMINATED_COMMENT:
	'**' COMMENT_BODY* EOF {
        raise UnterminatedComment() 
    };