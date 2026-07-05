class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        n, m = len(s), len(t)

        if m > n:
            return 0

        dp = [[-1] * m  for _ in range(n)]

        def recur(i, j):
            if j == m:
                return 1
            if i == n:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if s[i] == t[j]:
                dp[i][j] = recur(i+1, j) + recur(i+1, j+1)
            else:
                dp[i][j] = recur(i+1, j)
            
            return dp[i][j]
        
        return recur(0, 0)
            