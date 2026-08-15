class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = {}
        def dfs(i, j):
            if i >= m or j >= n:
                return 0
                
            if obstacleGrid[i][j] == 1:
                return 0
            
            if i == m-1 and j == n-1:
                return 1
            
            if (i, j) in dp:
                return dp[(i,j)]
            
            
            
            dp[(i, j)] = dfs(i, j+1) + dfs(i+1, j)
            return dp[(i, j)]
        
        return dfs(0,0)