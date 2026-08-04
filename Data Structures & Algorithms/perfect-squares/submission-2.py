import sys

sys.setrecursionlimit(100000)

class Solution:
    def numSquares(self, n: int) -> int:
        
        dp = {}
        def dfs(n):
            if n == 0:
                return 0
            
            if n in dp:
                return dp[n]
            
            res = float('inf')
            for i in range(1, n):
                v = n-i*i 
                if v < 0:
                    break
                res = min(res, 1 + dfs(v))
            
            dp[n] = res
            return res
        
        if n == 1:
            return 1
        
        return dfs(n)