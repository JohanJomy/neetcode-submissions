class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * (n+1)

        dp[1], dp[2] = nums[0], nums[1]

        for i in range(2, n):
            dp[i+1] = nums[i] + max(dp[i-1], dp[i-2])
        
        return max(dp[-1], dp[-2])