#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void print(char ** ans, int *returnSize);

void dfs(int n, int left, int right, char *substr, char **list, int *returnSize) {
    if (left == 0 && right == 0) {
        (*returnSize)++;
        list[*returnSize - 1] = substr;
        return;
    }
    
    if (left > 0) {
        char *left_string = (char*)malloc(sizeof(char) * 3 * n);        
        strcpy(left_string, substr);
        strcat(left_string, "(");        
        dfs(n, left - 1, right, left_string, list, returnSize);
    }
    
    if (right > 0 && right > left) {
        char *right_string = (char*)malloc(sizeof(char) * 3 * n);        
        strcpy(right_string, substr);
        strcat(right_string, ")");    
        dfs(n, left, right - 1, right_string, list, returnSize);
    }
}


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char ** generateParenthesis(int n, int* returnSize){
    char **list = (char **)malloc(sizeof(char*) * 1500);
    *returnSize = 0;
    char *left_par = (char*)malloc(sizeof(char) * 2);
    left_par = "(";

    dfs(n, n - 1, n, left_par, list, returnSize);
    
    return list;
}


void print(char **ans, int *returnSize) {
    printf("\nAns: %p    %d\n", *ans, *returnSize);
    for (int i = 0; i < *returnSize; i++) {
        printf("%s %d\n", ans[i], i);
    }

    printf("\n");
}

int main() {
    int *returnSize = (int*)malloc(sizeof(int));
    char **ans = generateParenthesis(8, returnSize);
    printf("Where is this illegal instruction");
    print(ans, returnSize);

    for (int i = 0; i < *returnSize; i++) {
        free(ans[i]);
    }

    free(ans);

}