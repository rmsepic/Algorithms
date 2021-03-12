from typing import List

def threeSumClosestBruteForce(nums: List[int], target: int) -> int:
    curr = 100000
    ans = -1
    for i in range(0, len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                t = abs(target - (nums[i] + nums[j] + nums[k]))
                print(t)
                if t < curr:
                    curr = t
                    ans = (nums[i] + nums[j] + nums[k])

    return ans

# Assume that nums.length is at least 3
def threeSumClosest_O2(nums: List[int], target: int) -> int:
    l = {}
    curr = nums[0] + nums[1] + nums[2]

    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            l.update({(i, j): nums[i] + nums[j]})

    print(l)

    for key in l:
        for k in range(key[1] + 1, len(nums)):
            x = nums[k] + l[key]
            if abs(target - x) < abs(target - curr):
                print("k: ", k)
                curr = x

    return curr
                
def threeSumClosest(nums: List[int], target: int) -> int:
    nums.sort()
    prev = 10000

    for i in range(0, len(nums) - 2):
        lo = i + 1
        hi = len(nums) - 1
        
        while lo < hi:
            comp = nums[i] + nums[hi] + nums[lo]

            if abs(target - comp) < abs(target - prev):
                prev = comp

            if comp > target:
                hi -= 1
            elif comp <= target:
                lo += 1

    return prev





if __name__ == "__main__":
    l = [-1,2,1,-4]
    target = 1
    ans = threeSumClosest(l, 1)
    print(ans)