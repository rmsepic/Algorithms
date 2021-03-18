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
    for (int i = 0; i < strlen(s); i++) {
        printf("%c    %c\n", s[i], p[j]);
        // Check for all occurences of s[i] in p
        if (i + 1 < strlen(s) && s[i + 1] == '*') {
            int remaining = getRemaining(i, s);
            printf("remaining %d, %lu     %d \n", remaining, strlen(p), j);
            while (j < ((int)strlen(p) - remaining)) { 
                if (s[i] == p[j] || s[i] == '.') {
                    j++;
                }
            }
            
            // Skip over the s[i + 1] because it is equal to '*'
            i++;
        } else if (j < (strlen(p)) && (s[i] == p[j] || s[i] == '.')) {
            j++;
        } else {
            printf("DID NOT MATCH \n");
            return false;
        }

        //printf("j: %d\n", j);
    }
    
    return j == strlen(p) ? true : false;
}

bool isMatch(char * s, char * p){
    return (match(s, p) == true || match(p, s) == true) ? true : false;
}

int main() {
    //bool ans = isMatch("a", ".*..a*");
    bool ans = isMatch("aasdfasdfasdfasdfas", "aasdf.*asdf.*asdf.*asdf.*s");
    printf("Ans %d\n", ans);
}