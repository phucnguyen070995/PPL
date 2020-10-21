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

program  : VAR COLON SEMI ID ;

fragment    LOWCASE         :   [a-z]   ;
fragment    UPPERCASE       :   [A-Z]   ;
fragment    DIGIT           :   [0-9]   ;
fragment    UNDERCORE       :   '_'     ;


fragment    BACK_SPACE      :   '\\b'   ;
fragment    FORM_FEED       :   '\\f'   ;
fragment    CARRIAGE_RETURN :   '\\r'   ;
fragment    NEW_LINE        :   '\\n'   ;
fragment    HORIZONTAL_TAB  :   '\\t'   ;
fragment    SINGLE_QUOTE    :   '\\\''    ;
fragment    DOUBLE_QUOTE    :   '"'    ;
fragment    BACK_SLASH      :   '\\\\' ;


// --------------------------------------------------------
// ---------------------- IDENTIFIERS ---------------------
// --------------------------------------------------------

ID                  :   LOWCASE (LOWCASE | UPPERCASE | UNDERCORE | DIGIT)* ;

// --------------------------------------------------------
// ------------------------ KEYWORDS ----------------------
// --------------------------------------------------------

BODY                :'Body'         ;
BREAK               :'Break'        ;
CONTINUE            :'Continue'     ;
DO                  :'Do'           ;
ELSE                :'Else'         ;
ELSEIF              :'ElseIf'       ;
ENDBODY             :'EndBody'      ;
ENDIF               :'Endif'        ;
ENDFOR              :'EndFor'       ;
ENDWHILE            :'EndWhile'     ;
FOR                 :'For'          ;
FUNCTION            :'Function'     ;
IF                  :'If'           ;
PARAMETER           :'Parameter'    ;
RETURN              :'Return'       ;
THEN                :'Then'         ;
VAR                 :'Var'          ;
WHILE               :'While'        ;
TRUE                :'True'         ;
FALSE               :'False'        ;
ENDDO               :'EndDo'        ;

// --------------------------------------------------------
// ----------------------- OPERATORS ----------------------
// --------------------------------------------------------
ADD                 :'+'            ;
ADDF                :'+.'           ;
SUB                 :'-'            ;
SUBF                :'-.'           ;
MUL                 :'*'            ;
MULF                :'*.'           ;
DIV                 :'\\'           ;
DIVF                :'\\.'          ;
MOD                 :'%'            ;
NOT                 :'!'            ;
AND                 :'&&'           ;
OR                  :'||'           ;
EQ                  :'=='           ;
NEQ                 :'!='           ;
LESS                :'<'            ;
GREAT               :'>'            ;
ELESS               :'<='           ;
EGREAT              :'>='           ;
NEQF                :'=/='          ;
LESSF               :'<.'           ;
GREATF              :'>.'           ;
ELESSF              :'<=.'          ;
EGREATF             :'>=.'          ;



// --------------------------------------------------------
// ----------------------- LITERALS -----------------------
// --------------------------------------------------------

// interger
fragment HEXA               :'0'('x' | 'X') ([1-9A-F] (DIGIT | [A-F])* | '0')       ;

fragment DECIMAL            :([1-9] DIGIT* | '0')                                   ;

fragment OCTAL              :'0'('o' | 'O') ([1-7][0-7]* | '0')                     ;

INTERGER                    :DECIMAL | HEXA | OCTAL                                 ;

// float
fragment EXPONENT_PART      :('e' | 'E') ('+' | '-')? DIGIT+                ;
fragment INTERGER_PART      :DIGIT+                                         ;
fragment DECIMAL_PART       :DOT DIGIT*                                     ;

FLOAT                       :INTERGER_PART  (
                                            DECIMAL_PART
                                            | EXPONENT_PART
                                            | DECIMAL_PART EXPONENT_PART
                                            );

// boolean
BOOLEAN                     : TRUE | FALSE                                  ;

// string - chua co ~EOF
fragment ESCAPE_SEQUENCE    :   BACK_SPACE
                            |   FORM_FEED
                            |   CARRIAGE_RETURN
                            |   NEW_LINE
                            |   HORIZONTAL_TAB
                            |   SINGLE_QUOTE
                            |   BACK_SLASH
                            ;
STRING                      :   DOUBLE_QUOTE 
                                    (
                                        (SINGLE_QUOTE DOUBLE_QUOTE) 
                                        |   ESCAPE_SEQUENCE
                                        |   ~[\n]
                                    )*?
                                DOUBLE_QUOTE;


// array

ARRAY                       :   LCB 
                                (
                                    INTERGER (COMMA INTERGER)*
                                    |   FLOAT (COMMA FLOAT)*
                                    |   STRING (COMMA STRING)*
                                    |   ARRAY (COMMA ARRAY)*
                                ) 
                                RCB;
                                

// --------------------------------------------------------
// ---------------------- SEPERATORS ----------------------
// --------------------------------------------------------

LP                  :'('            ;
RP                  :')'            ;
LB                  :'['            ;
RB                  :']'            ;
COLON               :':'            ;
DOT                 :'.'            ;
COMMA               :','            ;
SEMI                :';'            ;
LCB                 :'{'            ;
RCB                 :'}'            ;


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;