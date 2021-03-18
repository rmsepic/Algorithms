#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int fun2(const int index, const char *s) {
	int count = 0;
    int i = index;
    while (i < strlen(s)) {   
        if (i + 1 < strlen(s) && s[i + 1] == '*') {
            // Do not count this 
            i += 2;
        } else {
            count++;
            i++;
        }
    }

    return count;
}

int match(char *s, char *p) {
	for (int i = 0; i < strlen(s); i++) {
		fun2(0, s);
	}
    return 3;
}

int fun1(char *s) {
	//return match(".*..a*", "a");
	return match(s, "a");
}

int main() {
	char *s = ".*..a*";
	printf("%d\n", fun1(s));
	printf("%d\n", fun1(".*..a*"));
}