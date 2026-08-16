sys.setrecursionlimit(200000)

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        
        dp = {}
        def dfs(i):
            
            if i >= len(s) or s[i] == '1':
                return False
            
            if i == len(s) - 1:
                return True
            
            if i in dp:
                return dp[i]
            
            res = False
            for j in range(i + minJump, min(i + maxJump, len(s) - 1) + 1):
                if dfs(j):
                    res = True
                    break
            
            dp[i] = res
            return res
        
        return dfs(0)