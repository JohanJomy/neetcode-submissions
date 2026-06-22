class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        def dfs(row, col):
            
            a = 0
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r in range(ROWS) and 
                    c in range(COLS) and
                    (r, c) not in visited and
                    grid[r][c] == 1):
                    visited.add((r,c))
                    a += 1 + dfs(r,c)

            return a

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    visited.add((r,c))
                    area = max(1 + dfs(r, c), area)
        
        return area
'''
grid=[
[1,1,0,0,0],
[1,1,0,0,0],
[0,0,0,1,1],
[0,0,0,1,1]]
'''