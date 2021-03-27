// Leetcode problem

class Solution {
    private Map<Character, String> buttons = new HashMap<Character, String>();
    
    public void initialize_buttons() {
        buttons.put('2', "abc");
        buttons.put('3', "def");
        buttons.put('4', "ghi");
        buttons.put('5', "jkl");
        buttons.put('6', "mno");
        buttons.put('7', "pqrs");
        buttons.put('8', "tuv");
        buttons.put('9', "wxyz");
    }
    
    public List<String> dfs(List<String> level, String remaining_digits) {
        // If empty return empty
        if (remaining_digits.length() == 0) {
            return level;
        }

        String letters = buttons.get(remaining_digits.charAt(0));
        List<String> next_level = new ArrayList<String>();
        
        for (int i = 0; i < level.size(); i++) {
            for (int j = 0; j < letters.length(); j++) {
                next_level.add(level.get(i) + Character.toString(letters.charAt(j)));
            }
        }
        
        return dfs(next_level, remaining_digits.substring(1));
    }
    
    // Main function
    public List<String> letterCombinations(String digits) {
        List<String> permutations = new ArrayList<String>();
        List<String> first_level = new ArrayList<String>();
        
        if (digits.length() == 0) {
            return permutations;
        }
        
        initialize_buttons();
        
        // First set of letters
        String letters = buttons.get(digits.charAt(0));
        for (int i = 0; i < letters.length(); i++) {
            first_level.add(Character.toString(letters.charAt(i)));
        }
        
        permutations = dfs(first_level, digits.substring(1));
        
        return permutations;
    }
}