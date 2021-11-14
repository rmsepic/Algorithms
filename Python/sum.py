class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ans = 0
        cur = 0
        for n in nums:
            cur += n              
            ans = min(ans, cur)
        
        return -ans + 1