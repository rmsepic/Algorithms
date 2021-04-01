// Solution based on LeetCode solution
// One pass hash table

// Given an array [4, 1, 9] and a target 5
// Return the indexes of one solution 

class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        map<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int rem = target - nums[i];
            
            if (map.containsKey(rem)) {
                // Return the indexes of the numbers
                return new int[] {map.get(rem), i};
            }
            
            // If the map does not contain the remainder
            // Add the new number
            map.put(nums[i], i);
        }
    }
}