class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n < 3:
            return max(nums)
        
        dp = [0] * (n+1)

        dp[1], dp[2] = nums[0], nums[1]

        for i in range(2, n-1):
            dp[i+1] = nums[i] + max(dp[i-1], dp[i-2])
        
        dp1 = dp.copy()

        dp = [0] * (n+1)

        dp[1], dp[2] = nums[1], nums[2]

        for i in range(3, n):
            dp[i] = nums[i] + max(dp[i-2], dp[i-3])
        
        print(dp1, dp)
        return max(max(dp1[-3:-1]), max(dp[-2:]))