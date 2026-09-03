class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2 == 1:
            return False

        target = sum(nums) // 2

        dp = {}
        def dfs(i, sm):
            if i == len(nums):
                return sm == target
            
            if sm == target:
                return True

            if sm > target:
                return False
            
            if (i, sm) in dp:
                return dp[(i, sm)]
            
            dp[(i, sm)] = dfs(i+1, sm) or dfs(i+1, sm+nums[i])

            return dp[(i, sm)]
        
        return dfs(0, 0)