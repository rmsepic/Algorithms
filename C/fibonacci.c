int fib(int n){
    if (n == 0) {
        return 0;
    }
    
    if (n == 1) {
        return 1;
    }
    
    int x = 1;
    int y = 0;
    int ans = 0;
    
    for (int i = 0; i < n - 1; i++) {
        ans = x + y;
        y = x;
        x = ans;
    }
    
    return ans;
}