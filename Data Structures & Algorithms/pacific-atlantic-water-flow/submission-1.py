class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific = set()
        atlantic = set()

        ROWS = len(heights)
        COLS = len(heights[0])
        
        visited = set()

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        ocean = pacific

        def dfs(r, c, prev):
            if r not in range(ROWS) or c not in range(COLS):
                return
            
            if heights[r][c] < prev or (r,c) in visited:
                return 

            ocean.add((r,c))
            for dr, dc in directions:
                visited.add((r,c))
                dfs(r+dr, c+dc, heights[r][c])


        for c in range(COLS):
            dfs(0, c, -1)
        
        for r in range(ROWS):
            dfs(r, 0, -1)
        
        ocean = atlantic
        visited = set()

        for c in range(COLS):
            dfs(ROWS-1, c, -1)
        
        for r in range(ROWS):
            dfs(r, COLS-1, -1)
        
        # print(pacific, atlantic)
        return list(pacific.intersection(atlantic))

        
        
