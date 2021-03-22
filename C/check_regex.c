#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

// Iterate through s and p individually 
// Try to match one to the next
// Let i be in |s|
// If s[i] = . then ignore p[i]
// If s[i + 1] = '*' then check s[i] for 0 or more in p
int getRemaining(const int index, const char *s) {
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

bool match(char *s, char *p) {
    int j = 0;
    //printf("length %d\n", (int)strlen(s));
    for (int i = 0; i < (int)strlen(s); i++) {
        // Check for all occurences of s[i] in p
        printf("%d %c == %c\n", i, s[i], p[j]);
        if (i + 1 < strlen(s) && s[i + 1] == '*') {
            printf("Kleene\n");
            int remaining = getRemaining(i, s);

            while (j < ((int)strlen(p) - remaining)) { 
                if (s[i] == p[j] || s[i] == '.') {
                    j++;
                }
            }

            // Skip over the s[i + 1] because it is equal to '*'
            i++;
        // No Kleene star
        } else if (j < (strlen(p)) && (s[i] == p[j] || s[i] == '.')) {
            j++;
        } else {
            printf("DID NOT MATCH \n");
            return false;
        }

    }
    
    printf("Finished\n");
    return j == strlen(p) ? true : false;
}

bool isMatch(char * s, char * p){
    return (match(s, p) == true || match(p, s) == true) ? true : false;
}

int main() {
    bool ans = isMatch("aasdfasdfas", "aasdf.*asdf.*s");
    printf("Ans %d\n", ans);
}