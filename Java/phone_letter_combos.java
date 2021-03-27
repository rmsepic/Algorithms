class Solution {
    
    
    public String dfs(Map<Character, String> buttons, String remaining_digits) {
        if (remaining_digits.length() == 0) {
            return "";
        }
        
        List<String> permutations = new ArrayList<String>();
        String letters = buttons.get(digits.charAt(0));
        for (int i = 0; i < letter.length(); i++) {
            String str = digits.charAt(j) + dfs(buttons, digits.substring(1));
            permutations.add(str);         
        }
        
        return permutations;
        }
    }
    
    public List<String> letterCombinations(String digits) {
        List<String> permutations = new ArrayList<String>();
        
        if (digits.length() == 0) {
            return permutations;
        }
        
        Map<Character, String> buttons = new HashMap<Character, String>();
        buttons.put('2', "abc");
        buttons.put('3', "def");
        buttons.put('4', "ghi");
        buttons.put('5', "jkl");
        buttons.put('6', "mno");
        buttons.put('7', "pqrs");
        buttons.put('8', "tuv");
        buttons.put('9', "wxyz");
            
        // Phone letters 'abc', 'def', etc.
        String letters = buttons.get(digits.charAt(0)); 
        for (int j = 0; j < letters.length(); j++) {
            String str = digits.charAt(j) + dfs(buttons, digits.substring(1));
            permutations.add(str);         
        }
        
        return permutations;
    }
}