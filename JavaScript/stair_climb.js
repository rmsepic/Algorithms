/**
 * If you draw a tree for the first few n's
 * It can be noted that n is formed of two subtrees on its left and right
 * The left (starting with a 1) will branch into the tree (n - 1) 
 * The right (starting with a 2) will branch into the tree (n - 2)
 * If n = 1 return 1
 * If n = 2 return 2
 * If 
 */
var climbStairs = function(n) {    
    if (n == 1) {
        return 1;
    }
    
    if (n == 2) {
        return 2;
    }
    
    var x = 1;  // If n = 1 then the answer is 1
    var y = 2;  // If n = 2 then the ansewr is 2
    var ans = 1;
    
    for (let i = 0; i < n - 2; i++) {
        ans = x + y;
        x = y;
        y = ans;
    }
    
    return ans;
};