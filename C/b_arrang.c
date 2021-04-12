int* constructArray(int n, int k, int* returnSize){
    int *ans = (int*)malloc(sizeof(int) * 10000);
    int front = 1;
    int back = k + 1;
    
    for (int i = 0; i <= k; i++) {
        ans[i] = i % 2 == 0 ? front++ : back--;
    }
    
    for (int i = k + 1; i < n; i++) {
        ans[i] = i + 1;
    }
    
    *returnSize = n;
    return ans;
}