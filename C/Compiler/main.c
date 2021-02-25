#include <stdio.h>

void lay_foundation() {
	FILE *out = fopen("out.s", "wb");

	fprintf(out, ".text\n");
	fprintf(out, "\t.global _start\n");
	fprintf(out, "_start\n");
	fprintf(out, "\tmovel\t$2,%%ebx\n");
	fprintf(out, "\tmovel\t$1,%%eax\n");
	fprintf(out, "\tint\t\t$0x80\n");
}

int main() {
	//yyparse();
	lay_foundation();
}

