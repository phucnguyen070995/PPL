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

program  : VAR COLON ID SEMI EOF;

//-------------------------------Separators---------------------------------

LP          :'('        ;
RP          :')'        ;
LB          :'['        ;
RB          :']'        ;
COLON       :':'        ;
DOT         :'.'        ;
COMMA       :','        ;
SEMI        :';'        ;
LCB         :'{'        ;
RCB         :'}'        ;

//-------------------------------Operators---------------------------------

ADDOP       :'+'        ;
ADDF        :'+.'       ;
SUBOP       :'-'        ;
SUBF        :'-.'       ;
MULOP       :'*'        ;
MULF        :'*.'       ;
DIVOP       :'\\'       ;
DIVF        :'\\.'      ;
MODOP       :'%'        ;
NOT         :'!'        ;
CONJ        :'&&'       ;
DISJ        :'||'       ;
EQ          :'=='       ;
NEQ         :'!='       ;
LT          :'<'        ;
GT          :'>'        ;
LTE         :'<='       ;
GTE         :'>='       ;
NEQF        :'=/='      ;
LTF         :'<.'       ;
GTF         :'>.'       ;
LTEF        :'<=.'      ;
GTEF        :'>=.'      ;

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

fragment HEXA:       '0'('x' | 'X') ([1-9A-F] (NUMBER | [A-F])* | '0');
fragment DECIMAL:    [1-9] NUMBER* | '0';
fragment OCTAL:      '0'('o' | 'O') ([1-7][0-7]* | '0');
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

BOOLEAN:    TRUE | FALSE;
//-------------------------------Identifiers---------------------------------

ID: LOWCASE(LOWCASE|UPPERCASE|UNDERCORE|NUMBER)*;



WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;
