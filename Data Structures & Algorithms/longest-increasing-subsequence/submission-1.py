class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dfs Solution
        dp = {}

        def dfs(i):
            if i in dp:
                return dp[i]

            mx = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    mx = max(1+ dfs(j), mx)

            dp[i] = mx

            return dp[i]

        # for i in range(len(nums)):
        

        return max(dfs(i) for i in range(len(nums)))
            
