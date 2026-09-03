class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1] * len(nums)

        for i in range(len(nums)-2, -1, -1):
            mx = 0
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    mx = max(mx, dp[j])

            dp[i] += mx
        
        # print(dp)
        return max(dp)
