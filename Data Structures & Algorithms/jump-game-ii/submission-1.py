class Solution:
    def jump(self, nums: List[int]) -> int:
        
        dp = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums)-1:
                return 0

            if dp[i] != -1:
                return dp[i]            
            
            mn = float('inf')
            for j in range(nums[i]):
                mn = min(mn, 1 + dfs(i+j+1))

            # print(i, mn)
            dp[i] = mn
            return mn
        
        return dfs(0)
