class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = defaultdict(int) 

        dp[0] = 1 # 0 = cursum

        for num in nums:
            new_dp = defaultdict(int)

            for cur_sum, count in dp.items():
                new_dp[cur_sum + num] += count
                new_dp[cur_sum - num] += count
            dp = new_dp
        
        return dp[target]