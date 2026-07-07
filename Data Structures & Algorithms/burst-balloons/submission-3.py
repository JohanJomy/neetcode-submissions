class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)

        nums.insert(n, 1)
        nums.insert(0, 1)

        dp = [[-1] * n for _ in range(n)]
        
        def dfs(l, r):
            # consider poping the ith elemnet last then make to subarrays and find result
            if l > r:
                return 0
                
            if dp[l-2][r-2] != -1:
                return dp[l-2][r-2]
            
            mx = 0
            for i in range(l, r+1):
                # pop the ith element last
                mx = max(mx, 
                    nums[l-1] * nums[i] * nums[r+1] +
                    dfs(i+1, r) +
                    dfs(l, i-1)
                )
            
            dp[l-2][r-2] = mx

            return dp[l-2][r-2]
        
        return dfs(1, n)
        