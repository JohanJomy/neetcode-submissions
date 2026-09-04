class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        dp = {}
        def dfs(l, r):
            # consider poping the ith elemnet LAST then make to 
            # subarrays and find result
            if l > r:
                return 0

            if (l, r) in dp:
                return dp[(l, r)]
            
            dp[(l, r)] = 0
            res = 0
            for i in range(l, r+1):
                # pop the ith element last
                coins = nums[l-1] * nums[i] * nums[r+1]
                coins += dfs(i+1, r) +dfs(l, i-1)
                res = max(res, coins)
            
            dp[(l, r)] = res

            return res
        
        return dfs(1, len(nums)-2)
        