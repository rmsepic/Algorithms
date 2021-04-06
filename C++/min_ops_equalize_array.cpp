class MinOps {
public:
    int minOperations(int n) {
        int ops = 0;
        int half = n / 2; // If n = 4 then half = 2, if n = 5 then n = 2
            
        if (n % 2 == 0) {
            int front = half * 2 + 1;
            int back = (half - 1) * 2 + 1;
            
            ops++;
            for (int i = half + 1; i < n; i++) {
                ops += (i - half) * 2 + 1;
            }
        } else { // If odd
            for (int i = half + 1; i < n; i++) {
                ops += (i - half) * 2;
            }
        }
        
        return ops;
    }
};