grammar Sintatico;

program          : declaration* EOF;

declaration      : funDecl
                 | varDecl
                 | statement;

funDecl          : FUN function;

varDecl          : VAR IDENTIFIER (ASSIGN expression)? SEMICOLON;

statement        : exprStmt
                 | forStmt
                 | ifStmt
                 | printStmt
                 | returnStmt
                 | whileStmt
                 | block;

exprStmt         : expression SEMICOLON;

forStmt          : FOR OPEN_PAREN (varDecl | exprStmt | SEMICOLON)
                               expression? SEMICOLON
                               expression? CLOSE_PAREN statement;

ifStmt           : IF OPEN_PAREN expression CLOSE_PAREN statement (ELSE statement)?;

printStmt        : PRINT (expression | IDENTIFIER) SEMICOLON;

returnStmt       : RETURN expression? SEMICOLON;

whileStmt        : WHILE OPEN_PAREN expression CLOSE_PAREN block;

block            : OPEN_BRACE declaration* CLOSE_BRACE;

expression       : assignment;

assignment       : (call '.')? IDENTIFIER ASSIGN assignment
                 | logic_or;

logic_or         : logic_and (OR logic_and)*;

logic_and        : equality (AND equality)*;

equality         : comparison ((EQUAL | NOT_EQUAL) comparison)*;

comparison       : term ((LESS_THAN | GREATER_THAN | LESS_EQUAL | GREATER_EQUAL) term)*;

term             : factor ((PLUS | MINUS) factor)*;

factor           : unary ((MULTIPLY | DIVIDE | MODULO) unary)*;

unary            : (NOT | MINUS) unary
                 | call;

call             : primary (OPEN_PAREN arguments? CLOSE_PAREN | '.' IDENTIFIER)*;

primary          : 'true' | 'false' | 'nil' | 'this'
                 | NUMBER | STRING | IDENTIFIER | OPEN_PAREN expression CLOSE_PAREN
                 | 'super' '.' IDENTIFIER;

arguments        : expression (COMMA expression)*;

function       : IDENTIFIER OPEN_PAREN parameters? CLOSE_PAREN block;

parameters     : IDENTIFIER (COMMA IDENTIFIER)*;


// Lexer

VAR             : 'var';
FUN             : 'fun';
FOR             : 'for';
IF              : 'if';
ELSE            : 'else';
WHILE           : 'while';
PRINT           : 'print';
RETURN          : 'return';
OR              : 'or';
AND             : 'and';
NOT             : 'not';
TRUE            : 'true';
FALSE           : 'false';
NIL             : 'nil';
THIS            : 'this';
SUPER           : 'super';
OPEN_PAREN      : '(';
CLOSE_PAREN     : ')';
OPEN_BRACE      : '{';
CLOSE_BRACE     : '}';
COMMA           : ',';
DOT             : '.';
MINUS           : '-';
PLUS            : '+';
SEMICOLON       : ';';
DIVIDE          : '/';
MULTIPLY        : '*';
MODULO          : '%';
LESS_THAN       : '<';
GREATER_THAN    : '>';
EQUAL           : '==';
NOT_EQUAL       : '!=';
LESS_EQUAL      : '<=';
GREATER_EQUAL   : '>=';
ASSIGN          : '=';
IDENTIFIER      : [a-zA-Z_][a-zA-Z0-9_]*;
STRING          : '"' ~('\\'|'"')* '"';
NUMBER          : [0-9]+ ('.' [0-9]+)?;
COMMENT         : '//' ~[\r\n]* -> skip;
WHITESPACE      : [ \t\r\n]+ -> skip;
