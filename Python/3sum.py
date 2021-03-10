from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
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

if __name__ == "__main__":
    l = [-1,0,1,2,-1,-4]
    ans = threeSum(l)
    print(ans)