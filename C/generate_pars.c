#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void print(char ** ans, int *returnSize);

void copy(char *a, char *b) {
    while (b != '\0') {
        *a = *b;
        a++;
        b++;
    }
}

void dfs(int n, int left, int right, char *substr, char **list, char ***ans, int *returnSize) {
    printf("Left: %d    Right: %d    substr: %p    list: %p\n", left, right, substr, list);

    if (left == 0 && right == 0) {
        printf("update answer\n");
        (*returnSize)++;
        //list = (char**)realloc(list, sizeof(list) + (*returnSize + 1));
        //char **new_list = (char**)malloc(sizeof(char*) + sizeof(*list));
        //for (int i = 0; i < (*returnSize) - 2; i++) {
        //    new_list[i] = list[i];
        //}

        list[*returnSize - 1] = substr;
        //print(new_list, returnSize);
        //free(list);
        //*ans = new_list;
        //print(list, returnSize);
        return;
    }
    
    if (left > 0) {
        char *left_string = (char*)malloc(sizeof(char) * 2 * n);        
        strcat(left_string, substr);
        strcat(left_string, "(");        
        dfs(n, left - 1, right, left_string, list, ans, returnSize);
    }
    
    if (right > 0 && right > left) {
        char *right_string = (char*)malloc(sizeof(char) * 2 * n);        
        strcat(right_string, substr);
        strcat(right_string, ")");        
        dfs(n, left, right - 1, right_string, list, ans, returnSize);
    }
}


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char ** generateParenthesis(int n, int* returnSize){
    char ***ans = (char ***)malloc(sizeof(char**));
    char **list = (char **)malloc(sizeof(char*) * 1500);
    *returnSize = 0;
    
    dfs(n, n - 1, n, "(", list, ans, returnSize);
    
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
    char **ans = generateParenthesis(2, returnSize);
    printf("Where is this illegal instruction");
    print(ans, returnSize);

}