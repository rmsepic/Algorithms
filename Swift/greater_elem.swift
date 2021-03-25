func nextGreaterElement(_ nums1: [Int], _ nums2: [Int]) -> [Int] {
        var dict:[Int: Int] = [:]
        var stack:[Int] = []
        var ans:[Int] = []
        stack.append(nums2[0])
        
        for n in nums2 {            
            while stack.count > 0 && n > stack[stack.count - 1] {
                dict[stack[stack.count - 1]] = n
                stack.removeLast()
            }
            stack.append(n)
        }
        
        print(dict)
        
        for n1 in nums1 {
            if let x = dict[n1] {
                ans.append(x);      
            } else {
                ans.append(-1)   
            }
        }
        
        return ans;
    }

func nextGreaterElementNaive(_ nums1: [Int], _ nums2: [Int]) -> [Int] {
        var j = 0;
        var left = 0;
        var arr:[Int] = []
        
        for i in 0 ..< nums1.count {
            left = 0;
            while(left < nums2.count && nums1[i] != nums2[left]) {
                left += 1;
            }
            
            j = left + 1;
            
            while(j < nums2.count && nums1[i] > nums2[j]) {
                    j += 1;
            }
            
            if (j >= nums2.count || nums1[i] >= nums2[j]) {
                arr.append(-1);
            } else {
                arr.append(nums2[j]);
            }
        }
        
        return arr;
    }