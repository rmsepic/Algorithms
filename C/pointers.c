#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE 3

void foo(char *c) {
	free(c);
}

int main() {
	char *a = (char*)malloc(sizeof(char));

	strcpy(a, "abc");
	foo(a);


	printf("%s\n", a);
	

	return 0;
}