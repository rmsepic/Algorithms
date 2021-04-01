function sortNumber(a, b) {
    return a - b;
}

/// Naive approach
var fourSum = function(nums, const_target) {
    var ht = {}
    var ans = []
    nums.sort(sortNumber);

    // Initialize dictionary
    // If nums = [-2,-1,0,1,2]
    // {-2: 0, -1: 1, 0: 2, 1: 3, 2: 4}
    for (let i = 0; i < nums.length; i++) {
        ht[nums[i]] = i;
    }
    
    // Go through the array and for each index
    // Do a two pointers solutions like 3sum
    for (let i = 0; i < nums.length; i++) {
        if (i - 1 >= 0 && nums[i] == nums[i - 1]) {
            continue;
        } else {
            for (let j = i + 1; j < nums.length - 1; j++) {
                if (j - 1 >= i + 1 && nums[j] == nums[j - 1]) {
                    continue;
                } else {
                    for (let k = j + 1; k < nums.length; k++) {
                        if (k - 1 >= j + 1 && nums[k] == nums[k - 1]) {
                            continue;
                        } else {                        
                            let remainder = (nums[i] + nums[j] + nums[k]) * -1;
                            let target = (const_target + remainder);

                            if ((target in ht) && ht[target] > k) {
                                ans.push([nums[i], nums[j], nums[k], target]);
                            }
                        }
                    } // for k
                } // if else
            } // for j
        } // if/else
    } // for i
    
    return ans;
};