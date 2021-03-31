// Given two positive integers
// n and k where k <= n
// Return a set of combinations of [1..n] of length k

// Given n = 5 and k = 3
// Return [[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],
//          [2,3,4],[2,3,5],[2,4,5],[3,4,5]]

// My solution was to use a depth first search backtracking method
//                   1                           2                3
//           /           \      \             /     \              \
//          2            3       4          3        4              4
//      /  /  \       /     \     \        / \        \              \
//     3  4    5     4       5     5      4   5        5              5

// The combine function initialized the first level of the tree
// backtrack then computed the rest of the levels

class Combinations {
    private List<List<Integer>> backtrack(List<List<Integer>> level, int n, int k) {
        // Just check one of the lists because they should 
        // all be the same size
        if (level.get(0).size() == k) {
            return level;
        }
        
        List<List<Integer>> next_level = new ArrayList<List<Integer>>();
        
        for (int i = 0; i < level.size(); i++) {
            List<Integer> temp_arr = level.get(i);
            
            // Add number from the last number in the array to n
            for (int j = temp_arr.get(temp_arr.size() - 1) + 1; j <= n; j++) {
                // Copy the array
                List<Integer> sub_arr = new ArrayList<Integer>(level.get(i));
                
                sub_arr.add(j);
                next_level.add(sub_arr);
            }
        }
        
        return backtrack(next_level, n, k);
    }
    
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> first_level = new ArrayList<List<Integer>>();
        
        // Initialize the first level of the tree
        for (int i = 1; i <= (n - k + 1); i++) {
            List<Integer> sub_arr = new ArrayList<Integer>();
            sub_arr.add(i);
            first_level.add(sub_arr);
        }

        return backtrack(first_level, n, k);        
    }
}