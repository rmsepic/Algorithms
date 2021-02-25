all: compiler

lex.yy.c: main.l
	lex main.l

y.tab.c: main.y
	yacc -d main.y

compiler: lex.yy.c y.tab.c
	gcc -Wall lex.yy.c y.tab.c 
	./a.out