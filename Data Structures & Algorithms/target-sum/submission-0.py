class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {}

        def backtrack(i, sm):

            if i == len(nums):
                if sm == target:
                    return 1
                return 0
            
            if (i, sm) in dp:
                return dp[(i, sm)]
            
            dp[(i, sm)] = backtrack(i+1, sm+nums[i]) + backtrack(i+1, sm-nums[i])
            
            return dp[(i, sm)]

        return backtrack(0,0) 