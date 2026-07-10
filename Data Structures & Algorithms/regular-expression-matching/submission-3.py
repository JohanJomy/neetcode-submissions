class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        dp = set()
        def dfs(i, j):
            if i == len(s) and j == len(p):
                return True
            
            if j >= len(p):
                return False
            
            if (i, j) in dp:
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            if (j+1) < len(p) and p[j+1] == '*':
                if (match and dfs(i+1, j)) or dfs(i, j+2):
                    return True
            
            elif match:
                if dfs(i+1, j+1):
                    return True
            


            dp.add((i,j))
            return False
        
        return dfs(0, 0)

