#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

// p is the string
// s is the regex
bool match(char *s, char *p) {
    bool arr[(int)strlen(p) + 1][(int)strlen(s) + 1];

    for (int x = 0; x < (int)strlen(p) + 1; x++) {
        for (int y = 0; y < (int)strlen(s) + 1; y++) {
            arr[x][y] = false;
        }
    }

    arr[(int)strlen(p)][(int)strlen(s)] = true;

    // Loop through the string
    for (int j = (int)strlen(p); j >= 0; j--) {
        // Loop through the regex
        for (int i = (int)strlen(s) - 1; i >= 0; i--) {
            // Is the length of j less than the length of the string
            bool match = (j < (int)strlen(p)) && (s[i] == p[j] || s[i] == '.');
                        
            if (i + 1 < (int)strlen(s) && s[i + 1] == '*') {
                arr[j][i] = arr[j][i + 2] || (match && arr[j + 1][i]);
            } else {
                arr[j][i] = match && arr[j + 1][i + 1];
            }
        }
    }

    return arr[0][0];
}

bool isMatch(char * s, char * p){
    //return (match(s, p) == true || match(p, s) == true) ? true : false;
    return match(p, s);
}

int main() {
    // 10 13
    //bool ans = isMatch("aasdfasdfas", "aasdf.*asdf.*s");
    bool ans = isMatch("aa", "a*");
    printf("\nAns %d\n", ans);
}