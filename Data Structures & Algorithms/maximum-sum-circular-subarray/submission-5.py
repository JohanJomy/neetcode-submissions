class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        mx, mn = 0, 0
        globalmax = nums[0]
        globalmin = nums[0]
        
        sm = 0
        for n in nums:
            sm += n
            if mx + n < n:
                mx = 0
            
            if mn + n > n:
                mn = 0

            mx += n
            mn += n

            globalmax = max(globalmax, mx)
            globalmin = min(globalmin, mn)
        


        if globalmax >= 0:
            return max(globalmax, sm-globalmin)
        return globalmax
