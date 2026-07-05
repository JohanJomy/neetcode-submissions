class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])

        dp = {}
        res = 0
        def dfs(i, j, prev):
            nonlocal res
            if i not in range(n) or j not in range(m):
                return 0

            if prev >= matrix[i][j]:
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            dp[(i,j)] = 1 + max(dfs(i+1, j, matrix[i][j]),
                dfs(i-1, j, matrix[i][j]),
                dfs(i, j+1, matrix[i][j]),
                dfs(i, j-1, matrix[i][j]))
            
            res = max(res, dp[(i, j)])
            return dp[(i, j)]
        
        for i in range(n):
            for j in range(m):
                dfs(i, j, - 1)
                
        return res

