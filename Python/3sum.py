from typing import List

def threeSum_unique_duplicates(nums: List[int]) -> List[List[int]]:
    ans = []
    dic = {}
    size_ = len(nums)
    x = y = z = 1
    # O(n^2)
    for i in range(0, size_ - 2):
        for j in range(i + 1, size_ - 1):
            for k in range(j + i + 1, size_):
                if nums[k] + nums[j] + nums[i] == 0:
                    l = [nums[i], nums[j], nums[k]]
                    ans.append(l)

    return ans 

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    print(nums)
    ht = {}
    ans = []

    for i, val in enumerate(nums):
        ht[val] = i

    print(ht)

    for i in range(0, len(nums) - 1):
        if i - 1 >= 0 and nums[i] == nums[i - 1]: 
            continue
        else:
            for j in range(i + 1, len(nums)):
                if j - 1 >= i + 1 and nums[j] == nums[j - 1]:
                    continue
                else:
                    target = -1 * (nums[i] + nums[j])

                    if target in ht and ht[target] > j:
                        ans.append([nums[i], nums[j], target])

    return ans




if __name__ == "__main__":
    l = [0,0,0]
    ans = threeSum(l)
    print(ans)