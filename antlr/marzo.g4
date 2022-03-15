grammar marzo;

//declarar variable, asignar nuevo valor, referenciar valor de una variable declarada
@members {symbolTable = {};}

start: HELLO WORLD;

//Estructura del programa es la palabra program, el nombre del programa, llave, contenido y llave.
program: PROGRAM ID BRACKET_OPEN sentence* BRACKET_CLOSE;

//Sentencia se compone de declaración de variable, asignación de variable o impresión.
sentence:
	var_decl
	| var_assign
	| println
	| suma
	| resta
	| multiplicacion
	| division
	| ifsinelse
	| ifconelse;

//var_decl: VAR ID SEMICOLON {print('Declarando variable')};
var_decl: VAR ID SEMICOLON {self.symbolTable[$ID.text] = 0;};
//var_assign: ID ASSIGN expression SEMICOLON {print('Asignando variable')};
var_assign:
	ID ASSIGN expression SEMICOLON {self.symbolTable[$ID.text] = $expression.value;};
//println: PRINTLN expression SEMICOLON {print($expression.value)};
println: PRINTLN expression SEMICOLON;
expression
	returns[Object value]:
	NUMBER {$value = int($NUMBER.text);}
	| ID {$value = self.symbolTable.get($ID.text);};
suma: ID ASSIGN NUMBER PLUS NUMBER SEMICOLON;
resta: ID ASSIGN NUMBER MINUS NUMBER SEMICOLON;
multiplicacion: ID ASSIGN NUMBER MULT NUMBER SEMICOLON;
division: ID ASSIGN NUMBER DIV NUMBER SEMICOLON;
comparison: GT | LT | GEQ | LEQ | EQ | NEQ;
ifsinelse:
	IF PAR_OPEN NUMBER comparison NUMBER PAR_CLOSE BRACKET_OPEN sentence* BRACKET_CLOSE;
ifconelse:
	IF PAR_OPEN NUMBER comparison NUMBER PAR_CLOSE BRACKET_OPEN sentence* BRACKET_CLOSE ELSE
		BRACKET_OPEN sentence* BRACKET_CLOSE;

//Análisis léxico, gramática regular, tokens del lenguaje. Lexer los identifica pero no verifica que estén en orden.

//Palabras reservadas
PROGRAM: 'program';
VAR: 'var';
PRINTLN: 'println';

IF: 'if';
ELSE: 'else';

//Operadores ariméticos lógicos y de comparación
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';

AND: '&&';
OR: '||';
NOT: '!';

GT: '>';
LT: '<';
GEQ: '>=';
LEQ: '<=';
EQ: '==';
NEQ: '!=';

ASSIGN: '=';

TRUE: 'true';
FALSE: 'false';

//Paréntesis y símbolos de puntuación

BRACKET_OPEN: '{';
BRACKET_CLOSE: '}';

PAR_OPEN: '(';
PAR_CLOSE: ')';

SEMICOLON: ';';

//Identificadores (nombre del programa, nombres de variables)

//Primer caracter es letra o guion bajo, posterior es cualquier combinación
ID: [a-zA-Z_][a-zA-Z0-9_]*;

NUMBER: [0-9]+;

WS: [ \t\n\r]+ -> skip;

