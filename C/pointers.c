#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE 3

void foo(char *c) {
	
}

int main() {
	char *a = "abc";
	char *z = "xyz";

	char **c = (char**)malloc(sizeof(char*) * 2);
	c[0] = a;
	c[1] = z;

	free(c);
	//char **e = (char**)malloc(sizeof(char*) * 2);
	//e = c;
	char **d = (char**)malloc(sizeof(char*) * 2);
	for (int i = 0; i < 2; i++) {
		d[i] = c[i];
	}

	for (int i = 0; i < 2; i++) {
		printf("d: %s\n", d[i]);
	}

	return 0;
}