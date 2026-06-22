class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur, nums):
            if not nums:
                res.append(cur)
                return 
            
            for i in range(len(nums)):
                dfs(cur + [nums[i]], nums[:i] + nums[i+1:])

        dfs([], nums)
        
        return res