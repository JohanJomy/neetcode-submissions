class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        def bfs(r, c):
            q = deque()
            q.append((r,c))


            while q:
                row, col = q.popleft()

                visited.add((row,col))

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(ROWS) and 
                        c in range(COLS) and
                        (r, c) not in visited and
                        grid[r][c] == '1'):

                        q.append((r,c))


        islands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visited:
                    islands += 1
                    bfs(r, c)
        
        return islands