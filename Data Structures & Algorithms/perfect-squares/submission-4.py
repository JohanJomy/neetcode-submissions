
sys.setrecursionlimit(100001)
class Solution:
    def numSquares(self, n: int) -> int:
        
        dp = {}
        def dfs(target):
            if target == 0:
                return 1
            
            if target in dp:
                return dp[target]

            i = 1
            sq = 1
            res = float('inf')
            while sq <= target:
                res = min(res, 1 + dfs(target-sq))

                i += 1
                sq = i * i
            dp[target] = res
            return res
        
        return dfs(n) - 1