// Given some string of only '(' and ')'
// Find the longest substring of valid parentheses
// Valid meaning for each '(' there is a corresponding ')'
// in a valid parentheses format
// So ')(' would be invalid and '(())' is valid

// This is not my best solution
// The map could have been replaced with a dp array
// that held onto the scores

class LongestValidPars {
    public int longestValidParentheses(String s) {
        Map<Integer, Integer> map = new HashMap<>();
        Stack<Integer> stack = new Stack<>(); // Holds the indexes
        int max_ = 0;
        
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.add(i);
            } else if (stack.size() > 0) {
                if (map.containsKey(i - 1)) {
                    map.put(i, map.get(i - 1) + 2);
                } else {
                    map.put(i, 2);
                }
                
                int prev_index = stack.pop();
                int prev_score = 0;
                
                if (prev_index > 0) {
                    if (map.containsKey(prev_index - 1)) {
                        prev_score = map.get(prev_index - 1);
                    }
                    
                    map.put(i, prev_score + map.get(i));
                }
                
                // Store the max so the map doesn't have to be
                // iterated through later
                max_ = Math.max(max_, map.get(i));
            } 
        }
        
        return max_;
    }
}