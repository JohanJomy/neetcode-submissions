class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            a = 0
            while q:
                row, col = q.popleft()
                
                # visited.add((row,col))
                a += 1

                # print(row,col, a)
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(ROWS) and 
                        c in range(COLS) and
                        (r, c) not in visited and
                        grid[r][c] == 1):
                        visited.add((r,c))
                        q.append((r,c))
            # print(a)
            return a

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = max(bfs(r, c), area)
        
        return area
'''
grid=[
[1,1,0,0,0],
[1,1,0,0,0],
[0,0,0,1,1],
[0,0,0,1,1]]
'''