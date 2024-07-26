grammar soal1;

start: statement* EOF;

statement: variableDeclaration
         | assignmentStatement
         | ifStatement
         | whileStatement
         | compoundStatement
         ;

variableDeclaration: type Identifier SEMICOL;

assignmentStatement: Identifier '=' expression SEMICOL;

ifStatement: 'if' '(' expression  ')' statement;

whileStatement: 'while' '(' expression  ')' statement;

compoundStatement: '{' statement* '}';

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

Identifier: [a-zA-Z_][a-zA-Z0-9_]*;

COMMENT: '#' ~[\r\n]* -> skip;

WS: [ \t\r\n]+ -> skip;

SPACE: ' ' ;
SEMICOL: ';';

fragment DIGIT: [0-9];
