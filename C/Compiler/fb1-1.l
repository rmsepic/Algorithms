/* 	Should work just like UNIX wc
	From Flex and Bison */

/* Three sections in a flex program */

/* Declarations */
%{
int yylex();
int chars = 0;
int words = 0;
int lines = 0;
%}


/* List of patterns */

%% 

[a-zA-Z]+ {words++; chars += strlen(yytext);}
\n {chars++; lines++;}
. {chars++;}

%%

int main(int argc, char** argv) {
	yylex();
	printf("%8d%8d%8d\n", lines, words, chars);
}

