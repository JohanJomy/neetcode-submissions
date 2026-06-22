class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        res = 1
        for i in range(1, len(nums)):
            dp[i] += max([dp[j] if nums[j] < nums[i] else 0 for j in range(i)])
            res = max(dp[i], res)
        return res