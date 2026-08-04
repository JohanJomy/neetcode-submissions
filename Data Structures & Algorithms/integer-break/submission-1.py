class Solution:
    def integerBreak(self, n: int) -> int:
        
        dp = {}
        def dfs(n):
            if n <= 2:
                return 1
            
            if n in dp:
                return dp[n]
            
            res = 0
            for i in range(1, n):
                res = max(res, i * (n - i), i*dfs(n-i))
            
            dp[n] = res
            return res
        
        dfs(n)
        print(dp)

        return dfs(n)