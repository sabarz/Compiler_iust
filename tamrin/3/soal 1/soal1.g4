grammar soal1;

start: statement* EOF;

statement: variableDeclaration
         | assignmentStatement
         | ifStatement
         | whileStatement
         | compoundStatement
         | COMMENT
         ;

variableDeclaration: type SPACE Identifier SEMICOL NEWLINE;

assignmentStatement: Identifier '=' literal SEMICOL NEWLINE;

ifStatement: 'if' '(' expression  ')' NEWLINE compoundStatement;

whileStatement: 'while' '(' expression  ')' NEWLINE compoundStatement;

compoundStatement: '{' NEWLINE statement* NEWLINE '}' NEWLINE;

expression: literal
          | Identifier
          | expression arithmeticOperator expression
          | expression comparisonOperator expression
          | '(' expression ')'
          ;

literal: IntegerLiteral | BooleanLiteral | 'true' | 'false';

arithmeticOperator: '+' | '-';

comparisonOperator: '==' | '<' | '>' ;

type: 'int' | 'boolean';

IntegerLiteral: '-'? DIGIT+;

BooleanLiteral: 'true' | 'false';

Identifier: [a-zA-Z];

COMMENT: '#' ~[\r\n]* ;

WS: [ \t\r\n]+;

SPACE: ' ' ;
SEMICOL: ';';
NEWLINE: '\r'? '\n' | '\r';

fragment DIGIT: [0-9];
